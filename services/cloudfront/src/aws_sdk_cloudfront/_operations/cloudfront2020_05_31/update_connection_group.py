"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateConnectionGroup``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_cloudfront._auth._signers
import aws_sdk_cloudfront._auth._sigv4
import aws_sdk_cloudfront.errors.access_denied
import aws_sdk_cloudfront.errors.entity_already_exists
import aws_sdk_cloudfront.errors.entity_limit_exceeded
import aws_sdk_cloudfront.errors.entity_not_found
import aws_sdk_cloudfront.errors.invalid_argument
import aws_sdk_cloudfront.errors.invalid_if_match_version
import aws_sdk_cloudfront.errors.precondition_failed
import aws_sdk_cloudfront.errors.resource_in_use
import aws_sdk_cloudfront.types.connection_group
import aws_sdk_cloudfront.types.update_connection_group_request
import aws_sdk_cloudfront.types.update_connection_group_result
from aws_sdk_cloudfront._protocol.errors import parse_error_metadata
from aws_sdk_cloudfront._protocol.xml import Element, SubElement, fromstring, tostring
from aws_sdk_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloudfront._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudfront.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AccessDenied":
            raise aws_sdk_cloudfront.errors.access_denied.AccessDenied.from_xml(root)
        case "EntityAlreadyExists":
            raise aws_sdk_cloudfront.errors.entity_already_exists.EntityAlreadyExists.from_xml(
                root
            )
        case "EntityLimitExceeded":
            raise aws_sdk_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded.from_xml(
                root
            )
        case "EntityNotFound":
            raise aws_sdk_cloudfront.errors.entity_not_found.EntityNotFound.from_xml(
                root
            )
        case "InvalidArgument":
            raise aws_sdk_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                root
            )
        case "InvalidIfMatchVersion":
            raise aws_sdk_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion.from_xml(
                root
            )
        case "PreconditionFailed":
            raise aws_sdk_cloudfront.errors.precondition_failed.PreconditionFailed.from_xml(
                root
            )
        case "ResourceInUse":
            raise aws_sdk_cloudfront.errors.resource_in_use.ResourceInUse.from_xml(root)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_cloudfront.types.update_connection_group_result.UpdateConnectionGroupResult
):
    out: aws_sdk_cloudfront.types.update_connection_group_result.UpdateConnectionGroupResult = {
        "connection_group": aws_sdk_cloudfront.types.connection_group.deserialize_xml(
            fromstring(response.read())
        )
    }  # type: ignore[typeddict-item]
    if "ETag" in response.headers:
        out["e_tag"] = str(response.headers["ETag"])
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_cloudfront.types.update_connection_group_result.UpdateConnectionGroupResult
):
    out: aws_sdk_cloudfront.types.update_connection_group_result.UpdateConnectionGroupResult = {
        "connection_group": aws_sdk_cloudfront.types.connection_group.deserialize_xml(
            fromstring(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    if "ETag" in response.headers:
        out["e_tag"] = str(response.headers["ETag"])
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
    input_: aws_sdk_cloudfront.types.update_connection_group_request.UpdateConnectionGroupRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/connection-group/{Id}"
    url = url.replace("{Id}", quote(str(input_["id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "if_match" in input_:
        headers["If-Match"] = str(input_["if_match"])
    root = Element("UpdateConnectionGroupRequest")
    if "ipv6_enabled" in input_:
        SubElement(root, "Ipv6Enabled").text = str(input_["ipv6_enabled"])
    if "anycast_ip_list_id" in input_:
        SubElement(root, "AnycastIpListId").text = str(input_["anycast_ip_list_id"])
    if "enabled" in input_:
        SubElement(root, "Enabled").text = str(input_["enabled"])
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def update_connection_group(
    options: OperationOptions,
    input_: aws_sdk_cloudfront.types.update_connection_group_request.UpdateConnectionGroupRequest,
) -> tuple[
    aws_sdk_cloudfront.types.update_connection_group_result.UpdateConnectionGroupResult,
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


async def async_update_connection_group(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudfront.types.update_connection_group_request.UpdateConnectionGroupRequest,
) -> tuple[
    aws_sdk_cloudfront.types.update_connection_group_result.UpdateConnectionGroupResult,
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
