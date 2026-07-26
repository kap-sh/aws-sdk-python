"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetWorkflowExecution``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_imagebuilder._auth._signers
import capo_imagebuilder._auth._sigv4
import capo_imagebuilder.errors.call_rate_limit_exceeded_exception
import capo_imagebuilder.errors.client_exception
import capo_imagebuilder.errors.forbidden_exception
import capo_imagebuilder.errors.invalid_request_exception
import capo_imagebuilder.errors.service_exception
import capo_imagebuilder.errors.service_unavailable_exception
import capo_imagebuilder.types.get_workflow_execution_request
import capo_imagebuilder.types.get_workflow_execution_response
import capo_imagebuilder.types.workflow_execution_status
import capo_imagebuilder.types.workflow_type
from capo_imagebuilder._protocol.errors import parse_error_metadata_json
from capo_imagebuilder._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_imagebuilder._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_imagebuilder.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CallRateLimitExceededException":
            raise capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException.from_json(
                data
            )
        case "ClientException":
            raise capo_imagebuilder.errors.client_exception.ClientException.from_json(
                data
            )
        case "ForbiddenException":
            raise capo_imagebuilder.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "InvalidRequestException":
            raise capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "ServiceException":
            raise capo_imagebuilder.errors.service_exception.ServiceException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    capo_imagebuilder.types.get_workflow_execution_response.GetWorkflowExecutionResponse
):
    out: capo_imagebuilder.types.get_workflow_execution_response.GetWorkflowExecutionResponse = capo_imagebuilder.types.get_workflow_execution_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    capo_imagebuilder.types.get_workflow_execution_response.GetWorkflowExecutionResponse
):
    out: capo_imagebuilder.types.get_workflow_execution_response.GetWorkflowExecutionResponse = capo_imagebuilder.types.get_workflow_execution_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_imagebuilder._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_imagebuilder._auth._sigv4.build_sigv4_auth_scheme(
                "imagebuilder", options.region
            )
        )
        if sigv4_config is not None:
            return capo_imagebuilder._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_imagebuilder.types.get_workflow_execution_request.GetWorkflowExecutionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/GetWorkflowExecution"
    params: dict[str, str] = {}
    if "workflow_execution_id" in input_:
        params["workflowExecutionId"] = str(input_["workflow_execution_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_workflow_execution(
    options: OperationOptions,
    input_: capo_imagebuilder.types.get_workflow_execution_request.GetWorkflowExecutionRequest,
) -> tuple[
    capo_imagebuilder.types.get_workflow_execution_response.GetWorkflowExecutionResponse,
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


async def async_get_workflow_execution(
    options: AsyncOperationOptions,
    input_: capo_imagebuilder.types.get_workflow_execution_request.GetWorkflowExecutionRequest,
) -> tuple[
    capo_imagebuilder.types.get_workflow_execution_response.GetWorkflowExecutionResponse,
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
