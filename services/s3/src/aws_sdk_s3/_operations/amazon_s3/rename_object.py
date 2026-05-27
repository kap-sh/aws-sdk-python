"""Generated from Smithy shape ``com.amazonaws.s3#RenameObject``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any
from aws_sdk_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3._rule_engine._endpoint_runtime import apply_label
import zapros
from urllib.parse import quote
from aws_sdk_s3.errors import UnknownServiceError
from aws_sdk_s3._protocol.errors import parse_error_metadata
from aws_sdk_s3._protocol.xml import fromstring
import aws_sdk_s3._auth._signers
from aws_sdk_s3._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_s3.types.rename_object_request
    import aws_sdk_s3.types.rename_object_output


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "IdempotencyParameterMismatch":
            import aws_sdk_s3.errors.idempotency_parameter_mismatch

            raise aws_sdk_s3.errors.idempotency_parameter_mismatch.IdempotencyParameterMismatch.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_s3.types.rename_object_output.RenameObjectOutput:
    out: aws_sdk_s3.types.rename_object_output.RenameObjectOutput = {}  # type: ignore[typeddict-item]
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
    input: aws_sdk_s3.types.rename_object_request.RenameObjectRequest,
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
    url = endpoint.url.rstrip("/") + "/{Bucket}/{Key+}?renameObject"
    url = apply_label(url, "{Bucket}", str(input["bucket"]))
    url = url.replace("{Key+}", quote(str(input["key"]), safe="/"))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "rename_source" in input:
        headers["x-amz-rename-source"] = str(input["rename_source"])
    if "destination_if_match" in input:
        headers["If-Match"] = str(input["destination_if_match"])
    if "destination_if_none_match" in input:
        headers["If-None-Match"] = str(input["destination_if_none_match"])
    if "destination_if_modified_since" in input:
        headers["If-Modified-Since"] = str(input["destination_if_modified_since"])
    if "destination_if_unmodified_since" in input:
        headers["If-Unmodified-Since"] = str(input["destination_if_unmodified_since"])
    if "source_if_match" in input:
        headers["x-amz-rename-source-if-match"] = str(input["source_if_match"])
    if "source_if_none_match" in input:
        headers["x-amz-rename-source-if-none-match"] = str(
            input["source_if_none_match"]
        )
    if "source_if_modified_since" in input:
        headers["x-amz-rename-source-if-modified-since"] = str(
            input["source_if_modified_since"]
        )
    if "source_if_unmodified_since" in input:
        headers["x-amz-rename-source-if-unmodified-since"] = str(
            input["source_if_unmodified_since"]
        )
    if "client_token" in input:
        headers["x-amz-client-token"] = str(input["client_token"])
    body: bytes | None = b""
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


def rename_object(
    options: OperationOptions,
    input: aws_sdk_s3.types.rename_object_request.RenameObjectRequest,
) -> tuple[aws_sdk_s3.types.rename_object_output.RenameObjectOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_rename_object(
    options: AsyncOperationOptions,
    input: aws_sdk_s3.types.rename_object_request.RenameObjectRequest,
) -> tuple[aws_sdk_s3.types.rename_object_output.RenameObjectOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        response.close()
        raise
