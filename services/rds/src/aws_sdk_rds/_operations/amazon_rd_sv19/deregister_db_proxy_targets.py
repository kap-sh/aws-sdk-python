"""Generated from Smithy shape ``com.amazonaws.rds#DeregisterDBProxyTargets``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_rds._auth._signers
import aws_sdk_rds._auth._sigv4
import aws_sdk_rds.errors.db_proxy_not_found_fault
import aws_sdk_rds.errors.db_proxy_target_group_not_found_fault
import aws_sdk_rds.errors.db_proxy_target_not_found_fault
import aws_sdk_rds.errors.invalid_db_proxy_state_fault
import aws_sdk_rds.types.deregister_db_proxy_targets_request
import aws_sdk_rds.types.deregister_db_proxy_targets_response
import aws_sdk_rds.types.string_list
from aws_sdk_rds._protocol.errors import parse_error_metadata
from aws_sdk_rds._protocol.xml import fromstring
from aws_sdk_rds._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_rds._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_rds.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "DBProxyNotFoundFault":
            raise aws_sdk_rds.errors.db_proxy_not_found_fault.DBProxyNotFoundFault.from_query(
                root
            )
        case "DBProxyTargetGroupNotFoundFault":
            raise aws_sdk_rds.errors.db_proxy_target_group_not_found_fault.DBProxyTargetGroupNotFoundFault.from_query(
                root
            )
        case "DBProxyTargetNotFoundFault":
            raise aws_sdk_rds.errors.db_proxy_target_not_found_fault.DBProxyTargetNotFoundFault.from_query(
                root
            )
        case "InvalidDBProxyStateFault":
            raise aws_sdk_rds.errors.invalid_db_proxy_state_fault.InvalidDBProxyStateFault.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_rds.types.deregister_db_proxy_targets_response.DeregisterDBProxyTargetsResponse:
    root = fromstring(response.read())
    result = root.find("DeregisterDBProxyTargetsResult")
    out: aws_sdk_rds.types.deregister_db_proxy_targets_response.DeregisterDBProxyTargetsResponse = aws_sdk_rds.types.deregister_db_proxy_targets_response.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_rds.types.deregister_db_proxy_targets_response.DeregisterDBProxyTargetsResponse:
    root = fromstring(await response.aread())
    result = root.find("DeregisterDBProxyTargetsResult")
    out: aws_sdk_rds.types.deregister_db_proxy_targets_response.DeregisterDBProxyTargetsResponse = aws_sdk_rds.types.deregister_db_proxy_targets_response.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_rds._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_rds._auth._sigv4.build_sigv4_auth_scheme("rds", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_rds._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_rds.types.deregister_db_proxy_targets_request.DeregisterDBProxyTargetsRequest,
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
    pairs.append(("Action", "DeregisterDBProxyTargets"))
    pairs.append(("Version", "2014-10-31"))
    aws_sdk_rds.types.deregister_db_proxy_targets_request.serialize_query(
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


def deregister_db_proxy_targets(
    options: OperationOptions,
    input_: aws_sdk_rds.types.deregister_db_proxy_targets_request.DeregisterDBProxyTargetsRequest,
) -> tuple[
    aws_sdk_rds.types.deregister_db_proxy_targets_response.DeregisterDBProxyTargetsResponse,
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


async def async_deregister_db_proxy_targets(
    options: AsyncOperationOptions,
    input_: aws_sdk_rds.types.deregister_db_proxy_targets_request.DeregisterDBProxyTargetsRequest,
) -> tuple[
    aws_sdk_rds.types.deregister_db_proxy_targets_response.DeregisterDBProxyTargetsResponse,
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
