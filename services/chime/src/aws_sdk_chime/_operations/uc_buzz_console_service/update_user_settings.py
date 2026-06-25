"""Generated from Smithy shape ``com.amazonaws.chime#UpdateUserSettings``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_chime._auth._signers
import aws_sdk_chime._auth._sigv4
import aws_sdk_chime.errors.bad_request_exception
import aws_sdk_chime.errors.forbidden_exception
import aws_sdk_chime.errors.not_found_exception
import aws_sdk_chime.errors.service_failure_exception
import aws_sdk_chime.errors.service_unavailable_exception
import aws_sdk_chime.errors.throttled_client_exception
import aws_sdk_chime.errors.unauthorized_client_exception
import aws_sdk_chime.types.update_user_settings_request
import aws_sdk_chime.types.user_settings
from aws_sdk_chime._protocol.errors import parse_error_metadata_json
from aws_sdk_chime._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_chime._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_chime.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise aws_sdk_chime.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ForbiddenException":
            raise aws_sdk_chime.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "NotFoundException":
            raise aws_sdk_chime.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "ServiceFailureException":
            raise aws_sdk_chime.errors.service_failure_exception.ServiceFailureException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_chime.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "ThrottledClientException":
            raise aws_sdk_chime.errors.throttled_client_exception.ThrottledClientException.from_json(
                data
            )
        case "UnauthorizedClientException":
            raise aws_sdk_chime.errors.unauthorized_client_exception.UnauthorizedClientException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_chime._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_chime._auth._sigv4.build_sigv4_auth_scheme(
                "chime", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_chime._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_chime.types.update_user_settings_request.UpdateUserSettingsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/accounts/{AccountId}/users/{UserId}/settings"
    url = url.replace("{AccountId}", quote(str(input_["account_id"]), safe=""))
    url = url.replace("{UserId}", quote(str(input_["user_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        aws_sdk_chime.types.update_user_settings_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def update_user_settings(
    options: OperationOptions,
    input_: aws_sdk_chime.types.update_user_settings_request.UpdateUserSettingsRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_update_user_settings(
    options: AsyncOperationOptions,
    input_: aws_sdk_chime.types.update_user_settings_request.UpdateUserSettingsRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
