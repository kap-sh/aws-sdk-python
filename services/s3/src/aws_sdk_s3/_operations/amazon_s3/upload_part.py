"""Generated from Smithy shape ``com.amazonaws.s3#UploadPart``."""

from __future__ import annotations

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
    import aws_sdk_s3.types.upload_part_output
    import aws_sdk_s3.types.upload_part_request


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_s3.types.upload_part_output.UploadPartOutput:
    out: aws_sdk_s3.types.upload_part_output.UploadPartOutput = {}  # type: ignore[typeddict-item]
    if "x-amz-server-side-encryption" in response.headers:
        import aws_sdk_s3.types.server_side_encryption

        out["server_side_encryption"] = (
            aws_sdk_s3.types.server_side_encryption.from_xml_text(
                response.headers["x-amz-server-side-encryption"]
            )
        )
    if "ETag" in response.headers:
        out["e_tag"] = str(response.headers["ETag"])
    if "x-amz-checksum-crc32" in response.headers:
        out["checksum_crc32"] = str(response.headers["x-amz-checksum-crc32"])
    if "x-amz-checksum-crc32c" in response.headers:
        out["checksum_crc32_c"] = str(response.headers["x-amz-checksum-crc32c"])
    if "x-amz-checksum-crc64nvme" in response.headers:
        out["checksum_crc64_nvme"] = str(response.headers["x-amz-checksum-crc64nvme"])
    if "x-amz-checksum-sha1" in response.headers:
        out["checksum_sha1"] = str(response.headers["x-amz-checksum-sha1"])
    if "x-amz-checksum-sha256" in response.headers:
        out["checksum_sha256"] = str(response.headers["x-amz-checksum-sha256"])
    if "x-amz-checksum-sha512" in response.headers:
        out["checksum_sha512"] = str(response.headers["x-amz-checksum-sha512"])
    if "x-amz-checksum-md5" in response.headers:
        out["checksum_md5"] = str(response.headers["x-amz-checksum-md5"])
    if "x-amz-checksum-xxhash64" in response.headers:
        out["checksum_xxhash64"] = str(response.headers["x-amz-checksum-xxhash64"])
    if "x-amz-checksum-xxhash3" in response.headers:
        out["checksum_xxhash3"] = str(response.headers["x-amz-checksum-xxhash3"])
    if "x-amz-checksum-xxhash128" in response.headers:
        out["checksum_xxhash128"] = str(response.headers["x-amz-checksum-xxhash128"])
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
    input: aws_sdk_s3.types.upload_part_request.UploadPartRequest,
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
    url = endpoint.url.rstrip("/") + "/{Bucket}/{Key+}?x-id=UploadPart"
    url = apply_label(url, "{Bucket}", str(input["bucket"]))
    url = url.replace("{Key+}", quote(str(input["key"]), safe="/"))
    params: dict[str, str] = {}
    if "part_number" in input:
        params["partNumber"] = str(input["part_number"])
    if "upload_id" in input:
        params["uploadId"] = str(input["upload_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "content_length" in input:
        headers["Content-Length"] = str(input["content_length"])
    if "content_md5" in input:
        headers["Content-MD5"] = str(input["content_md5"])
    if "checksum_algorithm" in input:
        headers["x-amz-sdk-checksum-algorithm"] = str(input["checksum_algorithm"])
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
    if "request_payer" in input:
        headers["x-amz-request-payer"] = str(input["request_payer"])
    if "expected_bucket_owner" in input:
        headers["x-amz-expected-bucket-owner"] = str(input["expected_bucket_owner"])
    body = input["body"]
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def upload_part(
    options: OperationOptions,
    input: aws_sdk_s3.types.upload_part_request.UploadPartRequest,
) -> tuple[aws_sdk_s3.types.upload_part_output.UploadPartOutput, zapros.Response]:
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


async def async_upload_part(
    options: AsyncOperationOptions,
    input: aws_sdk_s3.types.upload_part_request.UploadPartRequest,
) -> tuple[aws_sdk_s3.types.upload_part_output.UploadPartOutput, zapros.Response]:
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
