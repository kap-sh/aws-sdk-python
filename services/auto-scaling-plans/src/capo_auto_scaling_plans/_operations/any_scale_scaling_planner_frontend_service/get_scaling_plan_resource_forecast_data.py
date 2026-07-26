"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#GetScalingPlanResourceForecastData``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_auto_scaling_plans._auth._signers
import capo_auto_scaling_plans._auth._sigv4
import capo_auto_scaling_plans.errors.internal_service_exception
import capo_auto_scaling_plans.errors.validation_exception
import capo_auto_scaling_plans.types.datapoints
import capo_auto_scaling_plans.types.forecast_data_type
import capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_request
import capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response
import capo_auto_scaling_plans.types.scalable_dimension
import capo_auto_scaling_plans.types.service_namespace
import capo_auto_scaling_plans.types.timestamp_type
from capo_auto_scaling_plans._protocol.errors import parse_error_metadata_json
from capo_auto_scaling_plans._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_auto_scaling_plans._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_auto_scaling_plans.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServiceException":
            raise capo_auto_scaling_plans.errors.internal_service_exception.InternalServiceException.from_aws_json_1_1(
                data
            )
        case "ValidationException":
            raise capo_auto_scaling_plans.errors.validation_exception.ValidationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response.GetScalingPlanResourceForecastDataResponse:
    out: capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response.GetScalingPlanResourceForecastDataResponse = capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response.GetScalingPlanResourceForecastDataResponse:
    out: capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response.GetScalingPlanResourceForecastDataResponse = capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_auto_scaling_plans._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_auto_scaling_plans._auth._sigv4.build_sigv4_auth_scheme(
                "autoscaling-plans", options.region
            )
        )
        if sigv4_config is not None:
            return capo_auto_scaling_plans._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_request.GetScalingPlanResourceForecastDataRequest,
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
        "AnyScaleScalingPlannerFrontendService.GetScalingPlanResourceForecastData"
    )
    body: bytes | None = json.dumps(
        capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_request.serialize_aws_json_1_1(
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


def get_scaling_plan_resource_forecast_data(
    options: OperationOptions,
    input_: capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_request.GetScalingPlanResourceForecastDataRequest,
) -> tuple[
    capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response.GetScalingPlanResourceForecastDataResponse,
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


async def async_get_scaling_plan_resource_forecast_data(
    options: AsyncOperationOptions,
    input_: capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_request.GetScalingPlanResourceForecastDataRequest,
) -> tuple[
    capo_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response.GetScalingPlanResourceForecastDataResponse,
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
