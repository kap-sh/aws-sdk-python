"""Generated from Smithy shape ``com.amazonaws.storagegateway#StartAvailabilityMonitorTest``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any, cast
from aws_sdk_storage_gateway._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_storage_gateway._rule_engine._endpoint_runtime import apply_label
import jmespath
import zapros
from urllib.parse import quote, urlencode
from aws_sdk_storage_gateway.errors import ServiceError, UnknownServiceError
from aws_sdk_storage_gateway._protocol.errors import parse_error_metadata_json
import json
import aws_sdk_storage_gateway._auth._signers
import aws_sdk_storage_gateway._auth._sigv4
from aws_sdk_storage_gateway._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
import datetime
from email.utils import parsedate_to_datetime as _parse_http_date

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.start_availability_monitor_test_input
    import aws_sdk_storage_gateway.types.start_availability_monitor_test_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerError":
            import aws_sdk_storage_gateway.errors.internal_server_error

            raise aws_sdk_storage_gateway.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data
            )
        case "InvalidGatewayRequestException":
            import aws_sdk_storage_gateway.errors.invalid_gateway_request_exception

            raise aws_sdk_storage_gateway.errors.invalid_gateway_request_exception.InvalidGatewayRequestException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_storage_gateway.types.start_availability_monitor_test_output.StartAvailabilityMonitorTestOutput:
    import aws_sdk_storage_gateway.types.start_availability_monitor_test_output

    out: aws_sdk_storage_gateway.types.start_availability_monitor_test_output.StartAvailabilityMonitorTestOutput = aws_sdk_storage_gateway.types.start_availability_monitor_test_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_storage_gateway._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_storage_gateway._auth._sigv4.build_sigv4_auth_scheme(
                "storagegateway", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_storage_gateway._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_storage_gateway.types.start_availability_monitor_test_input.StartAvailabilityMonitorTestInput,
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
    headers["X-Amz-Target"] = "StorageGateway_20130630.StartAvailabilityMonitorTest"
    import aws_sdk_storage_gateway.types.start_availability_monitor_test_input

    body: bytes | None = json.dumps(
        aws_sdk_storage_gateway.types.start_availability_monitor_test_input.serialize_aws_json_1_1(
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


def start_availability_monitor_test(
    options: OperationOptions,
    input_: aws_sdk_storage_gateway.types.start_availability_monitor_test_input.StartAvailabilityMonitorTestInput,
) -> tuple[
    aws_sdk_storage_gateway.types.start_availability_monitor_test_output.StartAvailabilityMonitorTestOutput,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_start_availability_monitor_test(
    options: AsyncOperationOptions,
    input_: aws_sdk_storage_gateway.types.start_availability_monitor_test_input.StartAvailabilityMonitorTestInput,
) -> tuple[
    aws_sdk_storage_gateway.types.start_availability_monitor_test_output.StartAvailabilityMonitorTestOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
