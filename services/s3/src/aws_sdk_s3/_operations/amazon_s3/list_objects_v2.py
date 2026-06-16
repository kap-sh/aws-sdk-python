"""Generated from Smithy shape ``com.amazonaws.s3#ListObjectsV2``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_s3._auth._signers
import aws_sdk_s3._auth._sigv4
from aws_sdk_s3._protocol.errors import parse_error_metadata
from aws_sdk_s3._protocol.xml import fromstring
from aws_sdk_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3._rule_engine._endpoint_runtime import apply_label
from aws_sdk_s3._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_s3.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_s3.types.list_objects_v2_output
    import aws_sdk_s3.types.list_objects_v2_request


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "NoSuchBucket":
            import aws_sdk_s3.errors.no_such_bucket

            raise aws_sdk_s3.errors.no_such_bucket.NoSuchBucket.from_xml(root)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_s3.types.list_objects_v2_output.ListObjectsV2Output:
    import aws_sdk_s3.types.list_objects_v2_output

    out: aws_sdk_s3.types.list_objects_v2_output.ListObjectsV2Output = (
        aws_sdk_s3.types.list_objects_v2_output.deserialize_xml(
            fromstring(response.read())
        )
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
    input_: aws_sdk_s3.types.list_objects_v2_request.ListObjectsV2Request,
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
            Prefix=input_.get("prefix"),
            CopySource=options.copy_source,
            DisableAccessPoints=options.disable_access_points,
            DisableMultiRegionAccessPoints=options.disable_multi_region_access_points,
            UseArnRegion=options.use_arn_region,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
            DisableS3ExpressSessionAuth=options.disable_s3_express_session_auth,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/{Bucket}?list-type=2"
    url = apply_label(url, "{Bucket}", str(input_["bucket"]))
    params: dict[str, str] = {}
    if "delimiter" in input_:
        params["delimiter"] = str(input_["delimiter"])
    if "encoding_type" in input_:
        params["encoding-type"] = str(input_["encoding_type"])
    if "max_keys" in input_:
        params["max-keys"] = str(input_["max_keys"])
    if "prefix" in input_:
        params["prefix"] = str(input_["prefix"])
    if "continuation_token" in input_:
        params["continuation-token"] = str(input_["continuation_token"])
    if "fetch_owner" in input_:
        params["fetch-owner"] = str(input_["fetch_owner"])
    if "start_after" in input_:
        params["start-after"] = str(input_["start_after"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "request_payer" in input_:
        headers["x-amz-request-payer"] = str(input_["request_payer"])
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = str(input_["expected_bucket_owner"])
    if "optional_object_attributes" in input_:
        headers["x-amz-optional-object-attributes"] = str(
            input_["optional_object_attributes"]
        )
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_objects_v2(
    options: OperationOptions,
    input_: aws_sdk_s3.types.list_objects_v2_request.ListObjectsV2Request,
) -> tuple[
    aws_sdk_s3.types.list_objects_v2_output.ListObjectsV2Output, zapros.Response
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


async def async_list_objects_v2(
    options: AsyncOperationOptions,
    input_: aws_sdk_s3.types.list_objects_v2_request.ListObjectsV2Request,
) -> tuple[
    aws_sdk_s3.types.list_objects_v2_output.ListObjectsV2Output, zapros.Response
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
