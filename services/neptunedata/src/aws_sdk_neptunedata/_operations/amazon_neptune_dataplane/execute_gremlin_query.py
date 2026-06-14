"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteGremlinQuery``."""

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
    import aws_sdk_neptunedata.types.execute_gremlin_query_input
    import aws_sdk_neptunedata.types.execute_gremlin_query_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            import aws_sdk_neptunedata.errors.bad_request_exception

            raise aws_sdk_neptunedata.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "CancelledByUserException":
            import aws_sdk_neptunedata.errors.cancelled_by_user_exception

            raise aws_sdk_neptunedata.errors.cancelled_by_user_exception.CancelledByUserException.from_json(
                data
            )
        case "ClientTimeoutException":
            import aws_sdk_neptunedata.errors.client_timeout_exception

            raise aws_sdk_neptunedata.errors.client_timeout_exception.ClientTimeoutException.from_json(
                data
            )
        case "ConcurrentModificationException":
            import aws_sdk_neptunedata.errors.concurrent_modification_exception

            raise aws_sdk_neptunedata.errors.concurrent_modification_exception.ConcurrentModificationException.from_json(
                data
            )
        case "ConstraintViolationException":
            import aws_sdk_neptunedata.errors.constraint_violation_exception

            raise aws_sdk_neptunedata.errors.constraint_violation_exception.ConstraintViolationException.from_json(
                data
            )
        case "FailureByQueryException":
            import aws_sdk_neptunedata.errors.failure_by_query_exception

            raise aws_sdk_neptunedata.errors.failure_by_query_exception.FailureByQueryException.from_json(
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
        case "MalformedQueryException":
            import aws_sdk_neptunedata.errors.malformed_query_exception

            raise aws_sdk_neptunedata.errors.malformed_query_exception.MalformedQueryException.from_json(
                data
            )
        case "MemoryLimitExceededException":
            import aws_sdk_neptunedata.errors.memory_limit_exceeded_exception

            raise aws_sdk_neptunedata.errors.memory_limit_exceeded_exception.MemoryLimitExceededException.from_json(
                data
            )
        case "MissingParameterException":
            import aws_sdk_neptunedata.errors.missing_parameter_exception

            raise aws_sdk_neptunedata.errors.missing_parameter_exception.MissingParameterException.from_json(
                data
            )
        case "ParsingException":
            import aws_sdk_neptunedata.errors.parsing_exception

            raise aws_sdk_neptunedata.errors.parsing_exception.ParsingException.from_json(
                data
            )
        case "PreconditionsFailedException":
            import aws_sdk_neptunedata.errors.preconditions_failed_exception

            raise aws_sdk_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException.from_json(
                data
            )
        case "QueryLimitExceededException":
            import aws_sdk_neptunedata.errors.query_limit_exceeded_exception

            raise aws_sdk_neptunedata.errors.query_limit_exceeded_exception.QueryLimitExceededException.from_json(
                data
            )
        case "QueryLimitException":
            import aws_sdk_neptunedata.errors.query_limit_exception

            raise aws_sdk_neptunedata.errors.query_limit_exception.QueryLimitException.from_json(
                data
            )
        case "QueryTooLargeException":
            import aws_sdk_neptunedata.errors.query_too_large_exception

            raise aws_sdk_neptunedata.errors.query_too_large_exception.QueryTooLargeException.from_json(
                data
            )
        case "TimeLimitExceededException":
            import aws_sdk_neptunedata.errors.time_limit_exceeded_exception

            raise aws_sdk_neptunedata.errors.time_limit_exceeded_exception.TimeLimitExceededException.from_json(
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
) -> aws_sdk_neptunedata.types.execute_gremlin_query_output.ExecuteGremlinQueryOutput:
    import aws_sdk_neptunedata.types.execute_gremlin_query_output

    out: aws_sdk_neptunedata.types.execute_gremlin_query_output.ExecuteGremlinQueryOutput = aws_sdk_neptunedata.types.execute_gremlin_query_output.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_neptunedata._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_neptunedata.types.execute_gremlin_query_input.ExecuteGremlinQueryInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/gremlin"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "serializer" in input_:
        headers["accept"] = str(input_["serializer"])
    import aws_sdk_neptunedata.types.execute_gremlin_query_input

    body: bytes | None = json.dumps(
        aws_sdk_neptunedata.types.execute_gremlin_query_input.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def execute_gremlin_query(
    options: OperationOptions,
    input_: aws_sdk_neptunedata.types.execute_gremlin_query_input.ExecuteGremlinQueryInput,
) -> tuple[
    aws_sdk_neptunedata.types.execute_gremlin_query_output.ExecuteGremlinQueryOutput,
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


async def async_execute_gremlin_query(
    options: AsyncOperationOptions,
    input_: aws_sdk_neptunedata.types.execute_gremlin_query_input.ExecuteGremlinQueryInput,
) -> tuple[
    aws_sdk_neptunedata.types.execute_gremlin_query_output.ExecuteGremlinQueryOutput,
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
