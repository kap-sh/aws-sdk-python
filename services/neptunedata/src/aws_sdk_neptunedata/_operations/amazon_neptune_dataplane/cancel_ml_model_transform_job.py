"""Generated from Smithy shape ``com.amazonaws.neptunedata#CancelMLModelTransformJob``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_neptunedata._auth._signers
import aws_sdk_neptunedata._auth._sigv4
import aws_sdk_neptunedata.errors.bad_request_exception
import aws_sdk_neptunedata.errors.client_timeout_exception
import aws_sdk_neptunedata.errors.constraint_violation_exception
import aws_sdk_neptunedata.errors.illegal_argument_exception
import aws_sdk_neptunedata.errors.invalid_argument_exception
import aws_sdk_neptunedata.errors.invalid_parameter_exception
import aws_sdk_neptunedata.errors.missing_parameter_exception
import aws_sdk_neptunedata.errors.ml_resource_not_found_exception
import aws_sdk_neptunedata.errors.preconditions_failed_exception
import aws_sdk_neptunedata.errors.too_many_requests_exception
import aws_sdk_neptunedata.errors.unsupported_operation_exception
import aws_sdk_neptunedata.types.cancel_ml_model_transform_job_input
import aws_sdk_neptunedata.types.cancel_ml_model_transform_job_output
from aws_sdk_neptunedata._protocol.errors import parse_error_metadata_json
from aws_sdk_neptunedata._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_neptunedata._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_neptunedata.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise aws_sdk_neptunedata.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ClientTimeoutException":
            raise aws_sdk_neptunedata.errors.client_timeout_exception.ClientTimeoutException.from_json(
                data
            )
        case "ConstraintViolationException":
            raise aws_sdk_neptunedata.errors.constraint_violation_exception.ConstraintViolationException.from_json(
                data
            )
        case "IllegalArgumentException":
            raise aws_sdk_neptunedata.errors.illegal_argument_exception.IllegalArgumentException.from_json(
                data
            )
        case "InvalidArgumentException":
            raise aws_sdk_neptunedata.errors.invalid_argument_exception.InvalidArgumentException.from_json(
                data
            )
        case "InvalidParameterException":
            raise aws_sdk_neptunedata.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case "MissingParameterException":
            raise aws_sdk_neptunedata.errors.missing_parameter_exception.MissingParameterException.from_json(
                data
            )
        case "MLResourceNotFoundException":
            raise aws_sdk_neptunedata.errors.ml_resource_not_found_exception.MLResourceNotFoundException.from_json(
                data
            )
        case "PreconditionsFailedException":
            raise aws_sdk_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException.from_json(
                data
            )
        case "TooManyRequestsException":
            raise aws_sdk_neptunedata.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case "UnsupportedOperationException":
            raise aws_sdk_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_neptunedata.types.cancel_ml_model_transform_job_output.CancelMLModelTransformJobOutput:
    out: aws_sdk_neptunedata.types.cancel_ml_model_transform_job_output.CancelMLModelTransformJobOutput = aws_sdk_neptunedata.types.cancel_ml_model_transform_job_output.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_neptunedata.types.cancel_ml_model_transform_job_output.CancelMLModelTransformJobOutput:
    out: aws_sdk_neptunedata.types.cancel_ml_model_transform_job_output.CancelMLModelTransformJobOutput = aws_sdk_neptunedata.types.cancel_ml_model_transform_job_output.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_neptunedata._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_neptunedata._auth._sigv4.build_sigv4_auth_scheme(
                "neptune-db", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_neptunedata._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_neptunedata.types.cancel_ml_model_transform_job_input.CancelMLModelTransformJobInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/ml/modeltransform/{id}"
    url = url.replace("{id}", quote(str(input_["id"]), safe=""))
    params: dict[str, str] = {}
    if "neptune_iam_role_arn" in input_:
        params["neptuneIamRoleArn"] = str(input_["neptune_iam_role_arn"])
    if "clean" in input_:
        params["clean"] = str(input_["clean"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def cancel_ml_model_transform_job(
    options: OperationOptions,
    input_: aws_sdk_neptunedata.types.cancel_ml_model_transform_job_input.CancelMLModelTransformJobInput,
) -> tuple[
    aws_sdk_neptunedata.types.cancel_ml_model_transform_job_output.CancelMLModelTransformJobOutput,
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


async def async_cancel_ml_model_transform_job(
    options: AsyncOperationOptions,
    input_: aws_sdk_neptunedata.types.cancel_ml_model_transform_job_input.CancelMLModelTransformJobInput,
) -> tuple[
    aws_sdk_neptunedata.types.cancel_ml_model_transform_job_output.CancelMLModelTransformJobOutput,
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
