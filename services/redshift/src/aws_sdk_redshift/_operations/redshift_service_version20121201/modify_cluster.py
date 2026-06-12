"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyCluster``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never
from urllib.parse import urlencode

import zapros

import aws_sdk_redshift._auth._signers
import aws_sdk_redshift._auth._sigv4
from aws_sdk_redshift._protocol.errors import parse_error_metadata
from aws_sdk_redshift._protocol.xml import fromstring
from aws_sdk_redshift._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_redshift._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_redshift.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.modify_cluster_message
    import aws_sdk_redshift.types.modify_cluster_result


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "ClusterAlreadyExistsFault":
            import aws_sdk_redshift.errors.cluster_already_exists_fault

            raise aws_sdk_redshift.errors.cluster_already_exists_fault.ClusterAlreadyExistsFault.from_query(
                root
            )
        case "ClusterNotFoundFault":
            import aws_sdk_redshift.errors.cluster_not_found_fault

            raise aws_sdk_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault.from_query(
                root
            )
        case "ClusterParameterGroupNotFoundFault":
            import aws_sdk_redshift.errors.cluster_parameter_group_not_found_fault

            raise aws_sdk_redshift.errors.cluster_parameter_group_not_found_fault.ClusterParameterGroupNotFoundFault.from_query(
                root
            )
        case "ClusterSecurityGroupNotFoundFault":
            import aws_sdk_redshift.errors.cluster_security_group_not_found_fault

            raise aws_sdk_redshift.errors.cluster_security_group_not_found_fault.ClusterSecurityGroupNotFoundFault.from_query(
                root
            )
        case "CustomCnameAssociationFault":
            import aws_sdk_redshift.errors.custom_cname_association_fault

            raise aws_sdk_redshift.errors.custom_cname_association_fault.CustomCnameAssociationFault.from_query(
                root
            )
        case "DependentServiceRequestThrottlingFault":
            import aws_sdk_redshift.errors.dependent_service_request_throttling_fault

            raise aws_sdk_redshift.errors.dependent_service_request_throttling_fault.DependentServiceRequestThrottlingFault.from_query(
                root
            )
        case "HsmClientCertificateNotFoundFault":
            import aws_sdk_redshift.errors.hsm_client_certificate_not_found_fault

            raise aws_sdk_redshift.errors.hsm_client_certificate_not_found_fault.HsmClientCertificateNotFoundFault.from_query(
                root
            )
        case "HsmConfigurationNotFoundFault":
            import aws_sdk_redshift.errors.hsm_configuration_not_found_fault

            raise aws_sdk_redshift.errors.hsm_configuration_not_found_fault.HsmConfigurationNotFoundFault.from_query(
                root
            )
        case "InsufficientClusterCapacityFault":
            import aws_sdk_redshift.errors.insufficient_cluster_capacity_fault

            raise aws_sdk_redshift.errors.insufficient_cluster_capacity_fault.InsufficientClusterCapacityFault.from_query(
                root
            )
        case "InvalidClusterSecurityGroupStateFault":
            import aws_sdk_redshift.errors.invalid_cluster_security_group_state_fault

            raise aws_sdk_redshift.errors.invalid_cluster_security_group_state_fault.InvalidClusterSecurityGroupStateFault.from_query(
                root
            )
        case "InvalidClusterStateFault":
            import aws_sdk_redshift.errors.invalid_cluster_state_fault

            raise aws_sdk_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault.from_query(
                root
            )
        case "InvalidClusterTrackFault":
            import aws_sdk_redshift.errors.invalid_cluster_track_fault

            raise aws_sdk_redshift.errors.invalid_cluster_track_fault.InvalidClusterTrackFault.from_query(
                root
            )
        case "InvalidElasticIpFault":
            import aws_sdk_redshift.errors.invalid_elastic_ip_fault

            raise aws_sdk_redshift.errors.invalid_elastic_ip_fault.InvalidElasticIpFault.from_query(
                root
            )
        case "InvalidRetentionPeriodFault":
            import aws_sdk_redshift.errors.invalid_retention_period_fault

            raise aws_sdk_redshift.errors.invalid_retention_period_fault.InvalidRetentionPeriodFault.from_query(
                root
            )
        case "Ipv6CidrBlockNotFoundFault":
            import aws_sdk_redshift.errors.ipv6_cidr_block_not_found_fault

            raise aws_sdk_redshift.errors.ipv6_cidr_block_not_found_fault.Ipv6CidrBlockNotFoundFault.from_query(
                root
            )
        case "LimitExceededFault":
            import aws_sdk_redshift.errors.limit_exceeded_fault

            raise aws_sdk_redshift.errors.limit_exceeded_fault.LimitExceededFault.from_query(
                root
            )
        case "NumberOfNodesPerClusterLimitExceededFault":
            import aws_sdk_redshift.errors.number_of_nodes_per_cluster_limit_exceeded_fault

            raise aws_sdk_redshift.errors.number_of_nodes_per_cluster_limit_exceeded_fault.NumberOfNodesPerClusterLimitExceededFault.from_query(
                root
            )
        case "NumberOfNodesQuotaExceededFault":
            import aws_sdk_redshift.errors.number_of_nodes_quota_exceeded_fault

            raise aws_sdk_redshift.errors.number_of_nodes_quota_exceeded_fault.NumberOfNodesQuotaExceededFault.from_query(
                root
            )
        case "TableLimitExceededFault":
            import aws_sdk_redshift.errors.table_limit_exceeded_fault

            raise aws_sdk_redshift.errors.table_limit_exceeded_fault.TableLimitExceededFault.from_query(
                root
            )
        case "UnauthorizedOperation":
            import aws_sdk_redshift.errors.unauthorized_operation

            raise aws_sdk_redshift.errors.unauthorized_operation.UnauthorizedOperation.from_query(
                root
            )
        case "UnsupportedOperationFault":
            import aws_sdk_redshift.errors.unsupported_operation_fault

            raise aws_sdk_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault.from_query(
                root
            )
        case "UnsupportedOptionFault":
            import aws_sdk_redshift.errors.unsupported_option_fault

            raise aws_sdk_redshift.errors.unsupported_option_fault.UnsupportedOptionFault.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_redshift.types.modify_cluster_result.ModifyClusterResult:
    import aws_sdk_redshift.types.modify_cluster_result

    root = fromstring(response.read())
    result = root.find("ModifyClusterResult")
    out: aws_sdk_redshift.types.modify_cluster_result.ModifyClusterResult = (
        aws_sdk_redshift.types.modify_cluster_result.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_redshift._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_redshift._auth._sigv4.build_sigv4_auth_scheme(
                "redshift", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_redshift._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_redshift.types.modify_cluster_message.ModifyClusterMessage,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "ModifyCluster"))
    pairs.append(("Version", "2012-12-01"))
    import aws_sdk_redshift.types.modify_cluster_message

    aws_sdk_redshift.types.modify_cluster_message.serialize_query(input, pairs, "")
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def modify_cluster(
    options: OperationOptions,
    input: aws_sdk_redshift.types.modify_cluster_message.ModifyClusterMessage,
) -> tuple[
    aws_sdk_redshift.types.modify_cluster_result.ModifyClusterResult, zapros.Response
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_modify_cluster(
    options: AsyncOperationOptions,
    input: aws_sdk_redshift.types.modify_cluster_message.ModifyClusterMessage,
) -> tuple[
    aws_sdk_redshift.types.modify_cluster_result.ModifyClusterResult, zapros.Response
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
