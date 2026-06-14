"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateGrantVersion``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_license_manager._auth._signers
import aws_sdk_license_manager._auth._sigv4
from aws_sdk_license_manager._protocol.errors import parse_error_metadata_json
from aws_sdk_license_manager._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_license_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_license_manager.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.create_grant_version_request
    import aws_sdk_license_manager.types.create_grant_version_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_license_manager.errors.access_denied_exception

            raise aws_sdk_license_manager.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "AuthorizationException":
            import aws_sdk_license_manager.errors.authorization_exception

            raise aws_sdk_license_manager.errors.authorization_exception.AuthorizationException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterValueException":
            import aws_sdk_license_manager.errors.invalid_parameter_value_exception

            raise aws_sdk_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_aws_json_1_1(
                data
            )
        case "RateLimitExceededException":
            import aws_sdk_license_manager.errors.rate_limit_exceeded_exception

            raise aws_sdk_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException.from_aws_json_1_1(
                data
            )
        case "ResourceLimitExceededException":
            import aws_sdk_license_manager.errors.resource_limit_exceeded_exception

            raise aws_sdk_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException.from_aws_json_1_1(
                data
            )
        case "ServerInternalException":
            import aws_sdk_license_manager.errors.server_internal_exception

            raise aws_sdk_license_manager.errors.server_internal_exception.ServerInternalException.from_aws_json_1_1(
                data
            )
        case "ValidationException":
            import aws_sdk_license_manager.errors.validation_exception

            raise aws_sdk_license_manager.errors.validation_exception.ValidationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_license_manager.types.create_grant_version_response.CreateGrantVersionResponse:
    import aws_sdk_license_manager.types.create_grant_version_response

    out: aws_sdk_license_manager.types.create_grant_version_response.CreateGrantVersionResponse = aws_sdk_license_manager.types.create_grant_version_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_license_manager._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_license_manager._auth._sigv4.build_sigv4_auth_scheme(
                "license-manager", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_license_manager._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_license_manager.types.create_grant_version_request.CreateGrantVersionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSLicenseManager.CreateGrantVersion"
    import aws_sdk_license_manager.types.create_grant_version_request

    body: bytes | None = json.dumps(
        aws_sdk_license_manager.types.create_grant_version_request.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_grant_version(
    options: OperationOptions,
    input_: aws_sdk_license_manager.types.create_grant_version_request.CreateGrantVersionRequest,
) -> tuple[
    aws_sdk_license_manager.types.create_grant_version_response.CreateGrantVersionResponse,
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


async def async_create_grant_version(
    options: AsyncOperationOptions,
    input_: aws_sdk_license_manager.types.create_grant_version_request.CreateGrantVersionRequest,
) -> tuple[
    aws_sdk_license_manager.types.create_grant_version_response.CreateGrantVersionResponse,
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
