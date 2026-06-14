"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminRespondToAuthChallenge``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_cognito_identity_provider._auth._signers
import aws_sdk_cognito_identity_provider._auth._sigv4
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

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.admin_respond_to_auth_challenge_request
    import aws_sdk_cognito_identity_provider.types.admin_respond_to_auth_challenge_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AliasExistsException":
            import aws_sdk_cognito_identity_provider.errors.alias_exists_exception

            raise aws_sdk_cognito_identity_provider.errors.alias_exists_exception.AliasExistsException.from_aws_json_1_1(
                data
            )
        case "CodeMismatchException":
            import aws_sdk_cognito_identity_provider.errors.code_mismatch_exception

            raise aws_sdk_cognito_identity_provider.errors.code_mismatch_exception.CodeMismatchException.from_aws_json_1_1(
                data
            )
        case "ExpiredCodeException":
            import aws_sdk_cognito_identity_provider.errors.expired_code_exception

            raise aws_sdk_cognito_identity_provider.errors.expired_code_exception.ExpiredCodeException.from_aws_json_1_1(
                data
            )
        case "InternalErrorException":
            import aws_sdk_cognito_identity_provider.errors.internal_error_exception

            raise aws_sdk_cognito_identity_provider.errors.internal_error_exception.InternalErrorException.from_aws_json_1_1(
                data
            )
        case "InvalidEmailRoleAccessPolicyException":
            import aws_sdk_cognito_identity_provider.errors.invalid_email_role_access_policy_exception

            raise aws_sdk_cognito_identity_provider.errors.invalid_email_role_access_policy_exception.InvalidEmailRoleAccessPolicyException.from_aws_json_1_1(
                data
            )
        case "InvalidLambdaResponseException":
            import aws_sdk_cognito_identity_provider.errors.invalid_lambda_response_exception

            raise aws_sdk_cognito_identity_provider.errors.invalid_lambda_response_exception.InvalidLambdaResponseException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            import aws_sdk_cognito_identity_provider.errors.invalid_parameter_exception

            raise aws_sdk_cognito_identity_provider.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "InvalidPasswordException":
            import aws_sdk_cognito_identity_provider.errors.invalid_password_exception

            raise aws_sdk_cognito_identity_provider.errors.invalid_password_exception.InvalidPasswordException.from_aws_json_1_1(
                data
            )
        case "InvalidSmsRoleAccessPolicyException":
            import aws_sdk_cognito_identity_provider.errors.invalid_sms_role_access_policy_exception

            raise aws_sdk_cognito_identity_provider.errors.invalid_sms_role_access_policy_exception.InvalidSmsRoleAccessPolicyException.from_aws_json_1_1(
                data
            )
        case "InvalidSmsRoleTrustRelationshipException":
            import aws_sdk_cognito_identity_provider.errors.invalid_sms_role_trust_relationship_exception

            raise aws_sdk_cognito_identity_provider.errors.invalid_sms_role_trust_relationship_exception.InvalidSmsRoleTrustRelationshipException.from_aws_json_1_1(
                data
            )
        case "InvalidUserPoolConfigurationException":
            import aws_sdk_cognito_identity_provider.errors.invalid_user_pool_configuration_exception

            raise aws_sdk_cognito_identity_provider.errors.invalid_user_pool_configuration_exception.InvalidUserPoolConfigurationException.from_aws_json_1_1(
                data
            )
        case "MFAMethodNotFoundException":
            import aws_sdk_cognito_identity_provider.errors.mfa_method_not_found_exception

            raise aws_sdk_cognito_identity_provider.errors.mfa_method_not_found_exception.MFAMethodNotFoundException.from_aws_json_1_1(
                data
            )
        case "NotAuthorizedException":
            import aws_sdk_cognito_identity_provider.errors.not_authorized_exception

            raise aws_sdk_cognito_identity_provider.errors.not_authorized_exception.NotAuthorizedException.from_aws_json_1_1(
                data
            )
        case "OperationNotEnabledException":
            import aws_sdk_cognito_identity_provider.errors.operation_not_enabled_exception

            raise aws_sdk_cognito_identity_provider.errors.operation_not_enabled_exception.OperationNotEnabledException.from_aws_json_1_1(
                data
            )
        case "PasswordHistoryPolicyViolationException":
            import aws_sdk_cognito_identity_provider.errors.password_history_policy_violation_exception

            raise aws_sdk_cognito_identity_provider.errors.password_history_policy_violation_exception.PasswordHistoryPolicyViolationException.from_aws_json_1_1(
                data
            )
        case "PasswordResetRequiredException":
            import aws_sdk_cognito_identity_provider.errors.password_reset_required_exception

            raise aws_sdk_cognito_identity_provider.errors.password_reset_required_exception.PasswordResetRequiredException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_cognito_identity_provider.errors.resource_not_found_exception

            raise aws_sdk_cognito_identity_provider.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case "SoftwareTokenMFANotFoundException":
            import aws_sdk_cognito_identity_provider.errors.software_token_mfa_not_found_exception

            raise aws_sdk_cognito_identity_provider.errors.software_token_mfa_not_found_exception.SoftwareTokenMFANotFoundException.from_aws_json_1_1(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_cognito_identity_provider.errors.too_many_requests_exception

            raise aws_sdk_cognito_identity_provider.errors.too_many_requests_exception.TooManyRequestsException.from_aws_json_1_1(
                data
            )
        case "UnexpectedLambdaException":
            import aws_sdk_cognito_identity_provider.errors.unexpected_lambda_exception

            raise aws_sdk_cognito_identity_provider.errors.unexpected_lambda_exception.UnexpectedLambdaException.from_aws_json_1_1(
                data
            )
        case "UserLambdaValidationException":
            import aws_sdk_cognito_identity_provider.errors.user_lambda_validation_exception

            raise aws_sdk_cognito_identity_provider.errors.user_lambda_validation_exception.UserLambdaValidationException.from_aws_json_1_1(
                data
            )
        case "UserNotConfirmedException":
            import aws_sdk_cognito_identity_provider.errors.user_not_confirmed_exception

            raise aws_sdk_cognito_identity_provider.errors.user_not_confirmed_exception.UserNotConfirmedException.from_aws_json_1_1(
                data
            )
        case "UserNotFoundException":
            import aws_sdk_cognito_identity_provider.errors.user_not_found_exception

            raise aws_sdk_cognito_identity_provider.errors.user_not_found_exception.UserNotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cognito_identity_provider.types.admin_respond_to_auth_challenge_response.AdminRespondToAuthChallengeResponse:
    import aws_sdk_cognito_identity_provider.types.admin_respond_to_auth_challenge_response

    out: aws_sdk_cognito_identity_provider.types.admin_respond_to_auth_challenge_response.AdminRespondToAuthChallengeResponse = aws_sdk_cognito_identity_provider.types.admin_respond_to_auth_challenge_response.deserialize_aws_json_1_1(
        json.loads(response.read())
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
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_cognito_identity_provider.types.admin_respond_to_auth_challenge_request.AdminRespondToAuthChallengeRequest,
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
        "AWSCognitoIdentityProviderService.AdminRespondToAuthChallenge"
    )
    import aws_sdk_cognito_identity_provider.types.admin_respond_to_auth_challenge_request

    body: bytes | None = json.dumps(
        aws_sdk_cognito_identity_provider.types.admin_respond_to_auth_challenge_request.serialize_aws_json_1_1(
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


def admin_respond_to_auth_challenge(
    options: OperationOptions,
    input_: aws_sdk_cognito_identity_provider.types.admin_respond_to_auth_challenge_request.AdminRespondToAuthChallengeRequest,
) -> tuple[
    aws_sdk_cognito_identity_provider.types.admin_respond_to_auth_challenge_response.AdminRespondToAuthChallengeResponse,
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


async def async_admin_respond_to_auth_challenge(
    options: AsyncOperationOptions,
    input_: aws_sdk_cognito_identity_provider.types.admin_respond_to_auth_challenge_request.AdminRespondToAuthChallengeRequest,
) -> tuple[
    aws_sdk_cognito_identity_provider.types.admin_respond_to_auth_challenge_response.AdminRespondToAuthChallengeResponse,
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
