"""Generated from Smithy shape ``com.amazonaws.rdsdata#CommitTransaction``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_rds_data._auth._signers
import aws_sdk_rds_data._auth._sigv4
import aws_sdk_rds_data.errors.access_denied_exception
import aws_sdk_rds_data.errors.bad_request_exception
import aws_sdk_rds_data.errors.database_error_exception
import aws_sdk_rds_data.errors.database_not_found_exception
import aws_sdk_rds_data.errors.database_unavailable_exception
import aws_sdk_rds_data.errors.forbidden_exception
import aws_sdk_rds_data.errors.http_endpoint_not_enabled_exception
import aws_sdk_rds_data.errors.internal_server_error_exception
import aws_sdk_rds_data.errors.invalid_resource_state_exception
import aws_sdk_rds_data.errors.invalid_secret_exception
import aws_sdk_rds_data.errors.not_found_exception
import aws_sdk_rds_data.errors.secrets_error_exception
import aws_sdk_rds_data.errors.service_unavailable_error
import aws_sdk_rds_data.errors.statement_timeout_exception
import aws_sdk_rds_data.errors.transaction_not_found_exception
import aws_sdk_rds_data.types.commit_transaction_request
import aws_sdk_rds_data.types.commit_transaction_response
from aws_sdk_rds_data._protocol.errors import parse_error_metadata_json
from aws_sdk_rds_data._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_rds_data._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_rds_data.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_rds_data.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "BadRequestException":
            raise aws_sdk_rds_data.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "DatabaseErrorException":
            raise aws_sdk_rds_data.errors.database_error_exception.DatabaseErrorException.from_json(
                data
            )
        case "DatabaseNotFoundException":
            raise aws_sdk_rds_data.errors.database_not_found_exception.DatabaseNotFoundException.from_json(
                data
            )
        case "DatabaseUnavailableException":
            raise aws_sdk_rds_data.errors.database_unavailable_exception.DatabaseUnavailableException.from_json(
                data
            )
        case "ForbiddenException":
            raise aws_sdk_rds_data.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "HttpEndpointNotEnabledException":
            raise aws_sdk_rds_data.errors.http_endpoint_not_enabled_exception.HttpEndpointNotEnabledException.from_json(
                data
            )
        case "InternalServerErrorException":
            raise aws_sdk_rds_data.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "InvalidResourceStateException":
            raise aws_sdk_rds_data.errors.invalid_resource_state_exception.InvalidResourceStateException.from_json(
                data
            )
        case "InvalidSecretException":
            raise aws_sdk_rds_data.errors.invalid_secret_exception.InvalidSecretException.from_json(
                data
            )
        case "NotFoundException":
            raise aws_sdk_rds_data.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "SecretsErrorException":
            raise aws_sdk_rds_data.errors.secrets_error_exception.SecretsErrorException.from_json(
                data
            )
        case "ServiceUnavailableError":
            raise aws_sdk_rds_data.errors.service_unavailable_error.ServiceUnavailableError.from_json(
                data
            )
        case "StatementTimeoutException":
            raise aws_sdk_rds_data.errors.statement_timeout_exception.StatementTimeoutException.from_json(
                data
            )
        case "TransactionNotFoundException":
            raise aws_sdk_rds_data.errors.transaction_not_found_exception.TransactionNotFoundException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_rds_data.types.commit_transaction_response.CommitTransactionResponse:
    out: aws_sdk_rds_data.types.commit_transaction_response.CommitTransactionResponse = aws_sdk_rds_data.types.commit_transaction_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_rds_data.types.commit_transaction_response.CommitTransactionResponse:
    out: aws_sdk_rds_data.types.commit_transaction_response.CommitTransactionResponse = aws_sdk_rds_data.types.commit_transaction_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_rds_data._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_rds_data._auth._sigv4.build_sigv4_auth_scheme(
                "rds-data", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_rds_data._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_rds_data.types.commit_transaction_request.CommitTransactionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/CommitTransaction"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_rds_data.types.commit_transaction_request

    body: bytes | None = json.dumps(
        aws_sdk_rds_data.types.commit_transaction_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def commit_transaction(
    options: OperationOptions,
    input_: aws_sdk_rds_data.types.commit_transaction_request.CommitTransactionRequest,
) -> tuple[
    aws_sdk_rds_data.types.commit_transaction_response.CommitTransactionResponse,
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


async def async_commit_transaction(
    options: AsyncOperationOptions,
    input_: aws_sdk_rds_data.types.commit_transaction_request.CommitTransactionRequest,
) -> tuple[
    aws_sdk_rds_data.types.commit_transaction_response.CommitTransactionResponse,
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
