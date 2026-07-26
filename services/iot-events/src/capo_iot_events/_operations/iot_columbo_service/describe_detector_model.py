"""Generated from Smithy shape ``com.amazonaws.iotevents#DescribeDetectorModel``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_iot_events._auth._signers
import capo_iot_events._auth._sigv4
import capo_iot_events.errors.internal_failure_exception
import capo_iot_events.errors.invalid_request_exception
import capo_iot_events.errors.resource_not_found_exception
import capo_iot_events.errors.service_unavailable_exception
import capo_iot_events.errors.throttling_exception
import capo_iot_events.types.describe_detector_model_request
import capo_iot_events.types.describe_detector_model_response
import capo_iot_events.types.detector_model
from capo_iot_events._protocol.errors import parse_error_metadata_json
from capo_iot_events._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_iot_events._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_iot_events.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalFailureException":
            raise capo_iot_events.errors.internal_failure_exception.InternalFailureException.from_json(
                data
            )
        case "InvalidRequestException":
            raise capo_iot_events.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_iot_events.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise capo_iot_events.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_iot_events.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    capo_iot_events.types.describe_detector_model_response.DescribeDetectorModelResponse
):
    out: capo_iot_events.types.describe_detector_model_response.DescribeDetectorModelResponse = capo_iot_events.types.describe_detector_model_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    capo_iot_events.types.describe_detector_model_response.DescribeDetectorModelResponse
):
    out: capo_iot_events.types.describe_detector_model_response.DescribeDetectorModelResponse = capo_iot_events.types.describe_detector_model_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_iot_events._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_iot_events._auth._sigv4.build_sigv4_auth_scheme(
                "iotevents", options.region
            )
        )
        if sigv4_config is not None:
            return capo_iot_events._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_iot_events.types.describe_detector_model_request.DescribeDetectorModelRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/detector-models/{detectorModelName}"
    url = url.replace(
        "{detectorModelName}", quote(str(input_["detector_model_name"]), safe="")
    )
    params: dict[str, str] = {}
    if "detector_model_version" in input_:
        params["version"] = str(input_["detector_model_version"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def describe_detector_model(
    options: OperationOptions,
    input_: capo_iot_events.types.describe_detector_model_request.DescribeDetectorModelRequest,
) -> tuple[
    capo_iot_events.types.describe_detector_model_response.DescribeDetectorModelResponse,
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


async def async_describe_detector_model(
    options: AsyncOperationOptions,
    input_: capo_iot_events.types.describe_detector_model_request.DescribeDetectorModelRequest,
) -> tuple[
    capo_iot_events.types.describe_detector_model_response.DescribeDetectorModelResponse,
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
