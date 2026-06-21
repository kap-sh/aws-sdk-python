"""Generated from Smithy shape ``com.amazonaws.greengrass#ListLoggerDefinitionVersions``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_greengrass._auth._signers
import aws_sdk_greengrass._auth._sigv4
import aws_sdk_greengrass.errors.bad_request_exception
import aws_sdk_greengrass.types.__list_of_version_information
import aws_sdk_greengrass.types.list_logger_definition_versions_request
import aws_sdk_greengrass.types.list_logger_definition_versions_response
from aws_sdk_greengrass._protocol.errors import parse_error_metadata_json
from aws_sdk_greengrass._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_greengrass._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_greengrass.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise aws_sdk_greengrass.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_greengrass.types.list_logger_definition_versions_response.ListLoggerDefinitionVersionsResponse:
    out: aws_sdk_greengrass.types.list_logger_definition_versions_response.ListLoggerDefinitionVersionsResponse = aws_sdk_greengrass.types.list_logger_definition_versions_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_greengrass.types.list_logger_definition_versions_response.ListLoggerDefinitionVersionsResponse:
    out: aws_sdk_greengrass.types.list_logger_definition_versions_response.ListLoggerDefinitionVersionsResponse = aws_sdk_greengrass.types.list_logger_definition_versions_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_greengrass._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_greengrass._auth._sigv4.build_sigv4_auth_scheme(
                "greengrass", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_greengrass._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_greengrass.types.list_logger_definition_versions_request.ListLoggerDefinitionVersionsRequest,
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
        endpoint.url.rstrip("/")
        + "/greengrass/definition/loggers/{LoggerDefinitionId}/versions"
    )
    url = url.replace(
        "{LoggerDefinitionId}", quote(str(input_["logger_definition_id"]), safe="")
    )
    params: dict[str, str] = {}
    if "max_results" in input_:
        params["MaxResults"] = str(input_["max_results"])
    if "next_token" in input_:
        params["NextToken"] = str(input_["next_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_logger_definition_versions(
    options: OperationOptions,
    input_: aws_sdk_greengrass.types.list_logger_definition_versions_request.ListLoggerDefinitionVersionsRequest,
) -> tuple[
    aws_sdk_greengrass.types.list_logger_definition_versions_response.ListLoggerDefinitionVersionsResponse,
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


async def async_list_logger_definition_versions(
    options: AsyncOperationOptions,
    input_: aws_sdk_greengrass.types.list_logger_definition_versions_request.ListLoggerDefinitionVersionsRequest,
) -> tuple[
    aws_sdk_greengrass.types.list_logger_definition_versions_response.ListLoggerDefinitionVersionsResponse,
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
