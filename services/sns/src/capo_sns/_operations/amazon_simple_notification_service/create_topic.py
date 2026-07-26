"""Generated from Smithy shape ``com.amazonaws.sns#CreateTopic``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_sns._auth._signers
import capo_sns._auth._sigv4
import capo_sns.errors.authorization_error_exception
import capo_sns.errors.concurrent_access_exception
import capo_sns.errors.internal_error_exception
import capo_sns.errors.invalid_parameter_exception
import capo_sns.errors.invalid_security_exception
import capo_sns.errors.stale_tag_exception
import capo_sns.errors.tag_limit_exceeded_exception
import capo_sns.errors.tag_policy_exception
import capo_sns.errors.topic_limit_exceeded_exception
import capo_sns.types.create_topic_input
import capo_sns.types.create_topic_response
import capo_sns.types.tag_list
import capo_sns.types.topic_attributes_map
from capo_sns._protocol.errors import parse_error_metadata
from capo_sns._protocol.xml import fromstring
from capo_sns._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_sns._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_sns.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AuthorizationErrorException":
            raise capo_sns.errors.authorization_error_exception.AuthorizationErrorException.from_query(
                root
            )
        case "ConcurrentAccessException":
            raise capo_sns.errors.concurrent_access_exception.ConcurrentAccessException.from_query(
                root
            )
        case "InternalErrorException":
            raise capo_sns.errors.internal_error_exception.InternalErrorException.from_query(
                root
            )
        case "InvalidParameterException":
            raise capo_sns.errors.invalid_parameter_exception.InvalidParameterException.from_query(
                root
            )
        case "InvalidSecurityException":
            raise capo_sns.errors.invalid_security_exception.InvalidSecurityException.from_query(
                root
            )
        case "StaleTagException":
            raise capo_sns.errors.stale_tag_exception.StaleTagException.from_query(root)
        case "TagLimitExceededException":
            raise capo_sns.errors.tag_limit_exceeded_exception.TagLimitExceededException.from_query(
                root
            )
        case "TagPolicyException":
            raise capo_sns.errors.tag_policy_exception.TagPolicyException.from_query(
                root
            )
        case "TopicLimitExceededException":
            raise capo_sns.errors.topic_limit_exceeded_exception.TopicLimitExceededException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_sns.types.create_topic_response.CreateTopicResponse:
    root = fromstring(response.read())
    result = root.find("CreateTopicResult")
    out: capo_sns.types.create_topic_response.CreateTopicResponse = (
        capo_sns.types.create_topic_response.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_sns.types.create_topic_response.CreateTopicResponse:
    root = fromstring(await response.aread())
    result = root.find("CreateTopicResult")
    out: capo_sns.types.create_topic_response.CreateTopicResponse = (
        capo_sns.types.create_topic_response.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_sns._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_sns._auth._sigv4.build_sigv4_auth_scheme("sns", options.region)
        )
        if sigv4_config is not None:
            return capo_sns._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_sns.types.create_topic_input.CreateTopicInput,
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
    pairs.append(("Action", "CreateTopic"))
    pairs.append(("Version", "2010-03-31"))
    capo_sns.types.create_topic_input.serialize_query(input_, pairs, "")
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_topic(
    options: OperationOptions,
    input_: capo_sns.types.create_topic_input.CreateTopicInput,
) -> tuple[capo_sns.types.create_topic_response.CreateTopicResponse, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_create_topic(
    options: AsyncOperationOptions,
    input_: capo_sns.types.create_topic_input.CreateTopicInput,
) -> tuple[capo_sns.types.create_topic_response.CreateTopicResponse, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
