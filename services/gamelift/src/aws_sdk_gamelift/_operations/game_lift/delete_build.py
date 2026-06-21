"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteBuild``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_gamelift._auth._signers
import aws_sdk_gamelift._auth._sigv4
import aws_sdk_gamelift.errors.internal_service_exception
import aws_sdk_gamelift.errors.invalid_request_exception
import aws_sdk_gamelift.errors.not_found_exception
import aws_sdk_gamelift.errors.tagging_failed_exception
import aws_sdk_gamelift.errors.unauthorized_exception
import aws_sdk_gamelift.types.delete_build_input
from aws_sdk_gamelift._protocol.errors import parse_error_metadata_json
from aws_sdk_gamelift._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_gamelift._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_gamelift.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServiceException":
            raise aws_sdk_gamelift.errors.internal_service_exception.InternalServiceException.from_aws_json_1_1(
                data
            )
        case "InvalidRequestException":
            raise aws_sdk_gamelift.errors.invalid_request_exception.InvalidRequestException.from_aws_json_1_1(
                data
            )
        case "NotFoundException":
            raise aws_sdk_gamelift.errors.not_found_exception.NotFoundException.from_aws_json_1_1(
                data
            )
        case "TaggingFailedException":
            raise aws_sdk_gamelift.errors.tagging_failed_exception.TaggingFailedException.from_aws_json_1_1(
                data
            )
        case "UnauthorizedException":
            raise aws_sdk_gamelift.errors.unauthorized_exception.UnauthorizedException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_gamelift._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_gamelift._auth._sigv4.build_sigv4_auth_scheme(
                "gamelift", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_gamelift._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_gamelift.types.delete_build_input.DeleteBuildInput,
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
    headers["X-Amz-Target"] = "GameLift.DeleteBuild"
    import aws_sdk_gamelift.types.delete_build_input

    body: bytes | None = json.dumps(
        aws_sdk_gamelift.types.delete_build_input.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def delete_build(
    options: OperationOptions,
    input_: aws_sdk_gamelift.types.delete_build_input.DeleteBuildInput,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_delete_build(
    options: AsyncOperationOptions,
    input_: aws_sdk_gamelift.types.delete_build_input.DeleteBuildInput,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
