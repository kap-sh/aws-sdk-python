"""Generated from Smithy shape ``com.amazonaws.datazone#ListSubscriptions``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_datazone._auth._signers
import aws_sdk_datazone._auth._sigv4
import aws_sdk_datazone.errors.access_denied_exception
import aws_sdk_datazone.errors.internal_server_exception
import aws_sdk_datazone.errors.resource_not_found_exception
import aws_sdk_datazone.errors.throttling_exception
import aws_sdk_datazone.errors.unauthorized_exception
import aws_sdk_datazone.errors.validation_exception
import aws_sdk_datazone.types.list_subscriptions_input
import aws_sdk_datazone.types.list_subscriptions_output
import aws_sdk_datazone.types.sort_key
import aws_sdk_datazone.types.sort_order
import aws_sdk_datazone.types.subscription_status
import aws_sdk_datazone.types.subscriptions
from aws_sdk_datazone._protocol.errors import parse_error_metadata_json
from aws_sdk_datazone._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_datazone._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_datazone.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_datazone.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "UnauthorizedException":
            raise aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_datazone.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_datazone.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_datazone.types.list_subscriptions_output.ListSubscriptionsOutput:
    out: aws_sdk_datazone.types.list_subscriptions_output.ListSubscriptionsOutput = (
        aws_sdk_datazone.types.list_subscriptions_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_datazone.types.list_subscriptions_output.ListSubscriptionsOutput:
    out: aws_sdk_datazone.types.list_subscriptions_output.ListSubscriptionsOutput = (
        aws_sdk_datazone.types.list_subscriptions_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_datazone._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_datazone._auth._sigv4.build_sigv4_auth_scheme(
                "datazone", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_datazone._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_datazone.types.list_subscriptions_input.ListSubscriptionsInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region, UseFIPS=options.use_fips, Endpoint=options.endpoint
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v2/domains/{domainIdentifier}/subscriptions"
    url = url.replace(
        "{domainIdentifier}", quote(str(input_["domain_identifier"]), safe="")
    )
    params: dict[str, str] = {}
    if "subscription_request_identifier" in input_:
        params["subscriptionRequestIdentifier"] = str(
            input_["subscription_request_identifier"]
        )
    if "status" in input_:
        params["status"] = str(input_["status"])
    if "subscribed_listing_id" in input_:
        params["subscribedListingId"] = str(input_["subscribed_listing_id"])
    if "owning_project_id" in input_:
        params["owningProjectId"] = str(input_["owning_project_id"])
    if "owning_iam_principal_arn" in input_:
        params["owningIamPrincipalArn"] = str(input_["owning_iam_principal_arn"])
    if "owning_user_id" in input_:
        params["owningUserId"] = str(input_["owning_user_id"])
    if "owning_group_id" in input_:
        params["owningGroupId"] = str(input_["owning_group_id"])
    if "approver_project_id" in input_:
        params["approverProjectId"] = str(input_["approver_project_id"])
    if "sort_by" in input_:
        params["sortBy"] = str(input_["sort_by"])
    if "sort_order" in input_:
        params["sortOrder"] = str(input_["sort_order"])
    if "max_results" in input_:
        params["maxResults"] = str(input_["max_results"])
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_subscriptions(
    options: OperationOptions,
    input_: aws_sdk_datazone.types.list_subscriptions_input.ListSubscriptionsInput,
) -> tuple[
    aws_sdk_datazone.types.list_subscriptions_output.ListSubscriptionsOutput,
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


async def async_list_subscriptions(
    options: AsyncOperationOptions,
    input_: aws_sdk_datazone.types.list_subscriptions_input.ListSubscriptionsInput,
) -> tuple[
    aws_sdk_datazone.types.list_subscriptions_output.ListSubscriptionsOutput,
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
