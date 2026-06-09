"""Generated from Smithy shape ``com.amazonaws.kms#DisconnectCustomKeyStore``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any
from aws_sdk_kms._rule_engine._endpoint_rule_set import EndpointParams, resolve
import zapros
from aws_sdk_kms.errors import UnknownServiceError
from aws_sdk_kms._protocol.errors import parse_error_metadata_json
import json
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.disconnect_custom_key_store_request
    import aws_sdk_kms.types.disconnect_custom_key_store_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CustomKeyStoreInvalidStateException":
            import aws_sdk_kms.errors.custom_key_store_invalid_state_exception

            raise aws_sdk_kms.errors.custom_key_store_invalid_state_exception.CustomKeyStoreInvalidStateException.from_aws_json_1_1(
                data
            )
        case "CustomKeyStoreNotFoundException":
            import aws_sdk_kms.errors.custom_key_store_not_found_exception

            raise aws_sdk_kms.errors.custom_key_store_not_found_exception.CustomKeyStoreNotFoundException.from_aws_json_1_1(
                data
            )
        case "KMSInternalException":
            import aws_sdk_kms.errors.kms_internal_exception

            raise aws_sdk_kms.errors.kms_internal_exception.KMSInternalException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_kms.types.disconnect_custom_key_store_response.DisconnectCustomKeyStoreResponse:
    out: aws_sdk_kms.types.disconnect_custom_key_store_response.DisconnectCustomKeyStoreResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_kms._auth._signers.Signer | None:
    if auth_schemes:
        for scheme in auth_schemes:
            match scheme["name"]:
                case "sigv4" | "sigv4a" | "sigv4-s3express" if (
                    options.credentials_provider is not None
                ):
                    return aws_sdk_kms._auth._signers.SigV4Signer(
                        options.credentials_provider, auth_scheme=scheme
                    )
                case "none":
                    return None
                case _:
                    raise RuntimeError(
                        f"Could not find provider for auth scheme {scheme['name']!r}"
                    )
    if options.credentials_provider is not None:
        if options.region is None:
            raise RuntimeError("options.region is required for SigV4 signing")
        return aws_sdk_kms._auth._signers.SigV4Signer(
            options.credentials_provider,
            auth_scheme={
                "name": "sigv4",
                "signingName": "kms",
                "signingRegion": options.region,
                "disableDoubleEncoding": False,
                "disableNormalizePath": False,
            },
        )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_kms.types.disconnect_custom_key_store_request.DisconnectCustomKeyStoreRequest,
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
    headers["X-Amz-Target"] = "TrentService.DisconnectCustomKeyStore"
    import aws_sdk_kms.types.disconnect_custom_key_store_request

    body: bytes | None = json.dumps(
        aws_sdk_kms.types.disconnect_custom_key_store_request.serialize_aws_json_1_1(
            input
        )
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


def disconnect_custom_key_store(
    options: OperationOptions,
    input: aws_sdk_kms.types.disconnect_custom_key_store_request.DisconnectCustomKeyStoreRequest,
) -> tuple[
    aws_sdk_kms.types.disconnect_custom_key_store_response.DisconnectCustomKeyStoreResponse,
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


async def async_disconnect_custom_key_store(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.disconnect_custom_key_store_request.DisconnectCustomKeyStoreRequest,
) -> tuple[
    aws_sdk_kms.types.disconnect_custom_key_store_response.DisconnectCustomKeyStoreResponse,
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
