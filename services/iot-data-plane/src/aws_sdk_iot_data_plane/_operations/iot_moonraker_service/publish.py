"""Generated from Smithy shape ``com.amazonaws.iotdataplane#Publish``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_iot_data_plane._auth._signers
import aws_sdk_iot_data_plane._auth._sigv4
from aws_sdk_iot_data_plane._protocol.errors import parse_error_metadata_json
from aws_sdk_iot_data_plane._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_iot_data_plane._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_iot_data_plane.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.publish_request


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalFailureException":
            import aws_sdk_iot_data_plane.errors.internal_failure_exception

            raise aws_sdk_iot_data_plane.errors.internal_failure_exception.InternalFailureException.from_json(
                data
            )
        case "InvalidRequestException":
            import aws_sdk_iot_data_plane.errors.invalid_request_exception

            raise aws_sdk_iot_data_plane.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "MethodNotAllowedException":
            import aws_sdk_iot_data_plane.errors.method_not_allowed_exception

            raise aws_sdk_iot_data_plane.errors.method_not_allowed_exception.MethodNotAllowedException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_iot_data_plane.errors.throttling_exception

            raise aws_sdk_iot_data_plane.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "UnauthorizedException":
            import aws_sdk_iot_data_plane.errors.unauthorized_exception

            raise aws_sdk_iot_data_plane.errors.unauthorized_exception.UnauthorizedException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_iot_data_plane._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_iot_data_plane._auth._sigv4.build_sigv4_auth_scheme(
                "iotdata", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_iot_data_plane._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_iot_data_plane.types.publish_request.PublishRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/topics/{topic}"
    url = url.replace("{topic}", quote(str(input_["topic"]), safe=""))
    params: dict[str, str] = {}
    params["qos"] = str(input_.get("qos", 0))
    params["retain"] = str(input_.get("retain", False))
    if "content_type" in input_:
        params["contentType"] = str(input_["content_type"])
    if "response_topic" in input_:
        params["responseTopic"] = str(input_["response_topic"])
    params["messageExpiry"] = str(input_.get("message_expiry", 0))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "user_properties" in input_:
        headers["x-amz-mqtt5-user-properties"] = str(input_["user_properties"])
    if "payload_format_indicator" in input_:
        headers["x-amz-mqtt5-payload-format-indicator"] = str(
            input_["payload_format_indicator"]
        )
    if "correlation_data" in input_:
        headers["x-amz-mqtt5-correlation-data"] = str(input_["correlation_data"])
    if "payload" in input_:
        import aws_sdk_iot_data_plane.types.payload

        body: bytes | None = json.dumps(
            aws_sdk_iot_data_plane.types.payload.serialize_json(input_["payload"])
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


def publish(
    options: OperationOptions,
    input_: aws_sdk_iot_data_plane.types.publish_request.PublishRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return None, response
    except BaseException:
        response.close()
        raise


async def async_publish(
    options: AsyncOperationOptions,
    input_: aws_sdk_iot_data_plane.types.publish_request.PublishRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return None, response
    except BaseException:
        await response.aclose()
        raise
