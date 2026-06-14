"""Generated from Smithy shape ``com.amazonaws.workdocs#DeactivateUser``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_workdocs._auth._signers
import aws_sdk_workdocs._auth._sigv4
from aws_sdk_workdocs._protocol.errors import parse_error_metadata_json
from aws_sdk_workdocs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_workdocs._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_workdocs.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.deactivate_user_request


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "EntityNotExistsException":
            import aws_sdk_workdocs.errors.entity_not_exists_exception

            raise aws_sdk_workdocs.errors.entity_not_exists_exception.EntityNotExistsException.from_json(
                data
            )
        case "FailedDependencyException":
            import aws_sdk_workdocs.errors.failed_dependency_exception

            raise aws_sdk_workdocs.errors.failed_dependency_exception.FailedDependencyException.from_json(
                data
            )
        case "ServiceUnavailableException":
            import aws_sdk_workdocs.errors.service_unavailable_exception

            raise aws_sdk_workdocs.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "UnauthorizedOperationException":
            import aws_sdk_workdocs.errors.unauthorized_operation_exception

            raise aws_sdk_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException.from_json(
                data
            )
        case "UnauthorizedResourceAccessException":
            import aws_sdk_workdocs.errors.unauthorized_resource_access_exception

            raise aws_sdk_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_workdocs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
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
    input_: aws_sdk_workdocs.types.deactivate_user_request.DeactivateUserRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/api/v1/users/{UserId}/activation"
    url = url.replace("{UserId}", quote(str(input_["user_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "authentication_token" in input_:
        headers["Authentication"] = str(input_["authentication_token"])
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def deactivate_user(
    options: OperationOptions,
    input_: aws_sdk_workdocs.types.deactivate_user_request.DeactivateUserRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return None, response
    except BaseException:
        response.close()
        raise


async def async_deactivate_user(
    options: AsyncOperationOptions,
    input_: aws_sdk_workdocs.types.deactivate_user_request.DeactivateUserRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return None, response
    except BaseException:
        await response.aclose()
        raise
