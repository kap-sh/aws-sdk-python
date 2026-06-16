"""Generated from Smithy shape ``com.amazonaws.sso#GetRoleCredentials``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_sso._auth._signers
import aws_sdk_sso._auth._sigv4
from aws_sdk_sso._protocol.errors import parse_error_metadata_json
from aws_sdk_sso._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_sso._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_sso.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_sso.types.get_role_credentials_request
    import aws_sdk_sso.types.get_role_credentials_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidRequestException":
            import aws_sdk_sso.errors.invalid_request_exception

            raise aws_sdk_sso.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_sso.errors.resource_not_found_exception

            raise aws_sdk_sso.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_sso.errors.too_many_requests_exception

            raise aws_sdk_sso.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case "UnauthorizedException":
            import aws_sdk_sso.errors.unauthorized_exception

            raise aws_sdk_sso.errors.unauthorized_exception.UnauthorizedException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_sso.types.get_role_credentials_response.GetRoleCredentialsResponse:
    import aws_sdk_sso.types.get_role_credentials_response

    out: aws_sdk_sso.types.get_role_credentials_response.GetRoleCredentialsResponse = (
        aws_sdk_sso.types.get_role_credentials_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sso._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_sso._auth._sigv4.build_sigv4_auth_scheme(
                "awsssoportal", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_sso._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    return None


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_sso.types.get_role_credentials_request.GetRoleCredentialsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/federation/credentials"
    params: dict[str, str] = {}
    if "role_name" in input_:
        params["role_name"] = str(input_["role_name"])
    if "account_id" in input_:
        params["account_id"] = str(input_["account_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "access_token" in input_:
        headers["x-amz-sso_bearer_token"] = str(input_["access_token"])
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_role_credentials(
    options: OperationOptions,
    input_: aws_sdk_sso.types.get_role_credentials_request.GetRoleCredentialsRequest,
) -> tuple[
    aws_sdk_sso.types.get_role_credentials_response.GetRoleCredentialsResponse,
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


async def async_get_role_credentials(
    options: AsyncOperationOptions,
    input_: aws_sdk_sso.types.get_role_credentials_request.GetRoleCredentialsRequest,
) -> tuple[
    aws_sdk_sso.types.get_role_credentials_response.GetRoleCredentialsResponse,
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
