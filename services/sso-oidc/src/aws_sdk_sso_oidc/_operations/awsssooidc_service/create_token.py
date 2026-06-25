"""Generated from Smithy shape ``com.amazonaws.ssooidc#CreateToken``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_sso_oidc._auth._signers
import aws_sdk_sso_oidc._auth._sigv4
import aws_sdk_sso_oidc.errors.access_denied_exception
import aws_sdk_sso_oidc.errors.authorization_pending_exception
import aws_sdk_sso_oidc.errors.expired_token_exception
import aws_sdk_sso_oidc.errors.internal_server_exception
import aws_sdk_sso_oidc.errors.invalid_client_exception
import aws_sdk_sso_oidc.errors.invalid_grant_exception
import aws_sdk_sso_oidc.errors.invalid_request_exception
import aws_sdk_sso_oidc.errors.invalid_scope_exception
import aws_sdk_sso_oidc.errors.slow_down_exception
import aws_sdk_sso_oidc.errors.unauthorized_client_exception
import aws_sdk_sso_oidc.errors.unsupported_grant_type_exception
import aws_sdk_sso_oidc.types.create_token_request
import aws_sdk_sso_oidc.types.create_token_response
import aws_sdk_sso_oidc.types.scopes
from aws_sdk_sso_oidc._protocol.errors import parse_error_metadata_json
from aws_sdk_sso_oidc._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_sso_oidc._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_sso_oidc.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_sso_oidc.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "AuthorizationPendingException":
            raise aws_sdk_sso_oidc.errors.authorization_pending_exception.AuthorizationPendingException.from_json(
                data
            )
        case "ExpiredTokenException":
            raise aws_sdk_sso_oidc.errors.expired_token_exception.ExpiredTokenException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_sso_oidc.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "InvalidClientException":
            raise aws_sdk_sso_oidc.errors.invalid_client_exception.InvalidClientException.from_json(
                data
            )
        case "InvalidGrantException":
            raise aws_sdk_sso_oidc.errors.invalid_grant_exception.InvalidGrantException.from_json(
                data
            )
        case "InvalidRequestException":
            raise aws_sdk_sso_oidc.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "InvalidScopeException":
            raise aws_sdk_sso_oidc.errors.invalid_scope_exception.InvalidScopeException.from_json(
                data
            )
        case "SlowDownException":
            raise aws_sdk_sso_oidc.errors.slow_down_exception.SlowDownException.from_json(
                data
            )
        case "UnauthorizedClientException":
            raise aws_sdk_sso_oidc.errors.unauthorized_client_exception.UnauthorizedClientException.from_json(
                data
            )
        case "UnsupportedGrantTypeException":
            raise aws_sdk_sso_oidc.errors.unsupported_grant_type_exception.UnsupportedGrantTypeException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_sso_oidc.types.create_token_response.CreateTokenResponse:
    out: aws_sdk_sso_oidc.types.create_token_response.CreateTokenResponse = (
        aws_sdk_sso_oidc.types.create_token_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_sso_oidc.types.create_token_response.CreateTokenResponse:
    out: aws_sdk_sso_oidc.types.create_token_response.CreateTokenResponse = (
        aws_sdk_sso_oidc.types.create_token_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sso_oidc._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_sso_oidc.types.create_token_request.CreateTokenRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/token"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        aws_sdk_sso_oidc.types.create_token_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_token(
    options: OperationOptions,
    input_: aws_sdk_sso_oidc.types.create_token_request.CreateTokenRequest,
) -> tuple[
    aws_sdk_sso_oidc.types.create_token_response.CreateTokenResponse, zapros.Response
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


async def async_create_token(
    options: AsyncOperationOptions,
    input_: aws_sdk_sso_oidc.types.create_token_request.CreateTokenRequest,
) -> tuple[
    aws_sdk_sso_oidc.types.create_token_response.CreateTokenResponse, zapros.Response
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
