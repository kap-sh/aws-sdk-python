"""Generated from Smithy shape ``com.amazonaws.rum#BatchDeleteRumMetricDefinitions``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_rum._auth._signers
import capo_rum._auth._sigv4
import capo_rum.errors.access_denied_exception
import capo_rum.errors.conflict_exception
import capo_rum.errors.internal_server_exception
import capo_rum.errors.resource_not_found_exception
import capo_rum.errors.throttling_exception
import capo_rum.errors.validation_exception
import capo_rum.types.batch_delete_rum_metric_definitions_errors
import capo_rum.types.batch_delete_rum_metric_definitions_request
import capo_rum.types.batch_delete_rum_metric_definitions_response
import capo_rum.types.metric_definition_ids
from capo_rum._protocol.errors import parse_error_metadata_json
from capo_rum._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_rum._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_rum.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_rum.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            raise capo_rum.errors.conflict_exception.ConflictException.from_json(data)
        case "InternalServerException":
            raise capo_rum.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_rum.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_rum.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise capo_rum.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_rum.types.batch_delete_rum_metric_definitions_response.BatchDeleteRumMetricDefinitionsResponse:
    out: capo_rum.types.batch_delete_rum_metric_definitions_response.BatchDeleteRumMetricDefinitionsResponse = capo_rum.types.batch_delete_rum_metric_definitions_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_rum.types.batch_delete_rum_metric_definitions_response.BatchDeleteRumMetricDefinitionsResponse:
    out: capo_rum.types.batch_delete_rum_metric_definitions_response.BatchDeleteRumMetricDefinitionsResponse = capo_rum.types.batch_delete_rum_metric_definitions_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_rum._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_rum._auth._sigv4.build_sigv4_auth_scheme("rum", options.region)
        )
        if sigv4_config is not None:
            return capo_rum._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_rum.types.batch_delete_rum_metric_definitions_request.BatchDeleteRumMetricDefinitionsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/rummetrics/{AppMonitorName}/metrics"
    url = url.replace(
        "{AppMonitorName}", quote(str(input_["app_monitor_name"]), safe="")
    )
    params: dict[str, str] = {}
    if "destination" in input_:
        params["destination"] = str(input_["destination"])
    if "destination_arn" in input_:
        params["destinationArn"] = str(input_["destination_arn"])
    if "metric_definition_ids" in input_:
        params["metricDefinitionIds"] = str(input_["metric_definition_ids"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def batch_delete_rum_metric_definitions(
    options: OperationOptions,
    input_: capo_rum.types.batch_delete_rum_metric_definitions_request.BatchDeleteRumMetricDefinitionsRequest,
) -> tuple[
    capo_rum.types.batch_delete_rum_metric_definitions_response.BatchDeleteRumMetricDefinitionsResponse,
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


async def async_batch_delete_rum_metric_definitions(
    options: AsyncOperationOptions,
    input_: capo_rum.types.batch_delete_rum_metric_definitions_request.BatchDeleteRumMetricDefinitionsRequest,
) -> tuple[
    capo_rum.types.batch_delete_rum_metric_definitions_response.BatchDeleteRumMetricDefinitionsResponse,
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
