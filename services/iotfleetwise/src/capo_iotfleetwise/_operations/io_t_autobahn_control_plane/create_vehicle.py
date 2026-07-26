"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateVehicle``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_iotfleetwise._auth._signers
import capo_iotfleetwise._auth._sigv4
import capo_iotfleetwise.errors.access_denied_exception
import capo_iotfleetwise.errors.conflict_exception
import capo_iotfleetwise.errors.internal_server_exception
import capo_iotfleetwise.errors.limit_exceeded_exception
import capo_iotfleetwise.errors.resource_not_found_exception
import capo_iotfleetwise.errors.throttling_exception
import capo_iotfleetwise.errors.validation_exception
import capo_iotfleetwise.types.attributes_map
import capo_iotfleetwise.types.create_vehicle_request
import capo_iotfleetwise.types.create_vehicle_response
import capo_iotfleetwise.types.state_template_associations
import capo_iotfleetwise.types.tag_list
import capo_iotfleetwise.types.vehicle_association_behavior
from capo_iotfleetwise._protocol.errors import parse_error_metadata_json
from capo_iotfleetwise._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_iotfleetwise._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_iotfleetwise.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            raise capo_iotfleetwise.errors.internal_server_exception.InternalServerException.from_aws_json_1_0(
                data
            )
        case "AccessDeniedException":
            raise capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_0(
                data
            )
        case "ConflictException":
            raise capo_iotfleetwise.errors.conflict_exception.ConflictException.from_aws_json_1_0(
                data
            )
        case "LimitExceededException":
            raise capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_0(
                data
            )
        case "ResourceNotFoundException":
            raise capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data
            )
        case "ThrottlingException":
            raise capo_iotfleetwise.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data
            )
        case "ValidationException":
            raise capo_iotfleetwise.errors.validation_exception.ValidationException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_iotfleetwise.types.create_vehicle_response.CreateVehicleResponse:
    out: capo_iotfleetwise.types.create_vehicle_response.CreateVehicleResponse = (
        capo_iotfleetwise.types.create_vehicle_response.deserialize_aws_json_1_0(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_iotfleetwise.types.create_vehicle_response.CreateVehicleResponse:
    out: capo_iotfleetwise.types.create_vehicle_response.CreateVehicleResponse = (
        capo_iotfleetwise.types.create_vehicle_response.deserialize_aws_json_1_0(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_iotfleetwise._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_iotfleetwise._auth._sigv4.build_sigv4_auth_scheme(
                "iotfleetwise", options.region
            )
        )
        if sigv4_config is not None:
            return capo_iotfleetwise._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_iotfleetwise.types.create_vehicle_request.CreateVehicleRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/vehicles/{vehicleName}"
    url = url.replace("{vehicleName}", quote(str(input_["vehicle_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "IoTAutobahnControlPlane.CreateVehicle"
    body: bytes | None = json.dumps(
        capo_iotfleetwise.types.create_vehicle_request.serialize_aws_json_1_0(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_vehicle(
    options: OperationOptions,
    input_: capo_iotfleetwise.types.create_vehicle_request.CreateVehicleRequest,
) -> tuple[
    capo_iotfleetwise.types.create_vehicle_response.CreateVehicleResponse,
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


async def async_create_vehicle(
    options: AsyncOperationOptions,
    input_: capo_iotfleetwise.types.create_vehicle_request.CreateVehicleRequest,
) -> tuple[
    capo_iotfleetwise.types.create_vehicle_response.CreateVehicleResponse,
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
