"""Generated from Smithy shape ``com.amazonaws.sqs#StartMessageMoveTask``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_sqs._auth._signers
import aws_sdk_sqs._auth._sigv4
from aws_sdk_sqs._protocol.errors import parse_error_metadata_json
from aws_sdk_sqs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_sqs._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_sqs.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.start_message_move_task_request
    import aws_sdk_sqs.types.start_message_move_task_result


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidAddress":
            import aws_sdk_sqs.errors.invalid_address

            raise aws_sdk_sqs.errors.invalid_address.InvalidAddress.from_aws_json_1_0(
                data
            )
        case "InvalidSecurity":
            import aws_sdk_sqs.errors.invalid_security

            raise aws_sdk_sqs.errors.invalid_security.InvalidSecurity.from_aws_json_1_0(
                data
            )
        case "RequestThrottled":
            import aws_sdk_sqs.errors.request_throttled

            raise aws_sdk_sqs.errors.request_throttled.RequestThrottled.from_aws_json_1_0(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_sqs.errors.resource_not_found_exception

            raise aws_sdk_sqs.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data
            )
        case "UnsupportedOperation":
            import aws_sdk_sqs.errors.unsupported_operation

            raise aws_sdk_sqs.errors.unsupported_operation.UnsupportedOperation.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_sqs.types.start_message_move_task_result.StartMessageMoveTaskResult:
    import aws_sdk_sqs.types.start_message_move_task_result

    out: aws_sdk_sqs.types.start_message_move_task_result.StartMessageMoveTaskResult = (
        aws_sdk_sqs.types.start_message_move_task_result.deserialize_aws_json_1_0(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sqs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_sqs._auth._sigv4.build_sigv4_auth_scheme("sqs", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_sqs._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_sqs.types.start_message_move_task_request.StartMessageMoveTaskRequest,
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
    headers["X-Amz-Target"] = "AmazonSQS.StartMessageMoveTask"
    import aws_sdk_sqs.types.start_message_move_task_request

    body: bytes | None = json.dumps(
        aws_sdk_sqs.types.start_message_move_task_request.serialize_aws_json_1_0(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def start_message_move_task(
    options: OperationOptions,
    input_: aws_sdk_sqs.types.start_message_move_task_request.StartMessageMoveTaskRequest,
) -> tuple[
    aws_sdk_sqs.types.start_message_move_task_result.StartMessageMoveTaskResult,
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


async def async_start_message_move_task(
    options: AsyncOperationOptions,
    input_: aws_sdk_sqs.types.start_message_move_task_request.StartMessageMoveTaskRequest,
) -> tuple[
    aws_sdk_sqs.types.start_message_move_task_result.StartMessageMoveTaskResult,
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
