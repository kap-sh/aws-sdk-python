"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateTrustStore``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_cloudfront._auth._signers
import aws_sdk_cloudfront._auth._sigv4
import aws_sdk_cloudfront.errors.access_denied
import aws_sdk_cloudfront.errors.entity_already_exists
import aws_sdk_cloudfront.errors.entity_limit_exceeded
import aws_sdk_cloudfront.errors.entity_not_found
import aws_sdk_cloudfront.errors.invalid_argument
import aws_sdk_cloudfront.errors.invalid_tagging
import aws_sdk_cloudfront.types.ca_certificates_bundle_source
import aws_sdk_cloudfront.types.create_trust_store_request
import aws_sdk_cloudfront.types.create_trust_store_result
import aws_sdk_cloudfront.types.tags
import aws_sdk_cloudfront.types.trust_store
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
        case "InvalidTagging":
            raise aws_sdk_cloudfront.errors.invalid_tagging.InvalidTagging.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_cloudfront.types.create_trust_store_result.CreateTrustStoreResult:
    out: aws_sdk_cloudfront.types.create_trust_store_result.CreateTrustStoreResult = {
        "trust_store": aws_sdk_cloudfront.types.trust_store.deserialize_xml(
            fromstring(response.read())
        )
    }  # type: ignore[typeddict-item]
    if "ETag" in response.headers:
        out["e_tag"] = str(response.headers["ETag"])
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_cloudfront.types.create_trust_store_result.CreateTrustStoreResult:
    out: aws_sdk_cloudfront.types.create_trust_store_result.CreateTrustStoreResult = {
        "trust_store": aws_sdk_cloudfront.types.trust_store.deserialize_xml(
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
    input_: aws_sdk_cloudfront.types.create_trust_store_request.CreateTrustStoreRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/trust-store"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    root = Element("CreateTrustStoreRequest")
    if "name" in input_:
        SubElement(root, "Name").text = str(input_["name"])
    if "ca_certificates_bundle_source" in input_:
        import aws_sdk_cloudfront.types.ca_certificates_bundle_source

        aws_sdk_cloudfront.types.ca_certificates_bundle_source.serialize_xml(
            input_["ca_certificates_bundle_source"], root, "CaCertificatesBundleSource"
        )
    if "use_client_certificate_ocsp_endpoint" in input_:
        SubElement(root, "UseClientCertificateOCSPEndpoint").text = str(
            input_["use_client_certificate_ocsp_endpoint"]
        )
    if "tags" in input_:
        import aws_sdk_cloudfront.types.tags

        aws_sdk_cloudfront.types.tags.serialize_xml(input_["tags"], root, "Tags")
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_trust_store(
    options: OperationOptions,
    input_: aws_sdk_cloudfront.types.create_trust_store_request.CreateTrustStoreRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_trust_store_result.CreateTrustStoreResult,
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


async def async_create_trust_store(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudfront.types.create_trust_store_request.CreateTrustStoreRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_trust_store_result.CreateTrustStoreResult,
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
