"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyEventSubscription``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_database_migration_service._auth._signers
import aws_sdk_database_migration_service._auth._sigv4
from aws_sdk_database_migration_service._protocol.errors import (
    parse_error_metadata_json,
)
from aws_sdk_database_migration_service._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_database_migration_service._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_database_migration_service.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.modify_event_subscription_message
    import aws_sdk_database_migration_service.types.modify_event_subscription_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedFault":
            import aws_sdk_database_migration_service.errors.access_denied_fault

            raise aws_sdk_database_migration_service.errors.access_denied_fault.AccessDeniedFault.from_aws_json_1_1(
                data
            )
        case "KMSAccessDeniedFault":
            import aws_sdk_database_migration_service.errors.kms_access_denied_fault

            raise aws_sdk_database_migration_service.errors.kms_access_denied_fault.KMSAccessDeniedFault.from_aws_json_1_1(
                data
            )
        case "KMSDisabledFault":
            import aws_sdk_database_migration_service.errors.kms_disabled_fault

            raise aws_sdk_database_migration_service.errors.kms_disabled_fault.KMSDisabledFault.from_aws_json_1_1(
                data
            )
        case "KMSInvalidStateFault":
            import aws_sdk_database_migration_service.errors.kms_invalid_state_fault

            raise aws_sdk_database_migration_service.errors.kms_invalid_state_fault.KMSInvalidStateFault.from_aws_json_1_1(
                data
            )
        case "KMSNotFoundFault":
            import aws_sdk_database_migration_service.errors.kms_not_found_fault

            raise aws_sdk_database_migration_service.errors.kms_not_found_fault.KMSNotFoundFault.from_aws_json_1_1(
                data
            )
        case "KMSThrottlingFault":
            import aws_sdk_database_migration_service.errors.kms_throttling_fault

            raise aws_sdk_database_migration_service.errors.kms_throttling_fault.KMSThrottlingFault.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundFault":
            import aws_sdk_database_migration_service.errors.resource_not_found_fault

            raise aws_sdk_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault.from_aws_json_1_1(
                data
            )
        case "ResourceQuotaExceededFault":
            import aws_sdk_database_migration_service.errors.resource_quota_exceeded_fault

            raise aws_sdk_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault.from_aws_json_1_1(
                data
            )
        case "SNSInvalidTopicFault":
            import aws_sdk_database_migration_service.errors.sns_invalid_topic_fault

            raise aws_sdk_database_migration_service.errors.sns_invalid_topic_fault.SNSInvalidTopicFault.from_aws_json_1_1(
                data
            )
        case "SNSNoAuthorizationFault":
            import aws_sdk_database_migration_service.errors.sns_no_authorization_fault

            raise aws_sdk_database_migration_service.errors.sns_no_authorization_fault.SNSNoAuthorizationFault.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_database_migration_service.types.modify_event_subscription_response.ModifyEventSubscriptionResponse:
    import aws_sdk_database_migration_service.types.modify_event_subscription_response

    out: aws_sdk_database_migration_service.types.modify_event_subscription_response.ModifyEventSubscriptionResponse = aws_sdk_database_migration_service.types.modify_event_subscription_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_database_migration_service._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_database_migration_service._auth._sigv4.build_sigv4_auth_scheme(
                "dms", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_database_migration_service._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_database_migration_service.types.modify_event_subscription_message.ModifyEventSubscriptionMessage,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AmazonDMSv20160101.ModifyEventSubscription"
    import aws_sdk_database_migration_service.types.modify_event_subscription_message

    body: bytes | None = json.dumps(
        aws_sdk_database_migration_service.types.modify_event_subscription_message.serialize_aws_json_1_1(
            input
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def modify_event_subscription(
    options: OperationOptions,
    input: aws_sdk_database_migration_service.types.modify_event_subscription_message.ModifyEventSubscriptionMessage,
) -> tuple[
    aws_sdk_database_migration_service.types.modify_event_subscription_response.ModifyEventSubscriptionResponse,
    zapros.Response,
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


async def async_modify_event_subscription(
    options: AsyncOperationOptions,
    input: aws_sdk_database_migration_service.types.modify_event_subscription_message.ModifyEventSubscriptionMessage,
) -> tuple[
    aws_sdk_database_migration_service.types.modify_event_subscription_response.ModifyEventSubscriptionResponse,
    zapros.Response,
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
