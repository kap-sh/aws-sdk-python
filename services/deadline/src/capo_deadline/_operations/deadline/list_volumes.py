"""Generated from Smithy shape ``com.amazonaws.deadline#ListVolumes``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_deadline._auth._signers
import capo_deadline._auth._sigv4
import capo_deadline.errors.access_denied_exception
import capo_deadline.errors.internal_server_error_exception
import capo_deadline.errors.resource_not_found_exception
import capo_deadline.errors.throttling_exception
import capo_deadline.errors.validation_exception
import capo_deadline.types.list_volumes_request
import capo_deadline.types.list_volumes_response
import capo_deadline.types.volume_summaries
from capo_deadline._protocol.errors import parse_error_metadata_json
from capo_deadline._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_deadline._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_deadline.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_deadline.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerErrorException":
            raise capo_deadline.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_deadline.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise capo_deadline.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_deadline.types.list_volumes_response.ListVolumesResponse:
    out: capo_deadline.types.list_volumes_response.ListVolumesResponse = (
        capo_deadline.types.list_volumes_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_deadline.types.list_volumes_response.ListVolumesResponse:
    out: capo_deadline.types.list_volumes_response.ListVolumesResponse = (
        capo_deadline.types.list_volumes_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_deadline._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_deadline._auth._sigv4.build_sigv4_auth_scheme(
                "deadline", options.region
            )
        )
        if sigv4_config is not None:
            return capo_deadline._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_deadline.types.list_volumes_request.ListVolumesRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/") + "/2023-10-12/farms/{farmId}/fleets/{fleetId}/volumes"
    )
    url = url.replace("{farmId}", quote(str(input_["farm_id"]), safe=""))
    url = url.replace("{fleetId}", quote(str(input_["fleet_id"]), safe=""))
    params: dict[str, str] = {}
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    params["maxResults"] = str(input_.get("max_results", 100))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_volumes(
    options: OperationOptions,
    input_: capo_deadline.types.list_volumes_request.ListVolumesRequest,
) -> tuple[
    capo_deadline.types.list_volumes_response.ListVolumesResponse, zapros.Response
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


async def async_list_volumes(
    options: AsyncOperationOptions,
    input_: capo_deadline.types.list_volumes_request.ListVolumesRequest,
) -> tuple[
    capo_deadline.types.list_volumes_response.ListVolumesResponse, zapros.Response
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
