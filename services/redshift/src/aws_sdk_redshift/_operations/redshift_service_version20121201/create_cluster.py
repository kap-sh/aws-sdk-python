"""Generated from Smithy shape ``com.amazonaws.redshift#CreateCluster``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_redshift._auth._signers
import aws_sdk_redshift._auth._sigv4
import aws_sdk_redshift.errors.cluster_already_exists_fault
import aws_sdk_redshift.errors.cluster_parameter_group_not_found_fault
import aws_sdk_redshift.errors.cluster_quota_exceeded_fault
import aws_sdk_redshift.errors.cluster_security_group_not_found_fault
import aws_sdk_redshift.errors.cluster_subnet_group_not_found_fault
import aws_sdk_redshift.errors.dependent_service_access_denied_fault
import aws_sdk_redshift.errors.dependent_service_request_throttling_fault
import aws_sdk_redshift.errors.dependent_service_unavailable_fault
import aws_sdk_redshift.errors.hsm_client_certificate_not_found_fault
import aws_sdk_redshift.errors.hsm_configuration_not_found_fault
import aws_sdk_redshift.errors.insufficient_cluster_capacity_fault
import aws_sdk_redshift.errors.invalid_cluster_subnet_group_state_fault
import aws_sdk_redshift.errors.invalid_cluster_track_fault
import aws_sdk_redshift.errors.invalid_elastic_ip_fault
import aws_sdk_redshift.errors.invalid_retention_period_fault
import aws_sdk_redshift.errors.invalid_subnet
import aws_sdk_redshift.errors.invalid_tag_fault
import aws_sdk_redshift.errors.invalid_vpc_network_state_fault
import aws_sdk_redshift.errors.ipv6_cidr_block_not_found_fault
import aws_sdk_redshift.errors.limit_exceeded_fault
import aws_sdk_redshift.errors.number_of_nodes_per_cluster_limit_exceeded_fault
import aws_sdk_redshift.errors.number_of_nodes_quota_exceeded_fault
import aws_sdk_redshift.errors.redshift_idc_application_not_exists_fault
import aws_sdk_redshift.errors.snapshot_schedule_not_found_fault
import aws_sdk_redshift.errors.tag_limit_exceeded_fault
import aws_sdk_redshift.errors.unauthorized_operation
import aws_sdk_redshift.errors.unsupported_operation_fault
import aws_sdk_redshift.types.aqua_configuration_status
import aws_sdk_redshift.types.cluster
import aws_sdk_redshift.types.cluster_security_group_name_list
import aws_sdk_redshift.types.create_cluster_message
import aws_sdk_redshift.types.create_cluster_result
import aws_sdk_redshift.types.iam_role_arn_list
import aws_sdk_redshift.types.tag_list
import aws_sdk_redshift.types.vpc_security_group_id_list
from aws_sdk_redshift._protocol.errors import parse_error_metadata
from aws_sdk_redshift._protocol.xml import fromstring
from aws_sdk_redshift._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_redshift._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_redshift.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "ClusterAlreadyExistsFault":
            raise aws_sdk_redshift.errors.cluster_already_exists_fault.ClusterAlreadyExistsFault.from_query(
                root
            )
        case "ClusterParameterGroupNotFoundFault":
            raise aws_sdk_redshift.errors.cluster_parameter_group_not_found_fault.ClusterParameterGroupNotFoundFault.from_query(
                root
            )
        case "ClusterQuotaExceededFault":
            raise aws_sdk_redshift.errors.cluster_quota_exceeded_fault.ClusterQuotaExceededFault.from_query(
                root
            )
        case "ClusterSecurityGroupNotFoundFault":
            raise aws_sdk_redshift.errors.cluster_security_group_not_found_fault.ClusterSecurityGroupNotFoundFault.from_query(
                root
            )
        case "ClusterSubnetGroupNotFoundFault":
            raise aws_sdk_redshift.errors.cluster_subnet_group_not_found_fault.ClusterSubnetGroupNotFoundFault.from_query(
                root
            )
        case "DependentServiceAccessDeniedFault":
            raise aws_sdk_redshift.errors.dependent_service_access_denied_fault.DependentServiceAccessDeniedFault.from_query(
                root
            )
        case "DependentServiceRequestThrottlingFault":
            raise aws_sdk_redshift.errors.dependent_service_request_throttling_fault.DependentServiceRequestThrottlingFault.from_query(
                root
            )
        case "DependentServiceUnavailableFault":
            raise aws_sdk_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault.from_query(
                root
            )
        case "HsmClientCertificateNotFoundFault":
            raise aws_sdk_redshift.errors.hsm_client_certificate_not_found_fault.HsmClientCertificateNotFoundFault.from_query(
                root
            )
        case "HsmConfigurationNotFoundFault":
            raise aws_sdk_redshift.errors.hsm_configuration_not_found_fault.HsmConfigurationNotFoundFault.from_query(
                root
            )
        case "InsufficientClusterCapacityFault":
            raise aws_sdk_redshift.errors.insufficient_cluster_capacity_fault.InsufficientClusterCapacityFault.from_query(
                root
            )
        case "InvalidClusterSubnetGroupStateFault":
            raise aws_sdk_redshift.errors.invalid_cluster_subnet_group_state_fault.InvalidClusterSubnetGroupStateFault.from_query(
                root
            )
        case "InvalidClusterTrackFault":
            raise aws_sdk_redshift.errors.invalid_cluster_track_fault.InvalidClusterTrackFault.from_query(
                root
            )
        case "InvalidElasticIpFault":
            raise aws_sdk_redshift.errors.invalid_elastic_ip_fault.InvalidElasticIpFault.from_query(
                root
            )
        case "InvalidRetentionPeriodFault":
            raise aws_sdk_redshift.errors.invalid_retention_period_fault.InvalidRetentionPeriodFault.from_query(
                root
            )
        case "InvalidSubnet":
            raise aws_sdk_redshift.errors.invalid_subnet.InvalidSubnet.from_query(root)
        case "InvalidTagFault":
            raise aws_sdk_redshift.errors.invalid_tag_fault.InvalidTagFault.from_query(
                root
            )
        case "InvalidVPCNetworkStateFault":
            raise aws_sdk_redshift.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault.from_query(
                root
            )
        case "Ipv6CidrBlockNotFoundFault":
            raise aws_sdk_redshift.errors.ipv6_cidr_block_not_found_fault.Ipv6CidrBlockNotFoundFault.from_query(
                root
            )
        case "LimitExceededFault":
            raise aws_sdk_redshift.errors.limit_exceeded_fault.LimitExceededFault.from_query(
                root
            )
        case "NumberOfNodesPerClusterLimitExceededFault":
            raise aws_sdk_redshift.errors.number_of_nodes_per_cluster_limit_exceeded_fault.NumberOfNodesPerClusterLimitExceededFault.from_query(
                root
            )
        case "NumberOfNodesQuotaExceededFault":
            raise aws_sdk_redshift.errors.number_of_nodes_quota_exceeded_fault.NumberOfNodesQuotaExceededFault.from_query(
                root
            )
        case "RedshiftIdcApplicationNotExistsFault":
            raise aws_sdk_redshift.errors.redshift_idc_application_not_exists_fault.RedshiftIdcApplicationNotExistsFault.from_query(
                root
            )
        case "SnapshotScheduleNotFoundFault":
            raise aws_sdk_redshift.errors.snapshot_schedule_not_found_fault.SnapshotScheduleNotFoundFault.from_query(
                root
            )
        case "TagLimitExceededFault":
            raise aws_sdk_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault.from_query(
                root
            )
        case "UnauthorizedOperation":
            raise aws_sdk_redshift.errors.unauthorized_operation.UnauthorizedOperation.from_query(
                root
            )
        case "UnsupportedOperationFault":
            raise aws_sdk_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_redshift.types.create_cluster_result.CreateClusterResult:
    root = fromstring(response.read())
    result = root.find("CreateClusterResult")
    out: aws_sdk_redshift.types.create_cluster_result.CreateClusterResult = (
        aws_sdk_redshift.types.create_cluster_result.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_redshift.types.create_cluster_result.CreateClusterResult:
    root = fromstring(await response.aread())
    result = root.find("CreateClusterResult")
    out: aws_sdk_redshift.types.create_cluster_result.CreateClusterResult = (
        aws_sdk_redshift.types.create_cluster_result.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_redshift._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_redshift.types.create_cluster_message.CreateClusterMessage,
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
    pairs.append(("Action", "CreateCluster"))
    pairs.append(("Version", "2012-12-01"))
    import aws_sdk_redshift.types.create_cluster_message

    aws_sdk_redshift.types.create_cluster_message.serialize_query(input_, pairs, "")
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_cluster(
    options: OperationOptions,
    input_: aws_sdk_redshift.types.create_cluster_message.CreateClusterMessage,
) -> tuple[
    aws_sdk_redshift.types.create_cluster_result.CreateClusterResult, zapros.Response
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
    input_: aws_sdk_redshift.types.create_cluster_message.CreateClusterMessage,
) -> tuple[
    aws_sdk_redshift.types.create_cluster_result.CreateClusterResult, zapros.Response
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
