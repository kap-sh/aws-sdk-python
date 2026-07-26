"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeFirewallMetadata``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_network_firewall._auth._signers
import capo_network_firewall._auth._sigv4
import capo_network_firewall.errors.internal_server_error
import capo_network_firewall.errors.invalid_request_exception
import capo_network_firewall.errors.resource_not_found_exception
import capo_network_firewall.errors.throttling_exception
import capo_network_firewall.types.describe_firewall_metadata_request
import capo_network_firewall.types.describe_firewall_metadata_response
import capo_network_firewall.types.firewall_status_value
import capo_network_firewall.types.supported_availability_zones
from capo_network_firewall._protocol.errors import parse_error_metadata_json
from capo_network_firewall._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_network_firewall._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_network_firewall.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerError":
            raise capo_network_firewall.errors.internal_server_error.InternalServerError.from_aws_json_1_0(
                data
            )
        case "InvalidRequestException":
            raise capo_network_firewall.errors.invalid_request_exception.InvalidRequestException.from_aws_json_1_0(
                data
            )
        case "ResourceNotFoundException":
            raise capo_network_firewall.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data
            )
        case "ThrottlingException":
            raise capo_network_firewall.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_network_firewall.types.describe_firewall_metadata_response.DescribeFirewallMetadataResponse:
    out: capo_network_firewall.types.describe_firewall_metadata_response.DescribeFirewallMetadataResponse = capo_network_firewall.types.describe_firewall_metadata_response.deserialize_aws_json_1_0(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_network_firewall.types.describe_firewall_metadata_response.DescribeFirewallMetadataResponse:
    out: capo_network_firewall.types.describe_firewall_metadata_response.DescribeFirewallMetadataResponse = capo_network_firewall.types.describe_firewall_metadata_response.deserialize_aws_json_1_0(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_network_firewall._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_network_firewall._auth._sigv4.build_sigv4_auth_scheme(
                "network-firewall", options.region
            )
        )
        if sigv4_config is not None:
            return capo_network_firewall._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_network_firewall.types.describe_firewall_metadata_request.DescribeFirewallMetadataRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "NetworkFirewall_20201112.DescribeFirewallMetadata"
    body: bytes | None = json.dumps(
        capo_network_firewall.types.describe_firewall_metadata_request.serialize_aws_json_1_0(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def describe_firewall_metadata(
    options: OperationOptions,
    input_: capo_network_firewall.types.describe_firewall_metadata_request.DescribeFirewallMetadataRequest,
) -> tuple[
    capo_network_firewall.types.describe_firewall_metadata_response.DescribeFirewallMetadataResponse,
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


async def async_describe_firewall_metadata(
    options: AsyncOperationOptions,
    input_: capo_network_firewall.types.describe_firewall_metadata_request.DescribeFirewallMetadataRequest,
) -> tuple[
    capo_network_firewall.types.describe_firewall_metadata_response.DescribeFirewallMetadataResponse,
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
