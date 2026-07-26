"""Generated from Smithy shape ``com.amazonaws.route53#CreateTrafficPolicyInstance``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_route_53._auth._signers
import capo_route_53._auth._sigv4
import capo_route_53.errors.invalid_input
import capo_route_53.errors.no_such_hosted_zone
import capo_route_53.errors.no_such_traffic_policy
import capo_route_53.errors.too_many_traffic_policy_instances
import capo_route_53.errors.traffic_policy_instance_already_exists
import capo_route_53.types.create_traffic_policy_instance_request
import capo_route_53.types.create_traffic_policy_instance_response
import capo_route_53.types.traffic_policy_instance
from capo_route_53._protocol.errors import parse_error_metadata
from capo_route_53._protocol.xml import Element, SubElement, fromstring, tostring
from capo_route_53._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_route_53._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_route_53.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InvalidInput":
            raise capo_route_53.errors.invalid_input.InvalidInput.from_xml(root)
        case "NoSuchHostedZone":
            raise capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone.from_xml(
                root
            )
        case "NoSuchTrafficPolicy":
            raise capo_route_53.errors.no_such_traffic_policy.NoSuchTrafficPolicy.from_xml(
                root
            )
        case "TooManyTrafficPolicyInstances":
            raise capo_route_53.errors.too_many_traffic_policy_instances.TooManyTrafficPolicyInstances.from_xml(
                root
            )
        case "TrafficPolicyInstanceAlreadyExists":
            raise capo_route_53.errors.traffic_policy_instance_already_exists.TrafficPolicyInstanceAlreadyExists.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_route_53.types.create_traffic_policy_instance_response.CreateTrafficPolicyInstanceResponse:
    out: capo_route_53.types.create_traffic_policy_instance_response.CreateTrafficPolicyInstanceResponse = capo_route_53.types.create_traffic_policy_instance_response.deserialize_xml(
        fromstring(response.read())
    )
    out["location"] = str(response.headers["Location"])
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_route_53.types.create_traffic_policy_instance_response.CreateTrafficPolicyInstanceResponse:
    out: capo_route_53.types.create_traffic_policy_instance_response.CreateTrafficPolicyInstanceResponse = capo_route_53.types.create_traffic_policy_instance_response.deserialize_xml(
        fromstring(await response.aread())
    )
    out["location"] = str(response.headers["Location"])
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
    input_: capo_route_53.types.create_traffic_policy_instance_request.CreateTrafficPolicyInstanceRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2013-04-01/trafficpolicyinstance"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    root = Element("CreateTrafficPolicyInstanceRequest")
    if "hosted_zone_id" in input_:
        SubElement(root, "HostedZoneId").text = str(input_["hosted_zone_id"])
    if "name" in input_:
        SubElement(root, "Name").text = str(input_["name"])
    if "ttl" in input_:
        SubElement(root, "TTL").text = str(input_["ttl"])
    if "traffic_policy_id" in input_:
        SubElement(root, "TrafficPolicyId").text = str(input_["traffic_policy_id"])
    if "traffic_policy_version" in input_:
        SubElement(root, "TrafficPolicyVersion").text = str(
            input_["traffic_policy_version"]
        )
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_traffic_policy_instance(
    options: OperationOptions,
    input_: capo_route_53.types.create_traffic_policy_instance_request.CreateTrafficPolicyInstanceRequest,
) -> tuple[
    capo_route_53.types.create_traffic_policy_instance_response.CreateTrafficPolicyInstanceResponse,
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


async def async_create_traffic_policy_instance(
    options: AsyncOperationOptions,
    input_: capo_route_53.types.create_traffic_policy_instance_request.CreateTrafficPolicyInstanceRequest,
) -> tuple[
    capo_route_53.types.create_traffic_policy_instance_response.CreateTrafficPolicyInstanceResponse,
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
