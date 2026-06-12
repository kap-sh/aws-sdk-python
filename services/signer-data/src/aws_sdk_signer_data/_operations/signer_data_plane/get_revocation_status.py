"""Generated from Smithy shape ``com.amazonaws.signerdata#GetRevocationStatus``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any
from typing import cast
from aws_sdk_signer_data._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_signer_data._rule_engine._endpoint_runtime import apply_label
import zapros
from urllib.parse import quote
from aws_sdk_signer_data.errors import ServiceError, UnknownServiceError
from aws_sdk_signer_data._protocol.errors import parse_error_metadata_json
import json
import aws_sdk_signer_data._auth._signers
import aws_sdk_signer_data._auth._sigv4
from aws_sdk_signer_data._services._pipeline import AsyncOperationOptions, OperationOptions
if TYPE_CHECKING:
    import aws_sdk_signer_data.types.get_revocation_status_request
    import aws_sdk_signer_data.types.get_revocation_status_response

def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_signer_data.errors.access_denied_exception
            raise aws_sdk_signer_data.errors.access_denied_exception.AccessDeniedException.from_json(data)
        case "InternalServiceErrorException":
            import aws_sdk_signer_data.errors.internal_service_error_exception
            raise aws_sdk_signer_data.errors.internal_service_error_exception.InternalServiceErrorException.from_json(data)
        case "TooManyRequestsException":
            import aws_sdk_signer_data.errors.too_many_requests_exception
            raise aws_sdk_signer_data.errors.too_many_requests_exception.TooManyRequestsException.from_json(data)
        case "ValidationException":
            import aws_sdk_signer_data.errors.validation_exception
            raise aws_sdk_signer_data.errors.validation_exception.ValidationException.from_json(data)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)

def handle_response(response: zapros.Response, is_async: bool) -> aws_sdk_signer_data.types.get_revocation_status_response.GetRevocationStatusResponse:
    import aws_sdk_signer_data.types.get_revocation_status_response
    out: aws_sdk_signer_data.types.get_revocation_status_response.GetRevocationStatusResponse = aws_sdk_signer_data.types.get_revocation_status_response.deserialize_json(json.loads(response.read()))
    return out

def get_signer(options: AsyncOperationOptions | OperationOptions, auth_schemes: list[dict[str, Any]] | None = None) -> aws_sdk_signer_data._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = name_to_schema.get("sigv4") or name_to_schema.get("sigv4a") or name_to_schema.get("sigv4-s3express") or aws_sdk_signer_data._auth._sigv4.build_sigv4_auth_scheme('signer', options.region)
        if sigv4_config is not None:
            return aws_sdk_signer_data._auth._signers.SigV4Signer(options.credentials_provider, auth_scheme=sigv4_config)
    raise RuntimeError("Auth was not resolved")

def build_request(options: OperationOptions | AsyncOperationOptions, input: aws_sdk_signer_data.types.get_revocation_status_request.GetRevocationStatusRequest) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/revocations"
    params: dict[str, str] = {}
    if "signature_timestamp" in input:
        params["signatureTimestamp"] = str(input["signature_timestamp"])
    if "platform_id" in input:
        params["platformId"] = str(input["platform_id"])
    if "profile_version_arn" in input:
        params["profileVersionArn"] = str(input["profile_version_arn"])
    if "job_arn" in input:
        params["jobArn"] = str(input["job_arn"])
    if "certificate_hashes" in input:
        params["certificateHashes"] = str(input["certificate_hashes"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "GET",
        headers=headers,
        body=body,
        context={"signer": signer},
    )

def get_revocation_status(options: OperationOptions, input: aws_sdk_signer_data.types.get_revocation_status_request.GetRevocationStatusRequest) -> tuple[aws_sdk_signer_data.types.get_revocation_status_response.GetRevocationStatusResponse, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise

async def async_get_revocation_status(options: AsyncOperationOptions, input: aws_sdk_signer_data.types.get_revocation_status_request.GetRevocationStatusRequest) -> tuple[aws_sdk_signer_data.types.get_revocation_status_response.GetRevocationStatusResponse, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise