"""Generated from Smithy shape ``com.amazonaws.ram#ListPendingInvitationResources``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_ram._auth._signers
import aws_sdk_ram._auth._sigv4
from aws_sdk_ram._protocol.errors import parse_error_metadata_json
from aws_sdk_ram._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_ram._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_ram.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.list_pending_invitation_resources_request
    import aws_sdk_ram.types.list_pending_invitation_resources_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidNextTokenException":
            import aws_sdk_ram.errors.invalid_next_token_exception

            raise aws_sdk_ram.errors.invalid_next_token_exception.InvalidNextTokenException.from_json(
                data
            )
        case "InvalidParameterException":
            import aws_sdk_ram.errors.invalid_parameter_exception

            raise aws_sdk_ram.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case "MalformedArnException":
            import aws_sdk_ram.errors.malformed_arn_exception

            raise aws_sdk_ram.errors.malformed_arn_exception.MalformedArnException.from_json(
                data
            )
        case "MissingRequiredParameterException":
            import aws_sdk_ram.errors.missing_required_parameter_exception

            raise aws_sdk_ram.errors.missing_required_parameter_exception.MissingRequiredParameterException.from_json(
                data
            )
        case "ResourceShareInvitationAlreadyRejectedException":
            import aws_sdk_ram.errors.resource_share_invitation_already_rejected_exception

            raise aws_sdk_ram.errors.resource_share_invitation_already_rejected_exception.ResourceShareInvitationAlreadyRejectedException.from_json(
                data
            )
        case "ResourceShareInvitationArnNotFoundException":
            import aws_sdk_ram.errors.resource_share_invitation_arn_not_found_exception

            raise aws_sdk_ram.errors.resource_share_invitation_arn_not_found_exception.ResourceShareInvitationArnNotFoundException.from_json(
                data
            )
        case "ResourceShareInvitationExpiredException":
            import aws_sdk_ram.errors.resource_share_invitation_expired_exception

            raise aws_sdk_ram.errors.resource_share_invitation_expired_exception.ResourceShareInvitationExpiredException.from_json(
                data
            )
        case "ServerInternalException":
            import aws_sdk_ram.errors.server_internal_exception

            raise aws_sdk_ram.errors.server_internal_exception.ServerInternalException.from_json(
                data
            )
        case "ServiceUnavailableException":
            import aws_sdk_ram.errors.service_unavailable_exception

            raise aws_sdk_ram.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_ram.types.list_pending_invitation_resources_response.ListPendingInvitationResourcesResponse:
    import aws_sdk_ram.types.list_pending_invitation_resources_response

    out: aws_sdk_ram.types.list_pending_invitation_resources_response.ListPendingInvitationResourcesResponse = aws_sdk_ram.types.list_pending_invitation_resources_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_ram._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_ram._auth._sigv4.build_sigv4_auth_scheme("ram", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_ram._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_ram.types.list_pending_invitation_resources_request.ListPendingInvitationResourcesRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/listpendinginvitationresources"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_ram.types.list_pending_invitation_resources_request

    body: bytes | None = json.dumps(
        aws_sdk_ram.types.list_pending_invitation_resources_request.serialize_json(
            input
        )
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


def list_pending_invitation_resources(
    options: OperationOptions,
    input: aws_sdk_ram.types.list_pending_invitation_resources_request.ListPendingInvitationResourcesRequest,
) -> tuple[
    aws_sdk_ram.types.list_pending_invitation_resources_response.ListPendingInvitationResourcesResponse,
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


async def async_list_pending_invitation_resources(
    options: AsyncOperationOptions,
    input: aws_sdk_ram.types.list_pending_invitation_resources_request.ListPendingInvitationResourcesRequest,
) -> tuple[
    aws_sdk_ram.types.list_pending_invitation_resources_response.ListPendingInvitationResourcesResponse,
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
