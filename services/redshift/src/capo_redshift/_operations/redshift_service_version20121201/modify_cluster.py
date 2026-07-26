"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyCluster``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_redshift._auth._signers
import capo_redshift._auth._sigv4
import capo_redshift.errors.cluster_already_exists_fault
import capo_redshift.errors.cluster_not_found_fault
import capo_redshift.errors.cluster_parameter_group_not_found_fault
import capo_redshift.errors.cluster_security_group_not_found_fault
import capo_redshift.errors.custom_cname_association_fault
import capo_redshift.errors.dependent_service_request_throttling_fault
import capo_redshift.errors.hsm_client_certificate_not_found_fault
import capo_redshift.errors.hsm_configuration_not_found_fault
import capo_redshift.errors.insufficient_cluster_capacity_fault
import capo_redshift.errors.invalid_cluster_security_group_state_fault
import capo_redshift.errors.invalid_cluster_state_fault
import capo_redshift.errors.invalid_cluster_track_fault
import capo_redshift.errors.invalid_elastic_ip_fault
import capo_redshift.errors.invalid_retention_period_fault
import capo_redshift.errors.ipv6_cidr_block_not_found_fault
import capo_redshift.errors.limit_exceeded_fault
import capo_redshift.errors.number_of_nodes_per_cluster_limit_exceeded_fault
import capo_redshift.errors.number_of_nodes_quota_exceeded_fault
import capo_redshift.errors.table_limit_exceeded_fault
import capo_redshift.errors.unauthorized_operation
import capo_redshift.errors.unsupported_operation_fault
import capo_redshift.errors.unsupported_option_fault
import capo_redshift.types.cluster
import capo_redshift.types.cluster_security_group_name_list
import capo_redshift.types.modify_cluster_message
import capo_redshift.types.modify_cluster_result
import capo_redshift.types.vpc_security_group_id_list
from capo_redshift._protocol.errors import parse_error_metadata
from capo_redshift._protocol.xml import fromstring
from capo_redshift._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_redshift._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_redshift.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "ClusterAlreadyExistsFault":
            raise capo_redshift.errors.cluster_already_exists_fault.ClusterAlreadyExistsFault.from_query(
                root
            )
        case "ClusterNotFoundFault":
            raise capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault.from_query(
                root
            )
        case "ClusterParameterGroupNotFoundFault":
            raise capo_redshift.errors.cluster_parameter_group_not_found_fault.ClusterParameterGroupNotFoundFault.from_query(
                root
            )
        case "ClusterSecurityGroupNotFoundFault":
            raise capo_redshift.errors.cluster_security_group_not_found_fault.ClusterSecurityGroupNotFoundFault.from_query(
                root
            )
        case "CustomCnameAssociationFault":
            raise capo_redshift.errors.custom_cname_association_fault.CustomCnameAssociationFault.from_query(
                root
            )
        case "DependentServiceRequestThrottlingFault":
            raise capo_redshift.errors.dependent_service_request_throttling_fault.DependentServiceRequestThrottlingFault.from_query(
                root
            )
        case "HsmClientCertificateNotFoundFault":
            raise capo_redshift.errors.hsm_client_certificate_not_found_fault.HsmClientCertificateNotFoundFault.from_query(
                root
            )
        case "HsmConfigurationNotFoundFault":
            raise capo_redshift.errors.hsm_configuration_not_found_fault.HsmConfigurationNotFoundFault.from_query(
                root
            )
        case "InsufficientClusterCapacityFault":
            raise capo_redshift.errors.insufficient_cluster_capacity_fault.InsufficientClusterCapacityFault.from_query(
                root
            )
        case "InvalidClusterSecurityGroupStateFault":
            raise capo_redshift.errors.invalid_cluster_security_group_state_fault.InvalidClusterSecurityGroupStateFault.from_query(
                root
            )
        case "InvalidClusterStateFault":
            raise capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault.from_query(
                root
            )
        case "InvalidClusterTrackFault":
            raise capo_redshift.errors.invalid_cluster_track_fault.InvalidClusterTrackFault.from_query(
                root
            )
        case "InvalidElasticIpFault":
            raise capo_redshift.errors.invalid_elastic_ip_fault.InvalidElasticIpFault.from_query(
                root
            )
        case "InvalidRetentionPeriodFault":
            raise capo_redshift.errors.invalid_retention_period_fault.InvalidRetentionPeriodFault.from_query(
                root
            )
        case "Ipv6CidrBlockNotFoundFault":
            raise capo_redshift.errors.ipv6_cidr_block_not_found_fault.Ipv6CidrBlockNotFoundFault.from_query(
                root
            )
        case "LimitExceededFault":
            raise capo_redshift.errors.limit_exceeded_fault.LimitExceededFault.from_query(
                root
            )
        case "NumberOfNodesPerClusterLimitExceededFault":
            raise capo_redshift.errors.number_of_nodes_per_cluster_limit_exceeded_fault.NumberOfNodesPerClusterLimitExceededFault.from_query(
                root
            )
        case "NumberOfNodesQuotaExceededFault":
            raise capo_redshift.errors.number_of_nodes_quota_exceeded_fault.NumberOfNodesQuotaExceededFault.from_query(
                root
            )
        case "TableLimitExceededFault":
            raise capo_redshift.errors.table_limit_exceeded_fault.TableLimitExceededFault.from_query(
                root
            )
        case "UnauthorizedOperation":
            raise capo_redshift.errors.unauthorized_operation.UnauthorizedOperation.from_query(
                root
            )
        case "UnsupportedOperationFault":
            raise capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault.from_query(
                root
            )
        case "UnsupportedOptionFault":
            raise capo_redshift.errors.unsupported_option_fault.UnsupportedOptionFault.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_redshift.types.modify_cluster_result.ModifyClusterResult:
    root = fromstring(response.read())
    result = root.find("ModifyClusterResult")
    out: capo_redshift.types.modify_cluster_result.ModifyClusterResult = (
        capo_redshift.types.modify_cluster_result.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_redshift.types.modify_cluster_result.ModifyClusterResult:
    root = fromstring(await response.aread())
    result = root.find("ModifyClusterResult")
    out: capo_redshift.types.modify_cluster_result.ModifyClusterResult = (
        capo_redshift.types.modify_cluster_result.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_redshift._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_redshift._auth._sigv4.build_sigv4_auth_scheme(
                "redshift", options.region
            )
        )
        if sigv4_config is not None:
            return capo_redshift._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_redshift.types.modify_cluster_message.ModifyClusterMessage,
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
    pairs.append(("Action", "ModifyCluster"))
    pairs.append(("Version", "2012-12-01"))
    capo_redshift.types.modify_cluster_message.serialize_query(input_, pairs, "")
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def modify_cluster(
    options: OperationOptions,
    input_: capo_redshift.types.modify_cluster_message.ModifyClusterMessage,
) -> tuple[
    capo_redshift.types.modify_cluster_result.ModifyClusterResult, zapros.Response
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


async def async_modify_cluster(
    options: AsyncOperationOptions,
    input_: capo_redshift.types.modify_cluster_message.ModifyClusterMessage,
) -> tuple[
    capo_redshift.types.modify_cluster_result.ModifyClusterResult, zapros.Response
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
