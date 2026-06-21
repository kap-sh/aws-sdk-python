"""Generated from Smithy shape ``com.amazonaws.route53#DeleteTrafficPolicyInstance``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_route_53._auth._signers
import aws_sdk_route_53._auth._sigv4
import aws_sdk_route_53.errors.invalid_input
import aws_sdk_route_53.errors.no_such_traffic_policy_instance
import aws_sdk_route_53.errors.prior_request_not_complete
import aws_sdk_route_53.types.delete_traffic_policy_instance_request
import aws_sdk_route_53.types.delete_traffic_policy_instance_response
from aws_sdk_route_53._protocol.errors import parse_error_metadata
from aws_sdk_route_53._protocol.xml import fromstring
from aws_sdk_route_53._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_route_53._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_route_53.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InvalidInput":
            raise aws_sdk_route_53.errors.invalid_input.InvalidInput.from_xml(root)
        case "NoSuchTrafficPolicyInstance":
            raise aws_sdk_route_53.errors.no_such_traffic_policy_instance.NoSuchTrafficPolicyInstance.from_xml(
                root
            )
        case "PriorRequestNotComplete":
            raise aws_sdk_route_53.errors.prior_request_not_complete.PriorRequestNotComplete.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_route_53.types.delete_traffic_policy_instance_response.DeleteTrafficPolicyInstanceResponse:
    out: aws_sdk_route_53.types.delete_traffic_policy_instance_response.DeleteTrafficPolicyInstanceResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_route_53.types.delete_traffic_policy_instance_response.DeleteTrafficPolicyInstanceResponse:
    out: aws_sdk_route_53.types.delete_traffic_policy_instance_response.DeleteTrafficPolicyInstanceResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_route_53._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_route_53.types.delete_traffic_policy_instance_request.DeleteTrafficPolicyInstanceRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2013-04-01/trafficpolicyinstance/{Id}"
    url = url.replace("{Id}", quote(str(input_["id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_traffic_policy_instance(
    options: OperationOptions,
    input_: aws_sdk_route_53.types.delete_traffic_policy_instance_request.DeleteTrafficPolicyInstanceRequest,
) -> tuple[
    aws_sdk_route_53.types.delete_traffic_policy_instance_response.DeleteTrafficPolicyInstanceResponse,
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


async def async_delete_traffic_policy_instance(
    options: AsyncOperationOptions,
    input_: aws_sdk_route_53.types.delete_traffic_policy_instance_request.DeleteTrafficPolicyInstanceRequest,
) -> tuple[
    aws_sdk_route_53.types.delete_traffic_policy_instance_response.DeleteTrafficPolicyInstanceResponse,
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
