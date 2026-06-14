"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetSparqlStream``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_neptunedata._auth._signers
import aws_sdk_neptunedata._auth._sigv4
from aws_sdk_neptunedata._protocol.errors import parse_error_metadata_json
from aws_sdk_neptunedata._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_neptunedata._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_neptunedata.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.get_sparql_stream_input
    import aws_sdk_neptunedata.types.get_sparql_stream_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ClientTimeoutException":
            import aws_sdk_neptunedata.errors.client_timeout_exception

            raise aws_sdk_neptunedata.errors.client_timeout_exception.ClientTimeoutException.from_json(
                data
            )
        case "ConstraintViolationException":
            import aws_sdk_neptunedata.errors.constraint_violation_exception

            raise aws_sdk_neptunedata.errors.constraint_violation_exception.ConstraintViolationException.from_json(
                data
            )
        case "ExpiredStreamException":
            import aws_sdk_neptunedata.errors.expired_stream_exception

            raise aws_sdk_neptunedata.errors.expired_stream_exception.ExpiredStreamException.from_json(
                data
            )
        case "IllegalArgumentException":
            import aws_sdk_neptunedata.errors.illegal_argument_exception

            raise aws_sdk_neptunedata.errors.illegal_argument_exception.IllegalArgumentException.from_json(
                data
            )
        case "InvalidArgumentException":
            import aws_sdk_neptunedata.errors.invalid_argument_exception

            raise aws_sdk_neptunedata.errors.invalid_argument_exception.InvalidArgumentException.from_json(
                data
            )
        case "InvalidParameterException":
            import aws_sdk_neptunedata.errors.invalid_parameter_exception

            raise aws_sdk_neptunedata.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case "MemoryLimitExceededException":
            import aws_sdk_neptunedata.errors.memory_limit_exceeded_exception

            raise aws_sdk_neptunedata.errors.memory_limit_exceeded_exception.MemoryLimitExceededException.from_json(
                data
            )
        case "PreconditionsFailedException":
            import aws_sdk_neptunedata.errors.preconditions_failed_exception

            raise aws_sdk_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException.from_json(
                data
            )
        case "StreamRecordsNotFoundException":
            import aws_sdk_neptunedata.errors.stream_records_not_found_exception

            raise aws_sdk_neptunedata.errors.stream_records_not_found_exception.StreamRecordsNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_neptunedata.errors.throttling_exception

            raise aws_sdk_neptunedata.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_neptunedata.errors.too_many_requests_exception

            raise aws_sdk_neptunedata.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case "UnsupportedOperationException":
            import aws_sdk_neptunedata.errors.unsupported_operation_exception

            raise aws_sdk_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_neptunedata.types.get_sparql_stream_output.GetSparqlStreamOutput:
    import aws_sdk_neptunedata.types.get_sparql_stream_output

    out: aws_sdk_neptunedata.types.get_sparql_stream_output.GetSparqlStreamOutput = (
        aws_sdk_neptunedata.types.get_sparql_stream_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_neptunedata._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_neptunedata._auth._sigv4.build_sigv4_auth_scheme(
                "neptune-db", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_neptunedata._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_neptunedata.types.get_sparql_stream_input.GetSparqlStreamInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/sparql/stream"
    params: dict[str, str] = {}
    if "limit" in input_:
        params["limit"] = str(input_["limit"])
    if "iterator_type" in input_:
        params["iteratorType"] = str(input_["iterator_type"])
    if "commit_num" in input_:
        params["commitNum"] = str(input_["commit_num"])
    if "op_num" in input_:
        params["opNum"] = str(input_["op_num"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "encoding" in input_:
        headers["Accept-Encoding"] = str(input_["encoding"])
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_sparql_stream(
    options: OperationOptions,
    input_: aws_sdk_neptunedata.types.get_sparql_stream_input.GetSparqlStreamInput,
) -> tuple[
    aws_sdk_neptunedata.types.get_sparql_stream_output.GetSparqlStreamOutput,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_get_sparql_stream(
    options: AsyncOperationOptions,
    input_: aws_sdk_neptunedata.types.get_sparql_stream_input.GetSparqlStreamInput,
) -> tuple[
    aws_sdk_neptunedata.types.get_sparql_stream_output.GetSparqlStreamOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
