"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DeleteProject``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_codecatalyst._auth._signers
import aws_sdk_codecatalyst._auth._sigv4
import aws_sdk_codecatalyst.errors.access_denied_exception
import aws_sdk_codecatalyst.errors.conflict_exception
import aws_sdk_codecatalyst.errors.resource_not_found_exception
import aws_sdk_codecatalyst.errors.service_quota_exceeded_exception
import aws_sdk_codecatalyst.errors.throttling_exception
import aws_sdk_codecatalyst.errors.validation_exception
import aws_sdk_codecatalyst.types.delete_project_request
import aws_sdk_codecatalyst.types.delete_project_response
from aws_sdk_codecatalyst._protocol.errors import parse_error_metadata_json
from aws_sdk_codecatalyst._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_codecatalyst._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codecatalyst.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_codecatalyst.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            raise aws_sdk_codecatalyst.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise aws_sdk_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_codecatalyst.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_codecatalyst.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_codecatalyst.types.delete_project_response.DeleteProjectResponse:
    out: aws_sdk_codecatalyst.types.delete_project_response.DeleteProjectResponse = (
        aws_sdk_codecatalyst.types.delete_project_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_codecatalyst.types.delete_project_response.DeleteProjectResponse:
    out: aws_sdk_codecatalyst.types.delete_project_response.DeleteProjectResponse = (
        aws_sdk_codecatalyst.types.delete_project_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_codecatalyst._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.bearer_provider is not None:
        return aws_sdk_codecatalyst._auth._signers.HttpBearerSigner(
            options.bearer_provider
        )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_codecatalyst.types.delete_project_request.DeleteProjectRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Region=options.region, Endpoint=options.endpoint
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/spaces/{spaceName}/projects/{name}"
    url = url.replace("{spaceName}", quote(str(input_["space_name"]), safe=""))
    url = url.replace("{name}", quote(str(input_["name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_project(
    options: OperationOptions,
    input_: aws_sdk_codecatalyst.types.delete_project_request.DeleteProjectRequest,
) -> tuple[
    aws_sdk_codecatalyst.types.delete_project_response.DeleteProjectResponse,
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


async def async_delete_project(
    options: AsyncOperationOptions,
    input_: aws_sdk_codecatalyst.types.delete_project_request.DeleteProjectRequest,
) -> tuple[
    aws_sdk_codecatalyst.types.delete_project_response.DeleteProjectResponse,
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
