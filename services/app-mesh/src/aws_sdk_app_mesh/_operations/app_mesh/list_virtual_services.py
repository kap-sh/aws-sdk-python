"""Generated from Smithy shape ``com.amazonaws.appmesh#ListVirtualServices``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_app_mesh._auth._signers
import aws_sdk_app_mesh._auth._sigv4
import aws_sdk_app_mesh.errors.bad_request_exception
import aws_sdk_app_mesh.errors.forbidden_exception
import aws_sdk_app_mesh.errors.internal_server_error_exception
import aws_sdk_app_mesh.errors.not_found_exception
import aws_sdk_app_mesh.errors.service_unavailable_exception
import aws_sdk_app_mesh.errors.too_many_requests_exception
import aws_sdk_app_mesh.types.list_virtual_services_input
import aws_sdk_app_mesh.types.list_virtual_services_output
import aws_sdk_app_mesh.types.virtual_service_list
from aws_sdk_app_mesh._protocol.errors import parse_error_metadata_json
from aws_sdk_app_mesh._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_app_mesh._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_app_mesh.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise aws_sdk_app_mesh.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ForbiddenException":
            raise aws_sdk_app_mesh.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "InternalServerErrorException":
            raise aws_sdk_app_mesh.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "NotFoundException":
            raise aws_sdk_app_mesh.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "TooManyRequestsException":
            raise aws_sdk_app_mesh.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_app_mesh.types.list_virtual_services_output.ListVirtualServicesOutput:
    out: aws_sdk_app_mesh.types.list_virtual_services_output.ListVirtualServicesOutput = aws_sdk_app_mesh.types.list_virtual_services_output.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_app_mesh.types.list_virtual_services_output.ListVirtualServicesOutput:
    out: aws_sdk_app_mesh.types.list_virtual_services_output.ListVirtualServicesOutput = aws_sdk_app_mesh.types.list_virtual_services_output.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_app_mesh._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_app_mesh._auth._sigv4.build_sigv4_auth_scheme(
                "appmesh", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_app_mesh._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_app_mesh.types.list_virtual_services_input.ListVirtualServicesInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v20190125/meshes/{meshName}/virtualServices"
    url = url.replace("{meshName}", quote(str(input_["mesh_name"]), safe=""))
    params: dict[str, str] = {}
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    if "limit" in input_:
        params["limit"] = str(input_["limit"])
    if "mesh_owner" in input_:
        params["meshOwner"] = str(input_["mesh_owner"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_virtual_services(
    options: OperationOptions,
    input_: aws_sdk_app_mesh.types.list_virtual_services_input.ListVirtualServicesInput,
) -> tuple[
    aws_sdk_app_mesh.types.list_virtual_services_output.ListVirtualServicesOutput,
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


async def async_list_virtual_services(
    options: AsyncOperationOptions,
    input_: aws_sdk_app_mesh.types.list_virtual_services_input.ListVirtualServicesInput,
) -> tuple[
    aws_sdk_app_mesh.types.list_virtual_services_output.ListVirtualServicesOutput,
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
