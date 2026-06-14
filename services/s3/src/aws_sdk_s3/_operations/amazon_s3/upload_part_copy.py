"""Generated from Smithy shape ``com.amazonaws.s3#UploadPartCopy``."""

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
    import aws_sdk_s3.types.upload_part_copy_output
    import aws_sdk_s3.types.upload_part_copy_request


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_s3.types.upload_part_copy_output.UploadPartCopyOutput:
    import aws_sdk_s3.types.copy_part_result

    out: aws_sdk_s3.types.upload_part_copy_output.UploadPartCopyOutput = {
        "copy_part_result": aws_sdk_s3.types.copy_part_result.deserialize_xml(
            fromstring(response.read())
        )
    }  # type: ignore[typeddict-item]
    if "x-amz-copy-source-version-id" in response.headers:
        out["copy_source_version_id"] = str(
            response.headers["x-amz-copy-source-version-id"]
        )
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
    input_: aws_sdk_s3.types.upload_part_copy_request.UploadPartCopyRequest,
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
            Key=options.key,
            Prefix=options.prefix,
            CopySource=options.copy_source,
            DisableAccessPoints=options.disable_access_points,
            DisableMultiRegionAccessPoints=options.disable_multi_region_access_points,
            UseArnRegion=options.use_arn_region,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
            DisableS3ExpressSessionAuth=True,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/{Bucket}/{Key+}?x-id=UploadPartCopy"
    url = apply_label(url, "{Bucket}", str(input_["bucket"]))
    url = url.replace("{Key+}", quote(str(input_["key"]), safe="/"))
    params: dict[str, str] = {}
    if "part_number" in input_:
        params["partNumber"] = str(input_["part_number"])
    if "upload_id" in input_:
        params["uploadId"] = str(input_["upload_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
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
    if "copy_source_range" in input_:
        headers["x-amz-copy-source-range"] = str(input_["copy_source_range"])
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


def upload_part_copy(
    options: OperationOptions,
    input_: aws_sdk_s3.types.upload_part_copy_request.UploadPartCopyRequest,
) -> tuple[
    aws_sdk_s3.types.upload_part_copy_output.UploadPartCopyOutput, zapros.Response
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


async def async_upload_part_copy(
    options: AsyncOperationOptions,
    input_: aws_sdk_s3.types.upload_part_copy_request.UploadPartCopyRequest,
) -> tuple[
    aws_sdk_s3.types.upload_part_copy_output.UploadPartCopyOutput, zapros.Response
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
