"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#InvokeEndpoint``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_sagemaker_runtime._auth._signers
import capo_sagemaker_runtime._auth._sigv4
import capo_sagemaker_runtime.errors.internal_dependency_exception
import capo_sagemaker_runtime.errors.internal_failure
import capo_sagemaker_runtime.errors.model_error
import capo_sagemaker_runtime.errors.model_not_ready_exception
import capo_sagemaker_runtime.errors.service_unavailable
import capo_sagemaker_runtime.errors.validation_error
import capo_sagemaker_runtime.types.body_blob
import capo_sagemaker_runtime.types.invoke_endpoint_input
import capo_sagemaker_runtime.types.invoke_endpoint_output
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
        case "InternalDependencyException":
            raise capo_sagemaker_runtime.errors.internal_dependency_exception.InternalDependencyException.from_json(
                data
            )
        case "InternalFailure":
            raise capo_sagemaker_runtime.errors.internal_failure.InternalFailure.from_json(
                data
            )
        case "ModelError":
            raise capo_sagemaker_runtime.errors.model_error.ModelError.from_json(data)
        case "ModelNotReadyException":
            raise capo_sagemaker_runtime.errors.model_not_ready_exception.ModelNotReadyException.from_json(
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
) -> capo_sagemaker_runtime.types.invoke_endpoint_output.InvokeEndpointOutput:
    out: capo_sagemaker_runtime.types.invoke_endpoint_output.InvokeEndpointOutput = {
        "body": capo_sagemaker_runtime.types.body_blob.deserialize_json(
            json.loads(response.read())
        )
    }  # type: ignore[typeddict-item]
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    if "x-Amzn-Invoked-Production-Variant" in response.headers:
        out["invoked_production_variant"] = str(
            response.headers["x-Amzn-Invoked-Production-Variant"]
        )
    if "X-Amzn-SageMaker-Custom-Attributes" in response.headers:
        out["custom_attributes"] = str(
            response.headers["X-Amzn-SageMaker-Custom-Attributes"]
        )
    if "X-Amzn-SageMaker-New-Session-Id" in response.headers:
        out["new_session_id"] = str(response.headers["X-Amzn-SageMaker-New-Session-Id"])
    if "X-Amzn-SageMaker-Closed-Session-Id" in response.headers:
        out["closed_session_id"] = str(
            response.headers["X-Amzn-SageMaker-Closed-Session-Id"]
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_sagemaker_runtime.types.invoke_endpoint_output.InvokeEndpointOutput:
    out: capo_sagemaker_runtime.types.invoke_endpoint_output.InvokeEndpointOutput = {
        "body": capo_sagemaker_runtime.types.body_blob.deserialize_json(
            json.loads(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    if "x-Amzn-Invoked-Production-Variant" in response.headers:
        out["invoked_production_variant"] = str(
            response.headers["x-Amzn-Invoked-Production-Variant"]
        )
    if "X-Amzn-SageMaker-Custom-Attributes" in response.headers:
        out["custom_attributes"] = str(
            response.headers["X-Amzn-SageMaker-Custom-Attributes"]
        )
    if "X-Amzn-SageMaker-New-Session-Id" in response.headers:
        out["new_session_id"] = str(response.headers["X-Amzn-SageMaker-New-Session-Id"])
    if "X-Amzn-SageMaker-Closed-Session-Id" in response.headers:
        out["closed_session_id"] = str(
            response.headers["X-Amzn-SageMaker-Closed-Session-Id"]
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
    input_: capo_sagemaker_runtime.types.invoke_endpoint_input.InvokeEndpointInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/endpoints/{EndpointName}/invocations"
    url = url.replace("{EndpointName}", quote(str(input_["endpoint_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "content_type" in input_:
        headers["Content-Type"] = str(input_["content_type"])
    if "accept" in input_:
        headers["Accept"] = str(input_["accept"])
    if "custom_attributes" in input_:
        headers["X-Amzn-SageMaker-Custom-Attributes"] = str(input_["custom_attributes"])
    if "target_model" in input_:
        headers["X-Amzn-SageMaker-Target-Model"] = str(input_["target_model"])
    if "target_variant" in input_:
        headers["X-Amzn-SageMaker-Target-Variant"] = str(input_["target_variant"])
    if "target_container_hostname" in input_:
        headers["X-Amzn-SageMaker-Target-Container-Hostname"] = str(
            input_["target_container_hostname"]
        )
    if "inference_id" in input_:
        headers["X-Amzn-SageMaker-Inference-Id"] = str(input_["inference_id"])
    if "enable_explanations" in input_:
        headers["X-Amzn-SageMaker-Enable-Explanations"] = str(
            input_["enable_explanations"]
        )
    if "inference_component_name" in input_:
        headers["X-Amzn-SageMaker-Inference-Component"] = str(
            input_["inference_component_name"]
        )
    if "session_id" in input_:
        headers["X-Amzn-SageMaker-Session-Id"] = str(input_["session_id"])
    if "body" in input_:
        body: bytes | None = json.dumps(
            capo_sagemaker_runtime.types.body_blob.serialize_json(input_["body"])
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


def invoke_endpoint(
    options: OperationOptions,
    input_: capo_sagemaker_runtime.types.invoke_endpoint_input.InvokeEndpointInput,
) -> tuple[
    capo_sagemaker_runtime.types.invoke_endpoint_output.InvokeEndpointOutput,
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


async def async_invoke_endpoint(
    options: AsyncOperationOptions,
    input_: capo_sagemaker_runtime.types.invoke_endpoint_input.InvokeEndpointInput,
) -> tuple[
    capo_sagemaker_runtime.types.invoke_endpoint_output.InvokeEndpointOutput,
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
