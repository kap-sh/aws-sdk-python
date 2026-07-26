"""Generated from Smithy shape ``com.amazonaws.socialmessaging#AssociateWhatsAppBusinessAccount``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_socialmessaging._auth._signers
import capo_socialmessaging._auth._sigv4
import capo_socialmessaging.errors.access_denied_exception
import capo_socialmessaging.errors.dependency_exception
import capo_socialmessaging.errors.invalid_parameters_exception
import capo_socialmessaging.errors.limit_exceeded_exception
import capo_socialmessaging.errors.throttled_request_exception
import capo_socialmessaging.errors.validation_exception
import capo_socialmessaging.types.associate_whats_app_business_account_input
import capo_socialmessaging.types.associate_whats_app_business_account_output
import capo_socialmessaging.types.whats_app_setup_finalization
import capo_socialmessaging.types.whats_app_signup_callback
import capo_socialmessaging.types.whats_app_signup_callback_result
from capo_socialmessaging._protocol.errors import parse_error_metadata_json
from capo_socialmessaging._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_socialmessaging._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_socialmessaging.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_socialmessaging.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ValidationException":
            raise capo_socialmessaging.errors.validation_exception.ValidationException.from_json(
                data
            )
        case "DependencyException":
            raise capo_socialmessaging.errors.dependency_exception.DependencyException.from_json(
                data
            )
        case "InvalidParametersException":
            raise capo_socialmessaging.errors.invalid_parameters_exception.InvalidParametersException.from_json(
                data
            )
        case "LimitExceededException":
            raise capo_socialmessaging.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "ThrottledRequestException":
            raise capo_socialmessaging.errors.throttled_request_exception.ThrottledRequestException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_socialmessaging.types.associate_whats_app_business_account_output.AssociateWhatsAppBusinessAccountOutput:
    out: capo_socialmessaging.types.associate_whats_app_business_account_output.AssociateWhatsAppBusinessAccountOutput = capo_socialmessaging.types.associate_whats_app_business_account_output.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_socialmessaging.types.associate_whats_app_business_account_output.AssociateWhatsAppBusinessAccountOutput:
    out: capo_socialmessaging.types.associate_whats_app_business_account_output.AssociateWhatsAppBusinessAccountOutput = capo_socialmessaging.types.associate_whats_app_business_account_output.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_socialmessaging._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_socialmessaging._auth._sigv4.build_sigv4_auth_scheme(
                "social-messaging", options.region
            )
        )
        if sigv4_config is not None:
            return capo_socialmessaging._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_socialmessaging.types.associate_whats_app_business_account_input.AssociateWhatsAppBusinessAccountInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/whatsapp/signup"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_socialmessaging.types.associate_whats_app_business_account_input.serialize_json(
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


def associate_whats_app_business_account(
    options: OperationOptions,
    input_: capo_socialmessaging.types.associate_whats_app_business_account_input.AssociateWhatsAppBusinessAccountInput,
) -> tuple[
    capo_socialmessaging.types.associate_whats_app_business_account_output.AssociateWhatsAppBusinessAccountOutput,
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


async def async_associate_whats_app_business_account(
    options: AsyncOperationOptions,
    input_: capo_socialmessaging.types.associate_whats_app_business_account_input.AssociateWhatsAppBusinessAccountInput,
) -> tuple[
    capo_socialmessaging.types.associate_whats_app_business_account_output.AssociateWhatsAppBusinessAccountOutput,
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
