"""Generated from Smithy shape ``com.amazonaws.sesv2#GetEmailIdentity``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_sesv2._auth._signers
import aws_sdk_sesv2._auth._sigv4
from aws_sdk_sesv2._protocol.errors import parse_error_metadata_json
from aws_sdk_sesv2._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_sesv2._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_sesv2.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.get_email_identity_request
    import aws_sdk_sesv2.types.get_email_identity_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            import aws_sdk_sesv2.errors.bad_request_exception

            raise aws_sdk_sesv2.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "NotFoundException":
            import aws_sdk_sesv2.errors.not_found_exception

            raise aws_sdk_sesv2.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_sesv2.errors.too_many_requests_exception

            raise aws_sdk_sesv2.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_sesv2.types.get_email_identity_response.GetEmailIdentityResponse:
    import aws_sdk_sesv2.types.get_email_identity_response

    out: aws_sdk_sesv2.types.get_email_identity_response.GetEmailIdentityResponse = (
        aws_sdk_sesv2.types.get_email_identity_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sesv2._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_sesv2._auth._sigv4.build_sigv4_auth_scheme("ses", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_sesv2._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_sesv2.types.get_email_identity_request.GetEmailIdentityRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            EndpointId=options.endpoint_id,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v2/email/identities/{EmailIdentity}"
    url = url.replace("{EmailIdentity}", quote(str(input_["email_identity"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_email_identity(
    options: OperationOptions,
    input_: aws_sdk_sesv2.types.get_email_identity_request.GetEmailIdentityRequest,
) -> tuple[
    aws_sdk_sesv2.types.get_email_identity_response.GetEmailIdentityResponse,
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


async def async_get_email_identity(
    options: AsyncOperationOptions,
    input_: aws_sdk_sesv2.types.get_email_identity_request.GetEmailIdentityRequest,
) -> tuple[
    aws_sdk_sesv2.types.get_email_identity_response.GetEmailIdentityResponse,
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
