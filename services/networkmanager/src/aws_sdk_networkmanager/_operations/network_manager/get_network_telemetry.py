"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetNetworkTelemetry``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_networkmanager._auth._signers
import aws_sdk_networkmanager._auth._sigv4
from aws_sdk_networkmanager._protocol.errors import parse_error_metadata_json
from aws_sdk_networkmanager._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_networkmanager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_networkmanager.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.get_network_telemetry_request
    import aws_sdk_networkmanager.types.get_network_telemetry_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_networkmanager.errors.access_denied_exception

            raise aws_sdk_networkmanager.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_networkmanager.errors.internal_server_exception

            raise aws_sdk_networkmanager.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_networkmanager.errors.resource_not_found_exception

            raise aws_sdk_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_networkmanager.errors.throttling_exception

            raise aws_sdk_networkmanager.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_networkmanager.errors.validation_exception

            raise aws_sdk_networkmanager.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_networkmanager.types.get_network_telemetry_response.GetNetworkTelemetryResponse:
    import aws_sdk_networkmanager.types.get_network_telemetry_response

    out: aws_sdk_networkmanager.types.get_network_telemetry_response.GetNetworkTelemetryResponse = aws_sdk_networkmanager.types.get_network_telemetry_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_networkmanager._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_networkmanager._auth._sigv4.build_sigv4_auth_scheme(
                "networkmanager", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_networkmanager._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_networkmanager.types.get_network_telemetry_request.GetNetworkTelemetryRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/global-networks/{GlobalNetworkId}/network-telemetry"
    )
    url = url.replace(
        "{GlobalNetworkId}", quote(str(input_["global_network_id"]), safe="")
    )
    params: dict[str, str] = {}
    if "core_network_id" in input_:
        params["coreNetworkId"] = str(input_["core_network_id"])
    if "registered_gateway_arn" in input_:
        params["registeredGatewayArn"] = str(input_["registered_gateway_arn"])
    if "aws_region" in input_:
        params["awsRegion"] = str(input_["aws_region"])
    if "account_id" in input_:
        params["accountId"] = str(input_["account_id"])
    if "resource_type" in input_:
        params["resourceType"] = str(input_["resource_type"])
    if "resource_arn" in input_:
        params["resourceArn"] = str(input_["resource_arn"])
    if "max_results" in input_:
        params["maxResults"] = str(input_["max_results"])
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_network_telemetry(
    options: OperationOptions,
    input_: aws_sdk_networkmanager.types.get_network_telemetry_request.GetNetworkTelemetryRequest,
) -> tuple[
    aws_sdk_networkmanager.types.get_network_telemetry_response.GetNetworkTelemetryResponse,
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


async def async_get_network_telemetry(
    options: AsyncOperationOptions,
    input_: aws_sdk_networkmanager.types.get_network_telemetry_request.GetNetworkTelemetryRequest,
) -> tuple[
    aws_sdk_networkmanager.types.get_network_telemetry_response.GetNetworkTelemetryResponse,
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
