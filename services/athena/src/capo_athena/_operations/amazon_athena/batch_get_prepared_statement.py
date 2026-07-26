"""Generated from Smithy shape ``com.amazonaws.athena#BatchGetPreparedStatement``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_athena._auth._signers
import capo_athena._auth._sigv4
import capo_athena.errors.internal_server_exception
import capo_athena.errors.invalid_request_exception
import capo_athena.types.batch_get_prepared_statement_input
import capo_athena.types.batch_get_prepared_statement_output
import capo_athena.types.prepared_statement_details_list
import capo_athena.types.prepared_statement_name_list
import capo_athena.types.unprocessed_prepared_statement_name_list
from capo_athena._protocol.errors import parse_error_metadata_json
from capo_athena._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_athena._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_athena.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            raise capo_athena.errors.internal_server_exception.InternalServerException.from_aws_json_1_1(
                data
            )
        case "InvalidRequestException":
            raise capo_athena.errors.invalid_request_exception.InvalidRequestException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_athena.types.batch_get_prepared_statement_output.BatchGetPreparedStatementOutput:
    out: capo_athena.types.batch_get_prepared_statement_output.BatchGetPreparedStatementOutput = capo_athena.types.batch_get_prepared_statement_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_athena.types.batch_get_prepared_statement_output.BatchGetPreparedStatementOutput:
    out: capo_athena.types.batch_get_prepared_statement_output.BatchGetPreparedStatementOutput = capo_athena.types.batch_get_prepared_statement_output.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_athena._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_athena._auth._sigv4.build_sigv4_auth_scheme(
                "athena", options.region
            )
        )
        if sigv4_config is not None:
            return capo_athena._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_athena.types.batch_get_prepared_statement_input.BatchGetPreparedStatementInput,
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
    headers["X-Amz-Target"] = "AmazonAthena.BatchGetPreparedStatement"
    body: bytes | None = json.dumps(
        capo_athena.types.batch_get_prepared_statement_input.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def batch_get_prepared_statement(
    options: OperationOptions,
    input_: capo_athena.types.batch_get_prepared_statement_input.BatchGetPreparedStatementInput,
) -> tuple[
    capo_athena.types.batch_get_prepared_statement_output.BatchGetPreparedStatementOutput,
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


async def async_batch_get_prepared_statement(
    options: AsyncOperationOptions,
    input_: capo_athena.types.batch_get_prepared_statement_input.BatchGetPreparedStatementInput,
) -> tuple[
    capo_athena.types.batch_get_prepared_statement_output.BatchGetPreparedStatementOutput,
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
