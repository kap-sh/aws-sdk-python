"""Generated from Smithy shape ``com.amazonaws.s3#CompleteMultipartUpload``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any
from aws_sdk_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3._rule_engine._endpoint_runtime import apply_label
import zapros
from urllib.parse import quote
from aws_sdk_s3.errors import UnknownServiceError
from aws_sdk_s3._protocol.errors import parse_error_metadata
from aws_sdk_s3._protocol.xml import Element, fromstring, tostring
import aws_sdk_s3._auth._signers
from aws_sdk_s3._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_s3.types.complete_multipart_upload_request
    import aws_sdk_s3.types.complete_multipart_upload_output


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_s3.types.complete_multipart_upload_output.CompleteMultipartUploadOutput:
    import aws_sdk_s3.types.complete_multipart_upload_output

    out: aws_sdk_s3.types.complete_multipart_upload_output.CompleteMultipartUploadOutput = aws_sdk_s3.types.complete_multipart_upload_output.deserialize_xml(
        fromstring(response.read())
    )
    if "x-amz-expiration" in response.headers:
        out["expiration"] = str(response.headers["x-amz-expiration"])
    if "x-amz-server-side-encryption" in response.headers:
        import aws_sdk_s3.types.server_side_encryption

        out["server_side_encryption"] = (
            aws_sdk_s3.types.server_side_encryption.from_xml_text(
                response.headers["x-amz-server-side-encryption"]
            )
        )
    if "x-amz-version-id" in response.headers:
        out["version_id"] = str(response.headers["x-amz-version-id"])
    if "x-amz-server-side-encryption-aws-kms-key-id" in response.headers:
        out["ssekms_key_id"] = str(
            response.headers["x-amz-server-side-encryption-aws-kms-key-id"]
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
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_s3._auth._signers.Signer | None:
    if auth_schemes:
        for scheme in auth_schemes:
            match scheme["name"]:
                case "sigv4" | "sigv4a" | "sigv4-s3express" if (
                    options.credentials_provider is not None
                ):
                    return aws_sdk_s3._auth._signers.SigV4Signer(
                        options.credentials_provider, auth_scheme=scheme
                    )
                case "none":
                    return None
                case _:
                    raise RuntimeError(
                        f"Could not find provider for auth scheme {scheme['name']!r}"
                    )
    if options.credentials_provider is not None:
        if options.region is None:
            raise RuntimeError("options.region is required for SigV4 signing")
        return aws_sdk_s3._auth._signers.SigV4Signer(
            options.credentials_provider,
            auth_scheme={
                "name": "sigv4",
                "signingName": "s3",
                "signingRegion": options.region,
                "disableDoubleEncoding": False,
                "disableNormalizePath": False,
            },
        )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_s3.types.complete_multipart_upload_request.CompleteMultipartUploadRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
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
    )
    url = endpoint.url.rstrip("/") + "/{Bucket}/{Key+}"
    url = apply_label(url, "{Bucket}", str(input["bucket"]))
    url = url.replace("{Key+}", quote(str(input["key"]), safe="/"))
    params: dict[str, str] = {}
    if "upload_id" in input:
        params["uploadId"] = str(input["upload_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "checksum_crc32" in input:
        headers["x-amz-checksum-crc32"] = str(input["checksum_crc32"])
    if "checksum_crc32_c" in input:
        headers["x-amz-checksum-crc32c"] = str(input["checksum_crc32_c"])
    if "checksum_crc64_nvme" in input:
        headers["x-amz-checksum-crc64nvme"] = str(input["checksum_crc64_nvme"])
    if "checksum_sha1" in input:
        headers["x-amz-checksum-sha1"] = str(input["checksum_sha1"])
    if "checksum_sha256" in input:
        headers["x-amz-checksum-sha256"] = str(input["checksum_sha256"])
    if "checksum_sha512" in input:
        headers["x-amz-checksum-sha512"] = str(input["checksum_sha512"])
    if "checksum_md5" in input:
        headers["x-amz-checksum-md5"] = str(input["checksum_md5"])
    if "checksum_xxhash64" in input:
        headers["x-amz-checksum-xxhash64"] = str(input["checksum_xxhash64"])
    if "checksum_xxhash3" in input:
        headers["x-amz-checksum-xxhash3"] = str(input["checksum_xxhash3"])
    if "checksum_xxhash128" in input:
        headers["x-amz-checksum-xxhash128"] = str(input["checksum_xxhash128"])
    if "checksum_type" in input:
        headers["x-amz-checksum-type"] = str(input["checksum_type"])
    if "mpu_object_size" in input:
        headers["x-amz-mp-object-size"] = str(input["mpu_object_size"])
    if "request_payer" in input:
        headers["x-amz-request-payer"] = str(input["request_payer"])
    if "expected_bucket_owner" in input:
        headers["x-amz-expected-bucket-owner"] = str(input["expected_bucket_owner"])
    if "if_match" in input:
        headers["If-Match"] = str(input["if_match"])
    if "if_none_match" in input:
        headers["If-None-Match"] = str(input["if_none_match"])
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
    if "multipart_upload" in input:
        import aws_sdk_s3.types.completed_multipart_upload

        payload_root = Element("_")
        aws_sdk_s3.types.completed_multipart_upload.serialize_xml(
            input["multipart_upload"], payload_root, "CompleteMultipartUpload"
        )
        body: bytes | None = tostring(payload_root[0])
        headers["content-type"] = "application/xml"
    else:
        body = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def complete_multipart_upload(
    options: OperationOptions,
    input: aws_sdk_s3.types.complete_multipart_upload_request.CompleteMultipartUploadRequest,
) -> tuple[
    aws_sdk_s3.types.complete_multipart_upload_output.CompleteMultipartUploadOutput,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_complete_multipart_upload(
    options: AsyncOperationOptions,
    input: aws_sdk_s3.types.complete_multipart_upload_request.CompleteMultipartUploadRequest,
) -> tuple[
    aws_sdk_s3.types.complete_multipart_upload_output.CompleteMultipartUploadOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
