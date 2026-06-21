"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#InvokeEndpointWithResponseStream``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_sagemaker_runtime._auth._signers
import aws_sdk_sagemaker_runtime._auth._sigv4
import aws_sdk_sagemaker_runtime.errors.internal_failure
import aws_sdk_sagemaker_runtime.errors.internal_stream_failure
import aws_sdk_sagemaker_runtime.errors.model_error
import aws_sdk_sagemaker_runtime.errors.model_stream_error
import aws_sdk_sagemaker_runtime.errors.service_unavailable
import aws_sdk_sagemaker_runtime.errors.validation_error
import aws_sdk_sagemaker_runtime.types.body_blob
import aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_input
import aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_output
import aws_sdk_sagemaker_runtime.types.response_stream
from aws_sdk_sagemaker_runtime._protocol.errors import parse_error_metadata_json
from aws_sdk_sagemaker_runtime._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from aws_sdk_sagemaker_runtime._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_sagemaker_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_sagemaker_runtime.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalFailure":
            raise aws_sdk_sagemaker_runtime.errors.internal_failure.InternalFailure.from_json(
                data
            )
        case "InternalStreamFailure":
            raise aws_sdk_sagemaker_runtime.errors.internal_stream_failure.InternalStreamFailure.from_json(
                data
            )
        case "ModelError":
            raise aws_sdk_sagemaker_runtime.errors.model_error.ModelError.from_json(
                data
            )
        case "ModelStreamError":
            raise aws_sdk_sagemaker_runtime.errors.model_stream_error.ModelStreamError.from_json(
                data
            )
        case "ServiceUnavailable":
            raise aws_sdk_sagemaker_runtime.errors.service_unavailable.ServiceUnavailable.from_json(
                data
            )
        case "ValidationError":
            raise aws_sdk_sagemaker_runtime.errors.validation_error.ValidationError.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_output.InvokeEndpointWithResponseStreamOutput:
    _message_decoder = MessageDecoder()
    _union_deser = (
        aws_sdk_sagemaker_runtime.types.response_stream.deserialize_event_json
    )
    _iter = cast(Any, response.iter_bytes())
    out: aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_output.InvokeEndpointWithResponseStreamOutput = {
        "body": cast(Any, raw_stream_to_events(_iter, _message_decoder, _union_deser))
    }  # type: ignore[reportAssignmentType]
    if "X-Amzn-SageMaker-Content-Type" in response.headers:
        out["content_type"] = str(response.headers["X-Amzn-SageMaker-Content-Type"])
    if "x-Amzn-Invoked-Production-Variant" in response.headers:
        out["invoked_production_variant"] = str(
            response.headers["x-Amzn-Invoked-Production-Variant"]
        )
    if "X-Amzn-SageMaker-Custom-Attributes" in response.headers:
        out["custom_attributes"] = str(
            response.headers["X-Amzn-SageMaker-Custom-Attributes"]
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_output.InvokeEndpointWithResponseStreamOutput:
    _message_decoder = MessageDecoder()
    _union_deser = (
        aws_sdk_sagemaker_runtime.types.response_stream.deserialize_event_json
    )
    _iter = cast(Any, response.async_iter_bytes())
    out: aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_output.InvokeEndpointWithResponseStreamOutput = {
        "body": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "X-Amzn-SageMaker-Content-Type" in response.headers:
        out["content_type"] = str(response.headers["X-Amzn-SageMaker-Content-Type"])
    if "x-Amzn-Invoked-Production-Variant" in response.headers:
        out["invoked_production_variant"] = str(
            response.headers["x-Amzn-Invoked-Production-Variant"]
        )
    if "X-Amzn-SageMaker-Custom-Attributes" in response.headers:
        out["custom_attributes"] = str(
            response.headers["X-Amzn-SageMaker-Custom-Attributes"]
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sagemaker_runtime._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_sagemaker_runtime._auth._sigv4.build_sigv4_auth_scheme(
                "sagemaker", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_sagemaker_runtime._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_input.InvokeEndpointWithResponseStreamInput,
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
        + "/endpoints/{EndpointName}/invocations-response-stream"
    )
    url = url.replace("{EndpointName}", quote(str(input_["endpoint_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "content_type" in input_:
        headers["Content-Type"] = str(input_["content_type"])
    if "accept" in input_:
        headers["X-Amzn-SageMaker-Accept"] = str(input_["accept"])
    if "custom_attributes" in input_:
        headers["X-Amzn-SageMaker-Custom-Attributes"] = str(input_["custom_attributes"])
    if "target_variant" in input_:
        headers["X-Amzn-SageMaker-Target-Variant"] = str(input_["target_variant"])
    if "target_container_hostname" in input_:
        headers["X-Amzn-SageMaker-Target-Container-Hostname"] = str(
            input_["target_container_hostname"]
        )
    if "inference_id" in input_:
        headers["X-Amzn-SageMaker-Inference-Id"] = str(input_["inference_id"])
    if "inference_component_name" in input_:
        headers["X-Amzn-SageMaker-Inference-Component"] = str(
            input_["inference_component_name"]
        )
    if "session_id" in input_:
        headers["X-Amzn-SageMaker-Session-Id"] = str(input_["session_id"])
    if "body" in input_:
        import aws_sdk_sagemaker_runtime.types.body_blob

        body: bytes | None = json.dumps(
            aws_sdk_sagemaker_runtime.types.body_blob.serialize_json(input_["body"])
        ).encode()
        headers["content-type"] = "application/json"
    else:
        body = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def invoke_endpoint_with_response_stream(
    options: OperationOptions,
    input_: aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_input.InvokeEndpointWithResponseStreamInput,
) -> tuple[
    aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_output.InvokeEndpointWithResponseStreamOutput,
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


async def async_invoke_endpoint_with_response_stream(
    options: AsyncOperationOptions,
    input_: aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_input.InvokeEndpointWithResponseStreamInput,
) -> tuple[
    aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_output.InvokeEndpointWithResponseStreamOutput,
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
