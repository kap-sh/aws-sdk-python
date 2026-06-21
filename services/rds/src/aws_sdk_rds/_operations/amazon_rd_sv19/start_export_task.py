"""Generated from Smithy shape ``com.amazonaws.rds#StartExportTask``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_rds._auth._signers
import aws_sdk_rds._auth._sigv4
import aws_sdk_rds.errors.db_cluster_not_found_fault
import aws_sdk_rds.errors.db_cluster_snapshot_not_found_fault
import aws_sdk_rds.errors.db_snapshot_not_found_fault
import aws_sdk_rds.errors.export_task_already_exists_fault
import aws_sdk_rds.errors.iam_role_missing_permissions_fault
import aws_sdk_rds.errors.iam_role_not_found_fault
import aws_sdk_rds.errors.invalid_export_only_fault
import aws_sdk_rds.errors.invalid_export_source_state_fault
import aws_sdk_rds.errors.invalid_s3_bucket_fault
import aws_sdk_rds.errors.kms_key_not_accessible_fault
import aws_sdk_rds.types.export_source_type
import aws_sdk_rds.types.export_task
import aws_sdk_rds.types.start_export_task_message
import aws_sdk_rds.types.string_list
import aws_sdk_rds.types.t_stamp
from aws_sdk_rds._protocol.errors import parse_error_metadata
from aws_sdk_rds._protocol.xml import fromstring
from aws_sdk_rds._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_rds._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_rds.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "DBClusterNotFoundFault":
            raise aws_sdk_rds.errors.db_cluster_not_found_fault.DBClusterNotFoundFault.from_query(
                root
            )
        case "DBClusterSnapshotNotFoundFault":
            raise aws_sdk_rds.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault.from_query(
                root
            )
        case "DBSnapshotNotFoundFault":
            raise aws_sdk_rds.errors.db_snapshot_not_found_fault.DBSnapshotNotFoundFault.from_query(
                root
            )
        case "ExportTaskAlreadyExistsFault":
            raise aws_sdk_rds.errors.export_task_already_exists_fault.ExportTaskAlreadyExistsFault.from_query(
                root
            )
        case "IamRoleMissingPermissionsFault":
            raise aws_sdk_rds.errors.iam_role_missing_permissions_fault.IamRoleMissingPermissionsFault.from_query(
                root
            )
        case "IamRoleNotFoundFault":
            raise aws_sdk_rds.errors.iam_role_not_found_fault.IamRoleNotFoundFault.from_query(
                root
            )
        case "InvalidExportOnlyFault":
            raise aws_sdk_rds.errors.invalid_export_only_fault.InvalidExportOnlyFault.from_query(
                root
            )
        case "InvalidExportSourceStateFault":
            raise aws_sdk_rds.errors.invalid_export_source_state_fault.InvalidExportSourceStateFault.from_query(
                root
            )
        case "InvalidS3BucketFault":
            raise aws_sdk_rds.errors.invalid_s3_bucket_fault.InvalidS3BucketFault.from_query(
                root
            )
        case "KMSKeyNotAccessibleFault":
            raise aws_sdk_rds.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_rds.types.export_task.ExportTask:
    root = fromstring(response.read())
    result = root.find("StartExportTaskResult")
    out: aws_sdk_rds.types.export_task.ExportTask = (
        aws_sdk_rds.types.export_task.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_rds.types.export_task.ExportTask:
    root = fromstring(await response.aread())
    result = root.find("StartExportTaskResult")
    out: aws_sdk_rds.types.export_task.ExportTask = (
        aws_sdk_rds.types.export_task.deserialize_query(
            result if result is not None else root
        )
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
    input_: aws_sdk_rds.types.start_export_task_message.StartExportTaskMessage,
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
    pairs.append(("Action", "StartExportTask"))
    pairs.append(("Version", "2014-10-31"))
    import aws_sdk_rds.types.start_export_task_message

    aws_sdk_rds.types.start_export_task_message.serialize_query(input_, pairs, "")
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def start_export_task(
    options: OperationOptions,
    input_: aws_sdk_rds.types.start_export_task_message.StartExportTaskMessage,
) -> tuple[aws_sdk_rds.types.export_task.ExportTask, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_start_export_task(
    options: AsyncOperationOptions,
    input_: aws_sdk_rds.types.start_export_task_message.StartExportTaskMessage,
) -> tuple[aws_sdk_rds.types.export_task.ExportTask, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
