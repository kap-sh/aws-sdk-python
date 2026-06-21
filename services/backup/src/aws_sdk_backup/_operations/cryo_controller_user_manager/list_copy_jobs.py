"""Generated from Smithy shape ``com.amazonaws.backup#ListCopyJobs``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_backup._auth._signers
import aws_sdk_backup._auth._sigv4
import aws_sdk_backup.errors.invalid_parameter_value_exception
import aws_sdk_backup.errors.service_unavailable_exception
import aws_sdk_backup.types.copy_job_state
import aws_sdk_backup.types.copy_jobs_list
import aws_sdk_backup.types.list_copy_jobs_input
import aws_sdk_backup.types.list_copy_jobs_output
import aws_sdk_backup.types.timestamp
from aws_sdk_backup._protocol.errors import parse_error_metadata_json
from aws_sdk_backup._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_backup._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_backup.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            raise aws_sdk_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_backup.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_backup.types.list_copy_jobs_output.ListCopyJobsOutput:
    out: aws_sdk_backup.types.list_copy_jobs_output.ListCopyJobsOutput = (
        aws_sdk_backup.types.list_copy_jobs_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_backup.types.list_copy_jobs_output.ListCopyJobsOutput:
    out: aws_sdk_backup.types.list_copy_jobs_output.ListCopyJobsOutput = (
        aws_sdk_backup.types.list_copy_jobs_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_backup._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_backup.types.list_copy_jobs_input.ListCopyJobsInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/copy-jobs"
    params: dict[str, str] = {}
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    if "max_results" in input_:
        params["maxResults"] = str(input_["max_results"])
    if "by_resource_arn" in input_:
        params["resourceArn"] = str(input_["by_resource_arn"])
    if "by_state" in input_:
        params["state"] = str(input_["by_state"])
    if "by_created_before" in input_:
        params["createdBefore"] = str(input_["by_created_before"])
    if "by_created_after" in input_:
        params["createdAfter"] = str(input_["by_created_after"])
    if "by_resource_type" in input_:
        params["resourceType"] = str(input_["by_resource_type"])
    if "by_destination_vault_arn" in input_:
        params["destinationVaultArn"] = str(input_["by_destination_vault_arn"])
    if "by_account_id" in input_:
        params["accountId"] = str(input_["by_account_id"])
    if "by_complete_before" in input_:
        params["completeBefore"] = str(input_["by_complete_before"])
    if "by_complete_after" in input_:
        params["completeAfter"] = str(input_["by_complete_after"])
    if "by_parent_job_id" in input_:
        params["parentJobId"] = str(input_["by_parent_job_id"])
    if "by_message_category" in input_:
        params["messageCategory"] = str(input_["by_message_category"])
    if "by_source_recovery_point_arn" in input_:
        params["sourceRecoveryPointArn"] = str(input_["by_source_recovery_point_arn"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_copy_jobs(
    options: OperationOptions,
    input_: aws_sdk_backup.types.list_copy_jobs_input.ListCopyJobsInput,
) -> tuple[
    aws_sdk_backup.types.list_copy_jobs_output.ListCopyJobsOutput, zapros.Response
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


async def async_list_copy_jobs(
    options: AsyncOperationOptions,
    input_: aws_sdk_backup.types.list_copy_jobs_input.ListCopyJobsInput,
) -> tuple[
    aws_sdk_backup.types.list_copy_jobs_output.ListCopyJobsOutput, zapros.Response
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
