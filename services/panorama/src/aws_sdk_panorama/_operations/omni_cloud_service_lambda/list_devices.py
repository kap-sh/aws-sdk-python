"""Generated from Smithy shape ``com.amazonaws.panorama#ListDevices``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_panorama._auth._signers
import aws_sdk_panorama._auth._sigv4
import aws_sdk_panorama.errors.access_denied_exception
import aws_sdk_panorama.errors.conflict_exception
import aws_sdk_panorama.errors.internal_server_exception
import aws_sdk_panorama.errors.validation_exception
import aws_sdk_panorama.types.device_list
import aws_sdk_panorama.types.list_devices_request
import aws_sdk_panorama.types.list_devices_response
from aws_sdk_panorama._protocol.errors import parse_error_metadata_json
from aws_sdk_panorama._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_panorama._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_panorama.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_panorama.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            raise aws_sdk_panorama.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_panorama.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_panorama.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_panorama.types.list_devices_response.ListDevicesResponse:
    out: aws_sdk_panorama.types.list_devices_response.ListDevicesResponse = (
        aws_sdk_panorama.types.list_devices_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_panorama.types.list_devices_response.ListDevicesResponse:
    out: aws_sdk_panorama.types.list_devices_response.ListDevicesResponse = (
        aws_sdk_panorama.types.list_devices_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_panorama._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_panorama._auth._sigv4.build_sigv4_auth_scheme(
                "panorama", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_panorama._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_panorama.types.list_devices_request.ListDevicesRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/devices"
    params: dict[str, str] = {}
    if "next_token" in input_:
        params["NextToken"] = str(input_["next_token"])
    params["MaxResults"] = str(input_.get("max_results", 0))
    if "sort_by" in input_:
        params["SortBy"] = str(input_["sort_by"])
    if "sort_order" in input_:
        params["SortOrder"] = str(input_["sort_order"])
    if "name_filter" in input_:
        params["NameFilter"] = str(input_["name_filter"])
    if "device_aggregated_status_filter" in input_:
        params["DeviceAggregatedStatusFilter"] = str(
            input_["device_aggregated_status_filter"]
        )
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_devices(
    options: OperationOptions,
    input_: aws_sdk_panorama.types.list_devices_request.ListDevicesRequest,
) -> tuple[
    aws_sdk_panorama.types.list_devices_response.ListDevicesResponse, zapros.Response
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


async def async_list_devices(
    options: AsyncOperationOptions,
    input_: aws_sdk_panorama.types.list_devices_request.ListDevicesRequest,
) -> tuple[
    aws_sdk_panorama.types.list_devices_response.ListDevicesResponse, zapros.Response
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
