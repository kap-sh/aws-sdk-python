"""Generated from Smithy shape ``com.amazonaws.ecrpublic#PutImage``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_ecr_public._auth._signers
import aws_sdk_ecr_public._auth._sigv4
from aws_sdk_ecr_public._protocol.errors import parse_error_metadata_json
from aws_sdk_ecr_public._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_ecr_public._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_ecr_public.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.put_image_request
    import aws_sdk_ecr_public.types.put_image_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ImageAlreadyExistsException":
            import aws_sdk_ecr_public.errors.image_already_exists_exception

            raise aws_sdk_ecr_public.errors.image_already_exists_exception.ImageAlreadyExistsException.from_aws_json_1_1(
                data
            )
        case "ImageDigestDoesNotMatchException":
            import aws_sdk_ecr_public.errors.image_digest_does_not_match_exception

            raise aws_sdk_ecr_public.errors.image_digest_does_not_match_exception.ImageDigestDoesNotMatchException.from_aws_json_1_1(
                data
            )
        case "ImageTagAlreadyExistsException":
            import aws_sdk_ecr_public.errors.image_tag_already_exists_exception

            raise aws_sdk_ecr_public.errors.image_tag_already_exists_exception.ImageTagAlreadyExistsException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            import aws_sdk_ecr_public.errors.invalid_parameter_exception

            raise aws_sdk_ecr_public.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "LayersNotFoundException":
            import aws_sdk_ecr_public.errors.layers_not_found_exception

            raise aws_sdk_ecr_public.errors.layers_not_found_exception.LayersNotFoundException.from_aws_json_1_1(
                data
            )
        case "LimitExceededException":
            import aws_sdk_ecr_public.errors.limit_exceeded_exception

            raise aws_sdk_ecr_public.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case "ReferencedImagesNotFoundException":
            import aws_sdk_ecr_public.errors.referenced_images_not_found_exception

            raise aws_sdk_ecr_public.errors.referenced_images_not_found_exception.ReferencedImagesNotFoundException.from_aws_json_1_1(
                data
            )
        case "RegistryNotFoundException":
            import aws_sdk_ecr_public.errors.registry_not_found_exception

            raise aws_sdk_ecr_public.errors.registry_not_found_exception.RegistryNotFoundException.from_aws_json_1_1(
                data
            )
        case "RepositoryNotFoundException":
            import aws_sdk_ecr_public.errors.repository_not_found_exception

            raise aws_sdk_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException.from_aws_json_1_1(
                data
            )
        case "ServerException":
            import aws_sdk_ecr_public.errors.server_exception

            raise aws_sdk_ecr_public.errors.server_exception.ServerException.from_aws_json_1_1(
                data
            )
        case "UnsupportedCommandException":
            import aws_sdk_ecr_public.errors.unsupported_command_exception

            raise aws_sdk_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_ecr_public.types.put_image_response.PutImageResponse:
    import aws_sdk_ecr_public.types.put_image_response

    out: aws_sdk_ecr_public.types.put_image_response.PutImageResponse = (
        aws_sdk_ecr_public.types.put_image_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_ecr_public._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_ecr_public._auth._sigv4.build_sigv4_auth_scheme(
                "ecr-public", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_ecr_public._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_ecr_public.types.put_image_request.PutImageRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "SpencerFrontendService.PutImage"
    import aws_sdk_ecr_public.types.put_image_request

    body: bytes | None = json.dumps(
        aws_sdk_ecr_public.types.put_image_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def put_image(
    options: OperationOptions,
    input_: aws_sdk_ecr_public.types.put_image_request.PutImageRequest,
) -> tuple[
    aws_sdk_ecr_public.types.put_image_response.PutImageResponse, zapros.Response
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


async def async_put_image(
    options: AsyncOperationOptions,
    input_: aws_sdk_ecr_public.types.put_image_request.PutImageRequest,
) -> tuple[
    aws_sdk_ecr_public.types.put_image_response.PutImageResponse, zapros.Response
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
