"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetInterpolatedAssetPropertyValues``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_iotsitewise._auth._signers
import aws_sdk_iotsitewise._auth._sigv4
from aws_sdk_iotsitewise._protocol.errors import parse_error_metadata_json
from aws_sdk_iotsitewise._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_iotsitewise._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_iotsitewise.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_request
    import aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalFailureException":
            import aws_sdk_iotsitewise.errors.internal_failure_exception

            raise aws_sdk_iotsitewise.errors.internal_failure_exception.InternalFailureException.from_json(
                data
            )
        case "InvalidRequestException":
            import aws_sdk_iotsitewise.errors.invalid_request_exception

            raise aws_sdk_iotsitewise.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_iotsitewise.errors.resource_not_found_exception

            raise aws_sdk_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceUnavailableException":
            import aws_sdk_iotsitewise.errors.service_unavailable_exception

            raise aws_sdk_iotsitewise.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_iotsitewise.errors.throttling_exception

            raise aws_sdk_iotsitewise.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_response.GetInterpolatedAssetPropertyValuesResponse:
    import aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_response

    out: aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_response.GetInterpolatedAssetPropertyValuesResponse = aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_iotsitewise._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_iotsitewise._auth._sigv4.build_sigv4_auth_scheme(
                "iotsitewise", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_iotsitewise._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_request.GetInterpolatedAssetPropertyValuesRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/properties/interpolated"
    params: dict[str, str] = {}
    if "asset_id" in input:
        params["assetId"] = str(input["asset_id"])
    if "property_id" in input:
        params["propertyId"] = str(input["property_id"])
    if "property_alias" in input:
        params["propertyAlias"] = str(input["property_alias"])
    if "start_time_in_seconds" in input:
        params["startTimeInSeconds"] = str(input["start_time_in_seconds"])
    if "start_time_offset_in_nanos" in input:
        params["startTimeOffsetInNanos"] = str(input["start_time_offset_in_nanos"])
    if "end_time_in_seconds" in input:
        params["endTimeInSeconds"] = str(input["end_time_in_seconds"])
    if "end_time_offset_in_nanos" in input:
        params["endTimeOffsetInNanos"] = str(input["end_time_offset_in_nanos"])
    if "quality" in input:
        params["quality"] = str(input["quality"])
    if "interval_in_seconds" in input:
        params["intervalInSeconds"] = str(input["interval_in_seconds"])
    if "next_token" in input:
        params["nextToken"] = str(input["next_token"])
    if "max_results" in input:
        params["maxResults"] = str(input["max_results"])
    if "type" in input:
        params["type"] = str(input["type"])
    if "interval_window_in_seconds" in input:
        params["intervalWindowInSeconds"] = str(input["interval_window_in_seconds"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "GET",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def get_interpolated_asset_property_values(
    options: OperationOptions,
    input: aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_request.GetInterpolatedAssetPropertyValuesRequest,
) -> tuple[
    aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_response.GetInterpolatedAssetPropertyValuesResponse,
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


async def async_get_interpolated_asset_property_values(
    options: AsyncOperationOptions,
    input: aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_request.GetInterpolatedAssetPropertyValuesRequest,
) -> tuple[
    aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_response.GetInterpolatedAssetPropertyValuesResponse,
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
