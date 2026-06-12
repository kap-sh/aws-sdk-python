"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#UpdateProfilingGroup``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_codeguruprofiler._auth._signers
import aws_sdk_codeguruprofiler._auth._sigv4
from aws_sdk_codeguruprofiler._protocol.errors import parse_error_metadata_json
from aws_sdk_codeguruprofiler._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_codeguruprofiler._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codeguruprofiler.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.update_profiling_group_request
    import aws_sdk_codeguruprofiler.types.update_profiling_group_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConflictException":
            import aws_sdk_codeguruprofiler.errors.conflict_exception

            raise aws_sdk_codeguruprofiler.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_codeguruprofiler.errors.internal_server_exception

            raise aws_sdk_codeguruprofiler.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_codeguruprofiler.errors.resource_not_found_exception

            raise aws_sdk_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_codeguruprofiler.errors.throttling_exception

            raise aws_sdk_codeguruprofiler.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_codeguruprofiler.errors.validation_exception

            raise aws_sdk_codeguruprofiler.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_codeguruprofiler.types.update_profiling_group_response.UpdateProfilingGroupResponse:
    import aws_sdk_codeguruprofiler.types.profiling_group_description

    out: aws_sdk_codeguruprofiler.types.update_profiling_group_response.UpdateProfilingGroupResponse = {
        "profiling_group": aws_sdk_codeguruprofiler.types.profiling_group_description.deserialize_json(
            json.loads(response.read())
        )
    }  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_codeguruprofiler._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_codeguruprofiler._auth._sigv4.build_sigv4_auth_scheme(
                "codeguru-profiler", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_codeguruprofiler._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_codeguruprofiler.types.update_profiling_group_request.UpdateProfilingGroupRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/profilingGroups/{profilingGroupName}"
    url = url.replace(
        "{profilingGroupName}", quote(str(input["profiling_group_name"]), safe="")
    )
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_codeguruprofiler.types.update_profiling_group_request

    body: bytes | None = json.dumps(
        aws_sdk_codeguruprofiler.types.update_profiling_group_request.serialize_json(
            input
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "PUT",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def update_profiling_group(
    options: OperationOptions,
    input: aws_sdk_codeguruprofiler.types.update_profiling_group_request.UpdateProfilingGroupRequest,
) -> tuple[
    aws_sdk_codeguruprofiler.types.update_profiling_group_response.UpdateProfilingGroupResponse,
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


async def async_update_profiling_group(
    options: AsyncOperationOptions,
    input: aws_sdk_codeguruprofiler.types.update_profiling_group_request.UpdateProfilingGroupRequest,
) -> tuple[
    aws_sdk_codeguruprofiler.types.update_profiling_group_response.UpdateProfilingGroupResponse,
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
