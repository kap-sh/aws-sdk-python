"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#CreateScheduledReport``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_bcm_dashboards._auth._signers
import capo_bcm_dashboards._auth._sigv4
import capo_bcm_dashboards.errors.access_denied_exception
import capo_bcm_dashboards.errors.conflict_exception
import capo_bcm_dashboards.errors.internal_server_exception
import capo_bcm_dashboards.errors.service_quota_exceeded_exception
import capo_bcm_dashboards.errors.throttling_exception
import capo_bcm_dashboards.errors.validation_exception
import capo_bcm_dashboards.types.create_scheduled_report_request
import capo_bcm_dashboards.types.create_scheduled_report_response
import capo_bcm_dashboards.types.resource_tag_list
import capo_bcm_dashboards.types.scheduled_report_input
from capo_bcm_dashboards._protocol.errors import parse_error_metadata_json
from capo_bcm_dashboards._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_bcm_dashboards._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_bcm_dashboards.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_bcm_dashboards.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_0(
                data
            )
        case "ConflictException":
            raise capo_bcm_dashboards.errors.conflict_exception.ConflictException.from_aws_json_1_0(
                data
            )
        case "InternalServerException":
            raise capo_bcm_dashboards.errors.internal_server_exception.InternalServerException.from_aws_json_1_0(
                data
            )
        case "ServiceQuotaExceededException":
            raise capo_bcm_dashboards.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_aws_json_1_0(
                data
            )
        case "ThrottlingException":
            raise capo_bcm_dashboards.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data
            )
        case "ValidationException":
            raise capo_bcm_dashboards.errors.validation_exception.ValidationException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_bcm_dashboards.types.create_scheduled_report_response.CreateScheduledReportResponse:
    out: capo_bcm_dashboards.types.create_scheduled_report_response.CreateScheduledReportResponse = capo_bcm_dashboards.types.create_scheduled_report_response.deserialize_aws_json_1_0(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_bcm_dashboards.types.create_scheduled_report_response.CreateScheduledReportResponse:
    out: capo_bcm_dashboards.types.create_scheduled_report_response.CreateScheduledReportResponse = capo_bcm_dashboards.types.create_scheduled_report_response.deserialize_aws_json_1_0(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_bcm_dashboards._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_bcm_dashboards._auth._sigv4.build_sigv4_auth_scheme(
                "bcm-dashboards", options.region
            )
        )
        if sigv4_config is not None:
            return capo_bcm_dashboards._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_bcm_dashboards.types.create_scheduled_report_request.CreateScheduledReportRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSBCMDashboardsService.CreateScheduledReport"
    if "client_token" in input_:
        headers["X-Amzn-Client-Token"] = str(input_["client_token"])
    body: bytes | None = json.dumps(
        capo_bcm_dashboards.types.create_scheduled_report_request.serialize_aws_json_1_0(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_scheduled_report(
    options: OperationOptions,
    input_: capo_bcm_dashboards.types.create_scheduled_report_request.CreateScheduledReportRequest,
) -> tuple[
    capo_bcm_dashboards.types.create_scheduled_report_response.CreateScheduledReportResponse,
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


async def async_create_scheduled_report(
    options: AsyncOperationOptions,
    input_: capo_bcm_dashboards.types.create_scheduled_report_request.CreateScheduledReportRequest,
) -> tuple[
    capo_bcm_dashboards.types.create_scheduled_report_response.CreateScheduledReportResponse,
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
