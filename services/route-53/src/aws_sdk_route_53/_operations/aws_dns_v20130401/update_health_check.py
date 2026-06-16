"""Generated from Smithy shape ``com.amazonaws.route53#UpdateHealthCheck``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any
from urllib.parse import quote

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
    import aws_sdk_route_53.types.update_health_check_request
    import aws_sdk_route_53.types.update_health_check_response


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "HealthCheckVersionMismatch":
            import aws_sdk_route_53.errors.health_check_version_mismatch

            raise aws_sdk_route_53.errors.health_check_version_mismatch.HealthCheckVersionMismatch.from_xml(
                root
            )
        case "InvalidInput":
            import aws_sdk_route_53.errors.invalid_input

            raise aws_sdk_route_53.errors.invalid_input.InvalidInput.from_xml(root)
        case "NoSuchHealthCheck":
            import aws_sdk_route_53.errors.no_such_health_check

            raise aws_sdk_route_53.errors.no_such_health_check.NoSuchHealthCheck.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_route_53.types.update_health_check_response.UpdateHealthCheckResponse:
    import aws_sdk_route_53.types.update_health_check_response

    out: aws_sdk_route_53.types.update_health_check_response.UpdateHealthCheckResponse = aws_sdk_route_53.types.update_health_check_response.deserialize_xml(
        fromstring(response.read())
    )
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
    input_: aws_sdk_route_53.types.update_health_check_request.UpdateHealthCheckRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2013-04-01/healthcheck/{HealthCheckId}"
    url = url.replace("{HealthCheckId}", quote(str(input_["health_check_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    root = Element("UpdateHealthCheckRequest")
    if "health_check_version" in input_:
        SubElement(root, "HealthCheckVersion").text = str(
            input_["health_check_version"]
        )
    if "ip_address" in input_:
        SubElement(root, "IPAddress").text = str(input_["ip_address"])
    if "port" in input_:
        SubElement(root, "Port").text = str(input_["port"])
    if "resource_path" in input_:
        SubElement(root, "ResourcePath").text = str(input_["resource_path"])
    if "fully_qualified_domain_name" in input_:
        SubElement(root, "FullyQualifiedDomainName").text = str(
            input_["fully_qualified_domain_name"]
        )
    if "search_string" in input_:
        SubElement(root, "SearchString").text = str(input_["search_string"])
    if "failure_threshold" in input_:
        SubElement(root, "FailureThreshold").text = str(input_["failure_threshold"])
    if "inverted" in input_:
        SubElement(root, "Inverted").text = str(input_["inverted"])
    if "disabled" in input_:
        SubElement(root, "Disabled").text = str(input_["disabled"])
    if "health_threshold" in input_:
        SubElement(root, "HealthThreshold").text = str(input_["health_threshold"])
    if "child_health_checks" in input_:
        import aws_sdk_route_53.types.child_health_check_list

        aws_sdk_route_53.types.child_health_check_list.serialize_xml(
            input_["child_health_checks"], root, "ChildHealthChecks"
        )
    if "enable_sni" in input_:
        SubElement(root, "EnableSNI").text = str(input_["enable_sni"])
    if "regions" in input_:
        import aws_sdk_route_53.types.health_check_region_list

        aws_sdk_route_53.types.health_check_region_list.serialize_xml(
            input_["regions"], root, "Regions"
        )
    if "alarm_identifier" in input_:
        import aws_sdk_route_53.types.alarm_identifier

        aws_sdk_route_53.types.alarm_identifier.serialize_xml(
            input_["alarm_identifier"], root, "AlarmIdentifier"
        )
    if "insufficient_data_health_status" in input_:
        import aws_sdk_route_53.types.insufficient_data_health_status

        aws_sdk_route_53.types.insufficient_data_health_status.serialize_xml(
            input_["insufficient_data_health_status"],
            root,
            "InsufficientDataHealthStatus",
        )
    if "reset_elements" in input_:
        import aws_sdk_route_53.types.resettable_element_name_list

        aws_sdk_route_53.types.resettable_element_name_list.serialize_xml(
            input_["reset_elements"], root, "ResetElements"
        )
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def update_health_check(
    options: OperationOptions,
    input_: aws_sdk_route_53.types.update_health_check_request.UpdateHealthCheckRequest,
) -> tuple[
    aws_sdk_route_53.types.update_health_check_response.UpdateHealthCheckResponse,
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


async def async_update_health_check(
    options: AsyncOperationOptions,
    input_: aws_sdk_route_53.types.update_health_check_request.UpdateHealthCheckRequest,
) -> tuple[
    aws_sdk_route_53.types.update_health_check_response.UpdateHealthCheckResponse,
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
