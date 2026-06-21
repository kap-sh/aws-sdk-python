"""Generated from Smithy shape ``com.amazonaws.route53#ChangeTagsForResource``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_route_53._auth._signers
import aws_sdk_route_53._auth._sigv4
import aws_sdk_route_53.errors.invalid_input
import aws_sdk_route_53.errors.no_such_health_check
import aws_sdk_route_53.errors.no_such_hosted_zone
import aws_sdk_route_53.errors.prior_request_not_complete
import aws_sdk_route_53.errors.throttling_exception
import aws_sdk_route_53.types.change_tags_for_resource_request
import aws_sdk_route_53.types.change_tags_for_resource_response
import aws_sdk_route_53.types.tag_key_list
import aws_sdk_route_53.types.tag_list
import aws_sdk_route_53.types.tag_resource_type
from aws_sdk_route_53._protocol.errors import parse_error_metadata
from aws_sdk_route_53._protocol.xml import Element, fromstring, tostring
from aws_sdk_route_53._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_route_53._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_route_53.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InvalidInput":
            raise aws_sdk_route_53.errors.invalid_input.InvalidInput.from_xml(root)
        case "NoSuchHealthCheck":
            raise aws_sdk_route_53.errors.no_such_health_check.NoSuchHealthCheck.from_xml(
                root
            )
        case "NoSuchHostedZone":
            raise aws_sdk_route_53.errors.no_such_hosted_zone.NoSuchHostedZone.from_xml(
                root
            )
        case "PriorRequestNotComplete":
            raise aws_sdk_route_53.errors.prior_request_not_complete.PriorRequestNotComplete.from_xml(
                root
            )
        case "ThrottlingException":
            raise aws_sdk_route_53.errors.throttling_exception.ThrottlingException.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_route_53.types.change_tags_for_resource_response.ChangeTagsForResourceResponse:
    out: aws_sdk_route_53.types.change_tags_for_resource_response.ChangeTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_route_53.types.change_tags_for_resource_response.ChangeTagsForResourceResponse:
    out: aws_sdk_route_53.types.change_tags_for_resource_response.ChangeTagsForResourceResponse = {}  # type: ignore[typeddict-item]
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
    input_: aws_sdk_route_53.types.change_tags_for_resource_request.ChangeTagsForResourceRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2013-04-01/tags/{ResourceType}/{ResourceId}"
    url = url.replace("{ResourceType}", quote(str(input_["resource_type"]), safe=""))
    url = url.replace("{ResourceId}", quote(str(input_["resource_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    root = Element("ChangeTagsForResourceRequest")
    if "add_tags" in input_:
        import aws_sdk_route_53.types.tag_list

        aws_sdk_route_53.types.tag_list.serialize_xml(
            input_["add_tags"], root, "AddTags"
        )
    if "remove_tag_keys" in input_:
        import aws_sdk_route_53.types.tag_key_list

        aws_sdk_route_53.types.tag_key_list.serialize_xml(
            input_["remove_tag_keys"], root, "RemoveTagKeys"
        )
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def change_tags_for_resource(
    options: OperationOptions,
    input_: aws_sdk_route_53.types.change_tags_for_resource_request.ChangeTagsForResourceRequest,
) -> tuple[
    aws_sdk_route_53.types.change_tags_for_resource_response.ChangeTagsForResourceResponse,
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


async def async_change_tags_for_resource(
    options: AsyncOperationOptions,
    input_: aws_sdk_route_53.types.change_tags_for_resource_request.ChangeTagsForResourceRequest,
) -> tuple[
    aws_sdk_route_53.types.change_tags_for_resource_response.ChangeTagsForResourceResponse,
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
