"""Generated from Smithy shape ``com.amazonaws.elasticache#PurchaseReservedCacheNodesOffering``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_elasticache._auth._signers
import aws_sdk_elasticache._auth._sigv4
import aws_sdk_elasticache.errors.invalid_parameter_combination_exception
import aws_sdk_elasticache.errors.invalid_parameter_value_exception
import aws_sdk_elasticache.errors.reserved_cache_node_already_exists_fault
import aws_sdk_elasticache.errors.reserved_cache_node_quota_exceeded_fault
import aws_sdk_elasticache.errors.reserved_cache_nodes_offering_not_found_fault
import aws_sdk_elasticache.errors.tag_quota_per_resource_exceeded
import aws_sdk_elasticache.types.purchase_reserved_cache_nodes_offering_message
import aws_sdk_elasticache.types.purchase_reserved_cache_nodes_offering_result
import aws_sdk_elasticache.types.reserved_cache_node
import aws_sdk_elasticache.types.tag_list
from aws_sdk_elasticache._protocol.errors import parse_error_metadata
from aws_sdk_elasticache._protocol.xml import fromstring
from aws_sdk_elasticache._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_elasticache._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_elasticache.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InvalidParameterCombinationException":
            raise aws_sdk_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException.from_query(
                root
            )
        case "InvalidParameterValueException":
            raise aws_sdk_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_query(
                root
            )
        case "ReservedCacheNodeAlreadyExistsFault":
            raise aws_sdk_elasticache.errors.reserved_cache_node_already_exists_fault.ReservedCacheNodeAlreadyExistsFault.from_query(
                root
            )
        case "ReservedCacheNodeQuotaExceededFault":
            raise aws_sdk_elasticache.errors.reserved_cache_node_quota_exceeded_fault.ReservedCacheNodeQuotaExceededFault.from_query(
                root
            )
        case "ReservedCacheNodesOfferingNotFoundFault":
            raise aws_sdk_elasticache.errors.reserved_cache_nodes_offering_not_found_fault.ReservedCacheNodesOfferingNotFoundFault.from_query(
                root
            )
        case "TagQuotaPerResourceExceeded":
            raise aws_sdk_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_elasticache.types.purchase_reserved_cache_nodes_offering_result.PurchaseReservedCacheNodesOfferingResult:
    root = fromstring(response.read())
    result = root.find("PurchaseReservedCacheNodesOfferingResult")
    out: aws_sdk_elasticache.types.purchase_reserved_cache_nodes_offering_result.PurchaseReservedCacheNodesOfferingResult = aws_sdk_elasticache.types.purchase_reserved_cache_nodes_offering_result.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_elasticache.types.purchase_reserved_cache_nodes_offering_result.PurchaseReservedCacheNodesOfferingResult:
    root = fromstring(await response.aread())
    result = root.find("PurchaseReservedCacheNodesOfferingResult")
    out: aws_sdk_elasticache.types.purchase_reserved_cache_nodes_offering_result.PurchaseReservedCacheNodesOfferingResult = aws_sdk_elasticache.types.purchase_reserved_cache_nodes_offering_result.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_elasticache._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_elasticache._auth._sigv4.build_sigv4_auth_scheme(
                "elasticache", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_elasticache._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_elasticache.types.purchase_reserved_cache_nodes_offering_message.PurchaseReservedCacheNodesOfferingMessage,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "PurchaseReservedCacheNodesOffering"))
    pairs.append(("Version", "2015-02-02"))
    aws_sdk_elasticache.types.purchase_reserved_cache_nodes_offering_message.serialize_query(
        input_, pairs, ""
    )
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def purchase_reserved_cache_nodes_offering(
    options: OperationOptions,
    input_: aws_sdk_elasticache.types.purchase_reserved_cache_nodes_offering_message.PurchaseReservedCacheNodesOfferingMessage,
) -> tuple[
    aws_sdk_elasticache.types.purchase_reserved_cache_nodes_offering_result.PurchaseReservedCacheNodesOfferingResult,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_purchase_reserved_cache_nodes_offering(
    options: AsyncOperationOptions,
    input_: aws_sdk_elasticache.types.purchase_reserved_cache_nodes_offering_message.PurchaseReservedCacheNodesOfferingMessage,
) -> tuple[
    aws_sdk_elasticache.types.purchase_reserved_cache_nodes_offering_result.PurchaseReservedCacheNodesOfferingResult,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
