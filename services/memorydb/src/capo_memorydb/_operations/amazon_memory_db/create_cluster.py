"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateCluster``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_memorydb._auth._signers
import capo_memorydb._auth._sigv4
import capo_memorydb.errors.acl_not_found_fault
import capo_memorydb.errors.cluster_already_exists_fault
import capo_memorydb.errors.cluster_quota_for_customer_exceeded_fault
import capo_memorydb.errors.insufficient_cluster_capacity_fault
import capo_memorydb.errors.invalid_acl_state_fault
import capo_memorydb.errors.invalid_credentials_exception
import capo_memorydb.errors.invalid_multi_region_cluster_state_fault
import capo_memorydb.errors.invalid_parameter_combination_exception
import capo_memorydb.errors.invalid_parameter_value_exception
import capo_memorydb.errors.invalid_vpc_network_state_fault
import capo_memorydb.errors.multi_region_cluster_not_found_fault
import capo_memorydb.errors.node_quota_for_cluster_exceeded_fault
import capo_memorydb.errors.node_quota_for_customer_exceeded_fault
import capo_memorydb.errors.parameter_group_not_found_fault
import capo_memorydb.errors.service_linked_role_not_found_fault
import capo_memorydb.errors.shards_per_cluster_quota_exceeded_fault
import capo_memorydb.errors.subnet_group_not_found_fault
import capo_memorydb.errors.tag_quota_per_resource_exceeded
import capo_memorydb.types.cluster
import capo_memorydb.types.create_cluster_request
import capo_memorydb.types.create_cluster_response
import capo_memorydb.types.ip_discovery
import capo_memorydb.types.network_type
import capo_memorydb.types.security_group_ids_list
import capo_memorydb.types.snapshot_arns_list
import capo_memorydb.types.tag_list
from capo_memorydb._protocol.errors import parse_error_metadata_json
from capo_memorydb._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_memorydb._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_memorydb.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ACLNotFoundFault":
            raise capo_memorydb.errors.acl_not_found_fault.ACLNotFoundFault.from_aws_json_1_1(
                data
            )
        case "ClusterAlreadyExistsFault":
            raise capo_memorydb.errors.cluster_already_exists_fault.ClusterAlreadyExistsFault.from_aws_json_1_1(
                data
            )
        case "ClusterQuotaForCustomerExceededFault":
            raise capo_memorydb.errors.cluster_quota_for_customer_exceeded_fault.ClusterQuotaForCustomerExceededFault.from_aws_json_1_1(
                data
            )
        case "InsufficientClusterCapacityFault":
            raise capo_memorydb.errors.insufficient_cluster_capacity_fault.InsufficientClusterCapacityFault.from_aws_json_1_1(
                data
            )
        case "InvalidACLStateFault":
            raise capo_memorydb.errors.invalid_acl_state_fault.InvalidACLStateFault.from_aws_json_1_1(
                data
            )
        case "InvalidCredentialsException":
            raise capo_memorydb.errors.invalid_credentials_exception.InvalidCredentialsException.from_aws_json_1_1(
                data
            )
        case "InvalidMultiRegionClusterStateFault":
            raise capo_memorydb.errors.invalid_multi_region_cluster_state_fault.InvalidMultiRegionClusterStateFault.from_aws_json_1_1(
                data
            )
        case "InvalidParameterCombinationException":
            raise capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterValueException":
            raise capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_aws_json_1_1(
                data
            )
        case "InvalidVPCNetworkStateFault":
            raise capo_memorydb.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault.from_aws_json_1_1(
                data
            )
        case "MultiRegionClusterNotFoundFault":
            raise capo_memorydb.errors.multi_region_cluster_not_found_fault.MultiRegionClusterNotFoundFault.from_aws_json_1_1(
                data
            )
        case "NodeQuotaForClusterExceededFault":
            raise capo_memorydb.errors.node_quota_for_cluster_exceeded_fault.NodeQuotaForClusterExceededFault.from_aws_json_1_1(
                data
            )
        case "NodeQuotaForCustomerExceededFault":
            raise capo_memorydb.errors.node_quota_for_customer_exceeded_fault.NodeQuotaForCustomerExceededFault.from_aws_json_1_1(
                data
            )
        case "ParameterGroupNotFoundFault":
            raise capo_memorydb.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault.from_aws_json_1_1(
                data
            )
        case "ServiceLinkedRoleNotFoundFault":
            raise capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault.from_aws_json_1_1(
                data
            )
        case "ShardsPerClusterQuotaExceededFault":
            raise capo_memorydb.errors.shards_per_cluster_quota_exceeded_fault.ShardsPerClusterQuotaExceededFault.from_aws_json_1_1(
                data
            )
        case "SubnetGroupNotFoundFault":
            raise capo_memorydb.errors.subnet_group_not_found_fault.SubnetGroupNotFoundFault.from_aws_json_1_1(
                data
            )
        case "TagQuotaPerResourceExceeded":
            raise capo_memorydb.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_memorydb.types.create_cluster_response.CreateClusterResponse:
    out: capo_memorydb.types.create_cluster_response.CreateClusterResponse = (
        capo_memorydb.types.create_cluster_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_memorydb.types.create_cluster_response.CreateClusterResponse:
    out: capo_memorydb.types.create_cluster_response.CreateClusterResponse = (
        capo_memorydb.types.create_cluster_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_memorydb._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_memorydb._auth._sigv4.build_sigv4_auth_scheme(
                "memorydb", options.region
            )
        )
        if sigv4_config is not None:
            return capo_memorydb._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_memorydb.types.create_cluster_request.CreateClusterRequest,
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
    headers["X-Amz-Target"] = "AmazonMemoryDB.CreateCluster"
    body: bytes | None = json.dumps(
        capo_memorydb.types.create_cluster_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_cluster(
    options: OperationOptions,
    input_: capo_memorydb.types.create_cluster_request.CreateClusterRequest,
) -> tuple[
    capo_memorydb.types.create_cluster_response.CreateClusterResponse, zapros.Response
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


async def async_create_cluster(
    options: AsyncOperationOptions,
    input_: capo_memorydb.types.create_cluster_request.CreateClusterRequest,
) -> tuple[
    capo_memorydb.types.create_cluster_response.CreateClusterResponse, zapros.Response
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
