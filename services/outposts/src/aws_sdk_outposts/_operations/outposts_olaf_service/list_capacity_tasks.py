"""Generated from Smithy shape ``com.amazonaws.outposts#ListCapacityTasks``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_outposts._auth._signers
import aws_sdk_outposts._auth._sigv4
from aws_sdk_outposts._protocol.errors import parse_error_metadata_json
from aws_sdk_outposts._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_outposts._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_outposts.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_outposts.types.list_capacity_tasks_input
    import aws_sdk_outposts.types.list_capacity_tasks_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_outposts.errors.access_denied_exception

            raise aws_sdk_outposts.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_outposts.errors.internal_server_exception

            raise aws_sdk_outposts.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "NotFoundException":
            import aws_sdk_outposts.errors.not_found_exception

            raise aws_sdk_outposts.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_outposts.errors.validation_exception

            raise aws_sdk_outposts.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_outposts.types.list_capacity_tasks_output.ListCapacityTasksOutput:
    import aws_sdk_outposts.types.list_capacity_tasks_output

    out: aws_sdk_outposts.types.list_capacity_tasks_output.ListCapacityTasksOutput = (
        aws_sdk_outposts.types.list_capacity_tasks_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_outposts._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_outposts._auth._sigv4.build_sigv4_auth_scheme(
                "outposts", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_outposts._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_outposts.types.list_capacity_tasks_input.ListCapacityTasksInput,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/capacity/tasks"
    params: dict[str, str] = {}
    if "outpost_identifier_filter" in input:
        params["OutpostIdentifierFilter"] = str(input["outpost_identifier_filter"])
    if "max_results" in input:
        params["MaxResults"] = str(input["max_results"])
    if "next_token" in input:
        params["NextToken"] = str(input["next_token"])
    if "capacity_task_status_filter" in input:
        params["CapacityTaskStatusFilter"] = str(input["capacity_task_status_filter"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "GET",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def list_capacity_tasks(
    options: OperationOptions,
    input: aws_sdk_outposts.types.list_capacity_tasks_input.ListCapacityTasksInput,
) -> tuple[
    aws_sdk_outposts.types.list_capacity_tasks_output.ListCapacityTasksOutput,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_list_capacity_tasks(
    options: AsyncOperationOptions,
    input: aws_sdk_outposts.types.list_capacity_tasks_input.ListCapacityTasksInput,
) -> tuple[
    aws_sdk_outposts.types.list_capacity_tasks_output.ListCapacityTasksOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
