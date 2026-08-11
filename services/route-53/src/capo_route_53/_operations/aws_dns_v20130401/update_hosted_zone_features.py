"""Generated from Smithy shape ``com.amazonaws.route53#UpdateHostedZoneFeatures``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_route_53._auth._signers
import capo_route_53._auth._sigv4
import capo_route_53.errors.invalid_input
import capo_route_53.errors.limits_exceeded
import capo_route_53.errors.no_such_hosted_zone
import capo_route_53.errors.prior_request_not_complete
import capo_route_53.types.update_hosted_zone_features_request
import capo_route_53.types.update_hosted_zone_features_response
from capo_route_53._protocol.errors import find_error_element, parse_error_metadata
from capo_route_53._protocol.xml import Element, SubElement, fromstring, tostring
from capo_route_53._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_route_53._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_route_53.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "InvalidInput":
            raise capo_route_53.errors.invalid_input.InvalidInput.from_xml(
                error_el, message
            )
        case "LimitsExceeded":
            raise capo_route_53.errors.limits_exceeded.LimitsExceeded.from_xml(
                error_el, message
            )
        case "NoSuchHostedZone":
            raise capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone.from_xml(
                error_el, message
            )
        case "PriorRequestNotComplete":
            raise capo_route_53.errors.prior_request_not_complete.PriorRequestNotComplete.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_route_53.types.update_hosted_zone_features_response.UpdateHostedZoneFeaturesResponse:
    out: capo_route_53.types.update_hosted_zone_features_response.UpdateHostedZoneFeaturesResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_route_53.types.update_hosted_zone_features_response.UpdateHostedZoneFeaturesResponse:
    out: capo_route_53.types.update_hosted_zone_features_response.UpdateHostedZoneFeaturesResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_route_53._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_route_53._auth._sigv4.build_sigv4_auth_scheme(
                "route53", options.region
            )
        )
        if sigv4_config is not None:
            return capo_route_53._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_route_53.types.update_hosted_zone_features_request.UpdateHostedZoneFeaturesRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2013-04-01/hostedzone/{HostedZoneId}/features"
    url = url.replace("{HostedZoneId}", quote(input_["hosted_zone_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    root = Element("UpdateHostedZoneFeaturesRequest")
    if "enable_accelerated_recovery" in input_:
        SubElement(root, "EnableAcceleratedRecovery").text = (
            "true" if input_["enable_accelerated_recovery"] else "false"
        )
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def update_hosted_zone_features(
    options: OperationOptions,
    input_: capo_route_53.types.update_hosted_zone_features_request.UpdateHostedZoneFeaturesRequest,
) -> tuple[
    capo_route_53.types.update_hosted_zone_features_response.UpdateHostedZoneFeaturesResponse,
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


async def async_update_hosted_zone_features(
    options: AsyncOperationOptions,
    input_: capo_route_53.types.update_hosted_zone_features_request.UpdateHostedZoneFeaturesRequest,
) -> tuple[
    capo_route_53.types.update_hosted_zone_features_response.UpdateHostedZoneFeaturesResponse,
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
