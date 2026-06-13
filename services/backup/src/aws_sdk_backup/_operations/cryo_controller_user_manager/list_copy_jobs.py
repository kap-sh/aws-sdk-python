"""Generated from Smithy shape ``com.amazonaws.backup#ListCopyJobs``."""

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
    import aws_sdk_backup.types.list_copy_jobs_input
    import aws_sdk_backup.types.list_copy_jobs_output


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
) -> aws_sdk_backup.types.list_copy_jobs_output.ListCopyJobsOutput:
    import aws_sdk_backup.types.list_copy_jobs_output

    out: aws_sdk_backup.types.list_copy_jobs_output.ListCopyJobsOutput = (
        aws_sdk_backup.types.list_copy_jobs_output.deserialize_json(
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
    input: aws_sdk_backup.types.list_copy_jobs_input.ListCopyJobsInput,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/copy-jobs"
    params: dict[str, str] = {}
    if "next_token" in input:
        params["nextToken"] = str(input["next_token"])
    if "max_results" in input:
        params["maxResults"] = str(input["max_results"])
    if "by_resource_arn" in input:
        params["resourceArn"] = str(input["by_resource_arn"])
    if "by_state" in input:
        params["state"] = str(input["by_state"])
    if "by_created_before" in input:
        params["createdBefore"] = str(input["by_created_before"])
    if "by_created_after" in input:
        params["createdAfter"] = str(input["by_created_after"])
    if "by_resource_type" in input:
        params["resourceType"] = str(input["by_resource_type"])
    if "by_destination_vault_arn" in input:
        params["destinationVaultArn"] = str(input["by_destination_vault_arn"])
    if "by_account_id" in input:
        params["accountId"] = str(input["by_account_id"])
    if "by_complete_before" in input:
        params["completeBefore"] = str(input["by_complete_before"])
    if "by_complete_after" in input:
        params["completeAfter"] = str(input["by_complete_after"])
    if "by_parent_job_id" in input:
        params["parentJobId"] = str(input["by_parent_job_id"])
    if "by_message_category" in input:
        params["messageCategory"] = str(input["by_message_category"])
    if "by_source_recovery_point_arn" in input:
        params["sourceRecoveryPointArn"] = str(input["by_source_recovery_point_arn"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "GET",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def list_copy_jobs(
    options: OperationOptions,
    input: aws_sdk_backup.types.list_copy_jobs_input.ListCopyJobsInput,
) -> tuple[
    aws_sdk_backup.types.list_copy_jobs_output.ListCopyJobsOutput, zapros.Response
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


async def async_list_copy_jobs(
    options: AsyncOperationOptions,
    input: aws_sdk_backup.types.list_copy_jobs_input.ListCopyJobsInput,
) -> tuple[
    aws_sdk_backup.types.list_copy_jobs_output.ListCopyJobsOutput, zapros.Response
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
