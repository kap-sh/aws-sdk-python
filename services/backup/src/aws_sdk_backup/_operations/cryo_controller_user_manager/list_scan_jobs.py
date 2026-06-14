"""Generated from Smithy shape ``com.amazonaws.backup#ListScanJobs``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_backup._auth._signers
import aws_sdk_backup._auth._sigv4
from aws_sdk_backup._protocol.errors import parse_error_metadata_json
from aws_sdk_backup._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_backup._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_backup.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_backup.types.list_scan_jobs_input
    import aws_sdk_backup.types.list_scan_jobs_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            import aws_sdk_backup.errors.invalid_parameter_value_exception

            raise aws_sdk_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "ServiceUnavailableException":
            import aws_sdk_backup.errors.service_unavailable_exception

            raise aws_sdk_backup.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_backup.types.list_scan_jobs_output.ListScanJobsOutput:
    import aws_sdk_backup.types.list_scan_jobs_output

    out: aws_sdk_backup.types.list_scan_jobs_output.ListScanJobsOutput = (
        aws_sdk_backup.types.list_scan_jobs_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_backup._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_backup._auth._sigv4.build_sigv4_auth_scheme(
                "backup", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_backup._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_backup.types.list_scan_jobs_input.ListScanJobsInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/scan/jobs"
    params: dict[str, str] = {}
    if "by_account_id" in input:
        params["ByAccountId"] = str(input["by_account_id"])
    if "by_backup_vault_name" in input:
        params["ByBackupVaultName"] = str(input["by_backup_vault_name"])
    if "by_complete_after" in input:
        params["ByCompleteAfter"] = str(input["by_complete_after"])
    if "by_complete_before" in input:
        params["ByCompleteBefore"] = str(input["by_complete_before"])
    if "by_malware_scanner" in input:
        params["ByMalwareScanner"] = str(input["by_malware_scanner"])
    if "by_recovery_point_arn" in input:
        params["ByRecoveryPointArn"] = str(input["by_recovery_point_arn"])
    if "by_resource_arn" in input:
        params["ByResourceArn"] = str(input["by_resource_arn"])
    if "by_resource_type" in input:
        params["ByResourceType"] = str(input["by_resource_type"])
    if "by_scan_result_status" in input:
        params["ByScanResultStatus"] = str(input["by_scan_result_status"])
    if "by_state" in input:
        params["ByState"] = str(input["by_state"])
    if "max_results" in input:
        params["MaxResults"] = str(input["max_results"])
    if "next_token" in input:
        params["NextToken"] = str(input["next_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_scan_jobs(
    options: OperationOptions,
    input: aws_sdk_backup.types.list_scan_jobs_input.ListScanJobsInput,
) -> tuple[
    aws_sdk_backup.types.list_scan_jobs_output.ListScanJobsOutput, zapros.Response
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_list_scan_jobs(
    options: AsyncOperationOptions,
    input: aws_sdk_backup.types.list_scan_jobs_input.ListScanJobsInput,
) -> tuple[
    aws_sdk_backup.types.list_scan_jobs_output.ListScanJobsOutput, zapros.Response
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
