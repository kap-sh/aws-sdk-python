"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateFolder``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_workdocs._auth._signers
import aws_sdk_workdocs._auth._sigv4
import aws_sdk_workdocs.errors.concurrent_modification_exception
import aws_sdk_workdocs.errors.conflicting_operation_exception
import aws_sdk_workdocs.errors.entity_already_exists_exception
import aws_sdk_workdocs.errors.entity_not_exists_exception
import aws_sdk_workdocs.errors.failed_dependency_exception
import aws_sdk_workdocs.errors.limit_exceeded_exception
import aws_sdk_workdocs.errors.prohibited_state_exception
import aws_sdk_workdocs.errors.service_unavailable_exception
import aws_sdk_workdocs.errors.unauthorized_operation_exception
import aws_sdk_workdocs.errors.unauthorized_resource_access_exception
import aws_sdk_workdocs.types.create_folder_request
import aws_sdk_workdocs.types.create_folder_response
import aws_sdk_workdocs.types.folder_metadata
from aws_sdk_workdocs._protocol.errors import parse_error_metadata_json
from aws_sdk_workdocs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_workdocs._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_workdocs.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConcurrentModificationException":
            raise aws_sdk_workdocs.errors.concurrent_modification_exception.ConcurrentModificationException.from_json(
                data
            )
        case "ConflictingOperationException":
            raise aws_sdk_workdocs.errors.conflicting_operation_exception.ConflictingOperationException.from_json(
                data
            )
        case "EntityAlreadyExistsException":
            raise aws_sdk_workdocs.errors.entity_already_exists_exception.EntityAlreadyExistsException.from_json(
                data
            )
        case "EntityNotExistsException":
            raise aws_sdk_workdocs.errors.entity_not_exists_exception.EntityNotExistsException.from_json(
                data
            )
        case "FailedDependencyException":
            raise aws_sdk_workdocs.errors.failed_dependency_exception.FailedDependencyException.from_json(
                data
            )
        case "LimitExceededException":
            raise aws_sdk_workdocs.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "ProhibitedStateException":
            raise aws_sdk_workdocs.errors.prohibited_state_exception.ProhibitedStateException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_workdocs.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "UnauthorizedOperationException":
            raise aws_sdk_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException.from_json(
                data
            )
        case "UnauthorizedResourceAccessException":
            raise aws_sdk_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_workdocs.types.create_folder_response.CreateFolderResponse:
    out: aws_sdk_workdocs.types.create_folder_response.CreateFolderResponse = (
        aws_sdk_workdocs.types.create_folder_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_workdocs.types.create_folder_response.CreateFolderResponse:
    out: aws_sdk_workdocs.types.create_folder_response.CreateFolderResponse = (
        aws_sdk_workdocs.types.create_folder_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_workdocs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_workdocs._auth._sigv4.build_sigv4_auth_scheme(
                "workdocs", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_workdocs._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_workdocs.types.create_folder_request.CreateFolderRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/api/v1/folders"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "authentication_token" in input_:
        headers["Authentication"] = str(input_["authentication_token"])
    import aws_sdk_workdocs.types.create_folder_request

    body: bytes | None = json.dumps(
        aws_sdk_workdocs.types.create_folder_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_folder(
    options: OperationOptions,
    input_: aws_sdk_workdocs.types.create_folder_request.CreateFolderRequest,
) -> tuple[
    aws_sdk_workdocs.types.create_folder_response.CreateFolderResponse, zapros.Response
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_create_folder(
    options: AsyncOperationOptions,
    input_: aws_sdk_workdocs.types.create_folder_request.CreateFolderRequest,
) -> tuple[
    aws_sdk_workdocs.types.create_folder_response.CreateFolderResponse, zapros.Response
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
