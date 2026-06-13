"""Generated from Smithy shape ``com.amazonaws.geomaps#GetStaticMap``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_geo_maps._auth._signers
import aws_sdk_geo_maps._auth._sigv4
from aws_sdk_geo_maps._protocol.errors import parse_error_metadata_json
from aws_sdk_geo_maps._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_geo_maps._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_geo_maps.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_geo_maps.types.get_static_map_request
    import aws_sdk_geo_maps.types.get_static_map_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_geo_maps.errors.access_denied_exception

            raise aws_sdk_geo_maps.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_geo_maps.errors.internal_server_exception

            raise aws_sdk_geo_maps.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_geo_maps.errors.throttling_exception

            raise aws_sdk_geo_maps.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_geo_maps.errors.validation_exception

            raise aws_sdk_geo_maps.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_geo_maps.types.get_static_map_response.GetStaticMapResponse:
    out: aws_sdk_geo_maps.types.get_static_map_response.GetStaticMapResponse = {
        "blob": response.read()
    }  # type: ignore[typeddict-item]
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    if "Cache-Control" in response.headers:
        out["cache_control"] = str(response.headers["Cache-Control"])
    if "ETag" in response.headers:
        out["e_tag"] = str(response.headers["ETag"])
    out["pricing_bucket"] = str(response.headers["x-amz-geo-pricing-bucket"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_geo_maps._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_geo_maps._auth._sigv4.build_sigv4_auth_scheme(
                "geo-maps", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_geo_maps._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_geo_maps.types.get_static_map_request.GetStaticMapRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )
    url = endpoint.url.rstrip("/") + "/static/{FileName}"
    url = url.replace("{FileName}", quote(str(input["file_name"]), safe=""))
    params: dict[str, str] = {}
    if "bounding_box" in input:
        params["bounding-box"] = str(input["bounding_box"])
    if "bounded_positions" in input:
        params["bounded-positions"] = str(input["bounded_positions"])
    if "center" in input:
        params["center"] = str(input["center"])
    if "color_scheme" in input:
        params["color-scheme"] = str(input["color_scheme"])
    if "compact_overlay" in input:
        params["compact-overlay"] = str(input["compact_overlay"])
    if "crop_labels" in input:
        params["crop-labels"] = str(input["crop_labels"])
    if "geo_json_overlay" in input:
        params["geojson-overlay"] = str(input["geo_json_overlay"])
    if "height" in input:
        params["height"] = str(input["height"])
    if "key" in input:
        params["key"] = str(input["key"])
    if "label_size" in input:
        params["label-size"] = str(input["label_size"])
    if "language" in input:
        params["lang"] = str(input["language"])
    if "padding" in input:
        params["padding"] = str(input["padding"])
    if "political_view" in input:
        params["political-view"] = str(input["political_view"])
    if "points_of_interests" in input:
        params["pois"] = str(input["points_of_interests"])
    if "radius" in input:
        params["radius"] = str(input["radius"])
    if "scale_bar_unit" in input:
        params["scale-unit"] = str(input["scale_bar_unit"])
    if "style" in input:
        params["style"] = str(input["style"])
    if "width" in input:
        params["width"] = str(input["width"])
    if "zoom" in input:
        params["zoom"] = str(input["zoom"])
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


def get_static_map(
    options: OperationOptions,
    input: aws_sdk_geo_maps.types.get_static_map_request.GetStaticMapRequest,
) -> tuple[
    aws_sdk_geo_maps.types.get_static_map_response.GetStaticMapResponse, zapros.Response
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


async def async_get_static_map(
    options: AsyncOperationOptions,
    input: aws_sdk_geo_maps.types.get_static_map_request.GetStaticMapRequest,
) -> tuple[
    aws_sdk_geo_maps.types.get_static_map_response.GetStaticMapResponse, zapros.Response
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
