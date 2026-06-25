"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RespondToAuthChallenge``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_cognito_identity_provider._auth._signers
import aws_sdk_cognito_identity_provider._auth._sigv4
import aws_sdk_cognito_identity_provider.errors.alias_exists_exception
import aws_sdk_cognito_identity_provider.errors.code_mismatch_exception
import aws_sdk_cognito_identity_provider.errors.expired_code_exception
import aws_sdk_cognito_identity_provider.errors.forbidden_exception
import aws_sdk_cognito_identity_provider.errors.internal_error_exception
import aws_sdk_cognito_identity_provider.errors.invalid_email_role_access_policy_exception
import aws_sdk_cognito_identity_provider.errors.invalid_lambda_response_exception
import aws_sdk_cognito_identity_provider.errors.invalid_parameter_exception
import aws_sdk_cognito_identity_provider.errors.invalid_password_exception
import aws_sdk_cognito_identity_provider.errors.invalid_sms_role_access_policy_exception
import aws_sdk_cognito_identity_provider.errors.invalid_sms_role_trust_relationship_exception
import aws_sdk_cognito_identity_provider.errors.invalid_user_pool_configuration_exception
import aws_sdk_cognito_identity_provider.errors.mfa_method_not_found_exception
import aws_sdk_cognito_identity_provider.errors.not_authorized_exception
import aws_sdk_cognito_identity_provider.errors.operation_not_enabled_exception
import aws_sdk_cognito_identity_provider.errors.password_history_policy_violation_exception
import aws_sdk_cognito_identity_provider.errors.password_reset_required_exception
import aws_sdk_cognito_identity_provider.errors.resource_not_found_exception
import aws_sdk_cognito_identity_provider.errors.software_token_mfa_not_found_exception
import aws_sdk_cognito_identity_provider.errors.too_many_requests_exception
import aws_sdk_cognito_identity_provider.errors.unexpected_lambda_exception
import aws_sdk_cognito_identity_provider.errors.user_lambda_validation_exception
import aws_sdk_cognito_identity_provider.errors.user_not_confirmed_exception
import aws_sdk_cognito_identity_provider.errors.user_not_found_exception
import aws_sdk_cognito_identity_provider.types.analytics_metadata_type
import aws_sdk_cognito_identity_provider.types.authentication_result_type
import aws_sdk_cognito_identity_provider.types.challenge_name_type
import aws_sdk_cognito_identity_provider.types.challenge_parameters_type
import aws_sdk_cognito_identity_provider.types.challenge_responses_type
import aws_sdk_cognito_identity_provider.types.client_metadata_type
import aws_sdk_cognito_identity_provider.types.respond_to_auth_challenge_request
import aws_sdk_cognito_identity_provider.types.respond_to_auth_challenge_response
import aws_sdk_cognito_identity_provider.types.user_context_data_type
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
        case "AliasExistsException":
            raise aws_sdk_cognito_identity_provider.errors.alias_exists_exception.AliasExistsException.from_aws_json_1_1(
                data
            )
        case "CodeMismatchException":
            raise aws_sdk_cognito_identity_provider.errors.code_mismatch_exception.CodeMismatchException.from_aws_json_1_1(
                data
            )
        case "ExpiredCodeException":
            raise aws_sdk_cognito_identity_provider.errors.expired_code_exception.ExpiredCodeException.from_aws_json_1_1(
                data
            )
        case "ForbiddenException":
            raise aws_sdk_cognito_identity_provider.errors.forbidden_exception.ForbiddenException.from_aws_json_1_1(
                data
            )
        case "InternalErrorException":
            raise aws_sdk_cognito_identity_provider.errors.internal_error_exception.InternalErrorException.from_aws_json_1_1(
                data
            )
        case "InvalidEmailRoleAccessPolicyException":
            raise aws_sdk_cognito_identity_provider.errors.invalid_email_role_access_policy_exception.InvalidEmailRoleAccessPolicyException.from_aws_json_1_1(
                data
            )
        case "InvalidLambdaResponseException":
            raise aws_sdk_cognito_identity_provider.errors.invalid_lambda_response_exception.InvalidLambdaResponseException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            raise aws_sdk_cognito_identity_provider.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "InvalidPasswordException":
            raise aws_sdk_cognito_identity_provider.errors.invalid_password_exception.InvalidPasswordException.from_aws_json_1_1(
                data
            )
        case "InvalidSmsRoleAccessPolicyException":
            raise aws_sdk_cognito_identity_provider.errors.invalid_sms_role_access_policy_exception.InvalidSmsRoleAccessPolicyException.from_aws_json_1_1(
                data
            )
        case "InvalidSmsRoleTrustRelationshipException":
            raise aws_sdk_cognito_identity_provider.errors.invalid_sms_role_trust_relationship_exception.InvalidSmsRoleTrustRelationshipException.from_aws_json_1_1(
                data
            )
        case "InvalidUserPoolConfigurationException":
            raise aws_sdk_cognito_identity_provider.errors.invalid_user_pool_configuration_exception.InvalidUserPoolConfigurationException.from_aws_json_1_1(
                data
            )
        case "MFAMethodNotFoundException":
            raise aws_sdk_cognito_identity_provider.errors.mfa_method_not_found_exception.MFAMethodNotFoundException.from_aws_json_1_1(
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
        case "PasswordHistoryPolicyViolationException":
            raise aws_sdk_cognito_identity_provider.errors.password_history_policy_violation_exception.PasswordHistoryPolicyViolationException.from_aws_json_1_1(
                data
            )
        case "PasswordResetRequiredException":
            raise aws_sdk_cognito_identity_provider.errors.password_reset_required_exception.PasswordResetRequiredException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_cognito_identity_provider.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case "SoftwareTokenMFANotFoundException":
            raise aws_sdk_cognito_identity_provider.errors.software_token_mfa_not_found_exception.SoftwareTokenMFANotFoundException.from_aws_json_1_1(
                data
            )
        case "TooManyRequestsException":
            raise aws_sdk_cognito_identity_provider.errors.too_many_requests_exception.TooManyRequestsException.from_aws_json_1_1(
                data
            )
        case "UnexpectedLambdaException":
            raise aws_sdk_cognito_identity_provider.errors.unexpected_lambda_exception.UnexpectedLambdaException.from_aws_json_1_1(
                data
            )
        case "UserLambdaValidationException":
            raise aws_sdk_cognito_identity_provider.errors.user_lambda_validation_exception.UserLambdaValidationException.from_aws_json_1_1(
                data
            )
        case "UserNotConfirmedException":
            raise aws_sdk_cognito_identity_provider.errors.user_not_confirmed_exception.UserNotConfirmedException.from_aws_json_1_1(
                data
            )
        case "UserNotFoundException":
            raise aws_sdk_cognito_identity_provider.errors.user_not_found_exception.UserNotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_cognito_identity_provider.types.respond_to_auth_challenge_response.RespondToAuthChallengeResponse:
    out: aws_sdk_cognito_identity_provider.types.respond_to_auth_challenge_response.RespondToAuthChallengeResponse = aws_sdk_cognito_identity_provider.types.respond_to_auth_challenge_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_cognito_identity_provider.types.respond_to_auth_challenge_response.RespondToAuthChallengeResponse:
    out: aws_sdk_cognito_identity_provider.types.respond_to_auth_challenge_response.RespondToAuthChallengeResponse = aws_sdk_cognito_identity_provider.types.respond_to_auth_challenge_response.deserialize_aws_json_1_1(
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
    input_: aws_sdk_cognito_identity_provider.types.respond_to_auth_challenge_request.RespondToAuthChallengeRequest,
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
    headers["X-Amz-Target"] = "AWSCognitoIdentityProviderService.RespondToAuthChallenge"
    body: bytes | None = json.dumps(
        aws_sdk_cognito_identity_provider.types.respond_to_auth_challenge_request.serialize_aws_json_1_1(
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


def respond_to_auth_challenge(
    options: OperationOptions,
    input_: aws_sdk_cognito_identity_provider.types.respond_to_auth_challenge_request.RespondToAuthChallengeRequest,
) -> tuple[
    aws_sdk_cognito_identity_provider.types.respond_to_auth_challenge_response.RespondToAuthChallengeResponse,
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


async def async_respond_to_auth_challenge(
    options: AsyncOperationOptions,
    input_: aws_sdk_cognito_identity_provider.types.respond_to_auth_challenge_request.RespondToAuthChallengeRequest,
) -> tuple[
    aws_sdk_cognito_identity_provider.types.respond_to_auth_challenge_response.RespondToAuthChallengeResponse,
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
