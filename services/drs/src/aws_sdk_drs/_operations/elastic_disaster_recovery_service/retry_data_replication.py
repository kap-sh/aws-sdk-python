"""Generated from Smithy shape ``com.amazonaws.drs#RetryDataReplication``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any
from typing import cast
from aws_sdk_drs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_drs._rule_engine._endpoint_runtime import apply_label
import zapros
from urllib.parse import quote
from aws_sdk_drs.errors import ServiceError, UnknownServiceError
from aws_sdk_drs._protocol.errors import parse_error_metadata_json
import json
import aws_sdk_drs._auth._signers
import aws_sdk_drs._auth._sigv4
from aws_sdk_drs._services._pipeline import AsyncOperationOptions, OperationOptions
if TYPE_CHECKING:
    import aws_sdk_drs.types.retry_data_replication_request
    import aws_sdk_drs.types.source_server

def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            import aws_sdk_drs.errors.internal_server_exception
            raise aws_sdk_drs.errors.internal_server_exception.InternalServerException.from_json(data)
        case "ResourceNotFoundException":
            import aws_sdk_drs.errors.resource_not_found_exception
            raise aws_sdk_drs.errors.resource_not_found_exception.ResourceNotFoundException.from_json(data)
        case "ThrottlingException":
            import aws_sdk_drs.errors.throttling_exception
            raise aws_sdk_drs.errors.throttling_exception.ThrottlingException.from_json(data)
        case "UninitializedAccountException":
            import aws_sdk_drs.errors.uninitialized_account_exception
            raise aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException.from_json(data)
        case "ValidationException":
            import aws_sdk_drs.errors.validation_exception
            raise aws_sdk_drs.errors.validation_exception.ValidationException.from_json(data)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)

def handle_response(response: zapros.Response, is_async: bool) -> aws_sdk_drs.types.source_server.SourceServer:
    import aws_sdk_drs.types.source_server
    out: aws_sdk_drs.types.source_server.SourceServer = aws_sdk_drs.types.source_server.deserialize_json(json.loads(response.read()))
    return out

def get_signer(options: AsyncOperationOptions | OperationOptions, auth_schemes: list[dict[str, Any]] | None = None) -> aws_sdk_drs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = name_to_schema.get("sigv4") or name_to_schema.get("sigv4a") or name_to_schema.get("sigv4-s3express") or aws_sdk_drs._auth._sigv4.build_sigv4_auth_scheme('drs', options.region)
        if sigv4_config is not None:
            return aws_sdk_drs._auth._signers.SigV4Signer(options.credentials_provider, auth_scheme=sigv4_config)
    raise RuntimeError("Auth was not resolved")

def build_request(options: OperationOptions | AsyncOperationOptions, input: aws_sdk_drs.types.retry_data_replication_request.RetryDataReplicationRequest) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/RetryDataReplication"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_drs.types.retry_data_replication_request
    body: bytes | None = json.dumps(aws_sdk_drs.types.retry_data_replication_request.serialize_json(input)).encode()
    headers["content-type"] = "application/json"
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

def retry_data_replication(options: OperationOptions, input: aws_sdk_drs.types.retry_data_replication_request.RetryDataReplicationRequest) -> tuple[aws_sdk_drs.types.source_server.SourceServer, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise

async def async_retry_data_replication(options: AsyncOperationOptions, input: aws_sdk_drs.types.retry_data_replication_request.RetryDataReplicationRequest) -> tuple[aws_sdk_drs.types.source_server.SourceServer, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise