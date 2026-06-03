"""Generated from Smithy shape ``com.amazonaws.s3#PutBucketAccelerateConfiguration``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any
from aws_sdk_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3._rule_engine._endpoint_runtime import apply_label
import zapros
from aws_sdk_s3.errors import UnknownServiceError
from aws_sdk_s3._protocol.errors import parse_error_metadata
from aws_sdk_s3._protocol.xml import Element, fromstring, tostring
import aws_sdk_s3._auth._signers
from aws_sdk_s3._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_s3.types.put_bucket_accelerate_configuration_request


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
    input: aws_sdk_s3.types.put_bucket_accelerate_configuration_request.PutBucketAccelerateConfigurationRequest,
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
            Key=options.key,
            Prefix=options.prefix,
            CopySource=options.copy_source,
            DisableAccessPoints=options.disable_access_points,
            DisableMultiRegionAccessPoints=options.disable_multi_region_access_points,
            UseArnRegion=options.use_arn_region,
            UseS3ExpressControlEndpoint=True,
            DisableS3ExpressSessionAuth=options.disable_s3_express_session_auth,
        )
    )
    url = endpoint.url.rstrip("/") + "/{Bucket}?accelerate"
    url = apply_label(url, "{Bucket}", str(input["bucket"]))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "expected_bucket_owner" in input:
        headers["x-amz-expected-bucket-owner"] = str(input["expected_bucket_owner"])
    if "checksum_algorithm" in input:
        headers["x-amz-sdk-checksum-algorithm"] = str(input["checksum_algorithm"])
    if "accelerate_configuration" in input:
        import aws_sdk_s3.types.accelerate_configuration

        payload_root = Element("_")
        aws_sdk_s3.types.accelerate_configuration.serialize_xml(
            input["accelerate_configuration"], payload_root, "AccelerateConfiguration"
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
        "PUT",
        headers=headers,
        body=body,  # type: ignore
        context={"signer": signer},  # type: ignore
    )


def put_bucket_accelerate_configuration(
    options: OperationOptions,
    input: aws_sdk_s3.types.put_bucket_accelerate_configuration_request.PutBucketAccelerateConfigurationRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_put_bucket_accelerate_configuration(
    options: AsyncOperationOptions,
    input: aws_sdk_s3.types.put_bucket_accelerate_configuration_request.PutBucketAccelerateConfigurationRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
