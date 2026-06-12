"""Generated from Smithy shape ``com.amazonaws.glue#UpdateSourceControlFromJob``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_glue._auth._signers
import aws_sdk_glue._auth._sigv4
from aws_sdk_glue._protocol.errors import parse_error_metadata_json
from aws_sdk_glue._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_glue._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_glue.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.update_source_control_from_job_request
    import aws_sdk_glue.types.update_source_control_from_job_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_glue.errors.access_denied_exception

            raise aws_sdk_glue.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "AlreadyExistsException":
            import aws_sdk_glue.errors.already_exists_exception

            raise aws_sdk_glue.errors.already_exists_exception.AlreadyExistsException.from_aws_json_1_1(
                data
            )
        case "EntityNotFoundException":
            import aws_sdk_glue.errors.entity_not_found_exception

            raise aws_sdk_glue.errors.entity_not_found_exception.EntityNotFoundException.from_aws_json_1_1(
                data
            )
        case "InternalServiceException":
            import aws_sdk_glue.errors.internal_service_exception

            raise aws_sdk_glue.errors.internal_service_exception.InternalServiceException.from_aws_json_1_1(
                data
            )
        case "InvalidInputException":
            import aws_sdk_glue.errors.invalid_input_exception

            raise aws_sdk_glue.errors.invalid_input_exception.InvalidInputException.from_aws_json_1_1(
                data
            )
        case "OperationTimeoutException":
            import aws_sdk_glue.errors.operation_timeout_exception

            raise aws_sdk_glue.errors.operation_timeout_exception.OperationTimeoutException.from_aws_json_1_1(
                data
            )
        case "ValidationException":
            import aws_sdk_glue.errors.validation_exception

            raise aws_sdk_glue.errors.validation_exception.ValidationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_glue.types.update_source_control_from_job_response.UpdateSourceControlFromJobResponse:
    import aws_sdk_glue.types.update_source_control_from_job_response

    out: aws_sdk_glue.types.update_source_control_from_job_response.UpdateSourceControlFromJobResponse = aws_sdk_glue.types.update_source_control_from_job_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_glue._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_glue._auth._sigv4.build_sigv4_auth_scheme("glue", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_glue._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_glue.types.update_source_control_from_job_request.UpdateSourceControlFromJobRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSGlue.UpdateSourceControlFromJob"
    import aws_sdk_glue.types.update_source_control_from_job_request

    body: bytes | None = json.dumps(
        aws_sdk_glue.types.update_source_control_from_job_request.serialize_aws_json_1_1(
            input
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def update_source_control_from_job(
    options: OperationOptions,
    input: aws_sdk_glue.types.update_source_control_from_job_request.UpdateSourceControlFromJobRequest,
) -> tuple[
    aws_sdk_glue.types.update_source_control_from_job_response.UpdateSourceControlFromJobResponse,
    zapros.Response,
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


async def async_update_source_control_from_job(
    options: AsyncOperationOptions,
    input: aws_sdk_glue.types.update_source_control_from_job_request.UpdateSourceControlFromJobRequest,
) -> tuple[
    aws_sdk_glue.types.update_source_control_from_job_response.UpdateSourceControlFromJobResponse,
    zapros.Response,
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
