"""Generated from Smithy shape ``com.amazonaws.backup#ListReportJobs``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_backup._auth._signers
import capo_backup._auth._sigv4
import capo_backup.errors.invalid_parameter_value_exception
import capo_backup.errors.resource_not_found_exception
import capo_backup.errors.service_unavailable_exception
import capo_backup.types.list_report_jobs_input
import capo_backup.types.list_report_jobs_output
import capo_backup.types.report_job_list
import capo_backup.types.timestamp
from capo_backup._protocol.errors import parse_error_metadata_json
from capo_backup._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_backup._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_backup.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            raise capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_backup.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise capo_backup.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_backup.types.list_report_jobs_output.ListReportJobsOutput:
    out: capo_backup.types.list_report_jobs_output.ListReportJobsOutput = (
        capo_backup.types.list_report_jobs_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_backup.types.list_report_jobs_output.ListReportJobsOutput:
    out: capo_backup.types.list_report_jobs_output.ListReportJobsOutput = (
        capo_backup.types.list_report_jobs_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_backup._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_backup._auth._sigv4.build_sigv4_auth_scheme(
                "backup", options.region
            )
        )
        if sigv4_config is not None:
            return capo_backup._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_backup.types.list_report_jobs_input.ListReportJobsInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/audit/report-jobs"
    params: dict[str, str] = {}
    if "by_report_plan_name" in input_:
        params["ReportPlanName"] = str(input_["by_report_plan_name"])
    if "by_creation_before" in input_:
        params["CreationBefore"] = str(input_["by_creation_before"])
    if "by_creation_after" in input_:
        params["CreationAfter"] = str(input_["by_creation_after"])
    if "by_status" in input_:
        params["Status"] = str(input_["by_status"])
    if "max_results" in input_:
        params["MaxResults"] = str(input_["max_results"])
    if "next_token" in input_:
        params["NextToken"] = str(input_["next_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_report_jobs(
    options: OperationOptions,
    input_: capo_backup.types.list_report_jobs_input.ListReportJobsInput,
) -> tuple[
    capo_backup.types.list_report_jobs_output.ListReportJobsOutput, zapros.Response
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


async def async_list_report_jobs(
    options: AsyncOperationOptions,
    input_: capo_backup.types.list_report_jobs_input.ListReportJobsInput,
) -> tuple[
    capo_backup.types.list_report_jobs_output.ListReportJobsOutput, zapros.Response
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
