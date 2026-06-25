"""Generated from Smithy shape ``com.amazonaws.codestarconnections#GetSyncBlockerSummary``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_codestar_connections._auth._signers
import aws_sdk_codestar_connections._auth._sigv4
import aws_sdk_codestar_connections.errors.access_denied_exception
import aws_sdk_codestar_connections.errors.internal_server_exception
import aws_sdk_codestar_connections.errors.invalid_input_exception
import aws_sdk_codestar_connections.errors.resource_not_found_exception
import aws_sdk_codestar_connections.errors.throttling_exception
import aws_sdk_codestar_connections.types.get_sync_blocker_summary_input
import aws_sdk_codestar_connections.types.get_sync_blocker_summary_output
import aws_sdk_codestar_connections.types.sync_blocker_summary
import aws_sdk_codestar_connections.types.sync_configuration_type
from aws_sdk_codestar_connections._protocol.errors import parse_error_metadata_json
from aws_sdk_codestar_connections._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_codestar_connections._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codestar_connections.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_codestar_connections.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_0(
                data
            )
        case "InternalServerException":
            raise aws_sdk_codestar_connections.errors.internal_server_exception.InternalServerException.from_aws_json_1_0(
                data
            )
        case "InvalidInputException":
            raise aws_sdk_codestar_connections.errors.invalid_input_exception.InvalidInputException.from_aws_json_1_0(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_codestar_connections.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_codestar_connections.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_codestar_connections.types.get_sync_blocker_summary_output.GetSyncBlockerSummaryOutput:
    out: aws_sdk_codestar_connections.types.get_sync_blocker_summary_output.GetSyncBlockerSummaryOutput = aws_sdk_codestar_connections.types.get_sync_blocker_summary_output.deserialize_aws_json_1_0(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_codestar_connections.types.get_sync_blocker_summary_output.GetSyncBlockerSummaryOutput:
    out: aws_sdk_codestar_connections.types.get_sync_blocker_summary_output.GetSyncBlockerSummaryOutput = aws_sdk_codestar_connections.types.get_sync_blocker_summary_output.deserialize_aws_json_1_0(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_codestar_connections._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_codestar_connections._auth._sigv4.build_sigv4_auth_scheme(
                "codestar-connections", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_codestar_connections._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_codestar_connections.types.get_sync_blocker_summary_input.GetSyncBlockerSummaryInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "CodeStar_connections_20191201.GetSyncBlockerSummary"
    body: bytes | None = json.dumps(
        aws_sdk_codestar_connections.types.get_sync_blocker_summary_input.serialize_aws_json_1_0(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def get_sync_blocker_summary(
    options: OperationOptions,
    input_: aws_sdk_codestar_connections.types.get_sync_blocker_summary_input.GetSyncBlockerSummaryInput,
) -> tuple[
    aws_sdk_codestar_connections.types.get_sync_blocker_summary_output.GetSyncBlockerSummaryOutput,
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


async def async_get_sync_blocker_summary(
    options: AsyncOperationOptions,
    input_: aws_sdk_codestar_connections.types.get_sync_blocker_summary_input.GetSyncBlockerSummaryInput,
) -> tuple[
    aws_sdk_codestar_connections.types.get_sync_blocker_summary_output.GetSyncBlockerSummaryOutput,
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
