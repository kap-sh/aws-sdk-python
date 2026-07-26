"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBInstanceReadReplica``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_rds._auth._signers
import capo_rds._auth._sigv4
import capo_rds.errors.certificate_not_found_fault
import capo_rds.errors.db_cluster_not_found_fault
import capo_rds.errors.db_instance_already_exists_fault
import capo_rds.errors.db_instance_not_found_fault
import capo_rds.errors.db_parameter_group_not_found_fault
import capo_rds.errors.db_security_group_not_found_fault
import capo_rds.errors.db_subnet_group_does_not_cover_enough_a_zs
import capo_rds.errors.db_subnet_group_not_allowed_fault
import capo_rds.errors.db_subnet_group_not_found_fault
import capo_rds.errors.domain_not_found_fault
import capo_rds.errors.instance_quota_exceeded_fault
import capo_rds.errors.insufficient_db_instance_capacity_fault
import capo_rds.errors.invalid_db_cluster_state_fault
import capo_rds.errors.invalid_db_instance_state_fault
import capo_rds.errors.invalid_db_subnet_group_fault
import capo_rds.errors.invalid_subnet
import capo_rds.errors.invalid_vpc_network_state_fault
import capo_rds.errors.kms_key_not_accessible_fault
import capo_rds.errors.network_type_not_supported
import capo_rds.errors.option_group_not_found_fault
import capo_rds.errors.provisioned_iops_not_available_in_az_fault
import capo_rds.errors.storage_quota_exceeded_fault
import capo_rds.errors.storage_type_not_supported_fault
import capo_rds.errors.tenant_database_quota_exceeded_fault
import capo_rds.errors.vpc_encryption_control_violation_exception
import capo_rds.types.additional_storage_volumes_list
import capo_rds.types.create_db_instance_read_replica_message
import capo_rds.types.create_db_instance_read_replica_result
import capo_rds.types.database_insights_mode
import capo_rds.types.db_instance
import capo_rds.types.log_type_list
import capo_rds.types.processor_feature_list
import capo_rds.types.replica_mode
import capo_rds.types.string_list
import capo_rds.types.tag_list
import capo_rds.types.tag_specification_list
import capo_rds.types.vpc_security_group_id_list
from capo_rds._protocol.errors import parse_error_metadata
from capo_rds._protocol.xml import fromstring
from capo_rds._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_rds._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_rds.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "CertificateNotFoundFault":
            raise capo_rds.errors.certificate_not_found_fault.CertificateNotFoundFault.from_query(
                root
            )
        case "DBClusterNotFoundFault":
            raise capo_rds.errors.db_cluster_not_found_fault.DBClusterNotFoundFault.from_query(
                root
            )
        case "DBInstanceAlreadyExistsFault":
            raise capo_rds.errors.db_instance_already_exists_fault.DBInstanceAlreadyExistsFault.from_query(
                root
            )
        case "DBInstanceNotFoundFault":
            raise capo_rds.errors.db_instance_not_found_fault.DBInstanceNotFoundFault.from_query(
                root
            )
        case "DBParameterGroupNotFoundFault":
            raise capo_rds.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault.from_query(
                root
            )
        case "DBSecurityGroupNotFoundFault":
            raise capo_rds.errors.db_security_group_not_found_fault.DBSecurityGroupNotFoundFault.from_query(
                root
            )
        case "DBSubnetGroupDoesNotCoverEnoughAZs":
            raise capo_rds.errors.db_subnet_group_does_not_cover_enough_a_zs.DBSubnetGroupDoesNotCoverEnoughAZs.from_query(
                root
            )
        case "DBSubnetGroupNotAllowedFault":
            raise capo_rds.errors.db_subnet_group_not_allowed_fault.DBSubnetGroupNotAllowedFault.from_query(
                root
            )
        case "DBSubnetGroupNotFoundFault":
            raise capo_rds.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault.from_query(
                root
            )
        case "DomainNotFoundFault":
            raise capo_rds.errors.domain_not_found_fault.DomainNotFoundFault.from_query(
                root
            )
        case "InstanceQuotaExceededFault":
            raise capo_rds.errors.instance_quota_exceeded_fault.InstanceQuotaExceededFault.from_query(
                root
            )
        case "InsufficientDBInstanceCapacityFault":
            raise capo_rds.errors.insufficient_db_instance_capacity_fault.InsufficientDBInstanceCapacityFault.from_query(
                root
            )
        case "InvalidDBClusterStateFault":
            raise capo_rds.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault.from_query(
                root
            )
        case "InvalidDBInstanceStateFault":
            raise capo_rds.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault.from_query(
                root
            )
        case "InvalidDBSubnetGroupFault":
            raise capo_rds.errors.invalid_db_subnet_group_fault.InvalidDBSubnetGroupFault.from_query(
                root
            )
        case "InvalidSubnet":
            raise capo_rds.errors.invalid_subnet.InvalidSubnet.from_query(root)
        case "InvalidVPCNetworkStateFault":
            raise capo_rds.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault.from_query(
                root
            )
        case "KMSKeyNotAccessibleFault":
            raise capo_rds.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault.from_query(
                root
            )
        case "NetworkTypeNotSupported":
            raise capo_rds.errors.network_type_not_supported.NetworkTypeNotSupported.from_query(
                root
            )
        case "OptionGroupNotFoundFault":
            raise capo_rds.errors.option_group_not_found_fault.OptionGroupNotFoundFault.from_query(
                root
            )
        case "ProvisionedIopsNotAvailableInAZFault":
            raise capo_rds.errors.provisioned_iops_not_available_in_az_fault.ProvisionedIopsNotAvailableInAZFault.from_query(
                root
            )
        case "StorageQuotaExceededFault":
            raise capo_rds.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault.from_query(
                root
            )
        case "StorageTypeNotSupportedFault":
            raise capo_rds.errors.storage_type_not_supported_fault.StorageTypeNotSupportedFault.from_query(
                root
            )
        case "TenantDatabaseQuotaExceededFault":
            raise capo_rds.errors.tenant_database_quota_exceeded_fault.TenantDatabaseQuotaExceededFault.from_query(
                root
            )
        case "VpcEncryptionControlViolationException":
            raise capo_rds.errors.vpc_encryption_control_violation_exception.VpcEncryptionControlViolationException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_rds.types.create_db_instance_read_replica_result.CreateDBInstanceReadReplicaResult:
    root = fromstring(response.read())
    result = root.find("CreateDBInstanceReadReplicaResult")
    out: capo_rds.types.create_db_instance_read_replica_result.CreateDBInstanceReadReplicaResult = capo_rds.types.create_db_instance_read_replica_result.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_rds.types.create_db_instance_read_replica_result.CreateDBInstanceReadReplicaResult:
    root = fromstring(await response.aread())
    result = root.find("CreateDBInstanceReadReplicaResult")
    out: capo_rds.types.create_db_instance_read_replica_result.CreateDBInstanceReadReplicaResult = capo_rds.types.create_db_instance_read_replica_result.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_rds._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_rds._auth._sigv4.build_sigv4_auth_scheme("rds", options.region)
        )
        if sigv4_config is not None:
            return capo_rds._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_rds.types.create_db_instance_read_replica_message.CreateDBInstanceReadReplicaMessage,
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
    pairs.append(("Action", "CreateDBInstanceReadReplica"))
    pairs.append(("Version", "2014-10-31"))
    capo_rds.types.create_db_instance_read_replica_message.serialize_query(
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


def create_db_instance_read_replica(
    options: OperationOptions,
    input_: capo_rds.types.create_db_instance_read_replica_message.CreateDBInstanceReadReplicaMessage,
) -> tuple[
    capo_rds.types.create_db_instance_read_replica_result.CreateDBInstanceReadReplicaResult,
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


async def async_create_db_instance_read_replica(
    options: AsyncOperationOptions,
    input_: capo_rds.types.create_db_instance_read_replica_message.CreateDBInstanceReadReplicaMessage,
) -> tuple[
    capo_rds.types.create_db_instance_read_replica_result.CreateDBInstanceReadReplicaResult,
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
