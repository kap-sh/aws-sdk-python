"""Generated from Smithy shape ``com.amazonaws.geomaps#GetStyleDescriptor``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_geo_maps._auth._signers
import aws_sdk_geo_maps._auth._sigv4
from aws_sdk_geo_maps._protocol.errors import parse_error_metadata_json
from aws_sdk_geo_maps._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_geo_maps._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_geo_maps.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_geo_maps.types.get_style_descriptor_request
    import aws_sdk_geo_maps.types.get_style_descriptor_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_geo_maps.types.get_style_descriptor_response.GetStyleDescriptorResponse:
    out: aws_sdk_geo_maps.types.get_style_descriptor_response.GetStyleDescriptorResponse = {
        "blob": response.read()
    }  # type: ignore[typeddict-item]
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    if "Cache-Control" in response.headers:
        out["cache_control"] = str(response.headers["Cache-Control"])
    if "ETag" in response.headers:
        out["e_tag"] = str(response.headers["ETag"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_geo_maps._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_geo_maps.types.get_style_descriptor_request.GetStyleDescriptorRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/styles/{Style}/descriptor"
    url = url.replace("{Style}", quote(str(input_["style"]), safe=""))
    params: dict[str, str] = {}
    if "color_scheme" in input_:
        params["color-scheme"] = str(input_["color_scheme"])
    if "political_view" in input_:
        params["political-view"] = str(input_["political_view"])
    if "terrain" in input_:
        params["terrain"] = str(input_["terrain"])
    if "contour_density" in input_:
        params["contour-density"] = str(input_["contour_density"])
    if "traffic" in input_:
        params["traffic"] = str(input_["traffic"])
    if "travel_modes" in input_:
        params["travel-modes"] = str(input_["travel_modes"])
    if "buildings" in input_:
        params["buildings"] = str(input_["buildings"])
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


def get_style_descriptor(
    options: OperationOptions,
    input_: aws_sdk_geo_maps.types.get_style_descriptor_request.GetStyleDescriptorRequest,
) -> tuple[
    aws_sdk_geo_maps.types.get_style_descriptor_response.GetStyleDescriptorResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_get_style_descriptor(
    options: AsyncOperationOptions,
    input_: aws_sdk_geo_maps.types.get_style_descriptor_request.GetStyleDescriptorRequest,
) -> tuple[
    aws_sdk_geo_maps.types.get_style_descriptor_response.GetStyleDescriptorResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
