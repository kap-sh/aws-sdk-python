"""Generated from Smithy shape ``com.amazonaws.route53#CreateQueryLoggingConfig``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_route_53._auth._signers
import aws_sdk_route_53._auth._sigv4
from aws_sdk_route_53._protocol.errors import parse_error_metadata
from aws_sdk_route_53._protocol.xml import Element, SubElement, fromstring, tostring
from aws_sdk_route_53._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_route_53._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_route_53.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.create_query_logging_config_request
    import aws_sdk_route_53.types.create_query_logging_config_response


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "ConcurrentModification":
            import aws_sdk_route_53.errors.concurrent_modification

            raise aws_sdk_route_53.errors.concurrent_modification.ConcurrentModification.from_xml(
                root
            )
        case "InsufficientCloudWatchLogsResourcePolicy":
            import aws_sdk_route_53.errors.insufficient_cloud_watch_logs_resource_policy

            raise aws_sdk_route_53.errors.insufficient_cloud_watch_logs_resource_policy.InsufficientCloudWatchLogsResourcePolicy.from_xml(
                root
            )
        case "InvalidInput":
            import aws_sdk_route_53.errors.invalid_input

            raise aws_sdk_route_53.errors.invalid_input.InvalidInput.from_xml(root)
        case "NoSuchCloudWatchLogsLogGroup":
            import aws_sdk_route_53.errors.no_such_cloud_watch_logs_log_group

            raise aws_sdk_route_53.errors.no_such_cloud_watch_logs_log_group.NoSuchCloudWatchLogsLogGroup.from_xml(
                root
            )
        case "NoSuchHostedZone":
            import aws_sdk_route_53.errors.no_such_hosted_zone

            raise aws_sdk_route_53.errors.no_such_hosted_zone.NoSuchHostedZone.from_xml(
                root
            )
        case "QueryLoggingConfigAlreadyExists":
            import aws_sdk_route_53.errors.query_logging_config_already_exists

            raise aws_sdk_route_53.errors.query_logging_config_already_exists.QueryLoggingConfigAlreadyExists.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_route_53.types.create_query_logging_config_response.CreateQueryLoggingConfigResponse:
    import aws_sdk_route_53.types.create_query_logging_config_response

    out: aws_sdk_route_53.types.create_query_logging_config_response.CreateQueryLoggingConfigResponse = aws_sdk_route_53.types.create_query_logging_config_response.deserialize_xml(
        fromstring(response.read())
    )
    out["location"] = str(response.headers["Location"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_route_53._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_route_53._auth._sigv4.build_sigv4_auth_scheme(
                "route53", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_route_53._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_route_53.types.create_query_logging_config_request.CreateQueryLoggingConfigRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2013-04-01/queryloggingconfig"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    root = Element("CreateQueryLoggingConfigRequest")
    if "hosted_zone_id" in input_:
        SubElement(root, "HostedZoneId").text = str(input_["hosted_zone_id"])
    if "cloud_watch_logs_log_group_arn" in input_:
        SubElement(root, "CloudWatchLogsLogGroupArn").text = str(
            input_["cloud_watch_logs_log_group_arn"]
        )
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_query_logging_config(
    options: OperationOptions,
    input_: aws_sdk_route_53.types.create_query_logging_config_request.CreateQueryLoggingConfigRequest,
) -> tuple[
    aws_sdk_route_53.types.create_query_logging_config_response.CreateQueryLoggingConfigResponse,
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


async def async_create_query_logging_config(
    options: AsyncOperationOptions,
    input_: aws_sdk_route_53.types.create_query_logging_config_request.CreateQueryLoggingConfigRequest,
) -> tuple[
    aws_sdk_route_53.types.create_query_logging_config_response.CreateQueryLoggingConfigResponse,
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
