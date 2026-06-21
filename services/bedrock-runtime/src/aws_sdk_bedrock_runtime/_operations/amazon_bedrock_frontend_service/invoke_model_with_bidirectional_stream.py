"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithBidirectionalStream``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_bedrock_runtime._auth._signers
import aws_sdk_bedrock_runtime._auth._sigv4
import aws_sdk_bedrock_runtime._iter
import aws_sdk_bedrock_runtime.errors.access_denied_exception
import aws_sdk_bedrock_runtime.errors.internal_server_exception
import aws_sdk_bedrock_runtime.errors.model_error_exception
import aws_sdk_bedrock_runtime.errors.model_not_ready_exception
import aws_sdk_bedrock_runtime.errors.model_stream_error_exception
import aws_sdk_bedrock_runtime.errors.model_timeout_exception
import aws_sdk_bedrock_runtime.errors.resource_not_found_exception
import aws_sdk_bedrock_runtime.errors.service_quota_exceeded_exception
import aws_sdk_bedrock_runtime.errors.service_unavailable_exception
import aws_sdk_bedrock_runtime.errors.throttling_exception
import aws_sdk_bedrock_runtime.errors.validation_exception
import aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input
import aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_output
import aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request
import aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response
from aws_sdk_bedrock_runtime._protocol.errors import parse_error_metadata_json
from aws_sdk_bedrock_runtime._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from aws_sdk_bedrock_runtime._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_bedrock_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_bedrock_runtime.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_bedrock_runtime.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_bedrock_runtime.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ModelErrorException":
            raise aws_sdk_bedrock_runtime.errors.model_error_exception.ModelErrorException.from_json(
                data
            )
        case "ModelNotReadyException":
            raise aws_sdk_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException.from_json(
                data
            )
        case "ModelStreamErrorException":
            raise aws_sdk_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException.from_json(
                data
            )
        case "ModelTimeoutException":
            raise aws_sdk_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise aws_sdk_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_bedrock_runtime.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_bedrock_runtime.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse:
    _message_decoder = MessageDecoder()
    _union_deser = aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_output.deserialize_event_json
    _iter = cast(Any, response.iter_bytes())
    out: aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse = {
        "body": cast(Any, raw_stream_to_events(_iter, _message_decoder, _union_deser))
    }  # type: ignore[reportAssignmentType]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse:
    _message_decoder = MessageDecoder()
    _union_deser = aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_output.deserialize_event_json
    _iter = cast(Any, response.async_iter_bytes())
    out: aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse = {
        "body": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_bedrock_runtime._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_bedrock_runtime._auth._sigv4.build_sigv4_auth_scheme(
                "bedrock", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_bedrock_runtime._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    if options.bearer_provider is not None:
        return aws_sdk_bedrock_runtime._auth._signers.HttpBearerSigner(
            options.bearer_provider
        )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/model/{modelId}/invoke-with-bidirectional-stream"
    url = url.replace("{modelId}", quote(str(input_["model_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}

    import aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input

    body = aws_sdk_bedrock_runtime._iter.map_sync_iterator(
        input_["body"],
        aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input.serialize_event_json,
    )

    headers["content-type"] = "application/vnd.amazon-eventstream"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def async_build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/model/{modelId}/invoke-with-bidirectional-stream"
    url = url.replace("{modelId}", quote(str(input_["model_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}

    import aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input

    body = aws_sdk_bedrock_runtime._iter.map_async_iterator(
        input_["body"],
        aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input.serialize_event_json,
    )

    headers["content-type"] = "application/vnd.amazon-eventstream"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def invoke_model_with_bidirectional_stream(
    options: OperationOptions,
    input_: aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest,
) -> tuple[
    aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse,
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


async def async_invoke_model_with_bidirectional_stream(
    options: AsyncOperationOptions,
    input_: aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest,
) -> tuple[
    aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(
        async_build_request(options, input_)
    )
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
