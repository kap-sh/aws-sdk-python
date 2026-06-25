"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateUserPool``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_cognito_identity_provider._auth._signers
import aws_sdk_cognito_identity_provider._auth._sigv4
import aws_sdk_cognito_identity_provider.errors.concurrent_modification_exception
import aws_sdk_cognito_identity_provider.errors.feature_unavailable_in_tier_exception
import aws_sdk_cognito_identity_provider.errors.internal_error_exception
import aws_sdk_cognito_identity_provider.errors.invalid_email_role_access_policy_exception
import aws_sdk_cognito_identity_provider.errors.invalid_parameter_exception
import aws_sdk_cognito_identity_provider.errors.invalid_sms_role_access_policy_exception
import aws_sdk_cognito_identity_provider.errors.invalid_sms_role_trust_relationship_exception
import aws_sdk_cognito_identity_provider.errors.not_authorized_exception
import aws_sdk_cognito_identity_provider.errors.operation_not_enabled_exception
import aws_sdk_cognito_identity_provider.errors.resource_not_found_exception
import aws_sdk_cognito_identity_provider.errors.tier_change_not_allowed_exception
import aws_sdk_cognito_identity_provider.errors.too_many_requests_exception
import aws_sdk_cognito_identity_provider.errors.user_import_in_progress_exception
import aws_sdk_cognito_identity_provider.errors.user_pool_tagging_exception
import aws_sdk_cognito_identity_provider.types.account_recovery_setting_type
import aws_sdk_cognito_identity_provider.types.admin_create_user_config_type
import aws_sdk_cognito_identity_provider.types.deletion_protection_type
import aws_sdk_cognito_identity_provider.types.device_configuration_type
import aws_sdk_cognito_identity_provider.types.email_configuration_type
import aws_sdk_cognito_identity_provider.types.issuer_configuration_type
import aws_sdk_cognito_identity_provider.types.key_configuration_type
import aws_sdk_cognito_identity_provider.types.lambda_config_type
import aws_sdk_cognito_identity_provider.types.sms_configuration_type
import aws_sdk_cognito_identity_provider.types.update_user_pool_request
import aws_sdk_cognito_identity_provider.types.update_user_pool_response
import aws_sdk_cognito_identity_provider.types.user_attribute_update_settings_type
import aws_sdk_cognito_identity_provider.types.user_pool_add_ons_type
import aws_sdk_cognito_identity_provider.types.user_pool_mfa_type
import aws_sdk_cognito_identity_provider.types.user_pool_policy_type
import aws_sdk_cognito_identity_provider.types.user_pool_tags_type
import aws_sdk_cognito_identity_provider.types.user_pool_tier_type
import aws_sdk_cognito_identity_provider.types.verification_message_template_type
import aws_sdk_cognito_identity_provider.types.verified_attributes_list_type
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
        case "ConcurrentModificationException":
            raise aws_sdk_cognito_identity_provider.errors.concurrent_modification_exception.ConcurrentModificationException.from_aws_json_1_1(
                data
            )
        case "FeatureUnavailableInTierException":
            raise aws_sdk_cognito_identity_provider.errors.feature_unavailable_in_tier_exception.FeatureUnavailableInTierException.from_aws_json_1_1(
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
        case "InvalidParameterException":
            raise aws_sdk_cognito_identity_provider.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
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
        case "NotAuthorizedException":
            raise aws_sdk_cognito_identity_provider.errors.not_authorized_exception.NotAuthorizedException.from_aws_json_1_1(
                data
            )
        case "OperationNotEnabledException":
            raise aws_sdk_cognito_identity_provider.errors.operation_not_enabled_exception.OperationNotEnabledException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_cognito_identity_provider.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case "TierChangeNotAllowedException":
            raise aws_sdk_cognito_identity_provider.errors.tier_change_not_allowed_exception.TierChangeNotAllowedException.from_aws_json_1_1(
                data
            )
        case "TooManyRequestsException":
            raise aws_sdk_cognito_identity_provider.errors.too_many_requests_exception.TooManyRequestsException.from_aws_json_1_1(
                data
            )
        case "UserImportInProgressException":
            raise aws_sdk_cognito_identity_provider.errors.user_import_in_progress_exception.UserImportInProgressException.from_aws_json_1_1(
                data
            )
        case "UserPoolTaggingException":
            raise aws_sdk_cognito_identity_provider.errors.user_pool_tagging_exception.UserPoolTaggingException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_cognito_identity_provider.types.update_user_pool_response.UpdateUserPoolResponse:
    out: aws_sdk_cognito_identity_provider.types.update_user_pool_response.UpdateUserPoolResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_cognito_identity_provider.types.update_user_pool_response.UpdateUserPoolResponse:
    out: aws_sdk_cognito_identity_provider.types.update_user_pool_response.UpdateUserPoolResponse = {}  # type: ignore[typeddict-item]
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
    input_: aws_sdk_cognito_identity_provider.types.update_user_pool_request.UpdateUserPoolRequest,
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
    headers["X-Amz-Target"] = "AWSCognitoIdentityProviderService.UpdateUserPool"
    body: bytes | None = json.dumps(
        aws_sdk_cognito_identity_provider.types.update_user_pool_request.serialize_aws_json_1_1(
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


def update_user_pool(
    options: OperationOptions,
    input_: aws_sdk_cognito_identity_provider.types.update_user_pool_request.UpdateUserPoolRequest,
) -> tuple[
    aws_sdk_cognito_identity_provider.types.update_user_pool_response.UpdateUserPoolResponse,
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


async def async_update_user_pool(
    options: AsyncOperationOptions,
    input_: aws_sdk_cognito_identity_provider.types.update_user_pool_request.UpdateUserPoolRequest,
) -> tuple[
    aws_sdk_cognito_identity_provider.types.update_user_pool_response.UpdateUserPoolResponse,
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
