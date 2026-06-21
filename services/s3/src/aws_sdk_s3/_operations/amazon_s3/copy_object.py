"""Generated from Smithy shape ``com.amazonaws.s3#CopyObject``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_s3._auth._signers
import aws_sdk_s3._auth._sigv4
import aws_sdk_s3._protocol.eventstream
import aws_sdk_s3.errors.object_not_in_active_tier_error
import aws_sdk_s3.types.checksum_algorithm
import aws_sdk_s3.types.copy_object_output
import aws_sdk_s3.types.copy_object_request
import aws_sdk_s3.types.copy_object_result
import aws_sdk_s3.types.copy_source_if_modified_since
import aws_sdk_s3.types.copy_source_if_unmodified_since
import aws_sdk_s3.types.metadata
import aws_sdk_s3.types.metadata_directive
import aws_sdk_s3.types.object_canned_acl
import aws_sdk_s3.types.object_lock_legal_hold_status
import aws_sdk_s3.types.object_lock_mode
import aws_sdk_s3.types.object_lock_retain_until_date
import aws_sdk_s3.types.request_charged
import aws_sdk_s3.types.request_payer
import aws_sdk_s3.types.server_side_encryption
import aws_sdk_s3.types.storage_class
import aws_sdk_s3.types.tagging_directive
from aws_sdk_s3._protocol.errors import parse_error_metadata
from aws_sdk_s3._protocol.xml import fromstring
from aws_sdk_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3._rule_engine._endpoint_runtime import apply_label
from aws_sdk_s3._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_s3.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "ObjectNotInActiveTierError":
            raise aws_sdk_s3.errors.object_not_in_active_tier_error.ObjectNotInActiveTierError.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_s3.types.copy_object_output.CopyObjectOutput:
    out: aws_sdk_s3.types.copy_object_output.CopyObjectOutput = {
        "copy_object_result": aws_sdk_s3.types.copy_object_result.deserialize_xml(
            fromstring(response.read())
        )
    }  # type: ignore[typeddict-item]
    if "x-amz-expiration" in response.headers:
        out["expiration"] = str(response.headers["x-amz-expiration"])
    if "x-amz-copy-source-version-id" in response.headers:
        out["copy_source_version_id"] = str(
            response.headers["x-amz-copy-source-version-id"]
        )
    if "x-amz-version-id" in response.headers:
        out["version_id"] = str(response.headers["x-amz-version-id"])
    if "x-amz-server-side-encryption" in response.headers:
        out["server_side_encryption"] = (
            aws_sdk_s3.types.server_side_encryption.from_xml_text(
                response.headers["x-amz-server-side-encryption"]
            )
        )
    if "x-amz-server-side-encryption-customer-algorithm" in response.headers:
        out["sse_customer_algorithm"] = str(
            response.headers["x-amz-server-side-encryption-customer-algorithm"]
        )
    if "x-amz-server-side-encryption-customer-key-MD5" in response.headers:
        out["sse_customer_key_md5"] = str(
            response.headers["x-amz-server-side-encryption-customer-key-MD5"]
        )
    if "x-amz-server-side-encryption-aws-kms-key-id" in response.headers:
        out["ssekms_key_id"] = str(
            response.headers["x-amz-server-side-encryption-aws-kms-key-id"]
        )
    if "x-amz-server-side-encryption-context" in response.headers:
        out["ssekms_encryption_context"] = str(
            response.headers["x-amz-server-side-encryption-context"]
        )
    if "x-amz-server-side-encryption-bucket-key-enabled" in response.headers:
        out["bucket_key_enabled"] = (
            response.headers["x-amz-server-side-encryption-bucket-key-enabled"].lower()
            == "true"
        )
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = aws_sdk_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_s3.types.copy_object_output.CopyObjectOutput:
    out: aws_sdk_s3.types.copy_object_output.CopyObjectOutput = {
        "copy_object_result": aws_sdk_s3.types.copy_object_result.deserialize_xml(
            fromstring(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    if "x-amz-expiration" in response.headers:
        out["expiration"] = str(response.headers["x-amz-expiration"])
    if "x-amz-copy-source-version-id" in response.headers:
        out["copy_source_version_id"] = str(
            response.headers["x-amz-copy-source-version-id"]
        )
    if "x-amz-version-id" in response.headers:
        out["version_id"] = str(response.headers["x-amz-version-id"])
    if "x-amz-server-side-encryption" in response.headers:
        out["server_side_encryption"] = (
            aws_sdk_s3.types.server_side_encryption.from_xml_text(
                response.headers["x-amz-server-side-encryption"]
            )
        )
    if "x-amz-server-side-encryption-customer-algorithm" in response.headers:
        out["sse_customer_algorithm"] = str(
            response.headers["x-amz-server-side-encryption-customer-algorithm"]
        )
    if "x-amz-server-side-encryption-customer-key-MD5" in response.headers:
        out["sse_customer_key_md5"] = str(
            response.headers["x-amz-server-side-encryption-customer-key-MD5"]
        )
    if "x-amz-server-side-encryption-aws-kms-key-id" in response.headers:
        out["ssekms_key_id"] = str(
            response.headers["x-amz-server-side-encryption-aws-kms-key-id"]
        )
    if "x-amz-server-side-encryption-context" in response.headers:
        out["ssekms_encryption_context"] = str(
            response.headers["x-amz-server-side-encryption-context"]
        )
    if "x-amz-server-side-encryption-bucket-key-enabled" in response.headers:
        out["bucket_key_enabled"] = (
            response.headers["x-amz-server-side-encryption-bucket-key-enabled"].lower()
            == "true"
        )
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = aws_sdk_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_s3._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_s3._auth._sigv4.build_sigv4_auth_scheme("s3", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_s3._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_s3.types.copy_object_request.CopyObjectRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Bucket=input_.get("bucket"),
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
            ForcePathStyle=options.force_path_style,
            Accelerate=options.accelerate,
            UseGlobalEndpoint=options.use_global_endpoint,
            UseObjectLambdaEndpoint=options.use_object_lambda_endpoint,
            Key=input_.get("key"),
            Prefix=options.prefix,
            CopySource=input_.get("copy_source"),
            DisableAccessPoints=options.disable_access_points,
            DisableMultiRegionAccessPoints=options.disable_multi_region_access_points,
            UseArnRegion=options.use_arn_region,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
            DisableS3ExpressSessionAuth=True,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/{Bucket}/{Key+}?x-id=CopyObject"
    url = apply_label(url, "{Bucket}", str(input_["bucket"]))
    url = url.replace("{Key+}", quote(str(input_["key"]), safe="/"))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "acl" in input_:
        headers["x-amz-acl"] = str(input_["acl"])
    if "cache_control" in input_:
        headers["Cache-Control"] = str(input_["cache_control"])
    if "checksum_algorithm" in input_:
        headers["x-amz-checksum-algorithm"] = str(input_["checksum_algorithm"])
    if "content_disposition" in input_:
        headers["Content-Disposition"] = str(input_["content_disposition"])
    if "content_encoding" in input_:
        headers["Content-Encoding"] = str(input_["content_encoding"])
    if "content_language" in input_:
        headers["Content-Language"] = str(input_["content_language"])
    if "content_type" in input_:
        headers["Content-Type"] = str(input_["content_type"])
    if "copy_source" in input_:
        headers["x-amz-copy-source"] = str(input_["copy_source"])
    if "copy_source_if_match" in input_:
        headers["x-amz-copy-source-if-match"] = str(input_["copy_source_if_match"])
    if "copy_source_if_modified_since" in input_:
        headers["x-amz-copy-source-if-modified-since"] = str(
            input_["copy_source_if_modified_since"]
        )
    if "copy_source_if_none_match" in input_:
        headers["x-amz-copy-source-if-none-match"] = str(
            input_["copy_source_if_none_match"]
        )
    if "copy_source_if_unmodified_since" in input_:
        headers["x-amz-copy-source-if-unmodified-since"] = str(
            input_["copy_source_if_unmodified_since"]
        )
    if "expires" in input_:
        headers["Expires"] = str(input_["expires"])
    if "grant_full_control" in input_:
        headers["x-amz-grant-full-control"] = str(input_["grant_full_control"])
    if "grant_read" in input_:
        headers["x-amz-grant-read"] = str(input_["grant_read"])
    if "grant_read_acp" in input_:
        headers["x-amz-grant-read-acp"] = str(input_["grant_read_acp"])
    if "grant_write_acp" in input_:
        headers["x-amz-grant-write-acp"] = str(input_["grant_write_acp"])
    if "if_match" in input_:
        headers["If-Match"] = str(input_["if_match"])
    if "if_none_match" in input_:
        headers["If-None-Match"] = str(input_["if_none_match"])
    if "metadata_directive" in input_:
        headers["x-amz-metadata-directive"] = str(input_["metadata_directive"])
    if "tagging_directive" in input_:
        headers["x-amz-tagging-directive"] = str(input_["tagging_directive"])
    if "server_side_encryption" in input_:
        headers["x-amz-server-side-encryption"] = str(input_["server_side_encryption"])
    if "storage_class" in input_:
        headers["x-amz-storage-class"] = str(input_["storage_class"])
    if "website_redirect_location" in input_:
        headers["x-amz-website-redirect-location"] = str(
            input_["website_redirect_location"]
        )
    if "sse_customer_algorithm" in input_:
        headers["x-amz-server-side-encryption-customer-algorithm"] = str(
            input_["sse_customer_algorithm"]
        )
    if "sse_customer_key" in input_:
        headers["x-amz-server-side-encryption-customer-key"] = str(
            input_["sse_customer_key"]
        )
    if "sse_customer_key_md5" in input_:
        headers["x-amz-server-side-encryption-customer-key-MD5"] = str(
            input_["sse_customer_key_md5"]
        )
    if "ssekms_key_id" in input_:
        headers["x-amz-server-side-encryption-aws-kms-key-id"] = str(
            input_["ssekms_key_id"]
        )
    if "ssekms_encryption_context" in input_:
        headers["x-amz-server-side-encryption-context"] = str(
            input_["ssekms_encryption_context"]
        )
    if "bucket_key_enabled" in input_:
        headers["x-amz-server-side-encryption-bucket-key-enabled"] = str(
            input_["bucket_key_enabled"]
        )
    if "copy_source_sse_customer_algorithm" in input_:
        headers["x-amz-copy-source-server-side-encryption-customer-algorithm"] = str(
            input_["copy_source_sse_customer_algorithm"]
        )
    if "copy_source_sse_customer_key" in input_:
        headers["x-amz-copy-source-server-side-encryption-customer-key"] = str(
            input_["copy_source_sse_customer_key"]
        )
    if "copy_source_sse_customer_key_md5" in input_:
        headers["x-amz-copy-source-server-side-encryption-customer-key-MD5"] = str(
            input_["copy_source_sse_customer_key_md5"]
        )
    if "request_payer" in input_:
        headers["x-amz-request-payer"] = str(input_["request_payer"])
    if "tagging" in input_:
        headers["x-amz-tagging"] = str(input_["tagging"])
    if "object_lock_mode" in input_:
        headers["x-amz-object-lock-mode"] = str(input_["object_lock_mode"])
    if "object_lock_retain_until_date" in input_:
        headers["x-amz-object-lock-retain-until-date"] = str(
            input_["object_lock_retain_until_date"]
        )
    if "object_lock_legal_hold_status" in input_:
        headers["x-amz-object-lock-legal-hold"] = str(
            input_["object_lock_legal_hold_status"]
        )
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = str(input_["expected_bucket_owner"])
    if "expected_source_bucket_owner" in input_:
        headers["x-amz-source-expected-bucket-owner"] = str(
            input_["expected_source_bucket_owner"]
        )
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def copy_object(
    options: OperationOptions,
    input_: aws_sdk_s3.types.copy_object_request.CopyObjectRequest,
) -> tuple[aws_sdk_s3.types.copy_object_output.CopyObjectOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_copy_object(
    options: AsyncOperationOptions,
    input_: aws_sdk_s3.types.copy_object_request.CopyObjectRequest,
) -> tuple[aws_sdk_s3.types.copy_object_output.CopyObjectOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
