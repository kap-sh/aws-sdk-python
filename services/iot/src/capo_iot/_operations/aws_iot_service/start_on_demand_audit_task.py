"""Generated from Smithy shape ``com.amazonaws.iot#StartOnDemandAuditTask``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_iot._auth._signers
import capo_iot._auth._sigv4
import capo_iot.errors.internal_failure_exception
import capo_iot.errors.invalid_request_exception
import capo_iot.errors.limit_exceeded_exception
import capo_iot.errors.throttling_exception
import capo_iot.types.start_on_demand_audit_task_request
import capo_iot.types.start_on_demand_audit_task_response
import capo_iot.types.target_audit_check_names
from capo_iot._protocol.errors import parse_error_metadata_json
from capo_iot._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_iot._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_iot.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalFailureException":
            raise capo_iot.errors.internal_failure_exception.InternalFailureException.from_json(
                data
            )
        case "InvalidRequestException":
            raise capo_iot.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "LimitExceededException":
            raise capo_iot.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_iot.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_iot.types.start_on_demand_audit_task_response.StartOnDemandAuditTaskResponse:
    out: capo_iot.types.start_on_demand_audit_task_response.StartOnDemandAuditTaskResponse = capo_iot.types.start_on_demand_audit_task_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_iot.types.start_on_demand_audit_task_response.StartOnDemandAuditTaskResponse:
    out: capo_iot.types.start_on_demand_audit_task_response.StartOnDemandAuditTaskResponse = capo_iot.types.start_on_demand_audit_task_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_iot._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_iot._auth._sigv4.build_sigv4_auth_scheme("iot", options.region)
        )
        if sigv4_config is not None:
            return capo_iot._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_iot.types.start_on_demand_audit_task_request.StartOnDemandAuditTaskRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/audit/tasks"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_iot.types.start_on_demand_audit_task_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def start_on_demand_audit_task(
    options: OperationOptions,
    input_: capo_iot.types.start_on_demand_audit_task_request.StartOnDemandAuditTaskRequest,
) -> tuple[
    capo_iot.types.start_on_demand_audit_task_response.StartOnDemandAuditTaskResponse,
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


async def async_start_on_demand_audit_task(
    options: AsyncOperationOptions,
    input_: capo_iot.types.start_on_demand_audit_task_request.StartOnDemandAuditTaskRequest,
) -> tuple[
    capo_iot.types.start_on_demand_audit_task_response.StartOnDemandAuditTaskResponse,
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
