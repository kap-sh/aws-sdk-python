"""Generated from Smithy shape ``com.amazonaws.datapipeline#EvaluateExpression``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_data_pipeline._auth._signers
import capo_data_pipeline._auth._sigv4
import capo_data_pipeline.errors.internal_service_error
import capo_data_pipeline.errors.invalid_request_exception
import capo_data_pipeline.errors.pipeline_deleted_exception
import capo_data_pipeline.errors.pipeline_not_found_exception
import capo_data_pipeline.errors.task_not_found_exception
import capo_data_pipeline.types.evaluate_expression_input
import capo_data_pipeline.types.evaluate_expression_output
from capo_data_pipeline._protocol.errors import parse_error_metadata_json
from capo_data_pipeline._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_data_pipeline._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_data_pipeline.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServiceError":
            raise capo_data_pipeline.errors.internal_service_error.InternalServiceError.from_aws_json_1_1(
                data
            )
        case "InvalidRequestException":
            raise capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException.from_aws_json_1_1(
                data
            )
        case "PipelineDeletedException":
            raise capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException.from_aws_json_1_1(
                data
            )
        case "PipelineNotFoundException":
            raise capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException.from_aws_json_1_1(
                data
            )
        case "TaskNotFoundException":
            raise capo_data_pipeline.errors.task_not_found_exception.TaskNotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_data_pipeline.types.evaluate_expression_output.EvaluateExpressionOutput:
    out: capo_data_pipeline.types.evaluate_expression_output.EvaluateExpressionOutput = capo_data_pipeline.types.evaluate_expression_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_data_pipeline.types.evaluate_expression_output.EvaluateExpressionOutput:
    out: capo_data_pipeline.types.evaluate_expression_output.EvaluateExpressionOutput = capo_data_pipeline.types.evaluate_expression_output.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_data_pipeline._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_data_pipeline._auth._sigv4.build_sigv4_auth_scheme(
                "datapipeline", options.region
            )
        )
        if sigv4_config is not None:
            return capo_data_pipeline._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_data_pipeline.types.evaluate_expression_input.EvaluateExpressionInput,
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
    headers["X-Amz-Target"] = "DataPipeline.EvaluateExpression"
    body: bytes | None = json.dumps(
        capo_data_pipeline.types.evaluate_expression_input.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def evaluate_expression(
    options: OperationOptions,
    input_: capo_data_pipeline.types.evaluate_expression_input.EvaluateExpressionInput,
) -> tuple[
    capo_data_pipeline.types.evaluate_expression_output.EvaluateExpressionOutput,
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


async def async_evaluate_expression(
    options: AsyncOperationOptions,
    input_: capo_data_pipeline.types.evaluate_expression_input.EvaluateExpressionInput,
) -> tuple[
    capo_data_pipeline.types.evaluate_expression_output.EvaluateExpressionOutput,
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
