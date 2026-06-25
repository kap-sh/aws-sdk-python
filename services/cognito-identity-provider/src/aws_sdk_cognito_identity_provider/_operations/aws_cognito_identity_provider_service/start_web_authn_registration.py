"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#StartWebAuthnRegistration``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_cognito_identity_provider._auth._signers
import aws_sdk_cognito_identity_provider._auth._sigv4
import aws_sdk_cognito_identity_provider.errors.forbidden_exception
import aws_sdk_cognito_identity_provider.errors.internal_error_exception
import aws_sdk_cognito_identity_provider.errors.invalid_parameter_exception
import aws_sdk_cognito_identity_provider.errors.limit_exceeded_exception
import aws_sdk_cognito_identity_provider.errors.not_authorized_exception
import aws_sdk_cognito_identity_provider.errors.operation_not_enabled_exception
import aws_sdk_cognito_identity_provider.errors.password_reset_required_exception
import aws_sdk_cognito_identity_provider.errors.too_many_requests_exception
import aws_sdk_cognito_identity_provider.errors.web_authn_configuration_missing_exception
import aws_sdk_cognito_identity_provider.errors.web_authn_not_enabled_exception
import aws_sdk_cognito_identity_provider.types.start_web_authn_registration_request
import aws_sdk_cognito_identity_provider.types.start_web_authn_registration_response
from aws_sdk_cognito_identity_provider._protocol.errors import parse_error_metadata_json
from aws_sdk_cognito_identity_provider._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_cognito_identity_provider._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cognito_identity_provider.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ForbiddenException":
            raise aws_sdk_cognito_identity_provider.errors.forbidden_exception.ForbiddenException.from_aws_json_1_1(
                data
            )
        case "InternalErrorException":
            raise aws_sdk_cognito_identity_provider.errors.internal_error_exception.InternalErrorException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            raise aws_sdk_cognito_identity_provider.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "LimitExceededException":
            raise aws_sdk_cognito_identity_provider.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case "NotAuthorizedException":
            raise aws_sdk_cognito_identity_provider.errors.not_authorized_exception.NotAuthorizedException.from_aws_json_1_1(
                data
            )
        case "OperationNotEnabledException":
            raise aws_sdk_cognito_identity_provider.errors.operation_not_enabled_exception.OperationNotEnabledException.from_aws_json_1_1(
                data
            )
        case "PasswordResetRequiredException":
            raise aws_sdk_cognito_identity_provider.errors.password_reset_required_exception.PasswordResetRequiredException.from_aws_json_1_1(
                data
            )
        case "TooManyRequestsException":
            raise aws_sdk_cognito_identity_provider.errors.too_many_requests_exception.TooManyRequestsException.from_aws_json_1_1(
                data
            )
        case "WebAuthnConfigurationMissingException":
            raise aws_sdk_cognito_identity_provider.errors.web_authn_configuration_missing_exception.WebAuthnConfigurationMissingException.from_aws_json_1_1(
                data
            )
        case "WebAuthnNotEnabledException":
            raise aws_sdk_cognito_identity_provider.errors.web_authn_not_enabled_exception.WebAuthnNotEnabledException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_cognito_identity_provider.types.start_web_authn_registration_response.StartWebAuthnRegistrationResponse:
    out: aws_sdk_cognito_identity_provider.types.start_web_authn_registration_response.StartWebAuthnRegistrationResponse = aws_sdk_cognito_identity_provider.types.start_web_authn_registration_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_cognito_identity_provider.types.start_web_authn_registration_response.StartWebAuthnRegistrationResponse:
    out: aws_sdk_cognito_identity_provider.types.start_web_authn_registration_response.StartWebAuthnRegistrationResponse = aws_sdk_cognito_identity_provider.types.start_web_authn_registration_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cognito_identity_provider._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cognito_identity_provider._auth._sigv4.build_sigv4_auth_scheme(
                "cognito-idp", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cognito_identity_provider._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    return None


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_cognito_identity_provider.types.start_web_authn_registration_request.StartWebAuthnRegistrationRequest,
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
    headers["X-Amz-Target"] = (
        "AWSCognitoIdentityProviderService.StartWebAuthnRegistration"
    )
    body: bytes | None = json.dumps(
        aws_sdk_cognito_identity_provider.types.start_web_authn_registration_request.serialize_aws_json_1_1(
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


def start_web_authn_registration(
    options: OperationOptions,
    input_: aws_sdk_cognito_identity_provider.types.start_web_authn_registration_request.StartWebAuthnRegistrationRequest,
) -> tuple[
    aws_sdk_cognito_identity_provider.types.start_web_authn_registration_response.StartWebAuthnRegistrationResponse,
    zapros.Response,
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


async def async_start_web_authn_registration(
    options: AsyncOperationOptions,
    input_: aws_sdk_cognito_identity_provider.types.start_web_authn_registration_request.StartWebAuthnRegistrationRequest,
) -> tuple[
    aws_sdk_cognito_identity_provider.types.start_web_authn_registration_response.StartWebAuthnRegistrationResponse,
    zapros.Response,
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
