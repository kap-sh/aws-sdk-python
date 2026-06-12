"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteCloudFrontOriginAccessIdentity``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_cloudfront._auth._signers
import aws_sdk_cloudfront._auth._sigv4
from aws_sdk_cloudfront._protocol.errors import parse_error_metadata
from aws_sdk_cloudfront._protocol.xml import fromstring
from aws_sdk_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloudfront._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudfront.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.delete_cloud_front_origin_access_identity_request


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AccessDenied":
            import aws_sdk_cloudfront.errors.access_denied

            raise aws_sdk_cloudfront.errors.access_denied.AccessDenied.from_xml(root)
        case "CloudFrontOriginAccessIdentityInUse":
            import aws_sdk_cloudfront.errors.cloud_front_origin_access_identity_in_use

            raise aws_sdk_cloudfront.errors.cloud_front_origin_access_identity_in_use.CloudFrontOriginAccessIdentityInUse.from_xml(
                root
            )
        case "InvalidIfMatchVersion":
            import aws_sdk_cloudfront.errors.invalid_if_match_version

            raise aws_sdk_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion.from_xml(
                root
            )
        case "NoSuchCloudFrontOriginAccessIdentity":
            import aws_sdk_cloudfront.errors.no_such_cloud_front_origin_access_identity

            raise aws_sdk_cloudfront.errors.no_such_cloud_front_origin_access_identity.NoSuchCloudFrontOriginAccessIdentity.from_xml(
                root
            )
        case "PreconditionFailed":
            import aws_sdk_cloudfront.errors.precondition_failed

            raise aws_sdk_cloudfront.errors.precondition_failed.PreconditionFailed.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloudfront._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
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
    input: aws_sdk_cloudfront.types.delete_cloud_front_origin_access_identity_request.DeleteCloudFrontOriginAccessIdentityRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )
    url = (
        endpoint.url.rstrip("/") + "/2020-05-31/origin-access-identity/cloudfront/{Id}"
    )
    url = url.replace("{Id}", quote(str(input["id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "if_match" in input:
        headers["If-Match"] = str(input["if_match"])
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "DELETE",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def delete_cloud_front_origin_access_identity(
    options: OperationOptions,
    input: aws_sdk_cloudfront.types.delete_cloud_front_origin_access_identity_request.DeleteCloudFrontOriginAccessIdentityRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_delete_cloud_front_origin_access_identity(
    options: AsyncOperationOptions,
    input: aws_sdk_cloudfront.types.delete_cloud_front_origin_access_identity_request.DeleteCloudFrontOriginAccessIdentityRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
