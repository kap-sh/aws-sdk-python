"""Generated from Smithy shape ``com.amazonaws.cloud9#UpdateEnvironmentMembership``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_cloud9._auth._signers
import aws_sdk_cloud9._auth._sigv4
from aws_sdk_cloud9._protocol.errors import parse_error_metadata_json
from aws_sdk_cloud9._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloud9._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_cloud9.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.update_environment_membership_request
    import aws_sdk_cloud9.types.update_environment_membership_result


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            import aws_sdk_cloud9.errors.bad_request_exception

            raise aws_sdk_cloud9.errors.bad_request_exception.BadRequestException.from_aws_json_1_1(
                data
            )
        case "ConflictException":
            import aws_sdk_cloud9.errors.conflict_exception

            raise aws_sdk_cloud9.errors.conflict_exception.ConflictException.from_aws_json_1_1(
                data
            )
        case "ForbiddenException":
            import aws_sdk_cloud9.errors.forbidden_exception

            raise aws_sdk_cloud9.errors.forbidden_exception.ForbiddenException.from_aws_json_1_1(
                data
            )
        case "InternalServerErrorException":
            import aws_sdk_cloud9.errors.internal_server_error_exception

            raise aws_sdk_cloud9.errors.internal_server_error_exception.InternalServerErrorException.from_aws_json_1_1(
                data
            )
        case "LimitExceededException":
            import aws_sdk_cloud9.errors.limit_exceeded_exception

            raise aws_sdk_cloud9.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case "NotFoundException":
            import aws_sdk_cloud9.errors.not_found_exception

            raise aws_sdk_cloud9.errors.not_found_exception.NotFoundException.from_aws_json_1_1(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_cloud9.errors.too_many_requests_exception

            raise aws_sdk_cloud9.errors.too_many_requests_exception.TooManyRequestsException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cloud9.types.update_environment_membership_result.UpdateEnvironmentMembershipResult:
    import aws_sdk_cloud9.types.update_environment_membership_result

    out: aws_sdk_cloud9.types.update_environment_membership_result.UpdateEnvironmentMembershipResult = aws_sdk_cloud9.types.update_environment_membership_result.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloud9._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cloud9._auth._sigv4.build_sigv4_auth_scheme(
                "cloud9", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cloud9._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_cloud9.types.update_environment_membership_request.UpdateEnvironmentMembershipRequest,
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
    headers["X-Amz-Target"] = (
        "AWSCloud9WorkspaceManagementService.UpdateEnvironmentMembership"
    )
    import aws_sdk_cloud9.types.update_environment_membership_request

    body: bytes | None = json.dumps(
        aws_sdk_cloud9.types.update_environment_membership_request.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def update_environment_membership(
    options: OperationOptions,
    input_: aws_sdk_cloud9.types.update_environment_membership_request.UpdateEnvironmentMembershipRequest,
) -> tuple[
    aws_sdk_cloud9.types.update_environment_membership_result.UpdateEnvironmentMembershipResult,
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


async def async_update_environment_membership(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloud9.types.update_environment_membership_request.UpdateEnvironmentMembershipRequest,
) -> tuple[
    aws_sdk_cloud9.types.update_environment_membership_result.UpdateEnvironmentMembershipResult,
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
