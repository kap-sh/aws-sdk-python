"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDomainConflicts``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudfront._auth._signers
import capo_cloudfront._auth._sigv4
import capo_cloudfront.errors.access_denied
import capo_cloudfront.errors.entity_not_found
import capo_cloudfront.errors.invalid_argument
import capo_cloudfront.types.distribution_resource_id
import capo_cloudfront.types.domain_conflicts_list
import capo_cloudfront.types.list_domain_conflicts_request
import capo_cloudfront.types.list_domain_conflicts_result
from capo_cloudfront._protocol.errors import parse_error_metadata
from capo_cloudfront._protocol.xml import Element, SubElement, fromstring, tostring
from capo_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudfront._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_cloudfront.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AccessDenied":
            raise capo_cloudfront.errors.access_denied.AccessDenied.from_xml(root)
        case "EntityNotFound":
            raise capo_cloudfront.errors.entity_not_found.EntityNotFound.from_xml(root)
        case "InvalidArgument":
            raise capo_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(root)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.list_domain_conflicts_result.ListDomainConflictsResult:
    out: capo_cloudfront.types.list_domain_conflicts_result.ListDomainConflictsResult = capo_cloudfront.types.list_domain_conflicts_result.deserialize_xml(
        fromstring(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.list_domain_conflicts_result.ListDomainConflictsResult:
    out: capo_cloudfront.types.list_domain_conflicts_result.ListDomainConflictsResult = capo_cloudfront.types.list_domain_conflicts_result.deserialize_xml(
        fromstring(await response.aread())
    )
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
    input_: capo_cloudfront.types.list_domain_conflicts_request.ListDomainConflictsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/domain-conflicts"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    root = Element("ListDomainConflictsRequest")
    if "domain" in input_:
        SubElement(root, "Domain").text = str(input_["domain"])
    if "domain_control_validation_resource" in input_:
        capo_cloudfront.types.distribution_resource_id.serialize_xml(
            input_["domain_control_validation_resource"],
            root,
            "DomainControlValidationResource",
        )
    if "max_items" in input_:
        SubElement(root, "MaxItems").text = str(input_["max_items"])
    if "marker" in input_:
        SubElement(root, "Marker").text = str(input_["marker"])
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def list_domain_conflicts(
    options: OperationOptions,
    input_: capo_cloudfront.types.list_domain_conflicts_request.ListDomainConflictsRequest,
) -> tuple[
    capo_cloudfront.types.list_domain_conflicts_result.ListDomainConflictsResult,
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


async def async_list_domain_conflicts(
    options: AsyncOperationOptions,
    input_: capo_cloudfront.types.list_domain_conflicts_request.ListDomainConflictsRequest,
) -> tuple[
    capo_cloudfront.types.list_domain_conflicts_result.ListDomainConflictsResult,
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
