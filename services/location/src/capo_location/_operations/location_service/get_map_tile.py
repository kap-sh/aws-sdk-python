"""Generated from Smithy shape ``com.amazonaws.location#GetMapTile``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_location._auth._signers
import capo_location._auth._sigv4
import capo_location.errors.access_denied_exception
import capo_location.errors.internal_server_exception
import capo_location.errors.resource_not_found_exception
import capo_location.errors.throttling_exception
import capo_location.errors.validation_exception
import capo_location.types.get_map_tile_request
import capo_location.types.get_map_tile_response
from capo_location._protocol.errors import parse_error_metadata_json
from capo_location._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_location._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_location.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_location.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise capo_location.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_location.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_location.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise capo_location.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_location.types.get_map_tile_response.GetMapTileResponse:
    out: capo_location.types.get_map_tile_response.GetMapTileResponse = {
        "blob": response.read()
    }  # type: ignore[typeddict-item]
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    if "Cache-Control" in response.headers:
        out["cache_control"] = str(response.headers["Cache-Control"])
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_location.types.get_map_tile_response.GetMapTileResponse:
    out: capo_location.types.get_map_tile_response.GetMapTileResponse = {
        "blob": await response.aread()
    }  # type: ignore[typeddict-item]
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    if "Cache-Control" in response.headers:
        out["cache_control"] = str(response.headers["Cache-Control"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_location._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_location._auth._sigv4.build_sigv4_auth_scheme("geo", options.region)
        )
        if sigv4_config is not None:
            return capo_location._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_location.types.get_map_tile_request.GetMapTileRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/maps/v0/maps/{MapName}/tiles/{Z}/{X}/{Y}"
    url = url.replace("{MapName}", quote(str(input_["map_name"]), safe=""))
    url = url.replace("{Z}", quote(str(input_["z"]), safe=""))
    url = url.replace("{X}", quote(str(input_["x"]), safe=""))
    url = url.replace("{Y}", quote(str(input_["y"]), safe=""))
    params: dict[str, str] = {}
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


def get_map_tile(
    options: OperationOptions,
    input_: capo_location.types.get_map_tile_request.GetMapTileRequest,
) -> tuple[
    capo_location.types.get_map_tile_response.GetMapTileResponse, zapros.Response
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


async def async_get_map_tile(
    options: AsyncOperationOptions,
    input_: capo_location.types.get_map_tile_request.GetMapTileRequest,
) -> tuple[
    capo_location.types.get_map_tile_response.GetMapTileResponse, zapros.Response
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
