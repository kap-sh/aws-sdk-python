"""Generated from Smithy shape ``com.amazonaws.iotevents#ListDetectorModels``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_iot_events._auth._signers
import aws_sdk_iot_events._auth._sigv4
from aws_sdk_iot_events._protocol.errors import parse_error_metadata_json
from aws_sdk_iot_events._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_iot_events._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_iot_events.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.list_detector_models_request
    import aws_sdk_iot_events.types.list_detector_models_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalFailureException":
            import aws_sdk_iot_events.errors.internal_failure_exception

            raise aws_sdk_iot_events.errors.internal_failure_exception.InternalFailureException.from_json(
                data
            )
        case "InvalidRequestException":
            import aws_sdk_iot_events.errors.invalid_request_exception

            raise aws_sdk_iot_events.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "ServiceUnavailableException":
            import aws_sdk_iot_events.errors.service_unavailable_exception

            raise aws_sdk_iot_events.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_iot_events.errors.throttling_exception

            raise aws_sdk_iot_events.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_iot_events.types.list_detector_models_response.ListDetectorModelsResponse:
    import aws_sdk_iot_events.types.list_detector_models_response

    out: aws_sdk_iot_events.types.list_detector_models_response.ListDetectorModelsResponse = aws_sdk_iot_events.types.list_detector_models_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_iot_events._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_iot_events._auth._sigv4.build_sigv4_auth_scheme(
                "iotevents", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_iot_events._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_iot_events.types.list_detector_models_request.ListDetectorModelsRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/detector-models"
    params: dict[str, str] = {}
    if "next_token" in input:
        params["nextToken"] = str(input["next_token"])
    if "max_results" in input:
        params["maxResults"] = str(input["max_results"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "GET",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def list_detector_models(
    options: OperationOptions,
    input: aws_sdk_iot_events.types.list_detector_models_request.ListDetectorModelsRequest,
) -> tuple[
    aws_sdk_iot_events.types.list_detector_models_response.ListDetectorModelsResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_list_detector_models(
    options: AsyncOperationOptions,
    input: aws_sdk_iot_events.types.list_detector_models_request.ListDetectorModelsRequest,
) -> tuple[
    aws_sdk_iot_events.types.list_detector_models_response.ListDetectorModelsResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
