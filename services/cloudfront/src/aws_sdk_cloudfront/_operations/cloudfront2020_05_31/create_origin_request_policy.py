"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateOriginRequestPolicy``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_cloudfront._auth._signers
import aws_sdk_cloudfront._auth._sigv4
import aws_sdk_cloudfront.errors.access_denied
import aws_sdk_cloudfront.errors.inconsistent_quantities
import aws_sdk_cloudfront.errors.invalid_argument
import aws_sdk_cloudfront.errors.origin_request_policy_already_exists
import aws_sdk_cloudfront.errors.too_many_cookies_in_origin_request_policy
import aws_sdk_cloudfront.errors.too_many_headers_in_origin_request_policy
import aws_sdk_cloudfront.errors.too_many_origin_request_policies
import aws_sdk_cloudfront.errors.too_many_query_strings_in_origin_request_policy
import aws_sdk_cloudfront.types.create_origin_request_policy_request
import aws_sdk_cloudfront.types.create_origin_request_policy_result
import aws_sdk_cloudfront.types.origin_request_policy
import aws_sdk_cloudfront.types.origin_request_policy_config
from aws_sdk_cloudfront._protocol.errors import parse_error_metadata
from aws_sdk_cloudfront._protocol.xml import Element, fromstring, tostring
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
        case "InconsistentQuantities":
            raise aws_sdk_cloudfront.errors.inconsistent_quantities.InconsistentQuantities.from_xml(
                root
            )
        case "InvalidArgument":
            raise aws_sdk_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                root
            )
        case "OriginRequestPolicyAlreadyExists":
            raise aws_sdk_cloudfront.errors.origin_request_policy_already_exists.OriginRequestPolicyAlreadyExists.from_xml(
                root
            )
        case "TooManyCookiesInOriginRequestPolicy":
            raise aws_sdk_cloudfront.errors.too_many_cookies_in_origin_request_policy.TooManyCookiesInOriginRequestPolicy.from_xml(
                root
            )
        case "TooManyHeadersInOriginRequestPolicy":
            raise aws_sdk_cloudfront.errors.too_many_headers_in_origin_request_policy.TooManyHeadersInOriginRequestPolicy.from_xml(
                root
            )
        case "TooManyOriginRequestPolicies":
            raise aws_sdk_cloudfront.errors.too_many_origin_request_policies.TooManyOriginRequestPolicies.from_xml(
                root
            )
        case "TooManyQueryStringsInOriginRequestPolicy":
            raise aws_sdk_cloudfront.errors.too_many_query_strings_in_origin_request_policy.TooManyQueryStringsInOriginRequestPolicy.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult:
    out: aws_sdk_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult = {
        "origin_request_policy": aws_sdk_cloudfront.types.origin_request_policy.deserialize_xml(
            fromstring(response.read())
        )
    }  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = str(response.headers["Location"])
    if "ETag" in response.headers:
        out["e_tag"] = str(response.headers["ETag"])
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult:
    out: aws_sdk_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult = {
        "origin_request_policy": aws_sdk_cloudfront.types.origin_request_policy.deserialize_xml(
            fromstring(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = str(response.headers["Location"])
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
    input_: aws_sdk_cloudfront.types.create_origin_request_policy_request.CreateOriginRequestPolicyRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/origin-request-policy"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "origin_request_policy_config" in input_:
        import aws_sdk_cloudfront.types.origin_request_policy_config

        payload_root = Element("_")
        aws_sdk_cloudfront.types.origin_request_policy_config.serialize_xml(
            input_["origin_request_policy_config"],
            payload_root,
            "OriginRequestPolicyConfig",
        )
        body: bytes | None = tostring(payload_root[0])
        headers["content-type"] = "application/xml"
    else:
        body = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_origin_request_policy(
    options: OperationOptions,
    input_: aws_sdk_cloudfront.types.create_origin_request_policy_request.CreateOriginRequestPolicyRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult,
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


async def async_create_origin_request_policy(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudfront.types.create_origin_request_policy_request.CreateOriginRequestPolicyRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult,
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
