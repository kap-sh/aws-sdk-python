"""Generated from Smithy shape ``com.amazonaws.geoplaces#GetPlace``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_geo_places._auth._signers
import capo_geo_places._auth._sigv4
import capo_geo_places.errors.access_denied_exception
import capo_geo_places.errors.internal_server_exception
import capo_geo_places.errors.throttling_exception
import capo_geo_places.errors.validation_exception
import capo_geo_places.types.access_point_list
import capo_geo_places.types.access_restriction_list
import capo_geo_places.types.address
import capo_geo_places.types.bounding_box
import capo_geo_places.types.business_chain_list
import capo_geo_places.types.category_list
import capo_geo_places.types.contacts
import capo_geo_places.types.food_type_list
import capo_geo_places.types.get_place_additional_feature_list
import capo_geo_places.types.get_place_request
import capo_geo_places.types.get_place_response
import capo_geo_places.types.opening_hours_list
import capo_geo_places.types.phoneme_details
import capo_geo_places.types.position
import capo_geo_places.types.postal_code_details_list
import capo_geo_places.types.related_place
import capo_geo_places.types.related_place_list
import capo_geo_places.types.time_zone
from capo_geo_places._protocol.errors import parse_error_metadata_json
from capo_geo_places._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_geo_places._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_geo_places.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_geo_places.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise capo_geo_places.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_geo_places.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise capo_geo_places.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_geo_places.types.get_place_response.GetPlaceResponse:
    out: capo_geo_places.types.get_place_response.GetPlaceResponse = (
        capo_geo_places.types.get_place_response.deserialize_json(
            json.loads(response.read())
        )
    )
    out["pricing_bucket"] = str(response.headers["x-amz-geo-pricing-bucket"])
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_geo_places.types.get_place_response.GetPlaceResponse:
    out: capo_geo_places.types.get_place_response.GetPlaceResponse = (
        capo_geo_places.types.get_place_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    out["pricing_bucket"] = str(response.headers["x-amz-geo-pricing-bucket"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_geo_places._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_geo_places._auth._sigv4.build_sigv4_auth_scheme(
                "geo-places", options.region
            )
        )
        if sigv4_config is not None:
            return capo_geo_places._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_geo_places.types.get_place_request.GetPlaceRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v2/place/{PlaceId}"
    url = url.replace("{PlaceId}", quote(str(input_["place_id"]), safe=""))
    params: dict[str, str] = {}
    if "additional_features" in input_:
        params["additional-features"] = str(input_["additional_features"])
    if "language" in input_:
        params["language"] = str(input_["language"])
    if "political_view" in input_:
        params["political-view"] = str(input_["political_view"])
    if "intended_use" in input_:
        params["intended-use"] = str(input_["intended_use"])
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


def get_place(
    options: OperationOptions,
    input_: capo_geo_places.types.get_place_request.GetPlaceRequest,
) -> tuple[capo_geo_places.types.get_place_response.GetPlaceResponse, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_get_place(
    options: AsyncOperationOptions,
    input_: capo_geo_places.types.get_place_request.GetPlaceRequest,
) -> tuple[capo_geo_places.types.get_place_response.GetPlaceResponse, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
