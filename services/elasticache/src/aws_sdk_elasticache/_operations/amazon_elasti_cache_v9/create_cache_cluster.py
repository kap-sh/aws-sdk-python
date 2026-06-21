"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateCacheCluster``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_elasticache._auth._signers
import aws_sdk_elasticache._auth._sigv4
import aws_sdk_elasticache.errors.cache_cluster_already_exists_fault
import aws_sdk_elasticache.errors.cache_parameter_group_not_found_fault
import aws_sdk_elasticache.errors.cache_security_group_not_found_fault
import aws_sdk_elasticache.errors.cache_subnet_group_not_found_fault
import aws_sdk_elasticache.errors.cluster_quota_for_customer_exceeded_fault
import aws_sdk_elasticache.errors.insufficient_cache_cluster_capacity_fault
import aws_sdk_elasticache.errors.invalid_parameter_combination_exception
import aws_sdk_elasticache.errors.invalid_parameter_value_exception
import aws_sdk_elasticache.errors.invalid_replication_group_state_fault
import aws_sdk_elasticache.errors.invalid_vpc_network_state_fault
import aws_sdk_elasticache.errors.node_quota_for_cluster_exceeded_fault
import aws_sdk_elasticache.errors.node_quota_for_customer_exceeded_fault
import aws_sdk_elasticache.errors.replication_group_not_found_fault
import aws_sdk_elasticache.errors.tag_quota_per_resource_exceeded
import aws_sdk_elasticache.types.az_mode
import aws_sdk_elasticache.types.cache_cluster
import aws_sdk_elasticache.types.cache_security_group_name_list
import aws_sdk_elasticache.types.create_cache_cluster_message
import aws_sdk_elasticache.types.create_cache_cluster_result
import aws_sdk_elasticache.types.ip_discovery
import aws_sdk_elasticache.types.log_delivery_configuration_request_list
import aws_sdk_elasticache.types.network_type
import aws_sdk_elasticache.types.outpost_mode
import aws_sdk_elasticache.types.preferred_availability_zone_list
import aws_sdk_elasticache.types.preferred_outpost_arn_list
import aws_sdk_elasticache.types.security_group_ids_list
import aws_sdk_elasticache.types.snapshot_arns_list
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
        case "CacheClusterAlreadyExistsFault":
            raise aws_sdk_elasticache.errors.cache_cluster_already_exists_fault.CacheClusterAlreadyExistsFault.from_query(
                root
            )
        case "CacheParameterGroupNotFoundFault":
            raise aws_sdk_elasticache.errors.cache_parameter_group_not_found_fault.CacheParameterGroupNotFoundFault.from_query(
                root
            )
        case "CacheSecurityGroupNotFoundFault":
            raise aws_sdk_elasticache.errors.cache_security_group_not_found_fault.CacheSecurityGroupNotFoundFault.from_query(
                root
            )
        case "CacheSubnetGroupNotFoundFault":
            raise aws_sdk_elasticache.errors.cache_subnet_group_not_found_fault.CacheSubnetGroupNotFoundFault.from_query(
                root
            )
        case "ClusterQuotaForCustomerExceededFault":
            raise aws_sdk_elasticache.errors.cluster_quota_for_customer_exceeded_fault.ClusterQuotaForCustomerExceededFault.from_query(
                root
            )
        case "InsufficientCacheClusterCapacityFault":
            raise aws_sdk_elasticache.errors.insufficient_cache_cluster_capacity_fault.InsufficientCacheClusterCapacityFault.from_query(
                root
            )
        case "InvalidParameterCombinationException":
            raise aws_sdk_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException.from_query(
                root
            )
        case "InvalidParameterValueException":
            raise aws_sdk_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_query(
                root
            )
        case "InvalidReplicationGroupStateFault":
            raise aws_sdk_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault.from_query(
                root
            )
        case "InvalidVPCNetworkStateFault":
            raise aws_sdk_elasticache.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault.from_query(
                root
            )
        case "NodeQuotaForClusterExceededFault":
            raise aws_sdk_elasticache.errors.node_quota_for_cluster_exceeded_fault.NodeQuotaForClusterExceededFault.from_query(
                root
            )
        case "NodeQuotaForCustomerExceededFault":
            raise aws_sdk_elasticache.errors.node_quota_for_customer_exceeded_fault.NodeQuotaForCustomerExceededFault.from_query(
                root
            )
        case "ReplicationGroupNotFoundFault":
            raise aws_sdk_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault.from_query(
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
) -> aws_sdk_elasticache.types.create_cache_cluster_result.CreateCacheClusterResult:
    root = fromstring(response.read())
    result = root.find("CreateCacheClusterResult")
    out: aws_sdk_elasticache.types.create_cache_cluster_result.CreateCacheClusterResult = aws_sdk_elasticache.types.create_cache_cluster_result.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_elasticache.types.create_cache_cluster_result.CreateCacheClusterResult:
    root = fromstring(await response.aread())
    result = root.find("CreateCacheClusterResult")
    out: aws_sdk_elasticache.types.create_cache_cluster_result.CreateCacheClusterResult = aws_sdk_elasticache.types.create_cache_cluster_result.deserialize_query(
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
    input_: aws_sdk_elasticache.types.create_cache_cluster_message.CreateCacheClusterMessage,
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
    pairs.append(("Action", "CreateCacheCluster"))
    pairs.append(("Version", "2015-02-02"))
    import aws_sdk_elasticache.types.create_cache_cluster_message

    aws_sdk_elasticache.types.create_cache_cluster_message.serialize_query(
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


def create_cache_cluster(
    options: OperationOptions,
    input_: aws_sdk_elasticache.types.create_cache_cluster_message.CreateCacheClusterMessage,
) -> tuple[
    aws_sdk_elasticache.types.create_cache_cluster_result.CreateCacheClusterResult,
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


async def async_create_cache_cluster(
    options: AsyncOperationOptions,
    input_: aws_sdk_elasticache.types.create_cache_cluster_message.CreateCacheClusterMessage,
) -> tuple[
    aws_sdk_elasticache.types.create_cache_cluster_result.CreateCacheClusterResult,
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
