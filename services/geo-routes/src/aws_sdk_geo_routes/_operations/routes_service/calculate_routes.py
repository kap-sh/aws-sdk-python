"""Generated from Smithy shape ``com.amazonaws.georoutes#CalculateRoutes``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_geo_routes._auth._signers
import aws_sdk_geo_routes._auth._sigv4
import aws_sdk_geo_routes.errors.access_denied_exception
import aws_sdk_geo_routes.errors.internal_server_exception
import aws_sdk_geo_routes.errors.throttling_exception
import aws_sdk_geo_routes.errors.validation_exception
import aws_sdk_geo_routes.types.calculate_routes_request
import aws_sdk_geo_routes.types.calculate_routes_response
import aws_sdk_geo_routes.types.geometry_format
import aws_sdk_geo_routes.types.language_tag_list
import aws_sdk_geo_routes.types.measurement_system
import aws_sdk_geo_routes.types.position
import aws_sdk_geo_routes.types.route_allow_options
import aws_sdk_geo_routes.types.route_avoidance_options
import aws_sdk_geo_routes.types.route_destination_options
import aws_sdk_geo_routes.types.route_driver_options
import aws_sdk_geo_routes.types.route_exclusion_options
import aws_sdk_geo_routes.types.route_leg_additional_feature_list
import aws_sdk_geo_routes.types.route_list
import aws_sdk_geo_routes.types.route_origin_options
import aws_sdk_geo_routes.types.route_response_notice_list
import aws_sdk_geo_routes.types.route_span_additional_feature_list
import aws_sdk_geo_routes.types.route_toll_options
import aws_sdk_geo_routes.types.route_traffic_options
import aws_sdk_geo_routes.types.route_travel_mode
import aws_sdk_geo_routes.types.route_travel_mode_options
import aws_sdk_geo_routes.types.route_travel_step_type
import aws_sdk_geo_routes.types.route_waypoint_list
import aws_sdk_geo_routes.types.routing_objective
from aws_sdk_geo_routes._protocol.errors import parse_error_metadata_json
from aws_sdk_geo_routes._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_geo_routes._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_geo_routes.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_geo_routes.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_geo_routes.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_geo_routes.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_geo_routes.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_geo_routes.types.calculate_routes_response.CalculateRoutesResponse:
    out: aws_sdk_geo_routes.types.calculate_routes_response.CalculateRoutesResponse = (
        aws_sdk_geo_routes.types.calculate_routes_response.deserialize_json(
            json.loads(response.read())
        )
    )
    out["pricing_bucket"] = str(response.headers["x-amz-geo-pricing-bucket"])
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_geo_routes.types.calculate_routes_response.CalculateRoutesResponse:
    out: aws_sdk_geo_routes.types.calculate_routes_response.CalculateRoutesResponse = (
        aws_sdk_geo_routes.types.calculate_routes_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    out["pricing_bucket"] = str(response.headers["x-amz-geo-pricing-bucket"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_geo_routes._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_geo_routes._auth._sigv4.build_sigv4_auth_scheme(
                "geo-routes", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_geo_routes._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_geo_routes.types.calculate_routes_request.CalculateRoutesRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v2/routes"
    params: dict[str, str] = {}
    if "key" in input_:
        params["key"] = str(input_["key"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_geo_routes.types.calculate_routes_request

    body: bytes | None = json.dumps(
        aws_sdk_geo_routes.types.calculate_routes_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def calculate_routes(
    options: OperationOptions,
    input_: aws_sdk_geo_routes.types.calculate_routes_request.CalculateRoutesRequest,
) -> tuple[
    aws_sdk_geo_routes.types.calculate_routes_response.CalculateRoutesResponse,
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


async def async_calculate_routes(
    options: AsyncOperationOptions,
    input_: aws_sdk_geo_routes.types.calculate_routes_request.CalculateRoutesRequest,
) -> tuple[
    aws_sdk_geo_routes.types.calculate_routes_response.CalculateRoutesResponse,
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
