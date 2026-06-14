"""Generated from Smithy shape ``com.amazonaws.s3#WriteGetObjectResponse``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_s3._auth._signers
import aws_sdk_s3._auth._sigv4
from aws_sdk_s3._protocol.errors import parse_error_metadata
from aws_sdk_s3._protocol.xml import fromstring
from aws_sdk_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_s3.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_s3.types.write_get_object_response_request


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


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
    input_: aws_sdk_s3.types.write_get_object_response_request.WriteGetObjectResponseRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Bucket=options.bucket,
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
            ForcePathStyle=options.force_path_style,
            Accelerate=options.accelerate,
            UseGlobalEndpoint=options.use_global_endpoint,
            UseObjectLambdaEndpoint=True,
            Key=options.key,
            Prefix=options.prefix,
            CopySource=options.copy_source,
            DisableAccessPoints=options.disable_access_points,
            DisableMultiRegionAccessPoints=options.disable_multi_region_access_points,
            UseArnRegion=options.use_arn_region,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
            DisableS3ExpressSessionAuth=options.disable_s3_express_session_auth,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/WriteGetObjectResponse"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "request_route" in input_:
        headers["x-amz-request-route"] = str(input_["request_route"])
    if "request_token" in input_:
        headers["x-amz-request-token"] = str(input_["request_token"])
    if "status_code" in input_:
        headers["x-amz-fwd-status"] = str(input_["status_code"])
    if "error_code" in input_:
        headers["x-amz-fwd-error-code"] = str(input_["error_code"])
    if "error_message" in input_:
        headers["x-amz-fwd-error-message"] = str(input_["error_message"])
    if "accept_ranges" in input_:
        headers["x-amz-fwd-header-accept-ranges"] = str(input_["accept_ranges"])
    if "cache_control" in input_:
        headers["x-amz-fwd-header-Cache-Control"] = str(input_["cache_control"])
    if "content_disposition" in input_:
        headers["x-amz-fwd-header-Content-Disposition"] = str(
            input_["content_disposition"]
        )
    if "content_encoding" in input_:
        headers["x-amz-fwd-header-Content-Encoding"] = str(input_["content_encoding"])
    if "content_language" in input_:
        headers["x-amz-fwd-header-Content-Language"] = str(input_["content_language"])
    if "content_length" in input_:
        headers["Content-Length"] = str(input_["content_length"])
    if "content_range" in input_:
        headers["x-amz-fwd-header-Content-Range"] = str(input_["content_range"])
    if "content_type" in input_:
        headers["x-amz-fwd-header-Content-Type"] = str(input_["content_type"])
    if "checksum_crc32" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-crc32"] = str(input_["checksum_crc32"])
    if "checksum_crc32_c" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-crc32c"] = str(
            input_["checksum_crc32_c"]
        )
    if "checksum_crc64_nvme" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-crc64nvme"] = str(
            input_["checksum_crc64_nvme"]
        )
    if "checksum_sha1" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-sha1"] = str(input_["checksum_sha1"])
    if "checksum_sha256" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-sha256"] = str(
            input_["checksum_sha256"]
        )
    if "checksum_sha512" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-sha512"] = str(
            input_["checksum_sha512"]
        )
    if "checksum_md5" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-md5"] = str(input_["checksum_md5"])
    if "checksum_xxhash64" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-xxhash64"] = str(
            input_["checksum_xxhash64"]
        )
    if "checksum_xxhash3" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-xxhash3"] = str(
            input_["checksum_xxhash3"]
        )
    if "checksum_xxhash128" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-xxhash128"] = str(
            input_["checksum_xxhash128"]
        )
    if "delete_marker" in input_:
        headers["x-amz-fwd-header-x-amz-delete-marker"] = str(input_["delete_marker"])
    if "e_tag" in input_:
        headers["x-amz-fwd-header-ETag"] = str(input_["e_tag"])
    if "expires" in input_:
        headers["x-amz-fwd-header-Expires"] = str(input_["expires"])
    if "expiration" in input_:
        headers["x-amz-fwd-header-x-amz-expiration"] = str(input_["expiration"])
    if "last_modified" in input_:
        headers["x-amz-fwd-header-Last-Modified"] = str(input_["last_modified"])
    if "missing_meta" in input_:
        headers["x-amz-fwd-header-x-amz-missing-meta"] = str(input_["missing_meta"])
    if "object_lock_mode" in input_:
        headers["x-amz-fwd-header-x-amz-object-lock-mode"] = str(
            input_["object_lock_mode"]
        )
    if "object_lock_legal_hold_status" in input_:
        headers["x-amz-fwd-header-x-amz-object-lock-legal-hold"] = str(
            input_["object_lock_legal_hold_status"]
        )
    if "object_lock_retain_until_date" in input_:
        headers["x-amz-fwd-header-x-amz-object-lock-retain-until-date"] = str(
            input_["object_lock_retain_until_date"]
        )
    if "parts_count" in input_:
        headers["x-amz-fwd-header-x-amz-mp-parts-count"] = str(input_["parts_count"])
    if "replication_status" in input_:
        headers["x-amz-fwd-header-x-amz-replication-status"] = str(
            input_["replication_status"]
        )
    if "request_charged" in input_:
        headers["x-amz-fwd-header-x-amz-request-charged"] = str(
            input_["request_charged"]
        )
    if "restore" in input_:
        headers["x-amz-fwd-header-x-amz-restore"] = str(input_["restore"])
    if "server_side_encryption" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption"] = str(
            input_["server_side_encryption"]
        )
    if "sse_customer_algorithm" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption-customer-algorithm"] = (
            str(input_["sse_customer_algorithm"])
        )
    if "ssekms_key_id" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption-aws-kms-key-id"] = str(
            input_["ssekms_key_id"]
        )
    if "sse_customer_key_md5" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption-customer-key-MD5"] = str(
            input_["sse_customer_key_md5"]
        )
    if "storage_class" in input_:
        headers["x-amz-fwd-header-x-amz-storage-class"] = str(input_["storage_class"])
    if "tag_count" in input_:
        headers["x-amz-fwd-header-x-amz-tagging-count"] = str(input_["tag_count"])
    if "version_id" in input_:
        headers["x-amz-fwd-header-x-amz-version-id"] = str(input_["version_id"])
    if "bucket_key_enabled" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption-bucket-key-enabled"] = (
            str(input_["bucket_key_enabled"])
        )
    body = input_["body"]
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def write_get_object_response(
    options: OperationOptions,
    input_: aws_sdk_s3.types.write_get_object_response_request.WriteGetObjectResponseRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return None, response
    except BaseException:
        response.close()
        raise


async def async_write_get_object_response(
    options: AsyncOperationOptions,
    input_: aws_sdk_s3.types.write_get_object_response_request.WriteGetObjectResponseRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return None, response
    except BaseException:
        await response.aclose()
        raise
