"""Generated from Smithy shape ``com.amazonaws.rds#RestoreDBInstanceFromDBSnapshot``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_rds._auth._signers
import aws_sdk_rds._auth._sigv4
import aws_sdk_rds.errors.authorization_not_found_fault
import aws_sdk_rds.errors.backup_policy_not_found_fault
import aws_sdk_rds.errors.certificate_not_found_fault
import aws_sdk_rds.errors.db_cluster_snapshot_not_found_fault
import aws_sdk_rds.errors.db_instance_already_exists_fault
import aws_sdk_rds.errors.db_parameter_group_not_found_fault
import aws_sdk_rds.errors.db_security_group_not_found_fault
import aws_sdk_rds.errors.db_snapshot_not_found_fault
import aws_sdk_rds.errors.db_subnet_group_does_not_cover_enough_a_zs
import aws_sdk_rds.errors.db_subnet_group_not_found_fault
import aws_sdk_rds.errors.domain_not_found_fault
import aws_sdk_rds.errors.instance_quota_exceeded_fault
import aws_sdk_rds.errors.insufficient_db_instance_capacity_fault
import aws_sdk_rds.errors.invalid_db_snapshot_state_fault
import aws_sdk_rds.errors.invalid_restore_fault
import aws_sdk_rds.errors.invalid_subnet
import aws_sdk_rds.errors.invalid_vpc_network_state_fault
import aws_sdk_rds.errors.kms_key_not_accessible_fault
import aws_sdk_rds.errors.network_type_not_supported
import aws_sdk_rds.errors.option_group_not_found_fault
import aws_sdk_rds.errors.provisioned_iops_not_available_in_az_fault
import aws_sdk_rds.errors.storage_quota_exceeded_fault
import aws_sdk_rds.errors.storage_type_not_supported_fault
import aws_sdk_rds.errors.tenant_database_quota_exceeded_fault
import aws_sdk_rds.errors.vpc_encryption_control_violation_exception
import aws_sdk_rds.types.additional_storage_volumes_list
import aws_sdk_rds.types.db_instance
import aws_sdk_rds.types.log_type_list
import aws_sdk_rds.types.processor_feature_list
import aws_sdk_rds.types.restore_db_instance_from_db_snapshot_message
import aws_sdk_rds.types.restore_db_instance_from_db_snapshot_result
import aws_sdk_rds.types.string_list
import aws_sdk_rds.types.tag_list
import aws_sdk_rds.types.tag_specification_list
import aws_sdk_rds.types.vpc_security_group_id_list
from aws_sdk_rds._protocol.errors import parse_error_metadata
from aws_sdk_rds._protocol.xml import fromstring
from aws_sdk_rds._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_rds._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_rds.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AuthorizationNotFoundFault":
            raise aws_sdk_rds.errors.authorization_not_found_fault.AuthorizationNotFoundFault.from_query(
                root
            )
        case "BackupPolicyNotFoundFault":
            raise aws_sdk_rds.errors.backup_policy_not_found_fault.BackupPolicyNotFoundFault.from_query(
                root
            )
        case "CertificateNotFoundFault":
            raise aws_sdk_rds.errors.certificate_not_found_fault.CertificateNotFoundFault.from_query(
                root
            )
        case "DBClusterSnapshotNotFoundFault":
            raise aws_sdk_rds.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault.from_query(
                root
            )
        case "DBInstanceAlreadyExistsFault":
            raise aws_sdk_rds.errors.db_instance_already_exists_fault.DBInstanceAlreadyExistsFault.from_query(
                root
            )
        case "DBParameterGroupNotFoundFault":
            raise aws_sdk_rds.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault.from_query(
                root
            )
        case "DBSecurityGroupNotFoundFault":
            raise aws_sdk_rds.errors.db_security_group_not_found_fault.DBSecurityGroupNotFoundFault.from_query(
                root
            )
        case "DBSnapshotNotFoundFault":
            raise aws_sdk_rds.errors.db_snapshot_not_found_fault.DBSnapshotNotFoundFault.from_query(
                root
            )
        case "DBSubnetGroupDoesNotCoverEnoughAZs":
            raise aws_sdk_rds.errors.db_subnet_group_does_not_cover_enough_a_zs.DBSubnetGroupDoesNotCoverEnoughAZs.from_query(
                root
            )
        case "DBSubnetGroupNotFoundFault":
            raise aws_sdk_rds.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault.from_query(
                root
            )
        case "DomainNotFoundFault":
            raise aws_sdk_rds.errors.domain_not_found_fault.DomainNotFoundFault.from_query(
                root
            )
        case "InstanceQuotaExceededFault":
            raise aws_sdk_rds.errors.instance_quota_exceeded_fault.InstanceQuotaExceededFault.from_query(
                root
            )
        case "InsufficientDBInstanceCapacityFault":
            raise aws_sdk_rds.errors.insufficient_db_instance_capacity_fault.InsufficientDBInstanceCapacityFault.from_query(
                root
            )
        case "InvalidDBSnapshotStateFault":
            raise aws_sdk_rds.errors.invalid_db_snapshot_state_fault.InvalidDBSnapshotStateFault.from_query(
                root
            )
        case "InvalidRestoreFault":
            raise aws_sdk_rds.errors.invalid_restore_fault.InvalidRestoreFault.from_query(
                root
            )
        case "InvalidSubnet":
            raise aws_sdk_rds.errors.invalid_subnet.InvalidSubnet.from_query(root)
        case "InvalidVPCNetworkStateFault":
            raise aws_sdk_rds.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault.from_query(
                root
            )
        case "KMSKeyNotAccessibleFault":
            raise aws_sdk_rds.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault.from_query(
                root
            )
        case "NetworkTypeNotSupported":
            raise aws_sdk_rds.errors.network_type_not_supported.NetworkTypeNotSupported.from_query(
                root
            )
        case "OptionGroupNotFoundFault":
            raise aws_sdk_rds.errors.option_group_not_found_fault.OptionGroupNotFoundFault.from_query(
                root
            )
        case "ProvisionedIopsNotAvailableInAZFault":
            raise aws_sdk_rds.errors.provisioned_iops_not_available_in_az_fault.ProvisionedIopsNotAvailableInAZFault.from_query(
                root
            )
        case "StorageQuotaExceededFault":
            raise aws_sdk_rds.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault.from_query(
                root
            )
        case "StorageTypeNotSupportedFault":
            raise aws_sdk_rds.errors.storage_type_not_supported_fault.StorageTypeNotSupportedFault.from_query(
                root
            )
        case "TenantDatabaseQuotaExceededFault":
            raise aws_sdk_rds.errors.tenant_database_quota_exceeded_fault.TenantDatabaseQuotaExceededFault.from_query(
                root
            )
        case "VpcEncryptionControlViolationException":
            raise aws_sdk_rds.errors.vpc_encryption_control_violation_exception.VpcEncryptionControlViolationException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_rds.types.restore_db_instance_from_db_snapshot_result.RestoreDBInstanceFromDBSnapshotResult:
    root = fromstring(response.read())
    result = root.find("RestoreDBInstanceFromDBSnapshotResult")
    out: aws_sdk_rds.types.restore_db_instance_from_db_snapshot_result.RestoreDBInstanceFromDBSnapshotResult = aws_sdk_rds.types.restore_db_instance_from_db_snapshot_result.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_rds.types.restore_db_instance_from_db_snapshot_result.RestoreDBInstanceFromDBSnapshotResult:
    root = fromstring(await response.aread())
    result = root.find("RestoreDBInstanceFromDBSnapshotResult")
    out: aws_sdk_rds.types.restore_db_instance_from_db_snapshot_result.RestoreDBInstanceFromDBSnapshotResult = aws_sdk_rds.types.restore_db_instance_from_db_snapshot_result.deserialize_query(
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
    input_: aws_sdk_rds.types.restore_db_instance_from_db_snapshot_message.RestoreDBInstanceFromDBSnapshotMessage,
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
    pairs.append(("Action", "RestoreDBInstanceFromDBSnapshot"))
    pairs.append(("Version", "2014-10-31"))
    import aws_sdk_rds.types.restore_db_instance_from_db_snapshot_message

    aws_sdk_rds.types.restore_db_instance_from_db_snapshot_message.serialize_query(
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


def restore_db_instance_from_db_snapshot(
    options: OperationOptions,
    input_: aws_sdk_rds.types.restore_db_instance_from_db_snapshot_message.RestoreDBInstanceFromDBSnapshotMessage,
) -> tuple[
    aws_sdk_rds.types.restore_db_instance_from_db_snapshot_result.RestoreDBInstanceFromDBSnapshotResult,
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


async def async_restore_db_instance_from_db_snapshot(
    options: AsyncOperationOptions,
    input_: aws_sdk_rds.types.restore_db_instance_from_db_snapshot_message.RestoreDBInstanceFromDBSnapshotMessage,
) -> tuple[
    aws_sdk_rds.types.restore_db_instance_from_db_snapshot_result.RestoreDBInstanceFromDBSnapshotResult,
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
