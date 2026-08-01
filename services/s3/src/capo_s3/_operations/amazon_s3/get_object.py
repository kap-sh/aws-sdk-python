"""Generated from Smithy shape ``com.amazonaws.s3#GetObject``."""

from __future__ import annotations

import datetime
from email.utils import parsedate_to_datetime as _parse_http_date
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_s3._auth._signers
import capo_s3._auth._sigv4
import capo_s3._protocol.eventstream
import capo_s3.errors.invalid_object_state
import capo_s3.errors.no_such_key
import capo_s3.types.checksum_mode
import capo_s3.types.checksum_type
import capo_s3.types.get_object_output
import capo_s3.types.get_object_request
import capo_s3.types.if_modified_since
import capo_s3.types.if_unmodified_since
import capo_s3.types.last_modified
import capo_s3.types.metadata
import capo_s3.types.object_lock_legal_hold_status
import capo_s3.types.object_lock_mode
import capo_s3.types.object_lock_retain_until_date
import capo_s3.types.replication_status
import capo_s3.types.request_charged
import capo_s3.types.request_payer
import capo_s3.types.response_expires
import capo_s3.types.server_side_encryption
import capo_s3.types.storage_class
import capo_s3.types.streaming_blob
from capo_s3._protocol.errors import parse_error_metadata
from capo_s3._protocol.xml import fromstring
from capo_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3._rule_engine._endpoint_runtime import apply_label
from capo_s3._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_s3.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InvalidObjectState":
            raise capo_s3.errors.invalid_object_state.InvalidObjectState.from_xml(root)
        case "NoSuchKey":
            raise capo_s3.errors.no_such_key.NoSuchKey.from_xml(root)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_s3.types.get_object_output.GetObjectOutput:
    _iter = cast(Any, response.iter_bytes())
    out: capo_s3.types.get_object_output.GetObjectOutput = {"body": _iter}  # type: ignore[reportAssignmentType]
    if "x-amz-delete-marker" in response.headers:
        out["delete_marker"] = response.headers["x-amz-delete-marker"].lower() == "true"
    if "accept-ranges" in response.headers:
        out["accept_ranges"] = str(response.headers["accept-ranges"])
    if "x-amz-expiration" in response.headers:
        out["expiration"] = str(response.headers["x-amz-expiration"])
    if "x-amz-restore" in response.headers:
        out["restore"] = str(response.headers["x-amz-restore"])
    if "Last-Modified" in response.headers:
        out["last_modified"] = _parse_http_date(response.headers["Last-Modified"])
    if "Content-Length" in response.headers:
        out["content_length"] = int(response.headers["Content-Length"])
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
    if "x-amz-checksum-type" in response.headers:
        out["checksum_type"] = capo_s3.types.checksum_type.from_xml_text(
            response.headers["x-amz-checksum-type"]
        )
    if "x-amz-missing-meta" in response.headers:
        out["missing_meta"] = int(response.headers["x-amz-missing-meta"])
    if "x-amz-version-id" in response.headers:
        out["version_id"] = str(response.headers["x-amz-version-id"])
    if "Cache-Control" in response.headers:
        out["cache_control"] = str(response.headers["Cache-Control"])
    if "Content-Disposition" in response.headers:
        out["content_disposition"] = str(response.headers["Content-Disposition"])
    if "Content-Encoding" in response.headers:
        out["content_encoding"] = str(response.headers["Content-Encoding"])
    if "Content-Language" in response.headers:
        out["content_language"] = str(response.headers["Content-Language"])
    if "Content-Range" in response.headers:
        out["content_range"] = str(response.headers["Content-Range"])
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    if "Expires" in response.headers:
        out["expires"] = str(response.headers["Expires"])
    if "x-amz-website-redirect-location" in response.headers:
        out["website_redirect_location"] = str(
            response.headers["x-amz-website-redirect-location"]
        )
    if "x-amz-server-side-encryption" in response.headers:
        out["server_side_encryption"] = (
            capo_s3.types.server_side_encryption.from_xml_text(
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
    if "x-amz-server-side-encryption-bucket-key-enabled" in response.headers:
        out["bucket_key_enabled"] = (
            response.headers["x-amz-server-side-encryption-bucket-key-enabled"].lower()
            == "true"
        )
    if "x-amz-storage-class" in response.headers:
        out["storage_class"] = capo_s3.types.storage_class.from_xml_text(
            response.headers["x-amz-storage-class"]
        )
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = capo_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    if "x-amz-replication-status" in response.headers:
        out["replication_status"] = capo_s3.types.replication_status.from_xml_text(
            response.headers["x-amz-replication-status"]
        )
    if "x-amz-mp-parts-count" in response.headers:
        out["parts_count"] = int(response.headers["x-amz-mp-parts-count"])
    if "x-amz-tagging-count" in response.headers:
        out["tag_count"] = int(response.headers["x-amz-tagging-count"])
    if "x-amz-object-lock-mode" in response.headers:
        out["object_lock_mode"] = capo_s3.types.object_lock_mode.from_xml_text(
            response.headers["x-amz-object-lock-mode"]
        )
    if "x-amz-object-lock-retain-until-date" in response.headers:
        out["object_lock_retain_until_date"] = datetime.datetime.fromisoformat(
            response.headers["x-amz-object-lock-retain-until-date"].replace(
                "Z", "+00:00"
            )
        )
    if "x-amz-object-lock-legal-hold" in response.headers:
        out["object_lock_legal_hold_status"] = (
            capo_s3.types.object_lock_legal_hold_status.from_xml_text(
                response.headers["x-amz-object-lock-legal-hold"]
            )
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3.types.get_object_output.GetObjectOutput:
    _iter = cast(Any, response.async_iter_bytes())
    out: capo_s3.types.get_object_output.GetObjectOutput = {"body": _iter}  # type: ignore[reportAssignmentType]
    if "x-amz-delete-marker" in response.headers:
        out["delete_marker"] = response.headers["x-amz-delete-marker"].lower() == "true"
    if "accept-ranges" in response.headers:
        out["accept_ranges"] = str(response.headers["accept-ranges"])
    if "x-amz-expiration" in response.headers:
        out["expiration"] = str(response.headers["x-amz-expiration"])
    if "x-amz-restore" in response.headers:
        out["restore"] = str(response.headers["x-amz-restore"])
    if "Last-Modified" in response.headers:
        out["last_modified"] = _parse_http_date(response.headers["Last-Modified"])
    if "Content-Length" in response.headers:
        out["content_length"] = int(response.headers["Content-Length"])
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
    if "x-amz-checksum-type" in response.headers:
        out["checksum_type"] = capo_s3.types.checksum_type.from_xml_text(
            response.headers["x-amz-checksum-type"]
        )
    if "x-amz-missing-meta" in response.headers:
        out["missing_meta"] = int(response.headers["x-amz-missing-meta"])
    if "x-amz-version-id" in response.headers:
        out["version_id"] = str(response.headers["x-amz-version-id"])
    if "Cache-Control" in response.headers:
        out["cache_control"] = str(response.headers["Cache-Control"])
    if "Content-Disposition" in response.headers:
        out["content_disposition"] = str(response.headers["Content-Disposition"])
    if "Content-Encoding" in response.headers:
        out["content_encoding"] = str(response.headers["Content-Encoding"])
    if "Content-Language" in response.headers:
        out["content_language"] = str(response.headers["Content-Language"])
    if "Content-Range" in response.headers:
        out["content_range"] = str(response.headers["Content-Range"])
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    if "Expires" in response.headers:
        out["expires"] = str(response.headers["Expires"])
    if "x-amz-website-redirect-location" in response.headers:
        out["website_redirect_location"] = str(
            response.headers["x-amz-website-redirect-location"]
        )
    if "x-amz-server-side-encryption" in response.headers:
        out["server_side_encryption"] = (
            capo_s3.types.server_side_encryption.from_xml_text(
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
    if "x-amz-server-side-encryption-bucket-key-enabled" in response.headers:
        out["bucket_key_enabled"] = (
            response.headers["x-amz-server-side-encryption-bucket-key-enabled"].lower()
            == "true"
        )
    if "x-amz-storage-class" in response.headers:
        out["storage_class"] = capo_s3.types.storage_class.from_xml_text(
            response.headers["x-amz-storage-class"]
        )
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = capo_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    if "x-amz-replication-status" in response.headers:
        out["replication_status"] = capo_s3.types.replication_status.from_xml_text(
            response.headers["x-amz-replication-status"]
        )
    if "x-amz-mp-parts-count" in response.headers:
        out["parts_count"] = int(response.headers["x-amz-mp-parts-count"])
    if "x-amz-tagging-count" in response.headers:
        out["tag_count"] = int(response.headers["x-amz-tagging-count"])
    if "x-amz-object-lock-mode" in response.headers:
        out["object_lock_mode"] = capo_s3.types.object_lock_mode.from_xml_text(
            response.headers["x-amz-object-lock-mode"]
        )
    if "x-amz-object-lock-retain-until-date" in response.headers:
        out["object_lock_retain_until_date"] = datetime.datetime.fromisoformat(
            response.headers["x-amz-object-lock-retain-until-date"].replace(
                "Z", "+00:00"
            )
        )
    if "x-amz-object-lock-legal-hold" in response.headers:
        out["object_lock_legal_hold_status"] = (
            capo_s3.types.object_lock_legal_hold_status.from_xml_text(
                response.headers["x-amz-object-lock-legal-hold"]
            )
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_s3._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_s3._auth._sigv4.build_sigv4_auth_scheme("s3", options.region)
        )
        if sigv4_config is not None:
            return capo_s3._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_s3.types.get_object_request.GetObjectRequest,
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
            CopySource=options.copy_source,
            DisableAccessPoints=options.disable_access_points,
            DisableMultiRegionAccessPoints=options.disable_multi_region_access_points,
            UseArnRegion=options.use_arn_region,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
            DisableS3ExpressSessionAuth=options.disable_s3_express_session_auth,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/{Bucket}/{Key+}?x-id=GetObject"
    url = apply_label(url, "{Bucket}", str(input_["bucket"]))
    url = url.replace("{Key+}", quote(str(input_["key"]), safe="/"))
    params: dict[str, str] = {}
    if "response_cache_control" in input_:
        params["response-cache-control"] = str(input_["response_cache_control"])
    if "response_content_disposition" in input_:
        params["response-content-disposition"] = str(
            input_["response_content_disposition"]
        )
    if "response_content_encoding" in input_:
        params["response-content-encoding"] = str(input_["response_content_encoding"])
    if "response_content_language" in input_:
        params["response-content-language"] = str(input_["response_content_language"])
    if "response_content_type" in input_:
        params["response-content-type"] = str(input_["response_content_type"])
    if "response_expires" in input_:
        params["response-expires"] = str(input_["response_expires"])
    if "version_id" in input_:
        params["versionId"] = str(input_["version_id"])
    if "part_number" in input_:
        params["partNumber"] = str(input_["part_number"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "if_match" in input_:
        headers["If-Match"] = str(input_["if_match"])
    if "if_modified_since" in input_:
        headers["If-Modified-Since"] = str(input_["if_modified_since"])
    if "if_none_match" in input_:
        headers["If-None-Match"] = str(input_["if_none_match"])
    if "if_unmodified_since" in input_:
        headers["If-Unmodified-Since"] = str(input_["if_unmodified_since"])
    if "range" in input_:
        headers["Range"] = str(input_["range"])
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
    if "request_payer" in input_:
        headers["x-amz-request-payer"] = str(input_["request_payer"])
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = str(input_["expected_bucket_owner"])
    if "checksum_mode" in input_:
        headers["x-amz-checksum-mode"] = str(input_["checksum_mode"])
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_object(
    options: OperationOptions, input_: capo_s3.types.get_object_request.GetObjectRequest
) -> tuple[capo_s3.types.get_object_output.GetObjectOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_get_object(
    options: AsyncOperationOptions,
    input_: capo_s3.types.get_object_request.GetObjectRequest,
) -> tuple[capo_s3.types.get_object_output.GetObjectOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
