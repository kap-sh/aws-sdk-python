"""Generated from Smithy shape ``com.amazonaws.socialmessaging#DeleteWhatsAppMessageMedia``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_socialmessaging._auth._signers
import aws_sdk_socialmessaging._auth._sigv4
from aws_sdk_socialmessaging._protocol.errors import parse_error_metadata_json
from aws_sdk_socialmessaging._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_socialmessaging._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_socialmessaging.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.delete_whats_app_message_media_input
    import aws_sdk_socialmessaging.types.delete_whats_app_message_media_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_socialmessaging.errors.access_denied_exception

            raise aws_sdk_socialmessaging.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_socialmessaging.errors.validation_exception

            raise aws_sdk_socialmessaging.errors.validation_exception.ValidationException.from_json(
                data
            )
        case "AccessDeniedByMetaException":
            import aws_sdk_socialmessaging.errors.access_denied_by_meta_exception

            raise aws_sdk_socialmessaging.errors.access_denied_by_meta_exception.AccessDeniedByMetaException.from_json(
                data
            )
        case "DependencyException":
            import aws_sdk_socialmessaging.errors.dependency_exception

            raise aws_sdk_socialmessaging.errors.dependency_exception.DependencyException.from_json(
                data
            )
        case "InternalServiceException":
            import aws_sdk_socialmessaging.errors.internal_service_exception

            raise aws_sdk_socialmessaging.errors.internal_service_exception.InternalServiceException.from_json(
                data
            )
        case "InvalidParametersException":
            import aws_sdk_socialmessaging.errors.invalid_parameters_exception

            raise aws_sdk_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_socialmessaging.errors.resource_not_found_exception

            raise aws_sdk_socialmessaging.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottledRequestException":
            import aws_sdk_socialmessaging.errors.throttled_request_exception

            raise aws_sdk_socialmessaging.errors.throttled_request_exception.ThrottledRequestException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_socialmessaging.types.delete_whats_app_message_media_output.DeleteWhatsAppMessageMediaOutput:
    import aws_sdk_socialmessaging.types.delete_whats_app_message_media_output

    out: aws_sdk_socialmessaging.types.delete_whats_app_message_media_output.DeleteWhatsAppMessageMediaOutput = aws_sdk_socialmessaging.types.delete_whats_app_message_media_output.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_socialmessaging._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_socialmessaging._auth._sigv4.build_sigv4_auth_scheme(
                "social-messaging", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_socialmessaging._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_socialmessaging.types.delete_whats_app_message_media_input.DeleteWhatsAppMessageMediaInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/whatsapp/media"
    params: dict[str, str] = {}
    if "media_id" in input_:
        params["mediaId"] = str(input_["media_id"])
    if "origination_phone_number_id" in input_:
        params["originationPhoneNumberId"] = str(input_["origination_phone_number_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_whats_app_message_media(
    options: OperationOptions,
    input_: aws_sdk_socialmessaging.types.delete_whats_app_message_media_input.DeleteWhatsAppMessageMediaInput,
) -> tuple[
    aws_sdk_socialmessaging.types.delete_whats_app_message_media_output.DeleteWhatsAppMessageMediaOutput,
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


async def async_delete_whats_app_message_media(
    options: AsyncOperationOptions,
    input_: aws_sdk_socialmessaging.types.delete_whats_app_message_media_input.DeleteWhatsAppMessageMediaInput,
) -> tuple[
    aws_sdk_socialmessaging.types.delete_whats_app_message_media_output.DeleteWhatsAppMessageMediaOutput,
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
