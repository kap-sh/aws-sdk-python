"""Generated from Smithy shape ``com.amazonaws.pinpointemail#SendEmail``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_pinpoint_email._auth._signers
import aws_sdk_pinpoint_email._auth._sigv4
import aws_sdk_pinpoint_email.errors.account_suspended_exception
import aws_sdk_pinpoint_email.errors.bad_request_exception
import aws_sdk_pinpoint_email.errors.limit_exceeded_exception
import aws_sdk_pinpoint_email.errors.mail_from_domain_not_verified_exception
import aws_sdk_pinpoint_email.errors.message_rejected
import aws_sdk_pinpoint_email.errors.not_found_exception
import aws_sdk_pinpoint_email.errors.sending_paused_exception
import aws_sdk_pinpoint_email.errors.too_many_requests_exception
import aws_sdk_pinpoint_email.types.destination
import aws_sdk_pinpoint_email.types.email_address_list
import aws_sdk_pinpoint_email.types.email_content
import aws_sdk_pinpoint_email.types.message_tag_list
import aws_sdk_pinpoint_email.types.send_email_request
import aws_sdk_pinpoint_email.types.send_email_response
from aws_sdk_pinpoint_email._protocol.errors import parse_error_metadata_json
from aws_sdk_pinpoint_email._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_pinpoint_email._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_pinpoint_email.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccountSuspendedException":
            raise aws_sdk_pinpoint_email.errors.account_suspended_exception.AccountSuspendedException.from_json(
                data
            )
        case "BadRequestException":
            raise aws_sdk_pinpoint_email.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "LimitExceededException":
            raise aws_sdk_pinpoint_email.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "MailFromDomainNotVerifiedException":
            raise aws_sdk_pinpoint_email.errors.mail_from_domain_not_verified_exception.MailFromDomainNotVerifiedException.from_json(
                data
            )
        case "MessageRejected":
            raise aws_sdk_pinpoint_email.errors.message_rejected.MessageRejected.from_json(
                data
            )
        case "NotFoundException":
            raise aws_sdk_pinpoint_email.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "SendingPausedException":
            raise aws_sdk_pinpoint_email.errors.sending_paused_exception.SendingPausedException.from_json(
                data
            )
        case "TooManyRequestsException":
            raise aws_sdk_pinpoint_email.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_pinpoint_email.types.send_email_response.SendEmailResponse:
    out: aws_sdk_pinpoint_email.types.send_email_response.SendEmailResponse = (
        aws_sdk_pinpoint_email.types.send_email_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_pinpoint_email.types.send_email_response.SendEmailResponse:
    out: aws_sdk_pinpoint_email.types.send_email_response.SendEmailResponse = (
        aws_sdk_pinpoint_email.types.send_email_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_pinpoint_email._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_pinpoint_email._auth._sigv4.build_sigv4_auth_scheme(
                "ses", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_pinpoint_email._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_pinpoint_email.types.send_email_request.SendEmailRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/email/outbound-emails"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        aws_sdk_pinpoint_email.types.send_email_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def send_email(
    options: OperationOptions,
    input_: aws_sdk_pinpoint_email.types.send_email_request.SendEmailRequest,
) -> tuple[
    aws_sdk_pinpoint_email.types.send_email_response.SendEmailResponse, zapros.Response
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


async def async_send_email(
    options: AsyncOperationOptions,
    input_: aws_sdk_pinpoint_email.types.send_email_request.SendEmailRequest,
) -> tuple[
    aws_sdk_pinpoint_email.types.send_email_response.SendEmailResponse, zapros.Response
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
