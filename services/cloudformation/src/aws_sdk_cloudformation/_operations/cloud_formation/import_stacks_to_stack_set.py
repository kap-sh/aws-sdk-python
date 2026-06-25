"""Generated from Smithy shape ``com.amazonaws.cloudformation#ImportStacksToStackSet``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_cloudformation._auth._signers
import aws_sdk_cloudformation._auth._sigv4
import aws_sdk_cloudformation.errors.invalid_operation_exception
import aws_sdk_cloudformation.errors.limit_exceeded_exception
import aws_sdk_cloudformation.errors.operation_id_already_exists_exception
import aws_sdk_cloudformation.errors.operation_in_progress_exception
import aws_sdk_cloudformation.errors.stack_not_found_exception
import aws_sdk_cloudformation.errors.stack_set_not_found_exception
import aws_sdk_cloudformation.errors.stale_request_exception
import aws_sdk_cloudformation.types.call_as
import aws_sdk_cloudformation.types.import_stacks_to_stack_set_input
import aws_sdk_cloudformation.types.import_stacks_to_stack_set_output
import aws_sdk_cloudformation.types.organizational_unit_id_list
import aws_sdk_cloudformation.types.stack_id_list
import aws_sdk_cloudformation.types.stack_set_operation_preferences
from aws_sdk_cloudformation._protocol.errors import parse_error_metadata
from aws_sdk_cloudformation._protocol.xml import (
    fromstring,
)
from aws_sdk_cloudformation._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_cloudformation._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudformation.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InvalidOperationException":
            raise aws_sdk_cloudformation.errors.invalid_operation_exception.InvalidOperationException.from_query(
                root
            )
        case "LimitExceededException":
            raise aws_sdk_cloudformation.errors.limit_exceeded_exception.LimitExceededException.from_query(
                root
            )
        case "OperationIdAlreadyExistsException":
            raise aws_sdk_cloudformation.errors.operation_id_already_exists_exception.OperationIdAlreadyExistsException.from_query(
                root
            )
        case "OperationInProgressException":
            raise aws_sdk_cloudformation.errors.operation_in_progress_exception.OperationInProgressException.from_query(
                root
            )
        case "StackNotFoundException":
            raise aws_sdk_cloudformation.errors.stack_not_found_exception.StackNotFoundException.from_query(
                root
            )
        case "StackSetNotFoundException":
            raise aws_sdk_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException.from_query(
                root
            )
        case "StaleRequestException":
            raise aws_sdk_cloudformation.errors.stale_request_exception.StaleRequestException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_cloudformation.types.import_stacks_to_stack_set_output.ImportStacksToStackSetOutput:
    root = fromstring(response.read())
    result = root.find("ImportStacksToStackSetResult")
    out: aws_sdk_cloudformation.types.import_stacks_to_stack_set_output.ImportStacksToStackSetOutput = aws_sdk_cloudformation.types.import_stacks_to_stack_set_output.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_cloudformation.types.import_stacks_to_stack_set_output.ImportStacksToStackSetOutput:
    root = fromstring(await response.aread())
    result = root.find("ImportStacksToStackSetResult")
    out: aws_sdk_cloudformation.types.import_stacks_to_stack_set_output.ImportStacksToStackSetOutput = aws_sdk_cloudformation.types.import_stacks_to_stack_set_output.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloudformation._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cloudformation._auth._sigv4.build_sigv4_auth_scheme(
                "cloudformation", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cloudformation._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_cloudformation.types.import_stacks_to_stack_set_input.ImportStacksToStackSetInput,
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
    pairs.append(("Action", "ImportStacksToStackSet"))
    pairs.append(("Version", "2010-05-15"))
    aws_sdk_cloudformation.types.import_stacks_to_stack_set_input.serialize_query(
        input_, pairs, ""
    )
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def import_stacks_to_stack_set(
    options: OperationOptions,
    input_: aws_sdk_cloudformation.types.import_stacks_to_stack_set_input.ImportStacksToStackSetInput,
) -> tuple[
    aws_sdk_cloudformation.types.import_stacks_to_stack_set_output.ImportStacksToStackSetOutput,
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


async def async_import_stacks_to_stack_set(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudformation.types.import_stacks_to_stack_set_input.ImportStacksToStackSetInput,
) -> tuple[
    aws_sdk_cloudformation.types.import_stacks_to_stack_set_output.ImportStacksToStackSetOutput,
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
