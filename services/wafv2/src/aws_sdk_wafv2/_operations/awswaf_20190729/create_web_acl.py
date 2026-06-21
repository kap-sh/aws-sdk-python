"""Generated from Smithy shape ``com.amazonaws.wafv2#CreateWebACL``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_wafv2._auth._signers
import aws_sdk_wafv2._auth._sigv4
import aws_sdk_wafv2.errors.waf_configuration_warning_exception
import aws_sdk_wafv2.errors.waf_duplicate_item_exception
import aws_sdk_wafv2.errors.waf_expired_managed_rule_group_version_exception
import aws_sdk_wafv2.errors.waf_internal_error_exception
import aws_sdk_wafv2.errors.waf_invalid_operation_exception
import aws_sdk_wafv2.errors.waf_invalid_parameter_exception
import aws_sdk_wafv2.errors.waf_invalid_resource_exception
import aws_sdk_wafv2.errors.waf_limits_exceeded_exception
import aws_sdk_wafv2.errors.waf_nonexistent_item_exception
import aws_sdk_wafv2.errors.waf_optimistic_lock_exception
import aws_sdk_wafv2.errors.waf_subscription_not_found_exception
import aws_sdk_wafv2.errors.waf_tag_operation_exception
import aws_sdk_wafv2.errors.waf_tag_operation_internal_error_exception
import aws_sdk_wafv2.errors.waf_unavailable_entity_exception
import aws_sdk_wafv2.types.application_config
import aws_sdk_wafv2.types.association_config
import aws_sdk_wafv2.types.captcha_config
import aws_sdk_wafv2.types.challenge_config
import aws_sdk_wafv2.types.create_web_acl_request
import aws_sdk_wafv2.types.create_web_acl_response
import aws_sdk_wafv2.types.custom_response_bodies
import aws_sdk_wafv2.types.data_protection_config
import aws_sdk_wafv2.types.default_action
import aws_sdk_wafv2.types.on_source_d_do_s_protection_config
import aws_sdk_wafv2.types.rules
import aws_sdk_wafv2.types.scope
import aws_sdk_wafv2.types.tag_list
import aws_sdk_wafv2.types.token_domains
import aws_sdk_wafv2.types.visibility_config
import aws_sdk_wafv2.types.web_acl_summary
from aws_sdk_wafv2._protocol.errors import parse_error_metadata_json
from aws_sdk_wafv2._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_wafv2._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_wafv2.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "WAFConfigurationWarningException":
            raise aws_sdk_wafv2.errors.waf_configuration_warning_exception.WAFConfigurationWarningException.from_aws_json_1_1(
                data
            )
        case "WAFDuplicateItemException":
            raise aws_sdk_wafv2.errors.waf_duplicate_item_exception.WAFDuplicateItemException.from_aws_json_1_1(
                data
            )
        case "WAFExpiredManagedRuleGroupVersionException":
            raise aws_sdk_wafv2.errors.waf_expired_managed_rule_group_version_exception.WAFExpiredManagedRuleGroupVersionException.from_aws_json_1_1(
                data
            )
        case "WAFInternalErrorException":
            raise aws_sdk_wafv2.errors.waf_internal_error_exception.WAFInternalErrorException.from_aws_json_1_1(
                data
            )
        case "WAFInvalidOperationException":
            raise aws_sdk_wafv2.errors.waf_invalid_operation_exception.WAFInvalidOperationException.from_aws_json_1_1(
                data
            )
        case "WAFInvalidParameterException":
            raise aws_sdk_wafv2.errors.waf_invalid_parameter_exception.WAFInvalidParameterException.from_aws_json_1_1(
                data
            )
        case "WAFInvalidResourceException":
            raise aws_sdk_wafv2.errors.waf_invalid_resource_exception.WAFInvalidResourceException.from_aws_json_1_1(
                data
            )
        case "WAFLimitsExceededException":
            raise aws_sdk_wafv2.errors.waf_limits_exceeded_exception.WAFLimitsExceededException.from_aws_json_1_1(
                data
            )
        case "WAFNonexistentItemException":
            raise aws_sdk_wafv2.errors.waf_nonexistent_item_exception.WAFNonexistentItemException.from_aws_json_1_1(
                data
            )
        case "WAFOptimisticLockException":
            raise aws_sdk_wafv2.errors.waf_optimistic_lock_exception.WAFOptimisticLockException.from_aws_json_1_1(
                data
            )
        case "WAFSubscriptionNotFoundException":
            raise aws_sdk_wafv2.errors.waf_subscription_not_found_exception.WAFSubscriptionNotFoundException.from_aws_json_1_1(
                data
            )
        case "WAFTagOperationException":
            raise aws_sdk_wafv2.errors.waf_tag_operation_exception.WAFTagOperationException.from_aws_json_1_1(
                data
            )
        case "WAFTagOperationInternalErrorException":
            raise aws_sdk_wafv2.errors.waf_tag_operation_internal_error_exception.WAFTagOperationInternalErrorException.from_aws_json_1_1(
                data
            )
        case "WAFUnavailableEntityException":
            raise aws_sdk_wafv2.errors.waf_unavailable_entity_exception.WAFUnavailableEntityException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_wafv2.types.create_web_acl_response.CreateWebACLResponse:
    out: aws_sdk_wafv2.types.create_web_acl_response.CreateWebACLResponse = (
        aws_sdk_wafv2.types.create_web_acl_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_wafv2.types.create_web_acl_response.CreateWebACLResponse:
    out: aws_sdk_wafv2.types.create_web_acl_response.CreateWebACLResponse = (
        aws_sdk_wafv2.types.create_web_acl_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_wafv2._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_wafv2._auth._sigv4.build_sigv4_auth_scheme(
                "wafv2", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_wafv2._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_wafv2.types.create_web_acl_request.CreateWebACLRequest,
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
    headers["X-Amz-Target"] = "AWSWAF_20190729.CreateWebACL"
    import aws_sdk_wafv2.types.create_web_acl_request

    body: bytes | None = json.dumps(
        aws_sdk_wafv2.types.create_web_acl_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_web_acl(
    options: OperationOptions,
    input_: aws_sdk_wafv2.types.create_web_acl_request.CreateWebACLRequest,
) -> tuple[
    aws_sdk_wafv2.types.create_web_acl_response.CreateWebACLResponse, zapros.Response
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


async def async_create_web_acl(
    options: AsyncOperationOptions,
    input_: aws_sdk_wafv2.types.create_web_acl_request.CreateWebACLRequest,
) -> tuple[
    aws_sdk_wafv2.types.create_web_acl_response.CreateWebACLResponse, zapros.Response
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
