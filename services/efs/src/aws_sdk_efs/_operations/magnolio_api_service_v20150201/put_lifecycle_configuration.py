"""Generated from Smithy shape ``com.amazonaws.efs#PutLifecycleConfiguration``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_efs._auth._signers
import aws_sdk_efs._auth._sigv4
from aws_sdk_efs._protocol.errors import parse_error_metadata_json
from aws_sdk_efs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_efs._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_efs.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_efs.types.lifecycle_configuration_description
    import aws_sdk_efs.types.put_lifecycle_configuration_request


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequest":
            import aws_sdk_efs.errors.bad_request

            raise aws_sdk_efs.errors.bad_request.BadRequest.from_json(data)
        case "FileSystemNotFound":
            import aws_sdk_efs.errors.file_system_not_found

            raise aws_sdk_efs.errors.file_system_not_found.FileSystemNotFound.from_json(
                data
            )
        case "IncorrectFileSystemLifeCycleState":
            import aws_sdk_efs.errors.incorrect_file_system_life_cycle_state

            raise aws_sdk_efs.errors.incorrect_file_system_life_cycle_state.IncorrectFileSystemLifeCycleState.from_json(
                data
            )
        case "InternalServerError":
            import aws_sdk_efs.errors.internal_server_error

            raise aws_sdk_efs.errors.internal_server_error.InternalServerError.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_efs.types.lifecycle_configuration_description.LifecycleConfigurationDescription:
    import aws_sdk_efs.types.lifecycle_configuration_description

    out: aws_sdk_efs.types.lifecycle_configuration_description.LifecycleConfigurationDescription = aws_sdk_efs.types.lifecycle_configuration_description.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_efs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_efs._auth._sigv4.build_sigv4_auth_scheme(
                "elasticfilesystem", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_efs._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_efs.types.put_lifecycle_configuration_request.PutLifecycleConfigurationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/2015-02-01/file-systems/{FileSystemId}/lifecycle-configuration"
    )
    url = url.replace("{FileSystemId}", quote(str(input_["file_system_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_efs.types.put_lifecycle_configuration_request

    body: bytes | None = json.dumps(
        aws_sdk_efs.types.put_lifecycle_configuration_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def put_lifecycle_configuration(
    options: OperationOptions,
    input_: aws_sdk_efs.types.put_lifecycle_configuration_request.PutLifecycleConfigurationRequest,
) -> tuple[
    aws_sdk_efs.types.lifecycle_configuration_description.LifecycleConfigurationDescription,
    zapros.Response,
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


async def async_put_lifecycle_configuration(
    options: AsyncOperationOptions,
    input_: aws_sdk_efs.types.put_lifecycle_configuration_request.PutLifecycleConfigurationRequest,
) -> tuple[
    aws_sdk_efs.types.lifecycle_configuration_description.LifecycleConfigurationDescription,
    zapros.Response,
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
