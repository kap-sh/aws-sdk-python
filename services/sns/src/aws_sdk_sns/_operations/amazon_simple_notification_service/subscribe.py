"""Generated from Smithy shape ``com.amazonaws.sns#Subscribe``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_sns._auth._signers
import aws_sdk_sns._auth._sigv4
import aws_sdk_sns.errors.authorization_error_exception
import aws_sdk_sns.errors.filter_policy_limit_exceeded_exception
import aws_sdk_sns.errors.internal_error_exception
import aws_sdk_sns.errors.invalid_parameter_exception
import aws_sdk_sns.errors.invalid_security_exception
import aws_sdk_sns.errors.not_found_exception
import aws_sdk_sns.errors.replay_limit_exceeded_exception
import aws_sdk_sns.errors.subscription_limit_exceeded_exception
import aws_sdk_sns.types.subscribe_input
import aws_sdk_sns.types.subscribe_response
import aws_sdk_sns.types.subscription_attributes_map
from aws_sdk_sns._protocol.errors import parse_error_metadata
from aws_sdk_sns._protocol.xml import fromstring
from aws_sdk_sns._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_sns._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_sns.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AuthorizationErrorException":
            raise aws_sdk_sns.errors.authorization_error_exception.AuthorizationErrorException.from_query(
                root
            )
        case "FilterPolicyLimitExceededException":
            raise aws_sdk_sns.errors.filter_policy_limit_exceeded_exception.FilterPolicyLimitExceededException.from_query(
                root
            )
        case "InternalErrorException":
            raise aws_sdk_sns.errors.internal_error_exception.InternalErrorException.from_query(
                root
            )
        case "InvalidParameterException":
            raise aws_sdk_sns.errors.invalid_parameter_exception.InvalidParameterException.from_query(
                root
            )
        case "InvalidSecurityException":
            raise aws_sdk_sns.errors.invalid_security_exception.InvalidSecurityException.from_query(
                root
            )
        case "NotFoundException":
            raise aws_sdk_sns.errors.not_found_exception.NotFoundException.from_query(
                root
            )
        case "ReplayLimitExceededException":
            raise aws_sdk_sns.errors.replay_limit_exceeded_exception.ReplayLimitExceededException.from_query(
                root
            )
        case "SubscriptionLimitExceededException":
            raise aws_sdk_sns.errors.subscription_limit_exceeded_exception.SubscriptionLimitExceededException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_sns.types.subscribe_response.SubscribeResponse:
    root = fromstring(response.read())
    result = root.find("SubscribeResult")
    out: aws_sdk_sns.types.subscribe_response.SubscribeResponse = (
        aws_sdk_sns.types.subscribe_response.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_sns.types.subscribe_response.SubscribeResponse:
    root = fromstring(await response.aread())
    result = root.find("SubscribeResult")
    out: aws_sdk_sns.types.subscribe_response.SubscribeResponse = (
        aws_sdk_sns.types.subscribe_response.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sns._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_sns._auth._sigv4.build_sigv4_auth_scheme("sns", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_sns._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_sns.types.subscribe_input.SubscribeInput,
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
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "Subscribe"))
    pairs.append(("Version", "2010-03-31"))
    aws_sdk_sns.types.subscribe_input.serialize_query(input_, pairs, "")
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def subscribe(
    options: OperationOptions, input_: aws_sdk_sns.types.subscribe_input.SubscribeInput
) -> tuple[aws_sdk_sns.types.subscribe_response.SubscribeResponse, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_subscribe(
    options: AsyncOperationOptions,
    input_: aws_sdk_sns.types.subscribe_input.SubscribeInput,
) -> tuple[aws_sdk_sns.types.subscribe_response.SubscribeResponse, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
