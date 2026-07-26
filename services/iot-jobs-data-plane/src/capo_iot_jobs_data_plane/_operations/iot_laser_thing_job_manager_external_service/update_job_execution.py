"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#UpdateJobExecution``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_iot_jobs_data_plane._auth._signers
import capo_iot_jobs_data_plane._auth._sigv4
import capo_iot_jobs_data_plane.errors.certificate_validation_exception
import capo_iot_jobs_data_plane.errors.invalid_request_exception
import capo_iot_jobs_data_plane.errors.invalid_state_transition_exception
import capo_iot_jobs_data_plane.errors.resource_not_found_exception
import capo_iot_jobs_data_plane.errors.service_unavailable_exception
import capo_iot_jobs_data_plane.errors.throttling_exception
import capo_iot_jobs_data_plane.types.details_map
import capo_iot_jobs_data_plane.types.job_execution_state
import capo_iot_jobs_data_plane.types.job_execution_status
import capo_iot_jobs_data_plane.types.update_job_execution_request
import capo_iot_jobs_data_plane.types.update_job_execution_response
from capo_iot_jobs_data_plane._protocol.errors import parse_error_metadata_json
from capo_iot_jobs_data_plane._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_iot_jobs_data_plane._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_iot_jobs_data_plane.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CertificateValidationException":
            raise capo_iot_jobs_data_plane.errors.certificate_validation_exception.CertificateValidationException.from_json(
                data
            )
        case "InvalidRequestException":
            raise capo_iot_jobs_data_plane.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "InvalidStateTransitionException":
            raise capo_iot_jobs_data_plane.errors.invalid_state_transition_exception.InvalidStateTransitionException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_iot_jobs_data_plane.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise capo_iot_jobs_data_plane.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_iot_jobs_data_plane.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_iot_jobs_data_plane.types.update_job_execution_response.UpdateJobExecutionResponse:
    out: capo_iot_jobs_data_plane.types.update_job_execution_response.UpdateJobExecutionResponse = capo_iot_jobs_data_plane.types.update_job_execution_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_iot_jobs_data_plane.types.update_job_execution_response.UpdateJobExecutionResponse:
    out: capo_iot_jobs_data_plane.types.update_job_execution_response.UpdateJobExecutionResponse = capo_iot_jobs_data_plane.types.update_job_execution_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_iot_jobs_data_plane._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_iot_jobs_data_plane._auth._sigv4.build_sigv4_auth_scheme(
                "iot-jobs-data", options.region
            )
        )
        if sigv4_config is not None:
            return capo_iot_jobs_data_plane._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_iot_jobs_data_plane.types.update_job_execution_request.UpdateJobExecutionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/things/{thingName}/jobs/{jobId}"
    url = url.replace("{jobId}", quote(str(input_["job_id"]), safe=""))
    url = url.replace("{thingName}", quote(str(input_["thing_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_iot_jobs_data_plane.types.update_job_execution_request.serialize_json(
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


def update_job_execution(
    options: OperationOptions,
    input_: capo_iot_jobs_data_plane.types.update_job_execution_request.UpdateJobExecutionRequest,
) -> tuple[
    capo_iot_jobs_data_plane.types.update_job_execution_response.UpdateJobExecutionResponse,
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


async def async_update_job_execution(
    options: AsyncOperationOptions,
    input_: capo_iot_jobs_data_plane.types.update_job_execution_request.UpdateJobExecutionRequest,
) -> tuple[
    capo_iot_jobs_data_plane.types.update_job_execution_response.UpdateJobExecutionResponse,
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
