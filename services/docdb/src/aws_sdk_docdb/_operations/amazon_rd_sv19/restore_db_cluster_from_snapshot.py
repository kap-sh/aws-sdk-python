"""Generated from Smithy shape ``com.amazonaws.docdb#RestoreDBClusterFromSnapshot``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_docdb._auth._signers
import aws_sdk_docdb._auth._sigv4
import aws_sdk_docdb.errors.db_cluster_already_exists_fault
import aws_sdk_docdb.errors.db_cluster_quota_exceeded_fault
import aws_sdk_docdb.errors.db_cluster_snapshot_not_found_fault
import aws_sdk_docdb.errors.db_snapshot_not_found_fault
import aws_sdk_docdb.errors.db_subnet_group_not_found_fault
import aws_sdk_docdb.errors.insufficient_db_cluster_capacity_fault
import aws_sdk_docdb.errors.insufficient_storage_cluster_capacity_fault
import aws_sdk_docdb.errors.invalid_db_cluster_snapshot_state_fault
import aws_sdk_docdb.errors.invalid_db_snapshot_state_fault
import aws_sdk_docdb.errors.invalid_restore_fault
import aws_sdk_docdb.errors.invalid_subnet
import aws_sdk_docdb.errors.invalid_vpc_network_state_fault
import aws_sdk_docdb.errors.kms_key_not_accessible_fault
import aws_sdk_docdb.errors.network_type_not_supported
import aws_sdk_docdb.errors.storage_quota_exceeded_fault
import aws_sdk_docdb.types.availability_zones
import aws_sdk_docdb.types.db_cluster
import aws_sdk_docdb.types.log_type_list
import aws_sdk_docdb.types.restore_db_cluster_from_snapshot_message
import aws_sdk_docdb.types.restore_db_cluster_from_snapshot_result
import aws_sdk_docdb.types.serverless_v2_scaling_configuration
import aws_sdk_docdb.types.tag_list
import aws_sdk_docdb.types.vpc_security_group_id_list
from aws_sdk_docdb._protocol.errors import parse_error_metadata
from aws_sdk_docdb._protocol.xml import fromstring
from aws_sdk_docdb._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_docdb._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_docdb.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "DBClusterAlreadyExistsFault":
            raise aws_sdk_docdb.errors.db_cluster_already_exists_fault.DBClusterAlreadyExistsFault.from_query(
                root
            )
        case "DBClusterQuotaExceededFault":
            raise aws_sdk_docdb.errors.db_cluster_quota_exceeded_fault.DBClusterQuotaExceededFault.from_query(
                root
            )
        case "DBClusterSnapshotNotFoundFault":
            raise aws_sdk_docdb.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault.from_query(
                root
            )
        case "DBSnapshotNotFoundFault":
            raise aws_sdk_docdb.errors.db_snapshot_not_found_fault.DBSnapshotNotFoundFault.from_query(
                root
            )
        case "DBSubnetGroupNotFoundFault":
            raise aws_sdk_docdb.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault.from_query(
                root
            )
        case "InsufficientDBClusterCapacityFault":
            raise aws_sdk_docdb.errors.insufficient_db_cluster_capacity_fault.InsufficientDBClusterCapacityFault.from_query(
                root
            )
        case "InsufficientStorageClusterCapacityFault":
            raise aws_sdk_docdb.errors.insufficient_storage_cluster_capacity_fault.InsufficientStorageClusterCapacityFault.from_query(
                root
            )
        case "InvalidDBClusterSnapshotStateFault":
            raise aws_sdk_docdb.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault.from_query(
                root
            )
        case "InvalidDBSnapshotStateFault":
            raise aws_sdk_docdb.errors.invalid_db_snapshot_state_fault.InvalidDBSnapshotStateFault.from_query(
                root
            )
        case "InvalidRestoreFault":
            raise aws_sdk_docdb.errors.invalid_restore_fault.InvalidRestoreFault.from_query(
                root
            )
        case "InvalidSubnet":
            raise aws_sdk_docdb.errors.invalid_subnet.InvalidSubnet.from_query(root)
        case "InvalidVPCNetworkStateFault":
            raise aws_sdk_docdb.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault.from_query(
                root
            )
        case "KMSKeyNotAccessibleFault":
            raise aws_sdk_docdb.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault.from_query(
                root
            )
        case "NetworkTypeNotSupported":
            raise aws_sdk_docdb.errors.network_type_not_supported.NetworkTypeNotSupported.from_query(
                root
            )
        case "StorageQuotaExceededFault":
            raise aws_sdk_docdb.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_docdb.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult:
    root = fromstring(response.read())
    result = root.find("RestoreDBClusterFromSnapshotResult")
    out: aws_sdk_docdb.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult = aws_sdk_docdb.types.restore_db_cluster_from_snapshot_result.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_docdb.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult:
    root = fromstring(await response.aread())
    result = root.find("RestoreDBClusterFromSnapshotResult")
    out: aws_sdk_docdb.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult = aws_sdk_docdb.types.restore_db_cluster_from_snapshot_result.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_docdb._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_docdb._auth._sigv4.build_sigv4_auth_scheme("rds", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_docdb._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_docdb.types.restore_db_cluster_from_snapshot_message.RestoreDBClusterFromSnapshotMessage,
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
    pairs.append(("Action", "RestoreDBClusterFromSnapshot"))
    pairs.append(("Version", "2014-10-31"))
    aws_sdk_docdb.types.restore_db_cluster_from_snapshot_message.serialize_query(
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


def restore_db_cluster_from_snapshot(
    options: OperationOptions,
    input_: aws_sdk_docdb.types.restore_db_cluster_from_snapshot_message.RestoreDBClusterFromSnapshotMessage,
) -> tuple[
    aws_sdk_docdb.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult,
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


async def async_restore_db_cluster_from_snapshot(
    options: AsyncOperationOptions,
    input_: aws_sdk_docdb.types.restore_db_cluster_from_snapshot_message.RestoreDBClusterFromSnapshotMessage,
) -> tuple[
    aws_sdk_docdb.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult,
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
