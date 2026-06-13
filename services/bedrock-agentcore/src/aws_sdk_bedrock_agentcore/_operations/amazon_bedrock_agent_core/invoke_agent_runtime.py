"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeAgentRuntime``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any, cast
from aws_sdk_bedrock_agentcore._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_bedrock_agentcore._rule_engine._endpoint_runtime import apply_label
import jmespath
import zapros
from urllib.parse import quote, urlencode
from aws_sdk_bedrock_agentcore.errors import ServiceError, UnknownServiceError
from aws_sdk_bedrock_agentcore._protocol.errors import parse_error_metadata_json
import json
import aws_sdk_bedrock_agentcore._auth._signers
import aws_sdk_bedrock_agentcore._auth._sigv4
from aws_sdk_bedrock_agentcore._services._pipeline import AsyncOperationOptions, OperationOptions
import datetime
from email.utils import parsedate_to_datetime as _parse_http_date
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_request
    import aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_response

def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_bedrock_agentcore.errors.access_denied_exception
            raise aws_sdk_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException.from_json(data)
        case "InternalServerException":
            import aws_sdk_bedrock_agentcore.errors.internal_server_exception
            raise aws_sdk_bedrock_agentcore.errors.internal_server_exception.InternalServerException.from_json(data)
        case "ResourceNotFoundException":
            import aws_sdk_bedrock_agentcore.errors.resource_not_found_exception
            raise aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException.from_json(data)
        case "RetryableConflictException":
            import aws_sdk_bedrock_agentcore.errors.retryable_conflict_exception
            raise aws_sdk_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException.from_json(data)
        case "RuntimeClientError":
            import aws_sdk_bedrock_agentcore.errors.runtime_client_error
            raise aws_sdk_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError.from_json(data)
        case "ServiceQuotaExceededException":
            import aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception
            raise aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(data)
        case "ThrottlingException":
            import aws_sdk_bedrock_agentcore.errors.throttling_exception
            raise aws_sdk_bedrock_agentcore.errors.throttling_exception.ThrottlingException.from_json(data)
        case "ValidationException":
            import aws_sdk_bedrock_agentcore.errors.validation_exception
            raise aws_sdk_bedrock_agentcore.errors.validation_exception.ValidationException.from_json(data)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)

def handle_response(response: zapros.Response, is_async: bool) -> aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse:
    _iter = cast(Any, response.async_iter_bytes() if is_async else response.iter_bytes())
    out: aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse = {"response": _iter}
    if "X-Amzn-Bedrock-AgentCore-Runtime-Session-Id" in response.headers:
        out["runtime_session_id"] = str(response.headers["X-Amzn-Bedrock-AgentCore-Runtime-Session-Id"])
    if "Mcp-Session-Id" in response.headers:
        out["mcp_session_id"] = str(response.headers["Mcp-Session-Id"])
    if "Mcp-Protocol-Version" in response.headers:
        out["mcp_protocol_version"] = str(response.headers["Mcp-Protocol-Version"])
    if "X-Amzn-Trace-Id" in response.headers:
        out["trace_id"] = str(response.headers["X-Amzn-Trace-Id"])
    if "traceparent" in response.headers:
        out["trace_parent"] = str(response.headers["traceparent"])
    if "tracestate" in response.headers:
        out["trace_state"] = str(response.headers["tracestate"])
    if "baggage" in response.headers:
        out["baggage"] = str(response.headers["baggage"])
    out["content_type"] = str(response.headers["Content-Type"])
    out["status_code"] = response.status
    return out

def get_signer(options: AsyncOperationOptions | OperationOptions, auth_schemes: list[dict[str, Any]] | None = None) -> aws_sdk_bedrock_agentcore._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = name_to_schema.get("sigv4") or name_to_schema.get("sigv4a") or name_to_schema.get("sigv4-s3express") or aws_sdk_bedrock_agentcore._auth._sigv4.build_sigv4_auth_scheme('bedrock-agentcore', options.region)
        if sigv4_config is not None:
            return aws_sdk_bedrock_agentcore._auth._signers.SigV4Signer(options.credentials_provider, auth_scheme=sigv4_config)
    raise RuntimeError("Auth was not resolved")

def build_request(options: OperationOptions | AsyncOperationOptions, input: aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_request.InvokeAgentRuntimeRequest) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/runtimes/{agentRuntimeArn}/invocations"
    url = url.replace("{agentRuntimeArn}", quote(str(input["agent_runtime_arn"]), safe=""))
    params: dict[str, str] = {}
    if "qualifier" in input:
        params["qualifier"] = str(input["qualifier"])
    if "account_id" in input:
        params["accountId"] = str(input["account_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "content_type" in input:
        headers["Content-Type"] = str(input["content_type"])
    if "accept" in input:
        headers["Accept"] = str(input["accept"])
    if "mcp_session_id" in input:
        headers["Mcp-Session-Id"] = str(input["mcp_session_id"])
    if "runtime_session_id" in input:
        headers["X-Amzn-Bedrock-AgentCore-Runtime-Session-Id"] = str(input["runtime_session_id"])
    if "mcp_protocol_version" in input:
        headers["Mcp-Protocol-Version"] = str(input["mcp_protocol_version"])
    if "runtime_user_id" in input:
        headers["X-Amzn-Bedrock-AgentCore-Runtime-User-Id"] = str(input["runtime_user_id"])
    if "trace_id" in input:
        headers["X-Amzn-Trace-Id"] = str(input["trace_id"])
    if "trace_parent" in input:
        headers["traceparent"] = str(input["trace_parent"])
    if "trace_state" in input:
        headers["tracestate"] = str(input["trace_state"])
    if "baggage" in input:
        headers["baggage"] = str(input["baggage"])
    if "payload" in input:
        import aws_sdk_bedrock_agentcore.types.body
        body: bytes | None = json.dumps(aws_sdk_bedrock_agentcore.types.body.serialize_json(input["payload"])).encode()
        headers["content-type"] = "application/json"
    else:
        body = b""
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

def invoke_agent_runtime(options: OperationOptions, input: aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_request.InvokeAgentRuntimeRequest) -> tuple[aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise

async def async_invoke_agent_runtime(options: AsyncOperationOptions, input: aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_request.InvokeAgentRuntimeRequest) -> tuple[aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise