"""Generated from Smithy shape ``com.amazonaws.glacier#InitiateJob``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_glacier._auth._signers
import aws_sdk_glacier._auth._sigv4
import aws_sdk_glacier.errors.insufficient_capacity_exception
import aws_sdk_glacier.errors.invalid_parameter_value_exception
import aws_sdk_glacier.errors.missing_parameter_value_exception
import aws_sdk_glacier.errors.no_longer_supported_exception
import aws_sdk_glacier.errors.policy_enforced_exception
import aws_sdk_glacier.errors.resource_not_found_exception
import aws_sdk_glacier.errors.service_unavailable_exception
import aws_sdk_glacier.types.initiate_job_input
import aws_sdk_glacier.types.initiate_job_output
import aws_sdk_glacier.types.job_parameters
from aws_sdk_glacier._protocol.errors import parse_error_metadata_json
from aws_sdk_glacier._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_glacier._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_glacier.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InsufficientCapacityException":
            raise aws_sdk_glacier.errors.insufficient_capacity_exception.InsufficientCapacityException.from_json(
                data
            )
        case "InvalidParameterValueException":
            raise aws_sdk_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "MissingParameterValueException":
            raise aws_sdk_glacier.errors.missing_parameter_value_exception.MissingParameterValueException.from_json(
                data
            )
        case "NoLongerSupportedException":
            raise aws_sdk_glacier.errors.no_longer_supported_exception.NoLongerSupportedException.from_json(
                data
            )
        case "PolicyEnforcedException":
            raise aws_sdk_glacier.errors.policy_enforced_exception.PolicyEnforcedException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_glacier.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_glacier.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_glacier.types.initiate_job_output.InitiateJobOutput:
    out: aws_sdk_glacier.types.initiate_job_output.InitiateJobOutput = {}  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = str(response.headers["Location"])
    if "x-amz-job-id" in response.headers:
        out["job_id"] = str(response.headers["x-amz-job-id"])
    if "x-amz-job-output-path" in response.headers:
        out["job_output_path"] = str(response.headers["x-amz-job-output-path"])
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_glacier.types.initiate_job_output.InitiateJobOutput:
    out: aws_sdk_glacier.types.initiate_job_output.InitiateJobOutput = {}  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = str(response.headers["Location"])
    if "x-amz-job-id" in response.headers:
        out["job_id"] = str(response.headers["x-amz-job-id"])
    if "x-amz-job-output-path" in response.headers:
        out["job_output_path"] = str(response.headers["x-amz-job-output-path"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_glacier._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_glacier._auth._sigv4.build_sigv4_auth_scheme(
                "glacier", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_glacier._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_glacier.types.initiate_job_input.InitiateJobInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/{accountId}/vaults/{vaultName}/jobs"
    url = url.replace("{accountId}", quote(str(input_["account_id"]), safe=""))
    url = url.replace("{vaultName}", quote(str(input_["vault_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "job_parameters" in input_:
        body: bytes | None = json.dumps(
            aws_sdk_glacier.types.job_parameters.serialize_json(
                input_["job_parameters"]
            )
        ).encode()
        headers["content-type"] = "application/json"
    else:
        body = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def initiate_job(
    options: OperationOptions,
    input_: aws_sdk_glacier.types.initiate_job_input.InitiateJobInput,
) -> tuple[
    aws_sdk_glacier.types.initiate_job_output.InitiateJobOutput, zapros.Response
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


async def async_initiate_job(
    options: AsyncOperationOptions,
    input_: aws_sdk_glacier.types.initiate_job_input.InitiateJobInput,
) -> tuple[
    aws_sdk_glacier.types.initiate_job_output.InitiateJobOutput, zapros.Response
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
