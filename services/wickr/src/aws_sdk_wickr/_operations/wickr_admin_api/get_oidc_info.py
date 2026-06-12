"""Generated from Smithy shape ``com.amazonaws.wickr#GetOidcInfo``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_wickr._auth._signers
import aws_sdk_wickr._auth._sigv4
from aws_sdk_wickr._protocol.errors import parse_error_metadata_json
from aws_sdk_wickr._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_wickr._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_wickr.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.get_oidc_info_request
    import aws_sdk_wickr.types.get_oidc_info_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestError":
            import aws_sdk_wickr.errors.bad_request_error

            raise aws_sdk_wickr.errors.bad_request_error.BadRequestError.from_json(data)
        case "ForbiddenError":
            import aws_sdk_wickr.errors.forbidden_error

            raise aws_sdk_wickr.errors.forbidden_error.ForbiddenError.from_json(data)
        case "InternalServerError":
            import aws_sdk_wickr.errors.internal_server_error

            raise aws_sdk_wickr.errors.internal_server_error.InternalServerError.from_json(
                data
            )
        case "RateLimitError":
            import aws_sdk_wickr.errors.rate_limit_error

            raise aws_sdk_wickr.errors.rate_limit_error.RateLimitError.from_json(data)
        case "ResourceNotFoundError":
            import aws_sdk_wickr.errors.resource_not_found_error

            raise aws_sdk_wickr.errors.resource_not_found_error.ResourceNotFoundError.from_json(
                data
            )
        case "UnauthorizedError":
            import aws_sdk_wickr.errors.unauthorized_error

            raise aws_sdk_wickr.errors.unauthorized_error.UnauthorizedError.from_json(
                data
            )
        case "ValidationError":
            import aws_sdk_wickr.errors.validation_error

            raise aws_sdk_wickr.errors.validation_error.ValidationError.from_json(data)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_wickr.types.get_oidc_info_response.GetOidcInfoResponse:
    import aws_sdk_wickr.types.get_oidc_info_response

    out: aws_sdk_wickr.types.get_oidc_info_response.GetOidcInfoResponse = (
        aws_sdk_wickr.types.get_oidc_info_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_wickr._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_wickr._auth._sigv4.build_sigv4_auth_scheme(
                "wickr", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_wickr._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_wickr.types.get_oidc_info_request.GetOidcInfoRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/networks/{networkId}/oidc"
    url = url.replace("{networkId}", quote(str(input["network_id"]), safe=""))
    params: dict[str, str] = {}
    if "client_id" in input:
        params["clientId"] = str(input["client_id"])
    if "code" in input:
        params["code"] = str(input["code"])
    if "grant_type" in input:
        params["grantType"] = str(input["grant_type"])
    if "redirect_uri" in input:
        params["redirectUri"] = str(input["redirect_uri"])
    if "url" in input:
        params["url"] = str(input["url"])
    if "client_secret" in input:
        params["clientSecret"] = str(input["client_secret"])
    if "code_verifier" in input:
        params["codeVerifier"] = str(input["code_verifier"])
    if "certificate" in input:
        params["certificate"] = str(input["certificate"])
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


def get_oidc_info(
    options: OperationOptions,
    input: aws_sdk_wickr.types.get_oidc_info_request.GetOidcInfoRequest,
) -> tuple[
    aws_sdk_wickr.types.get_oidc_info_response.GetOidcInfoResponse, zapros.Response
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


async def async_get_oidc_info(
    options: AsyncOperationOptions,
    input: aws_sdk_wickr.types.get_oidc_info_request.GetOidcInfoRequest,
) -> tuple[
    aws_sdk_wickr.types.get_oidc_info_response.GetOidcInfoResponse, zapros.Response
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
