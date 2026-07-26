"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetOriginRequestPolicy``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_cloudfront._auth._signers
import capo_cloudfront._auth._sigv4
import capo_cloudfront.errors.access_denied
import capo_cloudfront.errors.no_such_origin_request_policy
import capo_cloudfront.types.get_origin_request_policy_request
import capo_cloudfront.types.get_origin_request_policy_result
import capo_cloudfront.types.origin_request_policy
from capo_cloudfront._protocol.errors import parse_error_metadata
from capo_cloudfront._protocol.xml import fromstring
from capo_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudfront._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_cloudfront.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AccessDenied":
            raise capo_cloudfront.errors.access_denied.AccessDenied.from_xml(root)
        case "NoSuchOriginRequestPolicy":
            raise capo_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    capo_cloudfront.types.get_origin_request_policy_result.GetOriginRequestPolicyResult
):
    out: capo_cloudfront.types.get_origin_request_policy_result.GetOriginRequestPolicyResult = {
        "origin_request_policy": capo_cloudfront.types.origin_request_policy.deserialize_xml(
            fromstring(response.read())
        )
    }  # type: ignore[typeddict-item]
    if "ETag" in response.headers:
        out["e_tag"] = str(response.headers["ETag"])
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    capo_cloudfront.types.get_origin_request_policy_result.GetOriginRequestPolicyResult
):
    out: capo_cloudfront.types.get_origin_request_policy_result.GetOriginRequestPolicyResult = {
        "origin_request_policy": capo_cloudfront.types.origin_request_policy.deserialize_xml(
            fromstring(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    if "ETag" in response.headers:
        out["e_tag"] = str(response.headers["ETag"])
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
    input_: capo_cloudfront.types.get_origin_request_policy_request.GetOriginRequestPolicyRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/origin-request-policy/{Id}"
    url = url.replace("{Id}", quote(str(input_["id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_origin_request_policy(
    options: OperationOptions,
    input_: capo_cloudfront.types.get_origin_request_policy_request.GetOriginRequestPolicyRequest,
) -> tuple[
    capo_cloudfront.types.get_origin_request_policy_result.GetOriginRequestPolicyResult,
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


async def async_get_origin_request_policy(
    options: AsyncOperationOptions,
    input_: capo_cloudfront.types.get_origin_request_policy_request.GetOriginRequestPolicyRequest,
) -> tuple[
    capo_cloudfront.types.get_origin_request_policy_result.GetOriginRequestPolicyResult,
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
