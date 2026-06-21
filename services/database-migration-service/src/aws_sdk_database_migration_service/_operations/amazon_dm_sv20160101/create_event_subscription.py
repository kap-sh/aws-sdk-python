"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateEventSubscription``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_database_migration_service._auth._signers
import aws_sdk_database_migration_service._auth._sigv4
import aws_sdk_database_migration_service.errors.kms_access_denied_fault
import aws_sdk_database_migration_service.errors.kms_disabled_fault
import aws_sdk_database_migration_service.errors.kms_invalid_state_fault
import aws_sdk_database_migration_service.errors.kms_not_found_fault
import aws_sdk_database_migration_service.errors.kms_throttling_fault
import aws_sdk_database_migration_service.errors.resource_already_exists_fault
import aws_sdk_database_migration_service.errors.resource_not_found_fault
import aws_sdk_database_migration_service.errors.resource_quota_exceeded_fault
import aws_sdk_database_migration_service.errors.sns_invalid_topic_fault
import aws_sdk_database_migration_service.errors.sns_no_authorization_fault
import aws_sdk_database_migration_service.types.create_event_subscription_message
import aws_sdk_database_migration_service.types.create_event_subscription_response
import aws_sdk_database_migration_service.types.event_categories_list
import aws_sdk_database_migration_service.types.event_subscription
import aws_sdk_database_migration_service.types.source_ids_list
import aws_sdk_database_migration_service.types.tag_list
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


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "KMSAccessDeniedFault":
            raise aws_sdk_database_migration_service.errors.kms_access_denied_fault.KMSAccessDeniedFault.from_aws_json_1_1(
                data
            )
        case "KMSDisabledFault":
            raise aws_sdk_database_migration_service.errors.kms_disabled_fault.KMSDisabledFault.from_aws_json_1_1(
                data
            )
        case "KMSInvalidStateFault":
            raise aws_sdk_database_migration_service.errors.kms_invalid_state_fault.KMSInvalidStateFault.from_aws_json_1_1(
                data
            )
        case "KMSNotFoundFault":
            raise aws_sdk_database_migration_service.errors.kms_not_found_fault.KMSNotFoundFault.from_aws_json_1_1(
                data
            )
        case "KMSThrottlingFault":
            raise aws_sdk_database_migration_service.errors.kms_throttling_fault.KMSThrottlingFault.from_aws_json_1_1(
                data
            )
        case "ResourceAlreadyExistsFault":
            raise aws_sdk_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundFault":
            raise aws_sdk_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault.from_aws_json_1_1(
                data
            )
        case "ResourceQuotaExceededFault":
            raise aws_sdk_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault.from_aws_json_1_1(
                data
            )
        case "SNSInvalidTopicFault":
            raise aws_sdk_database_migration_service.errors.sns_invalid_topic_fault.SNSInvalidTopicFault.from_aws_json_1_1(
                data
            )
        case "SNSNoAuthorizationFault":
            raise aws_sdk_database_migration_service.errors.sns_no_authorization_fault.SNSNoAuthorizationFault.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_database_migration_service.types.create_event_subscription_response.CreateEventSubscriptionResponse:
    out: aws_sdk_database_migration_service.types.create_event_subscription_response.CreateEventSubscriptionResponse = aws_sdk_database_migration_service.types.create_event_subscription_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_database_migration_service.types.create_event_subscription_response.CreateEventSubscriptionResponse:
    out: aws_sdk_database_migration_service.types.create_event_subscription_response.CreateEventSubscriptionResponse = aws_sdk_database_migration_service.types.create_event_subscription_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_database_migration_service._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_database_migration_service.types.create_event_subscription_message.CreateEventSubscriptionMessage,
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
    headers["X-Amz-Target"] = "AmazonDMSv20160101.CreateEventSubscription"
    import aws_sdk_database_migration_service.types.create_event_subscription_message

    body: bytes | None = json.dumps(
        aws_sdk_database_migration_service.types.create_event_subscription_message.serialize_aws_json_1_1(
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


def create_event_subscription(
    options: OperationOptions,
    input_: aws_sdk_database_migration_service.types.create_event_subscription_message.CreateEventSubscriptionMessage,
) -> tuple[
    aws_sdk_database_migration_service.types.create_event_subscription_response.CreateEventSubscriptionResponse,
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


async def async_create_event_subscription(
    options: AsyncOperationOptions,
    input_: aws_sdk_database_migration_service.types.create_event_subscription_message.CreateEventSubscriptionMessage,
) -> tuple[
    aws_sdk_database_migration_service.types.create_event_subscription_response.CreateEventSubscriptionResponse,
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
