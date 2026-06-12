"""Generated from Smithy shape ``com.amazonaws.route53#ListTrafficPolicyInstancesByHostedZone``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_route_53._auth._signers
import aws_sdk_route_53._auth._sigv4
from aws_sdk_route_53._protocol.errors import parse_error_metadata
from aws_sdk_route_53._protocol.xml import fromstring
from aws_sdk_route_53._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_route_53._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_route_53.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.list_traffic_policy_instances_by_hosted_zone_request
    import aws_sdk_route_53.types.list_traffic_policy_instances_by_hosted_zone_response


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InvalidInput":
            import aws_sdk_route_53.errors.invalid_input

            raise aws_sdk_route_53.errors.invalid_input.InvalidInput.from_xml(root)
        case "NoSuchHostedZone":
            import aws_sdk_route_53.errors.no_such_hosted_zone

            raise aws_sdk_route_53.errors.no_such_hosted_zone.NoSuchHostedZone.from_xml(
                root
            )
        case "NoSuchTrafficPolicyInstance":
            import aws_sdk_route_53.errors.no_such_traffic_policy_instance

            raise aws_sdk_route_53.errors.no_such_traffic_policy_instance.NoSuchTrafficPolicyInstance.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_route_53.types.list_traffic_policy_instances_by_hosted_zone_response.ListTrafficPolicyInstancesByHostedZoneResponse:
    import aws_sdk_route_53.types.list_traffic_policy_instances_by_hosted_zone_response

    out: aws_sdk_route_53.types.list_traffic_policy_instances_by_hosted_zone_response.ListTrafficPolicyInstancesByHostedZoneResponse = aws_sdk_route_53.types.list_traffic_policy_instances_by_hosted_zone_response.deserialize_xml(
        fromstring(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_route_53._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_route_53._auth._sigv4.build_sigv4_auth_scheme(
                "route53", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_route_53._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_route_53.types.list_traffic_policy_instances_by_hosted_zone_request.ListTrafficPolicyInstancesByHostedZoneRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )
    url = endpoint.url.rstrip("/") + "/2013-04-01/trafficpolicyinstances/hostedzone"
    params: dict[str, str] = {}
    if "hosted_zone_id" in input:
        params["id"] = str(input["hosted_zone_id"])
    if "traffic_policy_instance_name_marker" in input:
        params["trafficpolicyinstancename"] = str(
            input["traffic_policy_instance_name_marker"]
        )
    if "traffic_policy_instance_type_marker" in input:
        params["trafficpolicyinstancetype"] = str(
            input["traffic_policy_instance_type_marker"]
        )
    if "max_items" in input:
        params["maxitems"] = str(input["max_items"])
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


def list_traffic_policy_instances_by_hosted_zone(
    options: OperationOptions,
    input: aws_sdk_route_53.types.list_traffic_policy_instances_by_hosted_zone_request.ListTrafficPolicyInstancesByHostedZoneRequest,
) -> tuple[
    aws_sdk_route_53.types.list_traffic_policy_instances_by_hosted_zone_response.ListTrafficPolicyInstancesByHostedZoneResponse,
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


async def async_list_traffic_policy_instances_by_hosted_zone(
    options: AsyncOperationOptions,
    input: aws_sdk_route_53.types.list_traffic_policy_instances_by_hosted_zone_request.ListTrafficPolicyInstancesByHostedZoneRequest,
) -> tuple[
    aws_sdk_route_53.types.list_traffic_policy_instances_by_hosted_zone_response.ListTrafficPolicyInstancesByHostedZoneResponse,
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
