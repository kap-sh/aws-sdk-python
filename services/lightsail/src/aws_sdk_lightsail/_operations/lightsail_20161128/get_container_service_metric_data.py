"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerServiceMetricData``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_lightsail._auth._signers
import aws_sdk_lightsail._auth._sigv4
import aws_sdk_lightsail.errors.access_denied_exception
import aws_sdk_lightsail.errors.invalid_input_exception
import aws_sdk_lightsail.errors.not_found_exception
import aws_sdk_lightsail.errors.region_setup_in_progress_exception
import aws_sdk_lightsail.errors.service_exception
import aws_sdk_lightsail.errors.unauthenticated_exception
import aws_sdk_lightsail.types.container_service_metric_name
import aws_sdk_lightsail.types.get_container_service_metric_data_request
import aws_sdk_lightsail.types.get_container_service_metric_data_result
import aws_sdk_lightsail.types.iso_date
import aws_sdk_lightsail.types.metric_datapoint_list
import aws_sdk_lightsail.types.metric_statistic_list
from aws_sdk_lightsail._protocol.errors import parse_error_metadata_json
from aws_sdk_lightsail._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_lightsail._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_lightsail.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_lightsail.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "InvalidInputException":
            raise aws_sdk_lightsail.errors.invalid_input_exception.InvalidInputException.from_aws_json_1_1(
                data
            )
        case "NotFoundException":
            raise aws_sdk_lightsail.errors.not_found_exception.NotFoundException.from_aws_json_1_1(
                data
            )
        case "RegionSetupInProgressException":
            raise aws_sdk_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException.from_aws_json_1_1(
                data
            )
        case "ServiceException":
            raise aws_sdk_lightsail.errors.service_exception.ServiceException.from_aws_json_1_1(
                data
            )
        case "UnauthenticatedException":
            raise aws_sdk_lightsail.errors.unauthenticated_exception.UnauthenticatedException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_lightsail.types.get_container_service_metric_data_result.GetContainerServiceMetricDataResult:
    out: aws_sdk_lightsail.types.get_container_service_metric_data_result.GetContainerServiceMetricDataResult = aws_sdk_lightsail.types.get_container_service_metric_data_result.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_lightsail.types.get_container_service_metric_data_result.GetContainerServiceMetricDataResult:
    out: aws_sdk_lightsail.types.get_container_service_metric_data_result.GetContainerServiceMetricDataResult = aws_sdk_lightsail.types.get_container_service_metric_data_result.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_lightsail._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_lightsail._auth._sigv4.build_sigv4_auth_scheme(
                "lightsail", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_lightsail._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_lightsail.types.get_container_service_metric_data_request.GetContainerServiceMetricDataRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/ls/api/2016-11-28/container-services/{serviceName}/metrics"
    )
    url = url.replace("{serviceName}", quote(str(input_["service_name"]), safe=""))
    params: dict[str, str] = {}
    if "metric_name" in input_:
        params["metricName"] = str(input_["metric_name"])
    if "start_time" in input_:
        params["startTime"] = str(input_["start_time"])
    if "end_time" in input_:
        params["endTime"] = str(input_["end_time"])
    if "period" in input_:
        params["period"] = str(input_["period"])
    if "statistics" in input_:
        params["statistics"] = str(input_["statistics"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "Lightsail_20161128.GetContainerServiceMetricData"
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_container_service_metric_data(
    options: OperationOptions,
    input_: aws_sdk_lightsail.types.get_container_service_metric_data_request.GetContainerServiceMetricDataRequest,
) -> tuple[
    aws_sdk_lightsail.types.get_container_service_metric_data_result.GetContainerServiceMetricDataResult,
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


async def async_get_container_service_metric_data(
    options: AsyncOperationOptions,
    input_: aws_sdk_lightsail.types.get_container_service_metric_data_request.GetContainerServiceMetricDataRequest,
) -> tuple[
    aws_sdk_lightsail.types.get_container_service_metric_data_result.GetContainerServiceMetricDataResult,
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
