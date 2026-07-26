"""Generated from Smithy shape ``com.amazonaws.efs#DescribeReplicationConfigurations``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_efs._auth._signers
import capo_efs._auth._sigv4
import capo_efs.errors.bad_request
import capo_efs.errors.file_system_not_found
import capo_efs.errors.internal_server_error
import capo_efs.errors.replication_not_found
import capo_efs.errors.validation_exception
import capo_efs.types.describe_replication_configurations_request
import capo_efs.types.describe_replication_configurations_response
import capo_efs.types.replication_configuration_descriptions
from capo_efs._protocol.errors import parse_error_metadata_json
from capo_efs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_efs._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_efs.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequest":
            raise capo_efs.errors.bad_request.BadRequest.from_json(data)
        case "FileSystemNotFound":
            raise capo_efs.errors.file_system_not_found.FileSystemNotFound.from_json(
                data
            )
        case "InternalServerError":
            raise capo_efs.errors.internal_server_error.InternalServerError.from_json(
                data
            )
        case "ReplicationNotFound":
            raise capo_efs.errors.replication_not_found.ReplicationNotFound.from_json(
                data
            )
        case "ValidationException":
            raise capo_efs.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_efs.types.describe_replication_configurations_response.DescribeReplicationConfigurationsResponse:
    out: capo_efs.types.describe_replication_configurations_response.DescribeReplicationConfigurationsResponse = capo_efs.types.describe_replication_configurations_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_efs.types.describe_replication_configurations_response.DescribeReplicationConfigurationsResponse:
    out: capo_efs.types.describe_replication_configurations_response.DescribeReplicationConfigurationsResponse = capo_efs.types.describe_replication_configurations_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_efs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_efs._auth._sigv4.build_sigv4_auth_scheme(
                "elasticfilesystem", options.region
            )
        )
        if sigv4_config is not None:
            return capo_efs._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_efs.types.describe_replication_configurations_request.DescribeReplicationConfigurationsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/") + "/2015-02-01/file-systems/replication-configurations"
    )
    params: dict[str, str] = {}
    if "file_system_id" in input_:
        params["FileSystemId"] = str(input_["file_system_id"])
    if "next_token" in input_:
        params["NextToken"] = str(input_["next_token"])
    if "max_results" in input_:
        params["MaxResults"] = str(input_["max_results"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def describe_replication_configurations(
    options: OperationOptions,
    input_: capo_efs.types.describe_replication_configurations_request.DescribeReplicationConfigurationsRequest,
) -> tuple[
    capo_efs.types.describe_replication_configurations_response.DescribeReplicationConfigurationsResponse,
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


async def async_describe_replication_configurations(
    options: AsyncOperationOptions,
    input_: capo_efs.types.describe_replication_configurations_request.DescribeReplicationConfigurationsRequest,
) -> tuple[
    capo_efs.types.describe_replication_configurations_response.DescribeReplicationConfigurationsResponse,
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
