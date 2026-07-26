"""Generated from Smithy shape ``com.amazonaws.s3files#ListFileSystems``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_s3files._auth._signers
import capo_s3files._auth._sigv4
import capo_s3files.errors.internal_server_exception
import capo_s3files.errors.throttling_exception
import capo_s3files.errors.validation_exception
import capo_s3files.types.file_systems
import capo_s3files.types.list_file_systems_request
import capo_s3files.types.list_file_systems_response
from capo_s3files._protocol.errors import parse_error_metadata_json
from capo_s3files._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3files._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_s3files.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ThrottlingException":
            raise capo_s3files.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "InternalServerException":
            raise capo_s3files.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ValidationException":
            raise capo_s3files.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_s3files.types.list_file_systems_response.ListFileSystemsResponse:
    out: capo_s3files.types.list_file_systems_response.ListFileSystemsResponse = (
        capo_s3files.types.list_file_systems_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3files.types.list_file_systems_response.ListFileSystemsResponse:
    out: capo_s3files.types.list_file_systems_response.ListFileSystemsResponse = (
        capo_s3files.types.list_file_systems_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_s3files._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_s3files._auth._sigv4.build_sigv4_auth_scheme(
                "s3files", options.region
            )
        )
        if sigv4_config is not None:
            return capo_s3files._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_s3files.types.list_file_systems_request.ListFileSystemsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/file-systems"
    params: dict[str, str] = {}
    if "bucket" in input_:
        params["bucket"] = str(input_["bucket"])
    params["maxResults"] = str(input_.get("max_results", 100))
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


def list_file_systems(
    options: OperationOptions,
    input_: capo_s3files.types.list_file_systems_request.ListFileSystemsRequest,
) -> tuple[
    capo_s3files.types.list_file_systems_response.ListFileSystemsResponse,
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


async def async_list_file_systems(
    options: AsyncOperationOptions,
    input_: capo_s3files.types.list_file_systems_request.ListFileSystemsRequest,
) -> tuple[
    capo_s3files.types.list_file_systems_response.ListFileSystemsResponse,
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
