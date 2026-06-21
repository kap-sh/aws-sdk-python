"""Generated from Smithy shape ``com.amazonaws.s3#DeleteObject``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_s3._auth._signers
import aws_sdk_s3._auth._sigv4
import aws_sdk_s3._protocol.eventstream
import aws_sdk_s3.types.delete_object_output
import aws_sdk_s3.types.delete_object_request
import aws_sdk_s3.types.if_match_last_modified_time
import aws_sdk_s3.types.request_charged
import aws_sdk_s3.types.request_payer
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
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_s3.types.delete_object_output.DeleteObjectOutput:
    out: aws_sdk_s3.types.delete_object_output.DeleteObjectOutput = {}  # type: ignore[typeddict-item]
    if "x-amz-delete-marker" in response.headers:
        out["delete_marker"] = response.headers["x-amz-delete-marker"].lower() == "true"
    if "x-amz-version-id" in response.headers:
        out["version_id"] = str(response.headers["x-amz-version-id"])
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = aws_sdk_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_s3.types.delete_object_output.DeleteObjectOutput:
    out: aws_sdk_s3.types.delete_object_output.DeleteObjectOutput = {}  # type: ignore[typeddict-item]
    if "x-amz-delete-marker" in response.headers:
        out["delete_marker"] = response.headers["x-amz-delete-marker"].lower() == "true"
    if "x-amz-version-id" in response.headers:
        out["version_id"] = str(response.headers["x-amz-version-id"])
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
    input_: aws_sdk_s3.types.delete_object_request.DeleteObjectRequest,
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
    url = endpoint.url.rstrip("/") + "/{Bucket}/{Key+}?x-id=DeleteObject"
    url = apply_label(url, "{Bucket}", str(input_["bucket"]))
    url = url.replace("{Key+}", quote(str(input_["key"]), safe="/"))
    params: dict[str, str] = {}
    if "version_id" in input_:
        params["versionId"] = str(input_["version_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "mfa" in input_:
        headers["x-amz-mfa"] = str(input_["mfa"])
    if "request_payer" in input_:
        headers["x-amz-request-payer"] = str(input_["request_payer"])
    if "bypass_governance_retention" in input_:
        headers["x-amz-bypass-governance-retention"] = str(
            input_["bypass_governance_retention"]
        )
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = str(input_["expected_bucket_owner"])
    if "if_match" in input_:
        headers["If-Match"] = str(input_["if_match"])
    if "if_match_last_modified_time" in input_:
        headers["x-amz-if-match-last-modified-time"] = str(
            input_["if_match_last_modified_time"]
        )
    if "if_match_size" in input_:
        headers["x-amz-if-match-size"] = str(input_["if_match_size"])
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_object(
    options: OperationOptions,
    input_: aws_sdk_s3.types.delete_object_request.DeleteObjectRequest,
) -> tuple[aws_sdk_s3.types.delete_object_output.DeleteObjectOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_delete_object(
    options: AsyncOperationOptions,
    input_: aws_sdk_s3.types.delete_object_request.DeleteObjectRequest,
) -> tuple[aws_sdk_s3.types.delete_object_output.DeleteObjectOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
