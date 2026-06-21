"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#GetWorkflowRun``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_mwaa_serverless._auth._signers
import aws_sdk_mwaa_serverless._auth._sigv4
import aws_sdk_mwaa_serverless.errors.access_denied_exception
import aws_sdk_mwaa_serverless.errors.internal_server_exception
import aws_sdk_mwaa_serverless.errors.operation_timeout_exception
import aws_sdk_mwaa_serverless.errors.resource_not_found_exception
import aws_sdk_mwaa_serverless.errors.throttling_exception
import aws_sdk_mwaa_serverless.errors.validation_exception
import aws_sdk_mwaa_serverless.types.get_workflow_run_request
import aws_sdk_mwaa_serverless.types.get_workflow_run_response
import aws_sdk_mwaa_serverless.types.object_map
import aws_sdk_mwaa_serverless.types.run_type
import aws_sdk_mwaa_serverless.types.workflow_run_detail
from aws_sdk_mwaa_serverless._protocol.errors import parse_error_metadata_json
from aws_sdk_mwaa_serverless._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_mwaa_serverless._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_mwaa_serverless.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_mwaa_serverless.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_0(
                data
            )
        case "InternalServerException":
            raise aws_sdk_mwaa_serverless.errors.internal_server_exception.InternalServerException.from_aws_json_1_0(
                data
            )
        case "OperationTimeoutException":
            raise aws_sdk_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException.from_aws_json_1_0(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_mwaa_serverless.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data
            )
        case "ValidationException":
            raise aws_sdk_mwaa_serverless.errors.validation_exception.ValidationException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse:
    out: aws_sdk_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse = aws_sdk_mwaa_serverless.types.get_workflow_run_response.deserialize_aws_json_1_0(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse:
    out: aws_sdk_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse = aws_sdk_mwaa_serverless.types.get_workflow_run_response.deserialize_aws_json_1_0(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_mwaa_serverless._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_mwaa_serverless._auth._sigv4.build_sigv4_auth_scheme(
                "airflow-serverless", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_mwaa_serverless._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_mwaa_serverless.types.get_workflow_run_request.GetWorkflowRunRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/workflows/{WorkflowArn}/runs/{RunId}"
    url = url.replace("{WorkflowArn}", quote(str(input_["workflow_arn"]), safe=""))
    url = url.replace("{RunId}", quote(str(input_["run_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AmazonMWAAServerless.GetWorkflowRun"
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_workflow_run(
    options: OperationOptions,
    input_: aws_sdk_mwaa_serverless.types.get_workflow_run_request.GetWorkflowRunRequest,
) -> tuple[
    aws_sdk_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse,
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


async def async_get_workflow_run(
    options: AsyncOperationOptions,
    input_: aws_sdk_mwaa_serverless.types.get_workflow_run_request.GetWorkflowRunRequest,
) -> tuple[
    aws_sdk_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse,
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
