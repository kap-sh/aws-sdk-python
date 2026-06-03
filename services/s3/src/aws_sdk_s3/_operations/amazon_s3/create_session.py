"""Generated from Smithy shape ``com.amazonaws.s3#CreateSession``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any
from aws_sdk_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3._rule_engine._endpoint_runtime import apply_label
import zapros
from aws_sdk_s3.errors import UnknownServiceError
from aws_sdk_s3._protocol.errors import parse_error_metadata
from aws_sdk_s3._protocol.xml import fromstring
import aws_sdk_s3._auth._signers
from aws_sdk_s3._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_s3.types.create_session_request
    import aws_sdk_s3.types.create_session_output


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
) -> aws_sdk_s3.types.create_session_output.CreateSessionOutput:
    import aws_sdk_s3.types.create_session_output

    out: aws_sdk_s3.types.create_session_output.CreateSessionOutput = (
        aws_sdk_s3.types.create_session_output.deserialize_xml(
            fromstring(response.read())
        )
    )
    if "x-amz-server-side-encryption" in response.headers:
        import aws_sdk_s3.types.server_side_encryption

        out["server_side_encryption"] = (
            aws_sdk_s3.types.server_side_encryption.from_xml_text(
                response.headers["x-amz-server-side-encryption"]
            )
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
    input: aws_sdk_s3.types.create_session_request.CreateSessionRequest,
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
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
            DisableS3ExpressSessionAuth=True,
        )
    )
    url = endpoint.url.rstrip("/") + "/{Bucket}?session"
    url = apply_label(url, "{Bucket}", str(input["bucket"]))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "session_mode" in input:
        headers["x-amz-create-session-mode"] = str(input["session_mode"])
    if "server_side_encryption" in input:
        headers["x-amz-server-side-encryption"] = str(input["server_side_encryption"])
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
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "GET",
        headers=headers,
        body=body,  # type: ignore
        context={"signer": signer},  # type: ignore
    )


def create_session(
    options: OperationOptions,
    input: aws_sdk_s3.types.create_session_request.CreateSessionRequest,
) -> tuple[aws_sdk_s3.types.create_session_output.CreateSessionOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_create_session(
    options: AsyncOperationOptions,
    input: aws_sdk_s3.types.create_session_request.CreateSessionRequest,
) -> tuple[aws_sdk_s3.types.create_session_output.CreateSessionOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
