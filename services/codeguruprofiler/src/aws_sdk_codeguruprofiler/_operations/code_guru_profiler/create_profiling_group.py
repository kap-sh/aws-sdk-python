"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#CreateProfilingGroup``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_codeguruprofiler._auth._signers
import aws_sdk_codeguruprofiler._auth._sigv4
import aws_sdk_codeguruprofiler.errors.conflict_exception
import aws_sdk_codeguruprofiler.errors.internal_server_exception
import aws_sdk_codeguruprofiler.errors.service_quota_exceeded_exception
import aws_sdk_codeguruprofiler.errors.throttling_exception
import aws_sdk_codeguruprofiler.errors.validation_exception
import aws_sdk_codeguruprofiler.types.agent_orchestration_config
import aws_sdk_codeguruprofiler.types.create_profiling_group_request
import aws_sdk_codeguruprofiler.types.create_profiling_group_response
import aws_sdk_codeguruprofiler.types.profiling_group_description
import aws_sdk_codeguruprofiler.types.tags_map
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


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConflictException":
            raise aws_sdk_codeguruprofiler.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_codeguruprofiler.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise aws_sdk_codeguruprofiler.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_codeguruprofiler.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_codeguruprofiler.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_codeguruprofiler.types.create_profiling_group_response.CreateProfilingGroupResponse:
    out: aws_sdk_codeguruprofiler.types.create_profiling_group_response.CreateProfilingGroupResponse = {
        "profiling_group": aws_sdk_codeguruprofiler.types.profiling_group_description.deserialize_json(
            json.loads(response.read())
        )
    }  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_codeguruprofiler.types.create_profiling_group_response.CreateProfilingGroupResponse:
    out: aws_sdk_codeguruprofiler.types.create_profiling_group_response.CreateProfilingGroupResponse = {
        "profiling_group": aws_sdk_codeguruprofiler.types.profiling_group_description.deserialize_json(
            json.loads(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_codeguruprofiler._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_codeguruprofiler.types.create_profiling_group_request.CreateProfilingGroupRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/profilingGroups"
    params: dict[str, str] = {}
    if "client_token" in input_:
        params["clientToken"] = str(input_["client_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_codeguruprofiler.types.create_profiling_group_request

    body: bytes | None = json.dumps(
        aws_sdk_codeguruprofiler.types.create_profiling_group_request.serialize_json(
            input_
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_profiling_group(
    options: OperationOptions,
    input_: aws_sdk_codeguruprofiler.types.create_profiling_group_request.CreateProfilingGroupRequest,
) -> tuple[
    aws_sdk_codeguruprofiler.types.create_profiling_group_response.CreateProfilingGroupResponse,
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


async def async_create_profiling_group(
    options: AsyncOperationOptions,
    input_: aws_sdk_codeguruprofiler.types.create_profiling_group_request.CreateProfilingGroupRequest,
) -> tuple[
    aws_sdk_codeguruprofiler.types.create_profiling_group_response.CreateProfilingGroupResponse,
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
