"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#GetSuiteDefinition``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_iotdeviceadvisor._auth._signers
import capo_iotdeviceadvisor._auth._sigv4
import capo_iotdeviceadvisor.errors.internal_server_exception
import capo_iotdeviceadvisor.errors.resource_not_found_exception
import capo_iotdeviceadvisor.errors.validation_exception
import capo_iotdeviceadvisor.types.get_suite_definition_request
import capo_iotdeviceadvisor.types.get_suite_definition_response
import capo_iotdeviceadvisor.types.suite_definition_configuration
import capo_iotdeviceadvisor.types.tag_map
import capo_iotdeviceadvisor.types.timestamp
from capo_iotdeviceadvisor._protocol.errors import parse_error_metadata_json
from capo_iotdeviceadvisor._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_iotdeviceadvisor._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_iotdeviceadvisor.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            raise capo_iotdeviceadvisor.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_iotdeviceadvisor.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ValidationException":
            raise capo_iotdeviceadvisor.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    capo_iotdeviceadvisor.types.get_suite_definition_response.GetSuiteDefinitionResponse
):
    out: capo_iotdeviceadvisor.types.get_suite_definition_response.GetSuiteDefinitionResponse = capo_iotdeviceadvisor.types.get_suite_definition_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    capo_iotdeviceadvisor.types.get_suite_definition_response.GetSuiteDefinitionResponse
):
    out: capo_iotdeviceadvisor.types.get_suite_definition_response.GetSuiteDefinitionResponse = capo_iotdeviceadvisor.types.get_suite_definition_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_iotdeviceadvisor._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_iotdeviceadvisor._auth._sigv4.build_sigv4_auth_scheme(
                "iotdeviceadvisor", options.region
            )
        )
        if sigv4_config is not None:
            return capo_iotdeviceadvisor._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_iotdeviceadvisor.types.get_suite_definition_request.GetSuiteDefinitionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/suiteDefinitions/{suiteDefinitionId}"
    url = url.replace(
        "{suiteDefinitionId}", quote(str(input_["suite_definition_id"]), safe="")
    )
    params: dict[str, str] = {}
    if "suite_definition_version" in input_:
        params["suiteDefinitionVersion"] = str(input_["suite_definition_version"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_suite_definition(
    options: OperationOptions,
    input_: capo_iotdeviceadvisor.types.get_suite_definition_request.GetSuiteDefinitionRequest,
) -> tuple[
    capo_iotdeviceadvisor.types.get_suite_definition_response.GetSuiteDefinitionResponse,
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


async def async_get_suite_definition(
    options: AsyncOperationOptions,
    input_: capo_iotdeviceadvisor.types.get_suite_definition_request.GetSuiteDefinitionRequest,
) -> tuple[
    capo_iotdeviceadvisor.types.get_suite_definition_response.GetSuiteDefinitionResponse,
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
