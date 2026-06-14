"""Generated from Smithy shape ``com.amazonaws.lambda#SendDurableExecutionCallbackHeartbeat``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_lambda._auth._signers
import aws_sdk_lambda._auth._sigv4
from aws_sdk_lambda._protocol.errors import parse_error_metadata_json
from aws_sdk_lambda._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_lambda._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_lambda.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_request
    import aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CallbackTimeoutException":
            import aws_sdk_lambda.errors.callback_timeout_exception

            raise aws_sdk_lambda.errors.callback_timeout_exception.CallbackTimeoutException.from_json(
                data
            )
        case "InvalidParameterValueException":
            import aws_sdk_lambda.errors.invalid_parameter_value_exception

            raise aws_sdk_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "ServiceException":
            import aws_sdk_lambda.errors.service_exception

            raise aws_sdk_lambda.errors.service_exception.ServiceException.from_json(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_lambda.errors.too_many_requests_exception

            raise aws_sdk_lambda.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_response.SendDurableExecutionCallbackHeartbeatResponse:
    out: aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_response.SendDurableExecutionCallbackHeartbeatResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_lambda._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_lambda._auth._sigv4.build_sigv4_auth_scheme(
                "lambda", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_lambda._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_request.SendDurableExecutionCallbackHeartbeatRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/2025-12-01/durable-execution-callbacks/{CallbackId}/heartbeat"
    )
    url = url.replace("{CallbackId}", quote(str(input_["callback_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def send_durable_execution_callback_heartbeat(
    options: OperationOptions,
    input_: aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_request.SendDurableExecutionCallbackHeartbeatRequest,
) -> tuple[
    aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_response.SendDurableExecutionCallbackHeartbeatResponse,
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


async def async_send_durable_execution_callback_heartbeat(
    options: AsyncOperationOptions,
    input_: aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_request.SendDurableExecutionCallbackHeartbeatRequest,
) -> tuple[
    aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_response.SendDurableExecutionCallbackHeartbeatResponse,
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
