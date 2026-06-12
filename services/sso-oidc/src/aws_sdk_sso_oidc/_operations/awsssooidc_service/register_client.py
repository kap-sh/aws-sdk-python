"""Generated from Smithy shape ``com.amazonaws.ssooidc#RegisterClient``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_sso_oidc._auth._signers
import aws_sdk_sso_oidc._auth._sigv4
from aws_sdk_sso_oidc._protocol.errors import parse_error_metadata_json
from aws_sdk_sso_oidc._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_sso_oidc._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_sso_oidc.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_sso_oidc.types.register_client_request
    import aws_sdk_sso_oidc.types.register_client_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            import aws_sdk_sso_oidc.errors.internal_server_exception

            raise aws_sdk_sso_oidc.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "InvalidClientMetadataException":
            import aws_sdk_sso_oidc.errors.invalid_client_metadata_exception

            raise aws_sdk_sso_oidc.errors.invalid_client_metadata_exception.InvalidClientMetadataException.from_json(
                data
            )
        case "InvalidRedirectUriException":
            import aws_sdk_sso_oidc.errors.invalid_redirect_uri_exception

            raise aws_sdk_sso_oidc.errors.invalid_redirect_uri_exception.InvalidRedirectUriException.from_json(
                data
            )
        case "InvalidRequestException":
            import aws_sdk_sso_oidc.errors.invalid_request_exception

            raise aws_sdk_sso_oidc.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "InvalidScopeException":
            import aws_sdk_sso_oidc.errors.invalid_scope_exception

            raise aws_sdk_sso_oidc.errors.invalid_scope_exception.InvalidScopeException.from_json(
                data
            )
        case "SlowDownException":
            import aws_sdk_sso_oidc.errors.slow_down_exception

            raise aws_sdk_sso_oidc.errors.slow_down_exception.SlowDownException.from_json(
                data
            )
        case "UnsupportedGrantTypeException":
            import aws_sdk_sso_oidc.errors.unsupported_grant_type_exception

            raise aws_sdk_sso_oidc.errors.unsupported_grant_type_exception.UnsupportedGrantTypeException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_sso_oidc.types.register_client_response.RegisterClientResponse:
    import aws_sdk_sso_oidc.types.register_client_response

    out: aws_sdk_sso_oidc.types.register_client_response.RegisterClientResponse = (
        aws_sdk_sso_oidc.types.register_client_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sso_oidc._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_sso_oidc._auth._sigv4.build_sigv4_auth_scheme(
                "sso-oauth", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_sso_oidc._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    return None


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_sso_oidc.types.register_client_request.RegisterClientRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/client/register"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_sso_oidc.types.register_client_request

    body: bytes | None = json.dumps(
        aws_sdk_sso_oidc.types.register_client_request.serialize_json(input)
    ).encode()
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


def register_client(
    options: OperationOptions,
    input: aws_sdk_sso_oidc.types.register_client_request.RegisterClientRequest,
) -> tuple[
    aws_sdk_sso_oidc.types.register_client_response.RegisterClientResponse,
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


async def async_register_client(
    options: AsyncOperationOptions,
    input: aws_sdk_sso_oidc.types.register_client_request.RegisterClientRequest,
) -> tuple[
    aws_sdk_sso_oidc.types.register_client_response.RegisterClientResponse,
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
