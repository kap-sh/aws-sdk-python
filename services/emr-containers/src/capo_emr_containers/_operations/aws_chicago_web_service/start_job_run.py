"""Generated from Smithy shape ``com.amazonaws.emrcontainers#StartJobRun``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_emr_containers._auth._signers
import capo_emr_containers._auth._sigv4
import capo_emr_containers.errors.internal_server_exception
import capo_emr_containers.errors.resource_not_found_exception
import capo_emr_containers.errors.validation_exception
import capo_emr_containers.types.configuration_overrides
import capo_emr_containers.types.job_driver
import capo_emr_containers.types.retry_policy_configuration
import capo_emr_containers.types.start_job_run_request
import capo_emr_containers.types.start_job_run_response
import capo_emr_containers.types.tag_map
import capo_emr_containers.types.template_parameter_input_map
from capo_emr_containers._protocol.errors import parse_error_metadata_json
from capo_emr_containers._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_emr_containers._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_emr_containers.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            raise capo_emr_containers.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_emr_containers.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ValidationException":
            raise capo_emr_containers.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_emr_containers.types.start_job_run_response.StartJobRunResponse:
    out: capo_emr_containers.types.start_job_run_response.StartJobRunResponse = (
        capo_emr_containers.types.start_job_run_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_emr_containers.types.start_job_run_response.StartJobRunResponse:
    out: capo_emr_containers.types.start_job_run_response.StartJobRunResponse = (
        capo_emr_containers.types.start_job_run_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_emr_containers._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_emr_containers._auth._sigv4.build_sigv4_auth_scheme(
                "emr-containers", options.region
            )
        )
        if sigv4_config is not None:
            return capo_emr_containers._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_emr_containers.types.start_job_run_request.StartJobRunRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/virtualclusters/{virtualClusterId}/jobruns"
    url = url.replace(
        "{virtualClusterId}", quote(str(input_["virtual_cluster_id"]), safe="")
    )
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_emr_containers.types.start_job_run_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def start_job_run(
    options: OperationOptions,
    input_: capo_emr_containers.types.start_job_run_request.StartJobRunRequest,
) -> tuple[
    capo_emr_containers.types.start_job_run_response.StartJobRunResponse,
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


async def async_start_job_run(
    options: AsyncOperationOptions,
    input_: capo_emr_containers.types.start_job_run_request.StartJobRunRequest,
) -> tuple[
    capo_emr_containers.types.start_job_run_response.StartJobRunResponse,
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
