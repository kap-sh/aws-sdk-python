"""Generated from Smithy shape ``com.amazonaws.bedrock#ListAdvancedPromptOptimizationJobs``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_bedrock._auth._signers
import aws_sdk_bedrock._auth._sigv4
from aws_sdk_bedrock._protocol.errors import parse_error_metadata_json
from aws_sdk_bedrock._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_bedrock._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_bedrock.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_request
    import aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_bedrock.errors.access_denied_exception

            raise aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_bedrock.errors.internal_server_exception

            raise aws_sdk_bedrock.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_bedrock.errors.throttling_exception

            raise aws_sdk_bedrock.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_bedrock.errors.validation_exception

            raise aws_sdk_bedrock.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_response.ListAdvancedPromptOptimizationJobsResponse:
    import aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_response

    out: aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_response.ListAdvancedPromptOptimizationJobsResponse = aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_bedrock._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_bedrock._auth._sigv4.build_sigv4_auth_scheme(
                "bedrock", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_bedrock._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    if options.bearer_provider is not None:
        return aws_sdk_bedrock._auth._signers.HttpBearerSigner(options.bearer_provider)
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_request.ListAdvancedPromptOptimizationJobsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/advanced-prompt-optimization-jobs"
    params: dict[str, str] = {}
    if "max_results" in input_:
        params["maxResults"] = str(input_["max_results"])
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    if "sort_by" in input_:
        params["sortBy"] = str(input_["sort_by"])
    if "sort_order" in input_:
        params["sortOrder"] = str(input_["sort_order"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_advanced_prompt_optimization_jobs(
    options: OperationOptions,
    input_: aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_request.ListAdvancedPromptOptimizationJobsRequest,
) -> tuple[
    aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_response.ListAdvancedPromptOptimizationJobsResponse,
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


async def async_list_advanced_prompt_optimization_jobs(
    options: AsyncOperationOptions,
    input_: aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_request.ListAdvancedPromptOptimizationJobsRequest,
) -> tuple[
    aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_response.ListAdvancedPromptOptimizationJobsResponse,
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
