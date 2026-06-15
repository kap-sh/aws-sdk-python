"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetResourcePolicy``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never

import zapros

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
    import aws_sdk_cloudfront.types.get_resource_policy_request
    import aws_sdk_cloudfront.types.get_resource_policy_result


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AccessDenied":
            import aws_sdk_cloudfront.errors.access_denied

            raise aws_sdk_cloudfront.errors.access_denied.AccessDenied.from_xml(root)
        case "EntityNotFound":
            import aws_sdk_cloudfront.errors.entity_not_found

            raise aws_sdk_cloudfront.errors.entity_not_found.EntityNotFound.from_xml(
                root
            )
        case "InvalidArgument":
            import aws_sdk_cloudfront.errors.invalid_argument

            raise aws_sdk_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                root
            )
        case "UnsupportedOperation":
            import aws_sdk_cloudfront.errors.unsupported_operation

            raise aws_sdk_cloudfront.errors.unsupported_operation.UnsupportedOperation.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cloudfront.types.get_resource_policy_result.GetResourcePolicyResult:
    import aws_sdk_cloudfront.types.get_resource_policy_result

    out: aws_sdk_cloudfront.types.get_resource_policy_result.GetResourcePolicyResult = (
        aws_sdk_cloudfront.types.get_resource_policy_result.deserialize_xml(
            fromstring(response.read())
        )
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
    input_: aws_sdk_cloudfront.types.get_resource_policy_request.GetResourcePolicyRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/get-resource-policy"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    root = Element("GetResourcePolicyRequest")
    if "resource_arn" in input_:
        SubElement(root, "ResourceArn").text = str(input_["resource_arn"])
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def get_resource_policy(
    options: OperationOptions,
    input_: aws_sdk_cloudfront.types.get_resource_policy_request.GetResourcePolicyRequest,
) -> tuple[
    aws_sdk_cloudfront.types.get_resource_policy_result.GetResourcePolicyResult,
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


async def async_get_resource_policy(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudfront.types.get_resource_policy_request.GetResourcePolicyRequest,
) -> tuple[
    aws_sdk_cloudfront.types.get_resource_policy_result.GetResourcePolicyResult,
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
