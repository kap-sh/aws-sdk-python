"""Generated from Smithy shape ``com.amazonaws.neptune#ModifyDBInstance``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_neptune._auth._signers
import capo_neptune._auth._sigv4
import capo_neptune.errors.authorization_not_found_fault
import capo_neptune.errors.certificate_not_found_fault
import capo_neptune.errors.db_instance_already_exists_fault
import capo_neptune.errors.db_instance_not_found_fault
import capo_neptune.errors.db_parameter_group_not_found_fault
import capo_neptune.errors.db_security_group_not_found_fault
import capo_neptune.errors.db_upgrade_dependency_failure_fault
import capo_neptune.errors.domain_not_found_fault
import capo_neptune.errors.insufficient_db_instance_capacity_fault
import capo_neptune.errors.invalid_db_instance_state_fault
import capo_neptune.errors.invalid_db_security_group_state_fault
import capo_neptune.errors.invalid_vpc_network_state_fault
import capo_neptune.errors.option_group_not_found_fault
import capo_neptune.errors.provisioned_iops_not_available_in_az_fault
import capo_neptune.errors.storage_quota_exceeded_fault
import capo_neptune.errors.storage_type_not_supported_fault
import capo_neptune.types.cloudwatch_logs_export_configuration
import capo_neptune.types.db_instance
import capo_neptune.types.db_security_group_name_list
import capo_neptune.types.modify_db_instance_message
import capo_neptune.types.modify_db_instance_result
import capo_neptune.types.vpc_security_group_id_list
from capo_neptune._protocol.errors import parse_error_metadata
from capo_neptune._protocol.xml import fromstring
from capo_neptune._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_neptune._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_neptune.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AuthorizationNotFoundFault":
            raise capo_neptune.errors.authorization_not_found_fault.AuthorizationNotFoundFault.from_query(
                root
            )
        case "CertificateNotFoundFault":
            raise capo_neptune.errors.certificate_not_found_fault.CertificateNotFoundFault.from_query(
                root
            )
        case "DBInstanceAlreadyExistsFault":
            raise capo_neptune.errors.db_instance_already_exists_fault.DBInstanceAlreadyExistsFault.from_query(
                root
            )
        case "DBInstanceNotFoundFault":
            raise capo_neptune.errors.db_instance_not_found_fault.DBInstanceNotFoundFault.from_query(
                root
            )
        case "DBParameterGroupNotFoundFault":
            raise capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault.from_query(
                root
            )
        case "DBSecurityGroupNotFoundFault":
            raise capo_neptune.errors.db_security_group_not_found_fault.DBSecurityGroupNotFoundFault.from_query(
                root
            )
        case "DBUpgradeDependencyFailureFault":
            raise capo_neptune.errors.db_upgrade_dependency_failure_fault.DBUpgradeDependencyFailureFault.from_query(
                root
            )
        case "DomainNotFoundFault":
            raise capo_neptune.errors.domain_not_found_fault.DomainNotFoundFault.from_query(
                root
            )
        case "InsufficientDBInstanceCapacityFault":
            raise capo_neptune.errors.insufficient_db_instance_capacity_fault.InsufficientDBInstanceCapacityFault.from_query(
                root
            )
        case "InvalidDBInstanceStateFault":
            raise capo_neptune.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault.from_query(
                root
            )
        case "InvalidDBSecurityGroupStateFault":
            raise capo_neptune.errors.invalid_db_security_group_state_fault.InvalidDBSecurityGroupStateFault.from_query(
                root
            )
        case "InvalidVPCNetworkStateFault":
            raise capo_neptune.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault.from_query(
                root
            )
        case "OptionGroupNotFoundFault":
            raise capo_neptune.errors.option_group_not_found_fault.OptionGroupNotFoundFault.from_query(
                root
            )
        case "ProvisionedIopsNotAvailableInAZFault":
            raise capo_neptune.errors.provisioned_iops_not_available_in_az_fault.ProvisionedIopsNotAvailableInAZFault.from_query(
                root
            )
        case "StorageQuotaExceededFault":
            raise capo_neptune.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault.from_query(
                root
            )
        case "StorageTypeNotSupportedFault":
            raise capo_neptune.errors.storage_type_not_supported_fault.StorageTypeNotSupportedFault.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_neptune.types.modify_db_instance_result.ModifyDBInstanceResult:
    root = fromstring(response.read())
    result = root.find("ModifyDBInstanceResult")
    out: capo_neptune.types.modify_db_instance_result.ModifyDBInstanceResult = (
        capo_neptune.types.modify_db_instance_result.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_neptune.types.modify_db_instance_result.ModifyDBInstanceResult:
    root = fromstring(await response.aread())
    result = root.find("ModifyDBInstanceResult")
    out: capo_neptune.types.modify_db_instance_result.ModifyDBInstanceResult = (
        capo_neptune.types.modify_db_instance_result.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_neptune._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_neptune._auth._sigv4.build_sigv4_auth_scheme("rds", options.region)
        )
        if sigv4_config is not None:
            return capo_neptune._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_neptune.types.modify_db_instance_message.ModifyDBInstanceMessage,
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
    pairs.append(("Action", "ModifyDBInstance"))
    pairs.append(("Version", "2014-10-31"))
    capo_neptune.types.modify_db_instance_message.serialize_query(input_, pairs, "")
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def modify_db_instance(
    options: OperationOptions,
    input_: capo_neptune.types.modify_db_instance_message.ModifyDBInstanceMessage,
) -> tuple[
    capo_neptune.types.modify_db_instance_result.ModifyDBInstanceResult, zapros.Response
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


async def async_modify_db_instance(
    options: AsyncOperationOptions,
    input_: capo_neptune.types.modify_db_instance_message.ModifyDBInstanceMessage,
) -> tuple[
    capo_neptune.types.modify_db_instance_result.ModifyDBInstanceResult, zapros.Response
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
