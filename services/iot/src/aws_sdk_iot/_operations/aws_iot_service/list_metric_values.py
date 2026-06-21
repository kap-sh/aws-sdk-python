"""Generated from Smithy shape ``com.amazonaws.iot#ListMetricValues``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_iot._auth._signers
import aws_sdk_iot._auth._sigv4
import aws_sdk_iot.errors.internal_failure_exception
import aws_sdk_iot.errors.invalid_request_exception
import aws_sdk_iot.errors.resource_not_found_exception
import aws_sdk_iot.errors.throttling_exception
import aws_sdk_iot.types.dimension_value_operator
import aws_sdk_iot.types.list_metric_values_request
import aws_sdk_iot.types.list_metric_values_response
import aws_sdk_iot.types.metric_datum_list
import aws_sdk_iot.types.timestamp
from aws_sdk_iot._protocol.errors import parse_error_metadata_json
from aws_sdk_iot._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_iot._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_iot.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalFailureException":
            raise aws_sdk_iot.errors.internal_failure_exception.InternalFailureException.from_json(
                data
            )
        case "InvalidRequestException":
            raise aws_sdk_iot.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_iot.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_iot.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_iot.types.list_metric_values_response.ListMetricValuesResponse:
    out: aws_sdk_iot.types.list_metric_values_response.ListMetricValuesResponse = (
        aws_sdk_iot.types.list_metric_values_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_iot.types.list_metric_values_response.ListMetricValuesResponse:
    out: aws_sdk_iot.types.list_metric_values_response.ListMetricValuesResponse = (
        aws_sdk_iot.types.list_metric_values_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_iot._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_iot._auth._sigv4.build_sigv4_auth_scheme("iot", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_iot._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_iot.types.list_metric_values_request.ListMetricValuesRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/metric-values"
    params: dict[str, str] = {}
    if "thing_name" in input_:
        params["thingName"] = str(input_["thing_name"])
    if "metric_name" in input_:
        params["metricName"] = str(input_["metric_name"])
    if "dimension_name" in input_:
        params["dimensionName"] = str(input_["dimension_name"])
    if "dimension_value_operator" in input_:
        params["dimensionValueOperator"] = str(input_["dimension_value_operator"])
    if "start_time" in input_:
        params["startTime"] = str(input_["start_time"])
    if "end_time" in input_:
        params["endTime"] = str(input_["end_time"])
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


def list_metric_values(
    options: OperationOptions,
    input_: aws_sdk_iot.types.list_metric_values_request.ListMetricValuesRequest,
) -> tuple[
    aws_sdk_iot.types.list_metric_values_response.ListMetricValuesResponse,
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


async def async_list_metric_values(
    options: AsyncOperationOptions,
    input_: aws_sdk_iot.types.list_metric_values_request.ListMetricValuesRequest,
) -> tuple[
    aws_sdk_iot.types.list_metric_values_response.ListMetricValuesResponse,
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
