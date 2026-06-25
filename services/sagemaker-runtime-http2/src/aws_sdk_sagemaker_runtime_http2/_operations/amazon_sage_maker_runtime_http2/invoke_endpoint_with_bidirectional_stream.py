"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#InvokeEndpointWithBidirectionalStream``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_sagemaker_runtime_http2._auth._signers
import aws_sdk_sagemaker_runtime_http2._auth._sigv4
import aws_sdk_sagemaker_runtime_http2._iter
import aws_sdk_sagemaker_runtime_http2.errors.input_validation_error
import aws_sdk_sagemaker_runtime_http2.errors.internal_server_error
import aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure
import aws_sdk_sagemaker_runtime_http2.errors.model_error
import aws_sdk_sagemaker_runtime_http2.errors.model_stream_error
import aws_sdk_sagemaker_runtime_http2.errors.service_unavailable_error
import aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_input
import aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_output
import aws_sdk_sagemaker_runtime_http2.types.request_stream_event
import aws_sdk_sagemaker_runtime_http2.types.response_stream_event
from aws_sdk_sagemaker_runtime_http2._protocol.errors import parse_error_metadata_json
from aws_sdk_sagemaker_runtime_http2._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from aws_sdk_sagemaker_runtime_http2._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_sagemaker_runtime_http2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_sagemaker_runtime_http2.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InputValidationError":
            raise aws_sdk_sagemaker_runtime_http2.errors.input_validation_error.InputValidationError.from_json(
                data
            )
        case "InternalServerError":
            raise aws_sdk_sagemaker_runtime_http2.errors.internal_server_error.InternalServerError.from_json(
                data
            )
        case "InternalStreamFailure":
            raise aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure.InternalStreamFailure.from_json(
                data
            )
        case "ModelError":
            raise aws_sdk_sagemaker_runtime_http2.errors.model_error.ModelError.from_json(
                data
            )
        case "ModelStreamError":
            raise aws_sdk_sagemaker_runtime_http2.errors.model_stream_error.ModelStreamError.from_json(
                data
            )
        case "ServiceUnavailableError":
            raise aws_sdk_sagemaker_runtime_http2.errors.service_unavailable_error.ServiceUnavailableError.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_output.InvokeEndpointWithBidirectionalStreamOutput:
    _message_decoder = MessageDecoder()
    _union_deser = aws_sdk_sagemaker_runtime_http2.types.response_stream_event.deserialize_event_json
    _iter = cast(Any, response.iter_bytes())
    out: aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_output.InvokeEndpointWithBidirectionalStreamOutput = {
        "body": cast(Any, raw_stream_to_events(_iter, _message_decoder, _union_deser))
    }  # type: ignore[reportAssignmentType]
    if "X-Amzn-Invoked-Production-Variant" in response.headers:
        out["invoked_production_variant"] = str(
            response.headers["X-Amzn-Invoked-Production-Variant"]
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_output.InvokeEndpointWithBidirectionalStreamOutput:
    _message_decoder = MessageDecoder()
    _union_deser = aws_sdk_sagemaker_runtime_http2.types.response_stream_event.deserialize_event_json
    _iter = cast(Any, response.async_iter_bytes())
    out: aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_output.InvokeEndpointWithBidirectionalStreamOutput = {
        "body": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "X-Amzn-Invoked-Production-Variant" in response.headers:
        out["invoked_production_variant"] = str(
            response.headers["X-Amzn-Invoked-Production-Variant"]
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sagemaker_runtime_http2._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_sagemaker_runtime_http2._auth._sigv4.build_sigv4_auth_scheme(
                "sagemaker", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_sagemaker_runtime_http2._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_input.InvokeEndpointWithBidirectionalStreamInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/endpoints/{EndpointName}/invocations-bidirectional-stream"
    )
    url = url.replace("{EndpointName}", quote(str(input_["endpoint_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "target_variant" in input_:
        headers["X-Amzn-SageMaker-Target-Variant"] = str(input_["target_variant"])
    if "model_invocation_path" in input_:
        headers["X-Amzn-SageMaker-Model-Invocation-Path"] = str(
            input_["model_invocation_path"]
        )
    if "model_query_string" in input_:
        headers["X-Amzn-SageMaker-Model-Query-String"] = str(
            input_["model_query_string"]
        )

    body = aws_sdk_sagemaker_runtime_http2._iter.map_sync_iterator(
        input_["body"],
        aws_sdk_sagemaker_runtime_http2.types.request_stream_event.serialize_event_json,
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
    input_: aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_input.InvokeEndpointWithBidirectionalStreamInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/endpoints/{EndpointName}/invocations-bidirectional-stream"
    )
    url = url.replace("{EndpointName}", quote(str(input_["endpoint_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "target_variant" in input_:
        headers["X-Amzn-SageMaker-Target-Variant"] = str(input_["target_variant"])
    if "model_invocation_path" in input_:
        headers["X-Amzn-SageMaker-Model-Invocation-Path"] = str(
            input_["model_invocation_path"]
        )
    if "model_query_string" in input_:
        headers["X-Amzn-SageMaker-Model-Query-String"] = str(
            input_["model_query_string"]
        )

    body = aws_sdk_sagemaker_runtime_http2._iter.map_async_iterator(
        input_["body"],
        aws_sdk_sagemaker_runtime_http2.types.request_stream_event.serialize_event_json,
    )

    headers["content-type"] = "application/vnd.amazon-eventstream"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def invoke_endpoint_with_bidirectional_stream(
    options: OperationOptions,
    input_: aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_input.InvokeEndpointWithBidirectionalStreamInput,
) -> tuple[
    aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_output.InvokeEndpointWithBidirectionalStreamOutput,
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


async def async_invoke_endpoint_with_bidirectional_stream(
    options: AsyncOperationOptions,
    input_: aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_input.InvokeEndpointWithBidirectionalStreamInput,
) -> tuple[
    aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_output.InvokeEndpointWithBidirectionalStreamOutput,
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
