"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptSubscriptionRequest``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any, cast
from aws_sdk_datazone._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_datazone._rule_engine._endpoint_runtime import apply_label
import jmespath
import zapros
from urllib.parse import quote, urlencode
from aws_sdk_datazone.errors import ServiceError, UnknownServiceError
from aws_sdk_datazone._protocol.errors import parse_error_metadata_json
import json
import aws_sdk_datazone._auth._signers
import aws_sdk_datazone._auth._sigv4
from aws_sdk_datazone._services._pipeline import AsyncOperationOptions, OperationOptions
import datetime
from email.utils import parsedate_to_datetime as _parse_http_date

if TYPE_CHECKING:
    import aws_sdk_datazone.types.accept_subscription_request_input
    import aws_sdk_datazone.types.accept_subscription_request_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_datazone.errors.access_denied_exception

            raise aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_datazone.errors.throttling_exception

            raise aws_sdk_datazone.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "UnauthorizedException":
            import aws_sdk_datazone.errors.unauthorized_exception

            raise aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException.from_json(
                data
            )
        case "ConflictException":
            import aws_sdk_datazone.errors.conflict_exception

            raise aws_sdk_datazone.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_datazone.errors.internal_server_exception

            raise aws_sdk_datazone.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_datazone.errors.resource_not_found_exception

            raise aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            import aws_sdk_datazone.errors.service_quota_exceeded_exception

            raise aws_sdk_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_datazone.errors.validation_exception

            raise aws_sdk_datazone.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_datazone.types.accept_subscription_request_output.AcceptSubscriptionRequestOutput:
    import aws_sdk_datazone.types.accept_subscription_request_output

    out: aws_sdk_datazone.types.accept_subscription_request_output.AcceptSubscriptionRequestOutput = aws_sdk_datazone.types.accept_subscription_request_output.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_datazone._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_datazone._auth._sigv4.build_sigv4_auth_scheme(
                "datazone", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_datazone._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_datazone.types.accept_subscription_request_input.AcceptSubscriptionRequestInput,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = (
        endpoint.url.rstrip("/")
        + "/v2/domains/{domainIdentifier}/subscription-requests/{identifier}/accept"
    )
    url = url.replace(
        "{domainIdentifier}", quote(str(input["domain_identifier"]), safe="")
    )
    url = url.replace("{identifier}", quote(str(input["identifier"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_datazone.types.accept_subscription_request_input

    body: bytes | None = json.dumps(
        aws_sdk_datazone.types.accept_subscription_request_input.serialize_json(input)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "PUT",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def accept_subscription_request(
    options: OperationOptions,
    input: aws_sdk_datazone.types.accept_subscription_request_input.AcceptSubscriptionRequestInput,
) -> tuple[
    aws_sdk_datazone.types.accept_subscription_request_output.AcceptSubscriptionRequestOutput,
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


async def async_accept_subscription_request(
    options: AsyncOperationOptions,
    input: aws_sdk_datazone.types.accept_subscription_request_input.AcceptSubscriptionRequestInput,
) -> tuple[
    aws_sdk_datazone.types.accept_subscription_request_output.AcceptSubscriptionRequestOutput,
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
