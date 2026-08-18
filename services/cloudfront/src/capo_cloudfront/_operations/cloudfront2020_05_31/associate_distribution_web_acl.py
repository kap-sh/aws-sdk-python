"""Generated from Smithy shape ``com.amazonaws.cloudfront#AssociateDistributionWebACL``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_cloudfront._auth._signers
import capo_cloudfront._auth._sigv4
import capo_cloudfront._protocol.eventstream
import capo_cloudfront.errors.access_denied
import capo_cloudfront.errors.entity_limit_exceeded
import capo_cloudfront.errors.entity_not_found
import capo_cloudfront.errors.invalid_argument
import capo_cloudfront.errors.invalid_if_match_version
import capo_cloudfront.errors.precondition_failed
import capo_cloudfront.types.associate_distribution_web_acl_request
import capo_cloudfront.types.associate_distribution_web_acl_result
from capo_cloudfront._protocol.errors import find_error_element, parse_error_metadata
from capo_cloudfront._protocol.xml import Element, SubElement, fromstring, tostring
from capo_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudfront._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_cloudfront.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "AccessDenied":
            raise capo_cloudfront.errors.access_denied.AccessDenied.from_xml(
                error_el, message
            )
        case "EntityLimitExceeded":
            raise capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded.from_xml(
                error_el, message
            )
        case "EntityNotFound":
            raise capo_cloudfront.errors.entity_not_found.EntityNotFound.from_xml(
                error_el, message
            )
        case "InvalidArgument":
            raise capo_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                error_el, message
            )
        case "InvalidIfMatchVersion":
            raise capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion.from_xml(
                error_el, message
            )
        case "PreconditionFailed":
            raise capo_cloudfront.errors.precondition_failed.PreconditionFailed.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.associate_distribution_web_acl_result.AssociateDistributionWebACLResult:
    out: capo_cloudfront.types.associate_distribution_web_acl_result.AssociateDistributionWebACLResult = capo_cloudfront.types.associate_distribution_web_acl_result.deserialize_xml(
        fromstring(response.read())
    )
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.associate_distribution_web_acl_result.AssociateDistributionWebACLResult:
    out: capo_cloudfront.types.associate_distribution_web_acl_result.AssociateDistributionWebACLResult = capo_cloudfront.types.associate_distribution_web_acl_result.deserialize_xml(
        fromstring(await response.aread())
    )
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudfront._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_cloudfront._auth._sigv4.build_sigv4_auth_scheme(
                "cloudfront", options.region
            )
        )
        if sigv4_config is not None:
            return capo_cloudfront._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudfront.types.associate_distribution_web_acl_request.AssociateDistributionWebACLRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/distribution/{Id}/associate-web-acl"
    url = url.replace("{Id}", quote(input_["id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "if_match" in input_:
        headers["If-Match"] = input_["if_match"]
    root = Element("AssociateDistributionWebACLRequest")
    if "web_acl_arn" in input_:
        SubElement(root, "WebACLArn").text = input_["web_acl_arn"]
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def associate_distribution_web_acl(
    options: OperationOptions,
    input_: capo_cloudfront.types.associate_distribution_web_acl_request.AssociateDistributionWebACLRequest,
) -> tuple[
    capo_cloudfront.types.associate_distribution_web_acl_result.AssociateDistributionWebACLResult,
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


async def async_associate_distribution_web_acl(
    options: AsyncOperationOptions,
    input_: capo_cloudfront.types.associate_distribution_web_acl_request.AssociateDistributionWebACLRequest,
) -> tuple[
    capo_cloudfront.types.associate_distribution_web_acl_result.AssociateDistributionWebACLResult,
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
