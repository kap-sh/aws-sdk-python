"""Generated from Smithy shape ``com.amazonaws.ram#AcceptResourceShareInvitation``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_ram._auth._signers
import aws_sdk_ram._auth._sigv4
import aws_sdk_ram.errors.idempotent_parameter_mismatch_exception
import aws_sdk_ram.errors.invalid_client_token_exception
import aws_sdk_ram.errors.malformed_arn_exception
import aws_sdk_ram.errors.operation_not_permitted_exception
import aws_sdk_ram.errors.resource_share_invitation_already_accepted_exception
import aws_sdk_ram.errors.resource_share_invitation_already_rejected_exception
import aws_sdk_ram.errors.resource_share_invitation_arn_not_found_exception
import aws_sdk_ram.errors.resource_share_invitation_expired_exception
import aws_sdk_ram.errors.server_internal_exception
import aws_sdk_ram.errors.service_unavailable_exception
import aws_sdk_ram.types.accept_resource_share_invitation_request
import aws_sdk_ram.types.accept_resource_share_invitation_response
import aws_sdk_ram.types.resource_share_invitation
from aws_sdk_ram._protocol.errors import parse_error_metadata_json
from aws_sdk_ram._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_ram._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_ram.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "IdempotentParameterMismatchException":
            raise aws_sdk_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException.from_json(
                data
            )
        case "InvalidClientTokenException":
            raise aws_sdk_ram.errors.invalid_client_token_exception.InvalidClientTokenException.from_json(
                data
            )
        case "MalformedArnException":
            raise aws_sdk_ram.errors.malformed_arn_exception.MalformedArnException.from_json(
                data
            )
        case "OperationNotPermittedException":
            raise aws_sdk_ram.errors.operation_not_permitted_exception.OperationNotPermittedException.from_json(
                data
            )
        case "ResourceShareInvitationAlreadyAcceptedException":
            raise aws_sdk_ram.errors.resource_share_invitation_already_accepted_exception.ResourceShareInvitationAlreadyAcceptedException.from_json(
                data
            )
        case "ResourceShareInvitationAlreadyRejectedException":
            raise aws_sdk_ram.errors.resource_share_invitation_already_rejected_exception.ResourceShareInvitationAlreadyRejectedException.from_json(
                data
            )
        case "ResourceShareInvitationArnNotFoundException":
            raise aws_sdk_ram.errors.resource_share_invitation_arn_not_found_exception.ResourceShareInvitationArnNotFoundException.from_json(
                data
            )
        case "ResourceShareInvitationExpiredException":
            raise aws_sdk_ram.errors.resource_share_invitation_expired_exception.ResourceShareInvitationExpiredException.from_json(
                data
            )
        case "ServerInternalException":
            raise aws_sdk_ram.errors.server_internal_exception.ServerInternalException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_ram.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_ram.types.accept_resource_share_invitation_response.AcceptResourceShareInvitationResponse:
    out: aws_sdk_ram.types.accept_resource_share_invitation_response.AcceptResourceShareInvitationResponse = aws_sdk_ram.types.accept_resource_share_invitation_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_ram.types.accept_resource_share_invitation_response.AcceptResourceShareInvitationResponse:
    out: aws_sdk_ram.types.accept_resource_share_invitation_response.AcceptResourceShareInvitationResponse = aws_sdk_ram.types.accept_resource_share_invitation_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_ram._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_ram.types.accept_resource_share_invitation_request.AcceptResourceShareInvitationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/acceptresourceshareinvitation"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        aws_sdk_ram.types.accept_resource_share_invitation_request.serialize_json(
            input_
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def accept_resource_share_invitation(
    options: OperationOptions,
    input_: aws_sdk_ram.types.accept_resource_share_invitation_request.AcceptResourceShareInvitationRequest,
) -> tuple[
    aws_sdk_ram.types.accept_resource_share_invitation_response.AcceptResourceShareInvitationResponse,
    zapros.Response,
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


async def async_accept_resource_share_invitation(
    options: AsyncOperationOptions,
    input_: aws_sdk_ram.types.accept_resource_share_invitation_request.AcceptResourceShareInvitationRequest,
) -> tuple[
    aws_sdk_ram.types.accept_resource_share_invitation_response.AcceptResourceShareInvitationResponse,
    zapros.Response,
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
