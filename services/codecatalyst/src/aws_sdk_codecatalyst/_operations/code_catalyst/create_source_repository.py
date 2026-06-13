"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CreateSourceRepository``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_codecatalyst._auth._signers
import aws_sdk_codecatalyst._auth._sigv4
from aws_sdk_codecatalyst._protocol.errors import parse_error_metadata_json
from aws_sdk_codecatalyst._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_codecatalyst._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codecatalyst.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.create_source_repository_request
    import aws_sdk_codecatalyst.types.create_source_repository_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_codecatalyst.errors.access_denied_exception

            raise aws_sdk_codecatalyst.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            import aws_sdk_codecatalyst.errors.conflict_exception

            raise aws_sdk_codecatalyst.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_codecatalyst.errors.resource_not_found_exception

            raise aws_sdk_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            import aws_sdk_codecatalyst.errors.service_quota_exceeded_exception

            raise aws_sdk_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_codecatalyst.errors.throttling_exception

            raise aws_sdk_codecatalyst.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_codecatalyst.errors.validation_exception

            raise aws_sdk_codecatalyst.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_codecatalyst.types.create_source_repository_response.CreateSourceRepositoryResponse:
    import aws_sdk_codecatalyst.types.create_source_repository_response

    out: aws_sdk_codecatalyst.types.create_source_repository_response.CreateSourceRepositoryResponse = aws_sdk_codecatalyst.types.create_source_repository_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_codecatalyst._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.bearer_provider is not None:
        return aws_sdk_codecatalyst._auth._signers.HttpBearerSigner(
            options.bearer_provider
        )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_codecatalyst.types.create_source_repository_request.CreateSourceRepositoryRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            UseFIPS=options.use_fips,
            Region=options.region,
            Endpoint=options.endpoint,
        )
    )
    url = (
        endpoint.url.rstrip("/")
        + "/v1/spaces/{spaceName}/projects/{projectName}/sourceRepositories/{name}"
    )
    url = url.replace("{spaceName}", quote(str(input["space_name"]), safe=""))
    url = url.replace("{projectName}", quote(str(input["project_name"]), safe=""))
    url = url.replace("{name}", quote(str(input["name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_codecatalyst.types.create_source_repository_request

    body: bytes | None = json.dumps(
        aws_sdk_codecatalyst.types.create_source_repository_request.serialize_json(
            input
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "PUT",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def create_source_repository(
    options: OperationOptions,
    input: aws_sdk_codecatalyst.types.create_source_repository_request.CreateSourceRepositoryRequest,
) -> tuple[
    aws_sdk_codecatalyst.types.create_source_repository_response.CreateSourceRepositoryResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_create_source_repository(
    options: AsyncOperationOptions,
    input: aws_sdk_codecatalyst.types.create_source_repository_request.CreateSourceRepositoryRequest,
) -> tuple[
    aws_sdk_codecatalyst.types.create_source_repository_response.CreateSourceRepositoryResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
