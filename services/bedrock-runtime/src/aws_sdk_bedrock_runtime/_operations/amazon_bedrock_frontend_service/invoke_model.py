"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModel``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_bedrock_runtime._auth._signers
import aws_sdk_bedrock_runtime._auth._sigv4
from aws_sdk_bedrock_runtime._protocol.errors import parse_error_metadata_json
from aws_sdk_bedrock_runtime._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_bedrock_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_bedrock_runtime.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.invoke_model_request
    import aws_sdk_bedrock_runtime.types.invoke_model_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_bedrock_runtime.errors.access_denied_exception

            raise aws_sdk_bedrock_runtime.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_bedrock_runtime.errors.internal_server_exception

            raise aws_sdk_bedrock_runtime.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ModelErrorException":
            import aws_sdk_bedrock_runtime.errors.model_error_exception

            raise aws_sdk_bedrock_runtime.errors.model_error_exception.ModelErrorException.from_json(
                data
            )
        case "ModelNotReadyException":
            import aws_sdk_bedrock_runtime.errors.model_not_ready_exception

            raise aws_sdk_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException.from_json(
                data
            )
        case "ModelTimeoutException":
            import aws_sdk_bedrock_runtime.errors.model_timeout_exception

            raise aws_sdk_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_bedrock_runtime.errors.resource_not_found_exception

            raise aws_sdk_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            import aws_sdk_bedrock_runtime.errors.service_quota_exceeded_exception

            raise aws_sdk_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ServiceUnavailableException":
            import aws_sdk_bedrock_runtime.errors.service_unavailable_exception

            raise aws_sdk_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_bedrock_runtime.errors.throttling_exception

            raise aws_sdk_bedrock_runtime.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_bedrock_runtime.errors.validation_exception

            raise aws_sdk_bedrock_runtime.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_bedrock_runtime.types.invoke_model_response.InvokeModelResponse:
    import aws_sdk_bedrock_runtime.types.body

    out: aws_sdk_bedrock_runtime.types.invoke_model_response.InvokeModelResponse = {
        "body": aws_sdk_bedrock_runtime.types.body.deserialize_json(
            json.loads(response.read())
        )
    }  # type: ignore[typeddict-item]
    out["content_type"] = str(response.headers["Content-Type"])
    if "X-Amzn-Bedrock-PerformanceConfig-Latency" in response.headers:
        import aws_sdk_bedrock_runtime.types.performance_config_latency

        out["performance_config_latency"] = (
            aws_sdk_bedrock_runtime.types.performance_config_latency.from_xml_text(
                response.headers["X-Amzn-Bedrock-PerformanceConfig-Latency"]
            )
        )
    if "X-Amzn-Bedrock-Service-Tier" in response.headers:
        import aws_sdk_bedrock_runtime.types.service_tier_type

        out["service_tier"] = (
            aws_sdk_bedrock_runtime.types.service_tier_type.from_xml_text(
                response.headers["X-Amzn-Bedrock-Service-Tier"]
            )
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_bedrock_runtime._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
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
    input_: aws_sdk_bedrock_runtime.types.invoke_model_request.InvokeModelRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/model/{modelId}/invoke"
    url = url.replace("{modelId}", quote(str(input_["model_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "content_type" in input_:
        headers["Content-Type"] = str(input_["content_type"])
    if "accept" in input_:
        headers["Accept"] = str(input_["accept"])
    if "trace" in input_:
        headers["X-Amzn-Bedrock-Trace"] = str(input_["trace"])
    if "guardrail_identifier" in input_:
        headers["X-Amzn-Bedrock-GuardrailIdentifier"] = str(
            input_["guardrail_identifier"]
        )
    if "guardrail_version" in input_:
        headers["X-Amzn-Bedrock-GuardrailVersion"] = str(input_["guardrail_version"])
    headers["X-Amzn-Bedrock-PerformanceConfig-Latency"] = str(
        input_.get("performance_config_latency", "standard")
    )
    if "service_tier" in input_:
        headers["X-Amzn-Bedrock-Service-Tier"] = str(input_["service_tier"])
    if "request_metadata" in input_:
        headers["X-Amzn-Bedrock-Request-Metadata"] = str(input_["request_metadata"])
    if "body" in input_:
        import aws_sdk_bedrock_runtime.types.body

        body: bytes | None = json.dumps(
            aws_sdk_bedrock_runtime.types.body.serialize_json(input_["body"])
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


def invoke_model(
    options: OperationOptions,
    input_: aws_sdk_bedrock_runtime.types.invoke_model_request.InvokeModelRequest,
) -> tuple[
    aws_sdk_bedrock_runtime.types.invoke_model_response.InvokeModelResponse,
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


async def async_invoke_model(
    options: AsyncOperationOptions,
    input_: aws_sdk_bedrock_runtime.types.invoke_model_request.InvokeModelRequest,
) -> tuple[
    aws_sdk_bedrock_runtime.types.invoke_model_response.InvokeModelResponse,
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
