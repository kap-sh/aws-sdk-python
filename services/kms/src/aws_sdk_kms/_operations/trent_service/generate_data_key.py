"""Generated from Smithy shape ``com.amazonaws.kms#GenerateDataKey``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_kms._auth._signers
import aws_sdk_kms._auth._sigv4
from aws_sdk_kms._protocol.errors import parse_error_metadata_json
from aws_sdk_kms._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_kms.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.generate_data_key_request
    import aws_sdk_kms.types.generate_data_key_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "DependencyTimeoutException":
            import aws_sdk_kms.errors.dependency_timeout_exception

            raise aws_sdk_kms.errors.dependency_timeout_exception.DependencyTimeoutException.from_aws_json_1_1(
                data
            )
        case "DisabledException":
            import aws_sdk_kms.errors.disabled_exception

            raise aws_sdk_kms.errors.disabled_exception.DisabledException.from_aws_json_1_1(
                data
            )
        case "DryRunOperationException":
            import aws_sdk_kms.errors.dry_run_operation_exception

            raise aws_sdk_kms.errors.dry_run_operation_exception.DryRunOperationException.from_aws_json_1_1(
                data
            )
        case "InvalidGrantTokenException":
            import aws_sdk_kms.errors.invalid_grant_token_exception

            raise aws_sdk_kms.errors.invalid_grant_token_exception.InvalidGrantTokenException.from_aws_json_1_1(
                data
            )
        case "InvalidKeyUsageException":
            import aws_sdk_kms.errors.invalid_key_usage_exception

            raise aws_sdk_kms.errors.invalid_key_usage_exception.InvalidKeyUsageException.from_aws_json_1_1(
                data
            )
        case "KeyUnavailableException":
            import aws_sdk_kms.errors.key_unavailable_exception

            raise aws_sdk_kms.errors.key_unavailable_exception.KeyUnavailableException.from_aws_json_1_1(
                data
            )
        case "KMSInternalException":
            import aws_sdk_kms.errors.kms_internal_exception

            raise aws_sdk_kms.errors.kms_internal_exception.KMSInternalException.from_aws_json_1_1(
                data
            )
        case "KMSInvalidStateException":
            import aws_sdk_kms.errors.kms_invalid_state_exception

            raise aws_sdk_kms.errors.kms_invalid_state_exception.KMSInvalidStateException.from_aws_json_1_1(
                data
            )
        case "NotFoundException":
            import aws_sdk_kms.errors.not_found_exception

            raise aws_sdk_kms.errors.not_found_exception.NotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_kms.types.generate_data_key_response.GenerateDataKeyResponse:
    import aws_sdk_kms.types.generate_data_key_response

    out: aws_sdk_kms.types.generate_data_key_response.GenerateDataKeyResponse = (
        aws_sdk_kms.types.generate_data_key_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_kms._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_kms._auth._sigv4.build_sigv4_auth_scheme("kms", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_kms._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_kms.types.generate_data_key_request.GenerateDataKeyRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "TrentService.GenerateDataKey"
    import aws_sdk_kms.types.generate_data_key_request

    body: bytes | None = json.dumps(
        aws_sdk_kms.types.generate_data_key_request.serialize_aws_json_1_1(input)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
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


def generate_data_key(
    options: OperationOptions,
    input: aws_sdk_kms.types.generate_data_key_request.GenerateDataKeyRequest,
) -> tuple[
    aws_sdk_kms.types.generate_data_key_response.GenerateDataKeyResponse,
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


async def async_generate_data_key(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.generate_data_key_request.GenerateDataKeyRequest,
) -> tuple[
    aws_sdk_kms.types.generate_data_key_response.GenerateDataKeyResponse,
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
