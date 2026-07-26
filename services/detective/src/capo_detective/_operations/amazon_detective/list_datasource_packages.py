"""Generated from Smithy shape ``com.amazonaws.detective#ListDatasourcePackages``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_detective._auth._signers
import capo_detective._auth._sigv4
import capo_detective.errors.access_denied_exception
import capo_detective.errors.internal_server_exception
import capo_detective.errors.resource_not_found_exception
import capo_detective.errors.validation_exception
import capo_detective.types.datasource_package_ingest_details
import capo_detective.types.list_datasource_packages_request
import capo_detective.types.list_datasource_packages_response
from capo_detective._protocol.errors import parse_error_metadata_json
from capo_detective._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_detective._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_detective.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_detective.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise capo_detective.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_detective.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ValidationException":
            raise capo_detective.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_detective.types.list_datasource_packages_response.ListDatasourcePackagesResponse:
    out: capo_detective.types.list_datasource_packages_response.ListDatasourcePackagesResponse = capo_detective.types.list_datasource_packages_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_detective.types.list_datasource_packages_response.ListDatasourcePackagesResponse:
    out: capo_detective.types.list_datasource_packages_response.ListDatasourcePackagesResponse = capo_detective.types.list_datasource_packages_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_detective._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_detective._auth._sigv4.build_sigv4_auth_scheme(
                "detective", options.region
            )
        )
        if sigv4_config is not None:
            return capo_detective._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_detective.types.list_datasource_packages_request.ListDatasourcePackagesRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/graph/datasources/list"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_detective.types.list_datasource_packages_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def list_datasource_packages(
    options: OperationOptions,
    input_: capo_detective.types.list_datasource_packages_request.ListDatasourcePackagesRequest,
) -> tuple[
    capo_detective.types.list_datasource_packages_response.ListDatasourcePackagesResponse,
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


async def async_list_datasource_packages(
    options: AsyncOperationOptions,
    input_: capo_detective.types.list_datasource_packages_request.ListDatasourcePackagesRequest,
) -> tuple[
    capo_detective.types.list_datasource_packages_response.ListDatasourcePackagesResponse,
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
