"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListIntentMetrics``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_lex_models_v2._auth._signers
import aws_sdk_lex_models_v2._auth._sigv4
import aws_sdk_lex_models_v2.errors.internal_server_exception
import aws_sdk_lex_models_v2.errors.precondition_failed_exception
import aws_sdk_lex_models_v2.errors.service_quota_exceeded_exception
import aws_sdk_lex_models_v2.errors.throttling_exception
import aws_sdk_lex_models_v2.errors.validation_exception
import aws_sdk_lex_models_v2.types.analytics_bin_by_list
import aws_sdk_lex_models_v2.types.analytics_intent_filters
import aws_sdk_lex_models_v2.types.analytics_intent_group_by_list
import aws_sdk_lex_models_v2.types.analytics_intent_metrics
import aws_sdk_lex_models_v2.types.analytics_intent_results
import aws_sdk_lex_models_v2.types.list_intent_metrics_request
import aws_sdk_lex_models_v2.types.list_intent_metrics_response
import aws_sdk_lex_models_v2.types.timestamp
from aws_sdk_lex_models_v2._protocol.errors import parse_error_metadata_json
from aws_sdk_lex_models_v2._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_lex_models_v2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_lex_models_v2.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            raise aws_sdk_lex_models_v2.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "PreconditionFailedException":
            raise aws_sdk_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise aws_sdk_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_lex_models_v2.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_lex_models_v2.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_lex_models_v2.types.list_intent_metrics_response.ListIntentMetricsResponse:
    out: aws_sdk_lex_models_v2.types.list_intent_metrics_response.ListIntentMetricsResponse = aws_sdk_lex_models_v2.types.list_intent_metrics_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_lex_models_v2.types.list_intent_metrics_response.ListIntentMetricsResponse:
    out: aws_sdk_lex_models_v2.types.list_intent_metrics_response.ListIntentMetricsResponse = aws_sdk_lex_models_v2.types.list_intent_metrics_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_lex_models_v2._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_lex_models_v2._auth._sigv4.build_sigv4_auth_scheme(
                "lex", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_lex_models_v2._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_lex_models_v2.types.list_intent_metrics_request.ListIntentMetricsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/bots/{botId}/analytics/intentmetrics"
    url = url.replace("{botId}", quote(str(input_["bot_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        aws_sdk_lex_models_v2.types.list_intent_metrics_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def list_intent_metrics(
    options: OperationOptions,
    input_: aws_sdk_lex_models_v2.types.list_intent_metrics_request.ListIntentMetricsRequest,
) -> tuple[
    aws_sdk_lex_models_v2.types.list_intent_metrics_response.ListIntentMetricsResponse,
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


async def async_list_intent_metrics(
    options: AsyncOperationOptions,
    input_: aws_sdk_lex_models_v2.types.list_intent_metrics_request.ListIntentMetricsRequest,
) -> tuple[
    aws_sdk_lex_models_v2.types.list_intent_metrics_response.ListIntentMetricsResponse,
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
