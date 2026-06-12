"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#InvokeEndpointAsync``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_sagemaker_runtime._auth._signers
import aws_sdk_sagemaker_runtime._auth._sigv4
from aws_sdk_sagemaker_runtime._protocol.errors import parse_error_metadata_json
from aws_sdk_sagemaker_runtime._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_sagemaker_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_sagemaker_runtime.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime.types.invoke_endpoint_async_input
    import aws_sdk_sagemaker_runtime.types.invoke_endpoint_async_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalFailure":
            import aws_sdk_sagemaker_runtime.errors.internal_failure

            raise aws_sdk_sagemaker_runtime.errors.internal_failure.InternalFailure.from_json(
                data
            )
        case "ServiceUnavailable":
            import aws_sdk_sagemaker_runtime.errors.service_unavailable

            raise aws_sdk_sagemaker_runtime.errors.service_unavailable.ServiceUnavailable.from_json(
                data
            )
        case "ValidationError":
            import aws_sdk_sagemaker_runtime.errors.validation_error

            raise aws_sdk_sagemaker_runtime.errors.validation_error.ValidationError.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_sagemaker_runtime.types.invoke_endpoint_async_output.InvokeEndpointAsyncOutput:
    import aws_sdk_sagemaker_runtime.types.invoke_endpoint_async_output

    out: aws_sdk_sagemaker_runtime.types.invoke_endpoint_async_output.InvokeEndpointAsyncOutput = aws_sdk_sagemaker_runtime.types.invoke_endpoint_async_output.deserialize_json(
        json.loads(response.read())
    )
    if "X-Amzn-SageMaker-OutputLocation" in response.headers:
        out["output_location"] = str(
            response.headers["X-Amzn-SageMaker-OutputLocation"]
        )
    if "X-Amzn-SageMaker-FailureLocation" in response.headers:
        out["failure_location"] = str(
            response.headers["X-Amzn-SageMaker-FailureLocation"]
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sagemaker_runtime._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
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
    input: aws_sdk_sagemaker_runtime.types.invoke_endpoint_async_input.InvokeEndpointAsyncInput,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/endpoints/{EndpointName}/async-invocations"
    url = url.replace("{EndpointName}", quote(str(input["endpoint_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "content_type" in input:
        headers["X-Amzn-SageMaker-Content-Type"] = str(input["content_type"])
    if "accept" in input:
        headers["X-Amzn-SageMaker-Accept"] = str(input["accept"])
    if "custom_attributes" in input:
        headers["X-Amzn-SageMaker-Custom-Attributes"] = str(input["custom_attributes"])
    if "inference_id" in input:
        headers["X-Amzn-SageMaker-Inference-Id"] = str(input["inference_id"])
    if "input_location" in input:
        headers["X-Amzn-SageMaker-InputLocation"] = str(input["input_location"])
    if "s3_output_path_extension" in input:
        headers["X-Amzn-SageMaker-S3OutputPathExtension"] = str(
            input["s3_output_path_extension"]
        )
    if "filename" in input:
        headers["X-Amzn-SageMaker-Filename"] = str(input["filename"])
    if "request_ttl_seconds" in input:
        headers["X-Amzn-SageMaker-RequestTTLSeconds"] = str(
            input["request_ttl_seconds"]
        )
    if "invocation_timeout_seconds" in input:
        headers["X-Amzn-SageMaker-InvocationTimeoutSeconds"] = str(
            input["invocation_timeout_seconds"]
        )
    body: bytes | None = b""
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


def invoke_endpoint_async(
    options: OperationOptions,
    input: aws_sdk_sagemaker_runtime.types.invoke_endpoint_async_input.InvokeEndpointAsyncInput,
) -> tuple[
    aws_sdk_sagemaker_runtime.types.invoke_endpoint_async_output.InvokeEndpointAsyncOutput,
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


async def async_invoke_endpoint_async(
    options: AsyncOperationOptions,
    input: aws_sdk_sagemaker_runtime.types.invoke_endpoint_async_input.InvokeEndpointAsyncInput,
) -> tuple[
    aws_sdk_sagemaker_runtime.types.invoke_endpoint_async_output.InvokeEndpointAsyncOutput,
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
