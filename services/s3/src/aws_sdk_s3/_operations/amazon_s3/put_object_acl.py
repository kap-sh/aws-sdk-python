"""Generated from Smithy shape ``com.amazonaws.s3#PutObjectAcl``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_s3._auth._signers
import aws_sdk_s3._auth._sigv4
from aws_sdk_s3._protocol.errors import parse_error_metadata
from aws_sdk_s3._protocol.xml import Element, fromstring, tostring
from aws_sdk_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3._rule_engine._endpoint_runtime import apply_label
from aws_sdk_s3._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_s3.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_s3.types.put_object_acl_output
    import aws_sdk_s3.types.put_object_acl_request


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "NoSuchKey":
            import aws_sdk_s3.errors.no_such_key

            raise aws_sdk_s3.errors.no_such_key.NoSuchKey.from_xml(root)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_s3.types.put_object_acl_output.PutObjectAclOutput:
    out: aws_sdk_s3.types.put_object_acl_output.PutObjectAclOutput = {}  # type: ignore[typeddict-item]
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
    input: aws_sdk_s3.types.put_object_acl_request.PutObjectAclRequest,
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
    url = endpoint.url.rstrip("/") + "/{Bucket}/{Key+}?acl"
    url = apply_label(url, "{Bucket}", str(input["bucket"]))
    url = url.replace("{Key+}", quote(str(input["key"]), safe="/"))
    params: dict[str, str] = {}
    if "version_id" in input:
        params["versionId"] = str(input["version_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "acl" in input:
        headers["x-amz-acl"] = str(input["acl"])
    if "content_md5" in input:
        headers["Content-MD5"] = str(input["content_md5"])
    if "checksum_algorithm" in input:
        headers["x-amz-sdk-checksum-algorithm"] = str(input["checksum_algorithm"])
    if "grant_full_control" in input:
        headers["x-amz-grant-full-control"] = str(input["grant_full_control"])
    if "grant_read" in input:
        headers["x-amz-grant-read"] = str(input["grant_read"])
    if "grant_read_acp" in input:
        headers["x-amz-grant-read-acp"] = str(input["grant_read_acp"])
    if "grant_write" in input:
        headers["x-amz-grant-write"] = str(input["grant_write"])
    if "grant_write_acp" in input:
        headers["x-amz-grant-write-acp"] = str(input["grant_write_acp"])
    if "request_payer" in input:
        headers["x-amz-request-payer"] = str(input["request_payer"])
    if "expected_bucket_owner" in input:
        headers["x-amz-expected-bucket-owner"] = str(input["expected_bucket_owner"])
    if "access_control_policy" in input:
        import aws_sdk_s3.types.access_control_policy

        payload_root = Element("_")
        aws_sdk_s3.types.access_control_policy.serialize_xml(
            input["access_control_policy"], payload_root, "AccessControlPolicy"
        )
        body: bytes | None = tostring(payload_root[0])
        headers["content-type"] = "application/xml"
    else:
        body = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def put_object_acl(
    options: OperationOptions,
    input: aws_sdk_s3.types.put_object_acl_request.PutObjectAclRequest,
) -> tuple[aws_sdk_s3.types.put_object_acl_output.PutObjectAclOutput, zapros.Response]:
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


async def async_put_object_acl(
    options: AsyncOperationOptions,
    input: aws_sdk_s3.types.put_object_acl_request.PutObjectAclRequest,
) -> tuple[aws_sdk_s3.types.put_object_acl_output.PutObjectAclOutput, zapros.Response]:
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
