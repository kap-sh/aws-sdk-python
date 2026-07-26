"""Generated from Smithy shape ``com.amazonaws.appstream#CreateUsageReportSubscription``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_appstream._auth._signers
import capo_appstream._auth._sigv4
import capo_appstream.errors.invalid_account_status_exception
import capo_appstream.errors.invalid_role_exception
import capo_appstream.errors.limit_exceeded_exception
import capo_appstream.types.create_usage_report_subscription_request
import capo_appstream.types.create_usage_report_subscription_result
import capo_appstream.types.usage_report_schedule
from capo_appstream._protocol.errors import parse_error_metadata_json
from capo_appstream._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_appstream._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_appstream.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidAccountStatusException":
            raise capo_appstream.errors.invalid_account_status_exception.InvalidAccountStatusException.from_aws_json_1_1(
                data
            )
        case "InvalidRoleException":
            raise capo_appstream.errors.invalid_role_exception.InvalidRoleException.from_aws_json_1_1(
                data
            )
        case "LimitExceededException":
            raise capo_appstream.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_appstream.types.create_usage_report_subscription_result.CreateUsageReportSubscriptionResult:
    out: capo_appstream.types.create_usage_report_subscription_result.CreateUsageReportSubscriptionResult = capo_appstream.types.create_usage_report_subscription_result.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_appstream.types.create_usage_report_subscription_result.CreateUsageReportSubscriptionResult:
    out: capo_appstream.types.create_usage_report_subscription_result.CreateUsageReportSubscriptionResult = capo_appstream.types.create_usage_report_subscription_result.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_appstream._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_appstream._auth._sigv4.build_sigv4_auth_scheme(
                "appstream", options.region
            )
        )
        if sigv4_config is not None:
            return capo_appstream._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_appstream.types.create_usage_report_subscription_request.CreateUsageReportSubscriptionRequest,
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
    headers["X-Amz-Target"] = "PhotonAdminProxyService.CreateUsageReportSubscription"
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_usage_report_subscription(
    options: OperationOptions,
    input_: capo_appstream.types.create_usage_report_subscription_request.CreateUsageReportSubscriptionRequest,
) -> tuple[
    capo_appstream.types.create_usage_report_subscription_result.CreateUsageReportSubscriptionResult,
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


async def async_create_usage_report_subscription(
    options: AsyncOperationOptions,
    input_: capo_appstream.types.create_usage_report_subscription_request.CreateUsageReportSubscriptionRequest,
) -> tuple[
    capo_appstream.types.create_usage_report_subscription_result.CreateUsageReportSubscriptionResult,
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
