"""Generated from Smithy shape ``com.amazonaws.transcribe#ListCallAnalyticsJobs``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_transcribe._auth._signers
import aws_sdk_transcribe._auth._sigv4
from aws_sdk_transcribe._protocol.errors import parse_error_metadata_json
from aws_sdk_transcribe._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_transcribe._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_transcribe.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.list_call_analytics_jobs_request
    import aws_sdk_transcribe.types.list_call_analytics_jobs_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            import aws_sdk_transcribe.errors.bad_request_exception

            raise aws_sdk_transcribe.errors.bad_request_exception.BadRequestException.from_aws_json_1_1(
                data
            )
        case "InternalFailureException":
            import aws_sdk_transcribe.errors.internal_failure_exception

            raise aws_sdk_transcribe.errors.internal_failure_exception.InternalFailureException.from_aws_json_1_1(
                data
            )
        case "LimitExceededException":
            import aws_sdk_transcribe.errors.limit_exceeded_exception

            raise aws_sdk_transcribe.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_transcribe.types.list_call_analytics_jobs_response.ListCallAnalyticsJobsResponse:
    import aws_sdk_transcribe.types.list_call_analytics_jobs_response

    out: aws_sdk_transcribe.types.list_call_analytics_jobs_response.ListCallAnalyticsJobsResponse = aws_sdk_transcribe.types.list_call_analytics_jobs_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_transcribe._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_transcribe._auth._sigv4.build_sigv4_auth_scheme(
                "transcribe", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_transcribe._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_transcribe.types.list_call_analytics_jobs_request.ListCallAnalyticsJobsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/callanalyticsjobs"
    params: dict[str, str] = {}
    if "status" in input_:
        params["Status"] = str(input_["status"])
    if "job_name_contains" in input_:
        params["JobNameContains"] = str(input_["job_name_contains"])
    if "next_token" in input_:
        params["NextToken"] = str(input_["next_token"])
    if "max_results" in input_:
        params["MaxResults"] = str(input_["max_results"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "Transcribe.ListCallAnalyticsJobs"
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_call_analytics_jobs(
    options: OperationOptions,
    input_: aws_sdk_transcribe.types.list_call_analytics_jobs_request.ListCallAnalyticsJobsRequest,
) -> tuple[
    aws_sdk_transcribe.types.list_call_analytics_jobs_response.ListCallAnalyticsJobsResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_list_call_analytics_jobs(
    options: AsyncOperationOptions,
    input_: aws_sdk_transcribe.types.list_call_analytics_jobs_request.ListCallAnalyticsJobsRequest,
) -> tuple[
    aws_sdk_transcribe.types.list_call_analytics_jobs_response.ListCallAnalyticsJobsResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
