"""Generated from Smithy shape ``com.amazonaws.securityhub#DeleteConfigurationPolicy``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_securityhub._auth._signers
import aws_sdk_securityhub._auth._sigv4
from aws_sdk_securityhub._protocol.errors import parse_error_metadata_json
from aws_sdk_securityhub._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_securityhub._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_securityhub.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.delete_configuration_policy_request
    import aws_sdk_securityhub.types.delete_configuration_policy_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_securityhub.errors.access_denied_exception

            raise aws_sdk_securityhub.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalException":
            import aws_sdk_securityhub.errors.internal_exception

            raise aws_sdk_securityhub.errors.internal_exception.InternalException.from_json(
                data
            )
        case "InvalidAccessException":
            import aws_sdk_securityhub.errors.invalid_access_exception

            raise aws_sdk_securityhub.errors.invalid_access_exception.InvalidAccessException.from_json(
                data
            )
        case "InvalidInputException":
            import aws_sdk_securityhub.errors.invalid_input_exception

            raise aws_sdk_securityhub.errors.invalid_input_exception.InvalidInputException.from_json(
                data
            )
        case "LimitExceededException":
            import aws_sdk_securityhub.errors.limit_exceeded_exception

            raise aws_sdk_securityhub.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "ResourceConflictException":
            import aws_sdk_securityhub.errors.resource_conflict_exception

            raise aws_sdk_securityhub.errors.resource_conflict_exception.ResourceConflictException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_securityhub.errors.resource_not_found_exception

            raise aws_sdk_securityhub.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_securityhub.types.delete_configuration_policy_response.DeleteConfigurationPolicyResponse:
    out: aws_sdk_securityhub.types.delete_configuration_policy_response.DeleteConfigurationPolicyResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_securityhub._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_securityhub._auth._sigv4.build_sigv4_auth_scheme(
                "securityhub", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_securityhub._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_securityhub.types.delete_configuration_policy_request.DeleteConfigurationPolicyRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/configurationPolicy/{Identifier}"
    url = url.replace("{Identifier}", quote(str(input_["identifier"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_configuration_policy(
    options: OperationOptions,
    input_: aws_sdk_securityhub.types.delete_configuration_policy_request.DeleteConfigurationPolicyRequest,
) -> tuple[
    aws_sdk_securityhub.types.delete_configuration_policy_response.DeleteConfigurationPolicyResponse,
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


async def async_delete_configuration_policy(
    options: AsyncOperationOptions,
    input_: aws_sdk_securityhub.types.delete_configuration_policy_request.DeleteConfigurationPolicyRequest,
) -> tuple[
    aws_sdk_securityhub.types.delete_configuration_policy_response.DeleteConfigurationPolicyResponse,
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
