"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#BatchUpdatePhoneNumber``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_chime_sdk_voice._auth._signers
import aws_sdk_chime_sdk_voice._auth._sigv4
import aws_sdk_chime_sdk_voice.errors.bad_request_exception
import aws_sdk_chime_sdk_voice.errors.forbidden_exception
import aws_sdk_chime_sdk_voice.errors.not_found_exception
import aws_sdk_chime_sdk_voice.errors.service_failure_exception
import aws_sdk_chime_sdk_voice.errors.service_unavailable_exception
import aws_sdk_chime_sdk_voice.errors.throttled_client_exception
import aws_sdk_chime_sdk_voice.errors.unauthorized_client_exception
import aws_sdk_chime_sdk_voice.types.batch_update_phone_number_request
import aws_sdk_chime_sdk_voice.types.batch_update_phone_number_response
import aws_sdk_chime_sdk_voice.types.phone_number_error_list
import aws_sdk_chime_sdk_voice.types.update_phone_number_request_item_list
from aws_sdk_chime_sdk_voice._protocol.errors import parse_error_metadata_json
from aws_sdk_chime_sdk_voice._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_chime_sdk_voice._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_chime_sdk_voice.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise aws_sdk_chime_sdk_voice.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ForbiddenException":
            raise aws_sdk_chime_sdk_voice.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "NotFoundException":
            raise aws_sdk_chime_sdk_voice.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "ServiceFailureException":
            raise aws_sdk_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "ThrottledClientException":
            raise aws_sdk_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException.from_json(
                data
            )
        case "UnauthorizedClientException":
            raise aws_sdk_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_chime_sdk_voice.types.batch_update_phone_number_response.BatchUpdatePhoneNumberResponse:
    out: aws_sdk_chime_sdk_voice.types.batch_update_phone_number_response.BatchUpdatePhoneNumberResponse = aws_sdk_chime_sdk_voice.types.batch_update_phone_number_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_chime_sdk_voice.types.batch_update_phone_number_response.BatchUpdatePhoneNumberResponse:
    out: aws_sdk_chime_sdk_voice.types.batch_update_phone_number_response.BatchUpdatePhoneNumberResponse = aws_sdk_chime_sdk_voice.types.batch_update_phone_number_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_chime_sdk_voice._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_chime_sdk_voice._auth._sigv4.build_sigv4_auth_scheme(
                "chime", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_chime_sdk_voice._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_chime_sdk_voice.types.batch_update_phone_number_request.BatchUpdatePhoneNumberRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/phone-numbers?operation=batch-update"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        aws_sdk_chime_sdk_voice.types.batch_update_phone_number_request.serialize_json(
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


def batch_update_phone_number(
    options: OperationOptions,
    input_: aws_sdk_chime_sdk_voice.types.batch_update_phone_number_request.BatchUpdatePhoneNumberRequest,
) -> tuple[
    aws_sdk_chime_sdk_voice.types.batch_update_phone_number_response.BatchUpdatePhoneNumberResponse,
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


async def async_batch_update_phone_number(
    options: AsyncOperationOptions,
    input_: aws_sdk_chime_sdk_voice.types.batch_update_phone_number_request.BatchUpdatePhoneNumberRequest,
) -> tuple[
    aws_sdk_chime_sdk_voice.types.batch_update_phone_number_response.BatchUpdatePhoneNumberResponse,
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
