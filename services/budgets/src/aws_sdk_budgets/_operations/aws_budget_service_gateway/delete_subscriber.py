"""Generated from Smithy shape ``com.amazonaws.budgets#DeleteSubscriber``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_budgets._auth._signers
import aws_sdk_budgets._auth._sigv4
from aws_sdk_budgets._protocol.errors import parse_error_metadata_json
from aws_sdk_budgets._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_budgets._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_budgets.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.delete_subscriber_request
    import aws_sdk_budgets.types.delete_subscriber_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_budgets.errors.access_denied_exception

            raise aws_sdk_budgets.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "InternalErrorException":
            import aws_sdk_budgets.errors.internal_error_exception

            raise aws_sdk_budgets.errors.internal_error_exception.InternalErrorException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            import aws_sdk_budgets.errors.invalid_parameter_exception

            raise aws_sdk_budgets.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "NotFoundException":
            import aws_sdk_budgets.errors.not_found_exception

            raise aws_sdk_budgets.errors.not_found_exception.NotFoundException.from_aws_json_1_1(
                data
            )
        case "ThrottlingException":
            import aws_sdk_budgets.errors.throttling_exception

            raise aws_sdk_budgets.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_budgets.types.delete_subscriber_response.DeleteSubscriberResponse:
    out: aws_sdk_budgets.types.delete_subscriber_response.DeleteSubscriberResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_budgets._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_budgets._auth._sigv4.build_sigv4_auth_scheme(
                "budgets", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_budgets._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_budgets.types.delete_subscriber_request.DeleteSubscriberRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSBudgetServiceGateway.DeleteSubscriber"
    import aws_sdk_budgets.types.delete_subscriber_request

    body: bytes | None = json.dumps(
        aws_sdk_budgets.types.delete_subscriber_request.serialize_aws_json_1_1(input)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
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


def delete_subscriber(
    options: OperationOptions,
    input: aws_sdk_budgets.types.delete_subscriber_request.DeleteSubscriberRequest,
) -> tuple[
    aws_sdk_budgets.types.delete_subscriber_response.DeleteSubscriberResponse,
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


async def async_delete_subscriber(
    options: AsyncOperationOptions,
    input: aws_sdk_budgets.types.delete_subscriber_request.DeleteSubscriberRequest,
) -> tuple[
    aws_sdk_budgets.types.delete_subscriber_response.DeleteSubscriberResponse,
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
