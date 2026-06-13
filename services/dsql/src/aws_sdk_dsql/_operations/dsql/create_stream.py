"""Generated from Smithy shape ``com.amazonaws.dsql#CreateStream``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_dsql._auth._signers
import aws_sdk_dsql._auth._sigv4
from aws_sdk_dsql._protocol.errors import parse_error_metadata_json
from aws_sdk_dsql._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_dsql._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_dsql.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_dsql.types.create_stream_input
    import aws_sdk_dsql.types.create_stream_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_dsql.errors.access_denied_exception

            raise aws_sdk_dsql.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_dsql.errors.internal_server_exception

            raise aws_sdk_dsql.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_dsql.errors.throttling_exception

            raise aws_sdk_dsql.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_dsql.errors.validation_exception

            raise aws_sdk_dsql.errors.validation_exception.ValidationException.from_json(
                data
            )
        case "ConflictException":
            import aws_sdk_dsql.errors.conflict_exception

            raise aws_sdk_dsql.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_dsql.errors.resource_not_found_exception

            raise aws_sdk_dsql.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            import aws_sdk_dsql.errors.service_quota_exceeded_exception

            raise aws_sdk_dsql.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_dsql.types.create_stream_output.CreateStreamOutput:
    import aws_sdk_dsql.types.create_stream_output

    out: aws_sdk_dsql.types.create_stream_output.CreateStreamOutput = (
        aws_sdk_dsql.types.create_stream_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_dsql._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_dsql._auth._sigv4.build_sigv4_auth_scheme("dsql", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_dsql._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_dsql.types.create_stream_input.CreateStreamInput,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )
    url = endpoint.url.rstrip("/") + "/stream/{clusterIdentifier}"
    url = url.replace(
        "{clusterIdentifier}", quote(str(input["cluster_identifier"]), safe="")
    )
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_dsql.types.create_stream_input

    body: bytes | None = json.dumps(
        aws_sdk_dsql.types.create_stream_input.serialize_json(input)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def create_stream(
    options: OperationOptions,
    input: aws_sdk_dsql.types.create_stream_input.CreateStreamInput,
) -> tuple[aws_sdk_dsql.types.create_stream_output.CreateStreamOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_create_stream(
    options: AsyncOperationOptions,
    input: aws_sdk_dsql.types.create_stream_input.CreateStreamInput,
) -> tuple[aws_sdk_dsql.types.create_stream_output.CreateStreamOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
