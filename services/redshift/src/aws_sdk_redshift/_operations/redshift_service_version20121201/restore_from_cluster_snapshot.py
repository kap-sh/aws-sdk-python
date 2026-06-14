"""Generated from Smithy shape ``com.amazonaws.redshift#RestoreFromClusterSnapshot``."""

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
    import aws_sdk_redshift.types.restore_from_cluster_snapshot_message
    import aws_sdk_redshift.types.restore_from_cluster_snapshot_result


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AccessToSnapshotDeniedFault":
            import aws_sdk_redshift.errors.access_to_snapshot_denied_fault

            raise aws_sdk_redshift.errors.access_to_snapshot_denied_fault.AccessToSnapshotDeniedFault.from_query(
                root
            )
        case "ClusterAlreadyExistsFault":
            import aws_sdk_redshift.errors.cluster_already_exists_fault

            raise aws_sdk_redshift.errors.cluster_already_exists_fault.ClusterAlreadyExistsFault.from_query(
                root
            )
        case "ClusterParameterGroupNotFoundFault":
            import aws_sdk_redshift.errors.cluster_parameter_group_not_found_fault

            raise aws_sdk_redshift.errors.cluster_parameter_group_not_found_fault.ClusterParameterGroupNotFoundFault.from_query(
                root
            )
        case "ClusterQuotaExceededFault":
            import aws_sdk_redshift.errors.cluster_quota_exceeded_fault

            raise aws_sdk_redshift.errors.cluster_quota_exceeded_fault.ClusterQuotaExceededFault.from_query(
                root
            )
        case "ClusterSecurityGroupNotFoundFault":
            import aws_sdk_redshift.errors.cluster_security_group_not_found_fault

            raise aws_sdk_redshift.errors.cluster_security_group_not_found_fault.ClusterSecurityGroupNotFoundFault.from_query(
                root
            )
        case "ClusterSnapshotNotFoundFault":
            import aws_sdk_redshift.errors.cluster_snapshot_not_found_fault

            raise aws_sdk_redshift.errors.cluster_snapshot_not_found_fault.ClusterSnapshotNotFoundFault.from_query(
                root
            )
        case "ClusterSubnetGroupNotFoundFault":
            import aws_sdk_redshift.errors.cluster_subnet_group_not_found_fault

            raise aws_sdk_redshift.errors.cluster_subnet_group_not_found_fault.ClusterSubnetGroupNotFoundFault.from_query(
                root
            )
        case "DependentServiceAccessDeniedFault":
            import aws_sdk_redshift.errors.dependent_service_access_denied_fault

            raise aws_sdk_redshift.errors.dependent_service_access_denied_fault.DependentServiceAccessDeniedFault.from_query(
                root
            )
        case "DependentServiceRequestThrottlingFault":
            import aws_sdk_redshift.errors.dependent_service_request_throttling_fault

            raise aws_sdk_redshift.errors.dependent_service_request_throttling_fault.DependentServiceRequestThrottlingFault.from_query(
                root
            )
        case "DependentServiceUnavailableFault":
            import aws_sdk_redshift.errors.dependent_service_unavailable_fault

            raise aws_sdk_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault.from_query(
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
        case "InvalidClusterSnapshotStateFault":
            import aws_sdk_redshift.errors.invalid_cluster_snapshot_state_fault

            raise aws_sdk_redshift.errors.invalid_cluster_snapshot_state_fault.InvalidClusterSnapshotStateFault.from_query(
                root
            )
        case "InvalidClusterSubnetGroupStateFault":
            import aws_sdk_redshift.errors.invalid_cluster_subnet_group_state_fault

            raise aws_sdk_redshift.errors.invalid_cluster_subnet_group_state_fault.InvalidClusterSubnetGroupStateFault.from_query(
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
        case "InvalidReservedNodeStateFault":
            import aws_sdk_redshift.errors.invalid_reserved_node_state_fault

            raise aws_sdk_redshift.errors.invalid_reserved_node_state_fault.InvalidReservedNodeStateFault.from_query(
                root
            )
        case "InvalidRestoreFault":
            import aws_sdk_redshift.errors.invalid_restore_fault

            raise aws_sdk_redshift.errors.invalid_restore_fault.InvalidRestoreFault.from_query(
                root
            )
        case "InvalidSubnet":
            import aws_sdk_redshift.errors.invalid_subnet

            raise aws_sdk_redshift.errors.invalid_subnet.InvalidSubnet.from_query(root)
        case "InvalidTagFault":
            import aws_sdk_redshift.errors.invalid_tag_fault

            raise aws_sdk_redshift.errors.invalid_tag_fault.InvalidTagFault.from_query(
                root
            )
        case "InvalidVPCNetworkStateFault":
            import aws_sdk_redshift.errors.invalid_vpc_network_state_fault

            raise aws_sdk_redshift.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault.from_query(
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
        case "RedshiftIdcApplicationNotExistsFault":
            import aws_sdk_redshift.errors.redshift_idc_application_not_exists_fault

            raise aws_sdk_redshift.errors.redshift_idc_application_not_exists_fault.RedshiftIdcApplicationNotExistsFault.from_query(
                root
            )
        case "ReservedNodeAlreadyExistsFault":
            import aws_sdk_redshift.errors.reserved_node_already_exists_fault

            raise aws_sdk_redshift.errors.reserved_node_already_exists_fault.ReservedNodeAlreadyExistsFault.from_query(
                root
            )
        case "ReservedNodeAlreadyMigratedFault":
            import aws_sdk_redshift.errors.reserved_node_already_migrated_fault

            raise aws_sdk_redshift.errors.reserved_node_already_migrated_fault.ReservedNodeAlreadyMigratedFault.from_query(
                root
            )
        case "ReservedNodeNotFoundFault":
            import aws_sdk_redshift.errors.reserved_node_not_found_fault

            raise aws_sdk_redshift.errors.reserved_node_not_found_fault.ReservedNodeNotFoundFault.from_query(
                root
            )
        case "ReservedNodeOfferingNotFoundFault":
            import aws_sdk_redshift.errors.reserved_node_offering_not_found_fault

            raise aws_sdk_redshift.errors.reserved_node_offering_not_found_fault.ReservedNodeOfferingNotFoundFault.from_query(
                root
            )
        case "SnapshotScheduleNotFoundFault":
            import aws_sdk_redshift.errors.snapshot_schedule_not_found_fault

            raise aws_sdk_redshift.errors.snapshot_schedule_not_found_fault.SnapshotScheduleNotFoundFault.from_query(
                root
            )
        case "TagLimitExceededFault":
            import aws_sdk_redshift.errors.tag_limit_exceeded_fault

            raise aws_sdk_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault.from_query(
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
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_redshift.types.restore_from_cluster_snapshot_result.RestoreFromClusterSnapshotResult:
    import aws_sdk_redshift.types.restore_from_cluster_snapshot_result

    root = fromstring(response.read())
    result = root.find("RestoreFromClusterSnapshotResult")
    out: aws_sdk_redshift.types.restore_from_cluster_snapshot_result.RestoreFromClusterSnapshotResult = aws_sdk_redshift.types.restore_from_cluster_snapshot_result.deserialize_query(
        result if result is not None else root
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
    input_: aws_sdk_redshift.types.restore_from_cluster_snapshot_message.RestoreFromClusterSnapshotMessage,
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
    pairs.append(("Action", "RestoreFromClusterSnapshot"))
    pairs.append(("Version", "2012-12-01"))
    import aws_sdk_redshift.types.restore_from_cluster_snapshot_message

    aws_sdk_redshift.types.restore_from_cluster_snapshot_message.serialize_query(
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


def restore_from_cluster_snapshot(
    options: OperationOptions,
    input_: aws_sdk_redshift.types.restore_from_cluster_snapshot_message.RestoreFromClusterSnapshotMessage,
) -> tuple[
    aws_sdk_redshift.types.restore_from_cluster_snapshot_result.RestoreFromClusterSnapshotResult,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_restore_from_cluster_snapshot(
    options: AsyncOperationOptions,
    input_: aws_sdk_redshift.types.restore_from_cluster_snapshot_message.RestoreFromClusterSnapshotMessage,
) -> tuple[
    aws_sdk_redshift.types.restore_from_cluster_snapshot_result.RestoreFromClusterSnapshotResult,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
