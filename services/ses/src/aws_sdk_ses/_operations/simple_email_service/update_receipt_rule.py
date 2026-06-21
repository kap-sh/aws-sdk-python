"""Generated from Smithy shape ``com.amazonaws.ses#UpdateReceiptRule``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_ses._auth._signers
import aws_sdk_ses._auth._sigv4
import aws_sdk_ses.errors.invalid_lambda_function_exception
import aws_sdk_ses.errors.invalid_s3_configuration_exception
import aws_sdk_ses.errors.invalid_sns_topic_exception
import aws_sdk_ses.errors.limit_exceeded_exception
import aws_sdk_ses.errors.rule_does_not_exist_exception
import aws_sdk_ses.errors.rule_set_does_not_exist_exception
import aws_sdk_ses.types.receipt_rule
import aws_sdk_ses.types.update_receipt_rule_request
import aws_sdk_ses.types.update_receipt_rule_response
from aws_sdk_ses._protocol.errors import parse_error_metadata
from aws_sdk_ses._protocol.xml import fromstring
from aws_sdk_ses._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_ses._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_ses.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InvalidLambdaFunctionException":
            raise aws_sdk_ses.errors.invalid_lambda_function_exception.InvalidLambdaFunctionException.from_query(
                root
            )
        case "InvalidS3ConfigurationException":
            raise aws_sdk_ses.errors.invalid_s3_configuration_exception.InvalidS3ConfigurationException.from_query(
                root
            )
        case "InvalidSnsTopicException":
            raise aws_sdk_ses.errors.invalid_sns_topic_exception.InvalidSnsTopicException.from_query(
                root
            )
        case "LimitExceededException":
            raise aws_sdk_ses.errors.limit_exceeded_exception.LimitExceededException.from_query(
                root
            )
        case "RuleDoesNotExistException":
            raise aws_sdk_ses.errors.rule_does_not_exist_exception.RuleDoesNotExistException.from_query(
                root
            )
        case "RuleSetDoesNotExistException":
            raise aws_sdk_ses.errors.rule_set_does_not_exist_exception.RuleSetDoesNotExistException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_ses.types.update_receipt_rule_response.UpdateReceiptRuleResponse:
    root = fromstring(response.read())
    result = root.find("UpdateReceiptRuleResult")
    out: aws_sdk_ses.types.update_receipt_rule_response.UpdateReceiptRuleResponse = (
        aws_sdk_ses.types.update_receipt_rule_response.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_ses.types.update_receipt_rule_response.UpdateReceiptRuleResponse:
    root = fromstring(await response.aread())
    result = root.find("UpdateReceiptRuleResult")
    out: aws_sdk_ses.types.update_receipt_rule_response.UpdateReceiptRuleResponse = (
        aws_sdk_ses.types.update_receipt_rule_response.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_ses._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_ses._auth._sigv4.build_sigv4_auth_scheme("ses", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_ses._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_ses.types.update_receipt_rule_request.UpdateReceiptRuleRequest,
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
    pairs.append(("Action", "UpdateReceiptRule"))
    pairs.append(("Version", "2010-12-01"))
    import aws_sdk_ses.types.update_receipt_rule_request

    aws_sdk_ses.types.update_receipt_rule_request.serialize_query(input_, pairs, "")
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def update_receipt_rule(
    options: OperationOptions,
    input_: aws_sdk_ses.types.update_receipt_rule_request.UpdateReceiptRuleRequest,
) -> tuple[
    aws_sdk_ses.types.update_receipt_rule_response.UpdateReceiptRuleResponse,
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


async def async_update_receipt_rule(
    options: AsyncOperationOptions,
    input_: aws_sdk_ses.types.update_receipt_rule_request.UpdateReceiptRuleRequest,
) -> tuple[
    aws_sdk_ses.types.update_receipt_rule_response.UpdateReceiptRuleResponse,
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
