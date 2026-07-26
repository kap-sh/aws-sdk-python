"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeGroups``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_workdocs._auth._signers
import capo_workdocs._auth._sigv4
import capo_workdocs.errors.failed_dependency_exception
import capo_workdocs.errors.service_unavailable_exception
import capo_workdocs.errors.unauthorized_operation_exception
import capo_workdocs.errors.unauthorized_resource_access_exception
import capo_workdocs.types.describe_groups_request
import capo_workdocs.types.describe_groups_response
import capo_workdocs.types.group_metadata_list
from capo_workdocs._protocol.errors import parse_error_metadata_json
from capo_workdocs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_workdocs._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_workdocs.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "FailedDependencyException":
            raise capo_workdocs.errors.failed_dependency_exception.FailedDependencyException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "UnauthorizedOperationException":
            raise capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException.from_json(
                data
            )
        case "UnauthorizedResourceAccessException":
            raise capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_workdocs.types.describe_groups_response.DescribeGroupsResponse:
    out: capo_workdocs.types.describe_groups_response.DescribeGroupsResponse = (
        capo_workdocs.types.describe_groups_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_workdocs.types.describe_groups_response.DescribeGroupsResponse:
    out: capo_workdocs.types.describe_groups_response.DescribeGroupsResponse = (
        capo_workdocs.types.describe_groups_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_workdocs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_workdocs._auth._sigv4.build_sigv4_auth_scheme(
                "workdocs", options.region
            )
        )
        if sigv4_config is not None:
            return capo_workdocs._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_workdocs.types.describe_groups_request.DescribeGroupsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/api/v1/groups"
    params: dict[str, str] = {}
    if "search_query" in input_:
        params["searchQuery"] = str(input_["search_query"])
    if "organization_id" in input_:
        params["organizationId"] = str(input_["organization_id"])
    if "marker" in input_:
        params["marker"] = str(input_["marker"])
    if "limit" in input_:
        params["limit"] = str(input_["limit"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "authentication_token" in input_:
        headers["Authentication"] = str(input_["authentication_token"])
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def describe_groups(
    options: OperationOptions,
    input_: capo_workdocs.types.describe_groups_request.DescribeGroupsRequest,
) -> tuple[
    capo_workdocs.types.describe_groups_response.DescribeGroupsResponse, zapros.Response
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


async def async_describe_groups(
    options: AsyncOperationOptions,
    input_: capo_workdocs.types.describe_groups_request.DescribeGroupsRequest,
) -> tuple[
    capo_workdocs.types.describe_groups_response.DescribeGroupsResponse, zapros.Response
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
