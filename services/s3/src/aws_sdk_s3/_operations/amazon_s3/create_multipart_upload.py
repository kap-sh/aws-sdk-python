"""Generated from Smithy shape ``com.amazonaws.s3#CreateMultipartUpload``."""

from __future__ import annotations

from email.utils import parsedate_to_datetime as _parse_http_date
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_s3._auth._signers
import aws_sdk_s3._auth._sigv4
from aws_sdk_s3._protocol.errors import parse_error_metadata
from aws_sdk_s3._protocol.xml import fromstring
from aws_sdk_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3._rule_engine._endpoint_runtime import apply_label
from aws_sdk_s3._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_s3.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_s3.types.create_multipart_upload_output
    import aws_sdk_s3.types.create_multipart_upload_request


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_s3.types.create_multipart_upload_output.CreateMultipartUploadOutput:
    import aws_sdk_s3.types.create_multipart_upload_output

    out: aws_sdk_s3.types.create_multipart_upload_output.CreateMultipartUploadOutput = (
        aws_sdk_s3.types.create_multipart_upload_output.deserialize_xml(
            fromstring(response.read())
        )
    )
    if "x-amz-abort-date" in response.headers:
        import aws_sdk_s3.types.abort_date

        out["abort_date"] = _parse_http_date(response.headers["x-amz-abort-date"])
    if "x-amz-abort-rule-id" in response.headers:
        out["abort_rule_id"] = str(response.headers["x-amz-abort-rule-id"])
    if "x-amz-server-side-encryption" in response.headers:
        import aws_sdk_s3.types.server_side_encryption

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
        import aws_sdk_s3.types.request_charged

        out["request_charged"] = aws_sdk_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    if "x-amz-checksum-algorithm" in response.headers:
        import aws_sdk_s3.types.checksum_algorithm

        out["checksum_algorithm"] = aws_sdk_s3.types.checksum_algorithm.from_xml_text(
            response.headers["x-amz-checksum-algorithm"]
        )
    if "x-amz-checksum-type" in response.headers:
        import aws_sdk_s3.types.checksum_type

        out["checksum_type"] = aws_sdk_s3.types.checksum_type.from_xml_text(
            response.headers["x-amz-checksum-type"]
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_s3._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
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
    input: aws_sdk_s3.types.create_multipart_upload_request.CreateMultipartUploadRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Bucket=input.get("bucket"),
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
            ForcePathStyle=options.force_path_style,
            Accelerate=options.accelerate,
            UseGlobalEndpoint=options.use_global_endpoint,
            UseObjectLambdaEndpoint=options.use_object_lambda_endpoint,
            Key=input.get("key"),
            Prefix=options.prefix,
            CopySource=options.copy_source,
            DisableAccessPoints=options.disable_access_points,
            DisableMultiRegionAccessPoints=options.disable_multi_region_access_points,
            UseArnRegion=options.use_arn_region,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
            DisableS3ExpressSessionAuth=options.disable_s3_express_session_auth,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/{Bucket}/{Key+}?uploads"
    url = apply_label(url, "{Bucket}", str(input["bucket"]))
    url = url.replace("{Key+}", quote(str(input["key"]), safe="/"))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "acl" in input:
        headers["x-amz-acl"] = str(input["acl"])
    if "cache_control" in input:
        headers["Cache-Control"] = str(input["cache_control"])
    if "content_disposition" in input:
        headers["Content-Disposition"] = str(input["content_disposition"])
    if "content_encoding" in input:
        headers["Content-Encoding"] = str(input["content_encoding"])
    if "content_language" in input:
        headers["Content-Language"] = str(input["content_language"])
    if "content_type" in input:
        headers["Content-Type"] = str(input["content_type"])
    if "expires" in input:
        headers["Expires"] = str(input["expires"])
    if "grant_full_control" in input:
        headers["x-amz-grant-full-control"] = str(input["grant_full_control"])
    if "grant_read" in input:
        headers["x-amz-grant-read"] = str(input["grant_read"])
    if "grant_read_acp" in input:
        headers["x-amz-grant-read-acp"] = str(input["grant_read_acp"])
    if "grant_write_acp" in input:
        headers["x-amz-grant-write-acp"] = str(input["grant_write_acp"])
    if "server_side_encryption" in input:
        headers["x-amz-server-side-encryption"] = str(input["server_side_encryption"])
    if "storage_class" in input:
        headers["x-amz-storage-class"] = str(input["storage_class"])
    if "website_redirect_location" in input:
        headers["x-amz-website-redirect-location"] = str(
            input["website_redirect_location"]
        )
    if "sse_customer_algorithm" in input:
        headers["x-amz-server-side-encryption-customer-algorithm"] = str(
            input["sse_customer_algorithm"]
        )
    if "sse_customer_key" in input:
        headers["x-amz-server-side-encryption-customer-key"] = str(
            input["sse_customer_key"]
        )
    if "sse_customer_key_md5" in input:
        headers["x-amz-server-side-encryption-customer-key-MD5"] = str(
            input["sse_customer_key_md5"]
        )
    if "ssekms_key_id" in input:
        headers["x-amz-server-side-encryption-aws-kms-key-id"] = str(
            input["ssekms_key_id"]
        )
    if "ssekms_encryption_context" in input:
        headers["x-amz-server-side-encryption-context"] = str(
            input["ssekms_encryption_context"]
        )
    if "bucket_key_enabled" in input:
        headers["x-amz-server-side-encryption-bucket-key-enabled"] = str(
            input["bucket_key_enabled"]
        )
    if "request_payer" in input:
        headers["x-amz-request-payer"] = str(input["request_payer"])
    if "tagging" in input:
        headers["x-amz-tagging"] = str(input["tagging"])
    if "object_lock_mode" in input:
        headers["x-amz-object-lock-mode"] = str(input["object_lock_mode"])
    if "object_lock_retain_until_date" in input:
        headers["x-amz-object-lock-retain-until-date"] = str(
            input["object_lock_retain_until_date"]
        )
    if "object_lock_legal_hold_status" in input:
        headers["x-amz-object-lock-legal-hold"] = str(
            input["object_lock_legal_hold_status"]
        )
    if "expected_bucket_owner" in input:
        headers["x-amz-expected-bucket-owner"] = str(input["expected_bucket_owner"])
    if "checksum_algorithm" in input:
        headers["x-amz-checksum-algorithm"] = str(input["checksum_algorithm"])
    if "checksum_type" in input:
        headers["x-amz-checksum-type"] = str(input["checksum_type"])
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_multipart_upload(
    options: OperationOptions,
    input: aws_sdk_s3.types.create_multipart_upload_request.CreateMultipartUploadRequest,
) -> tuple[
    aws_sdk_s3.types.create_multipart_upload_output.CreateMultipartUploadOutput,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_create_multipart_upload(
    options: AsyncOperationOptions,
    input: aws_sdk_s3.types.create_multipart_upload_request.CreateMultipartUploadRequest,
) -> tuple[
    aws_sdk_s3.types.create_multipart_upload_output.CreateMultipartUploadOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
