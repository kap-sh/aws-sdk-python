"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StartLiveTail``."""

from __future__ import annotations

import json
from typing import Any, cast

import zapros
from typing_extensions import Never

import aws_sdk_cloudwatch_logs._auth._signers
import aws_sdk_cloudwatch_logs._auth._sigv4
import aws_sdk_cloudwatch_logs._iter
import aws_sdk_cloudwatch_logs.errors.access_denied_exception
import aws_sdk_cloudwatch_logs.errors.invalid_operation_exception
import aws_sdk_cloudwatch_logs.errors.invalid_parameter_exception
import aws_sdk_cloudwatch_logs.errors.limit_exceeded_exception
import aws_sdk_cloudwatch_logs.errors.resource_not_found_exception
import aws_sdk_cloudwatch_logs.types.input_log_stream_names
import aws_sdk_cloudwatch_logs.types.start_live_tail_log_group_identifiers
import aws_sdk_cloudwatch_logs.types.start_live_tail_request
import aws_sdk_cloudwatch_logs.types.start_live_tail_response
import aws_sdk_cloudwatch_logs.types.start_live_tail_response_stream
from aws_sdk_cloudwatch_logs._protocol.errors import parse_error_metadata_json
from aws_sdk_cloudwatch_logs._protocol.eventstream import (
    MessageDecoder,
    async_read_messages,
    read_messages,
)
from aws_sdk_cloudwatch_logs._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_cloudwatch_logs._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudwatch_logs.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "InvalidOperationException":
            raise aws_sdk_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            raise aws_sdk_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "LimitExceededException":
            raise aws_sdk_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_cloudwatch_logs.types.start_live_tail_response.StartLiveTailResponse:
    _decoder = MessageDecoder()
    _messages = read_messages(response.iter_bytes(), _decoder)
    out: aws_sdk_cloudwatch_logs.types.start_live_tail_response.StartLiveTailResponse = {}  # type: ignore[typeddict-item]
    out["response_stream"] = cast(
        Any,
        aws_sdk_cloudwatch_logs._iter.map_sync_iterator(
            _messages,
            aws_sdk_cloudwatch_logs.types.start_live_tail_response_stream.deserialize_event_aws_json_1_1,
        ),
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_cloudwatch_logs.types.start_live_tail_response.StartLiveTailResponse:
    _decoder = MessageDecoder()
    _messages = async_read_messages(response.async_iter_bytes(), _decoder)
    out: aws_sdk_cloudwatch_logs.types.start_live_tail_response.StartLiveTailResponse = {}  # type: ignore[typeddict-item]
    out["response_stream"] = cast(
        Any,
        aws_sdk_cloudwatch_logs._iter.map_async_iterator(
            _messages,
            aws_sdk_cloudwatch_logs.types.start_live_tail_response_stream.deserialize_event_aws_json_1_1,
        ),
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloudwatch_logs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cloudwatch_logs._auth._sigv4.build_sigv4_auth_scheme(
                "logs", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cloudwatch_logs._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_cloudwatch_logs.types.start_live_tail_request.StartLiveTailRequest,
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
    headers["X-Amz-Target"] = "Logs_20140328.StartLiveTail"
    import aws_sdk_cloudwatch_logs.types.start_live_tail_request

    body: bytes | None = json.dumps(
        aws_sdk_cloudwatch_logs.types.start_live_tail_request.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def start_live_tail(
    options: OperationOptions,
    input_: aws_sdk_cloudwatch_logs.types.start_live_tail_request.StartLiveTailRequest,
) -> tuple[
    aws_sdk_cloudwatch_logs.types.start_live_tail_response.StartLiveTailResponse,
    zapros.Response,
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


async def async_start_live_tail(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudwatch_logs.types.start_live_tail_request.StartLiveTailRequest,
) -> tuple[
    aws_sdk_cloudwatch_logs.types.start_live_tail_response.StartLiveTailResponse,
    zapros.Response,
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
