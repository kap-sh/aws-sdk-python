"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#InvokeEndpointAsync``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_sagemaker_runtime._auth._signers
import capo_sagemaker_runtime._auth._sigv4
import capo_sagemaker_runtime.errors.internal_failure
import capo_sagemaker_runtime.errors.service_unavailable
import capo_sagemaker_runtime.errors.validation_error
import capo_sagemaker_runtime.types.invoke_endpoint_async_input
import capo_sagemaker_runtime.types.invoke_endpoint_async_output
from capo_sagemaker_runtime._protocol.errors import parse_error_metadata_json
from capo_sagemaker_runtime._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_sagemaker_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_sagemaker_runtime.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalFailure":
            raise capo_sagemaker_runtime.errors.internal_failure.InternalFailure.from_json(
                data
            )
        case "ServiceUnavailable":
            raise capo_sagemaker_runtime.errors.service_unavailable.ServiceUnavailable.from_json(
                data
            )
        case "ValidationError":
            raise capo_sagemaker_runtime.errors.validation_error.ValidationError.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    capo_sagemaker_runtime.types.invoke_endpoint_async_output.InvokeEndpointAsyncOutput
):
    out: capo_sagemaker_runtime.types.invoke_endpoint_async_output.InvokeEndpointAsyncOutput = capo_sagemaker_runtime.types.invoke_endpoint_async_output.deserialize_json(
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


async def async_handle_response(
    response: zapros.Response,
) -> (
    capo_sagemaker_runtime.types.invoke_endpoint_async_output.InvokeEndpointAsyncOutput
):
    out: capo_sagemaker_runtime.types.invoke_endpoint_async_output.InvokeEndpointAsyncOutput = capo_sagemaker_runtime.types.invoke_endpoint_async_output.deserialize_json(
        json.loads(await response.aread())
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
) -> capo_sagemaker_runtime._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_sagemaker_runtime._auth._sigv4.build_sigv4_auth_scheme(
                "sagemaker", options.region
            )
        )
        if sigv4_config is not None:
            return capo_sagemaker_runtime._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_sagemaker_runtime.types.invoke_endpoint_async_input.InvokeEndpointAsyncInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/endpoints/{EndpointName}/async-invocations"
    url = url.replace("{EndpointName}", quote(str(input_["endpoint_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "content_type" in input_:
        headers["X-Amzn-SageMaker-Content-Type"] = str(input_["content_type"])
    if "accept" in input_:
        headers["X-Amzn-SageMaker-Accept"] = str(input_["accept"])
    if "custom_attributes" in input_:
        headers["X-Amzn-SageMaker-Custom-Attributes"] = str(input_["custom_attributes"])
    if "inference_id" in input_:
        headers["X-Amzn-SageMaker-Inference-Id"] = str(input_["inference_id"])
    if "input_location" in input_:
        headers["X-Amzn-SageMaker-InputLocation"] = str(input_["input_location"])
    if "s3_output_path_extension" in input_:
        headers["X-Amzn-SageMaker-S3OutputPathExtension"] = str(
            input_["s3_output_path_extension"]
        )
    if "filename" in input_:
        headers["X-Amzn-SageMaker-Filename"] = str(input_["filename"])
    if "request_ttl_seconds" in input_:
        headers["X-Amzn-SageMaker-RequestTTLSeconds"] = str(
            input_["request_ttl_seconds"]
        )
    if "invocation_timeout_seconds" in input_:
        headers["X-Amzn-SageMaker-InvocationTimeoutSeconds"] = str(
            input_["invocation_timeout_seconds"]
        )
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def invoke_endpoint_async(
    options: OperationOptions,
    input_: capo_sagemaker_runtime.types.invoke_endpoint_async_input.InvokeEndpointAsyncInput,
) -> tuple[
    capo_sagemaker_runtime.types.invoke_endpoint_async_output.InvokeEndpointAsyncOutput,
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


async def async_invoke_endpoint_async(
    options: AsyncOperationOptions,
    input_: capo_sagemaker_runtime.types.invoke_endpoint_async_input.InvokeEndpointAsyncInput,
) -> tuple[
    capo_sagemaker_runtime.types.invoke_endpoint_async_output.InvokeEndpointAsyncOutput,
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
