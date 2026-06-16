"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateRealtimeLogConfig``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_cloudfront._auth._signers
import aws_sdk_cloudfront._auth._sigv4
from aws_sdk_cloudfront._protocol.errors import parse_error_metadata
from aws_sdk_cloudfront._protocol.xml import Element, SubElement, fromstring, tostring
from aws_sdk_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloudfront._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudfront.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.create_realtime_log_config_request
    import aws_sdk_cloudfront.types.create_realtime_log_config_result


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AccessDenied":
            import aws_sdk_cloudfront.errors.access_denied

            raise aws_sdk_cloudfront.errors.access_denied.AccessDenied.from_xml(root)
        case "InvalidArgument":
            import aws_sdk_cloudfront.errors.invalid_argument

            raise aws_sdk_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                root
            )
        case "RealtimeLogConfigAlreadyExists":
            import aws_sdk_cloudfront.errors.realtime_log_config_already_exists

            raise aws_sdk_cloudfront.errors.realtime_log_config_already_exists.RealtimeLogConfigAlreadyExists.from_xml(
                root
            )
        case "TooManyRealtimeLogConfigs":
            import aws_sdk_cloudfront.errors.too_many_realtime_log_configs

            raise aws_sdk_cloudfront.errors.too_many_realtime_log_configs.TooManyRealtimeLogConfigs.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cloudfront.types.create_realtime_log_config_result.CreateRealtimeLogConfigResult:
    import aws_sdk_cloudfront.types.create_realtime_log_config_result

    out: aws_sdk_cloudfront.types.create_realtime_log_config_result.CreateRealtimeLogConfigResult = aws_sdk_cloudfront.types.create_realtime_log_config_result.deserialize_xml(
        fromstring(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloudfront._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cloudfront._auth._sigv4.build_sigv4_auth_scheme(
                "cloudfront", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cloudfront._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_cloudfront.types.create_realtime_log_config_request.CreateRealtimeLogConfigRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/realtime-log-config"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    root = Element("CreateRealtimeLogConfigRequest")
    if "end_points" in input_:
        import aws_sdk_cloudfront.types.end_point_list

        aws_sdk_cloudfront.types.end_point_list.serialize_xml(
            input_["end_points"], root, "EndPoints"
        )
    if "fields" in input_:
        import aws_sdk_cloudfront.types.field_list

        aws_sdk_cloudfront.types.field_list.serialize_xml(
            input_["fields"], root, "Fields"
        )
    if "name" in input_:
        SubElement(root, "Name").text = str(input_["name"])
    if "sampling_rate" in input_:
        SubElement(root, "SamplingRate").text = str(input_["sampling_rate"])
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_realtime_log_config(
    options: OperationOptions,
    input_: aws_sdk_cloudfront.types.create_realtime_log_config_request.CreateRealtimeLogConfigRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_realtime_log_config_result.CreateRealtimeLogConfigResult,
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


async def async_create_realtime_log_config(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudfront.types.create_realtime_log_config_request.CreateRealtimeLogConfigRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_realtime_log_config_result.CreateRealtimeLogConfigResult,
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
