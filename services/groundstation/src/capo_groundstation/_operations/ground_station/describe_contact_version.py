"""Generated from Smithy shape ``com.amazonaws.groundstation#DescribeContactVersion``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_groundstation._auth._signers
import capo_groundstation._auth._sigv4
import capo_groundstation.errors.dependency_exception
import capo_groundstation.errors.invalid_parameter_exception
import capo_groundstation.errors.resource_not_found_exception
import capo_groundstation.types.contact_status
import capo_groundstation.types.contact_version
import capo_groundstation.types.dataflow_list
import capo_groundstation.types.describe_contact_version_request
import capo_groundstation.types.describe_contact_version_response
import capo_groundstation.types.elevation
import capo_groundstation.types.ephemeris_response_data
import capo_groundstation.types.tags_map
import capo_groundstation.types.tracking_overrides
from capo_groundstation._protocol.errors import parse_error_metadata_json
from capo_groundstation._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_groundstation._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_groundstation.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "DependencyException":
            raise capo_groundstation.errors.dependency_exception.DependencyException.from_json(
                data
            )
        case "InvalidParameterException":
            raise capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse:
    out: capo_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse = capo_groundstation.types.describe_contact_version_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse:
    out: capo_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse = capo_groundstation.types.describe_contact_version_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_groundstation._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_groundstation._auth._sigv4.build_sigv4_auth_scheme(
                "groundstation", options.region
            )
        )
        if sigv4_config is not None:
            return capo_groundstation._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_groundstation.types.describe_contact_version_request.DescribeContactVersionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/contact/{contactId}/versions/{versionId}"
    url = url.replace("{contactId}", quote(str(input_["contact_id"]), safe=""))
    url = url.replace("{versionId}", quote(str(input_["version_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def describe_contact_version(
    options: OperationOptions,
    input_: capo_groundstation.types.describe_contact_version_request.DescribeContactVersionRequest,
) -> tuple[
    capo_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse,
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


async def async_describe_contact_version(
    options: AsyncOperationOptions,
    input_: capo_groundstation.types.describe_contact_version_request.DescribeContactVersionRequest,
) -> tuple[
    capo_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse,
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
