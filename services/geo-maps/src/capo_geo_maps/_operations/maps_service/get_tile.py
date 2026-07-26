"""Generated from Smithy shape ``com.amazonaws.geomaps#GetTile``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_geo_maps._auth._signers
import capo_geo_maps._auth._sigv4
import capo_geo_maps.errors.access_denied_exception
import capo_geo_maps.errors.internal_server_exception
import capo_geo_maps.errors.resource_not_found_exception
import capo_geo_maps.errors.throttling_exception
import capo_geo_maps.errors.validation_exception
import capo_geo_maps.types.get_tile_request
import capo_geo_maps.types.get_tile_response
import capo_geo_maps.types.tile_additional_feature_list
from capo_geo_maps._protocol.errors import parse_error_metadata_json
from capo_geo_maps._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_geo_maps._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_geo_maps.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_geo_maps.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise capo_geo_maps.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_geo_maps.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_geo_maps.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise capo_geo_maps.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_geo_maps.types.get_tile_response.GetTileResponse:
    out: capo_geo_maps.types.get_tile_response.GetTileResponse = {
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


async def async_handle_response(
    response: zapros.Response,
) -> capo_geo_maps.types.get_tile_response.GetTileResponse:
    out: capo_geo_maps.types.get_tile_response.GetTileResponse = {
        "blob": await response.aread()
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
) -> capo_geo_maps._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_geo_maps._auth._sigv4.build_sigv4_auth_scheme(
                "geo-maps", options.region
            )
        )
        if sigv4_config is not None:
            return capo_geo_maps._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_geo_maps.types.get_tile_request.GetTileRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/tiles/{Tileset}/{Z}/{X}/{Y}"
    url = url.replace("{Tileset}", quote(str(input_["tileset"]), safe=""))
    url = url.replace("{Z}", quote(str(input_["z"]), safe=""))
    url = url.replace("{X}", quote(str(input_["x"]), safe=""))
    url = url.replace("{Y}", quote(str(input_["y"]), safe=""))
    params: dict[str, str] = {}
    if "additional_features" in input_:
        params["additional-features"] = str(input_["additional_features"])
    if "key" in input_:
        params["key"] = str(input_["key"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_tile(
    options: OperationOptions,
    input_: capo_geo_maps.types.get_tile_request.GetTileRequest,
) -> tuple[capo_geo_maps.types.get_tile_response.GetTileResponse, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_get_tile(
    options: AsyncOperationOptions,
    input_: capo_geo_maps.types.get_tile_request.GetTileRequest,
) -> tuple[capo_geo_maps.types.get_tile_response.GetTileResponse, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
