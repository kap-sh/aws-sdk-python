"""Generated from Smithy shape ``com.amazonaws.memorydb#ResetParameterGroup``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_memorydb._auth._signers
import aws_sdk_memorydb._auth._sigv4
from aws_sdk_memorydb._protocol.errors import parse_error_metadata_json
from aws_sdk_memorydb._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_memorydb._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_memorydb.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.reset_parameter_group_request
    import aws_sdk_memorydb.types.reset_parameter_group_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterCombinationException":
            import aws_sdk_memorydb.errors.invalid_parameter_combination_exception

            raise aws_sdk_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterGroupStateFault":
            import aws_sdk_memorydb.errors.invalid_parameter_group_state_fault

            raise aws_sdk_memorydb.errors.invalid_parameter_group_state_fault.InvalidParameterGroupStateFault.from_aws_json_1_1(
                data
            )
        case "InvalidParameterValueException":
            import aws_sdk_memorydb.errors.invalid_parameter_value_exception

            raise aws_sdk_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_aws_json_1_1(
                data
            )
        case "ParameterGroupNotFoundFault":
            import aws_sdk_memorydb.errors.parameter_group_not_found_fault

            raise aws_sdk_memorydb.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault.from_aws_json_1_1(
                data
            )
        case "ServiceLinkedRoleNotFoundFault":
            import aws_sdk_memorydb.errors.service_linked_role_not_found_fault

            raise aws_sdk_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_memorydb.types.reset_parameter_group_response.ResetParameterGroupResponse:
    import aws_sdk_memorydb.types.reset_parameter_group_response

    out: aws_sdk_memorydb.types.reset_parameter_group_response.ResetParameterGroupResponse = aws_sdk_memorydb.types.reset_parameter_group_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_memorydb._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_memorydb._auth._sigv4.build_sigv4_auth_scheme(
                "memorydb", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_memorydb._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_memorydb.types.reset_parameter_group_request.ResetParameterGroupRequest,
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
    headers["X-Amz-Target"] = "AmazonMemoryDB.ResetParameterGroup"
    import aws_sdk_memorydb.types.reset_parameter_group_request

    body: bytes | None = json.dumps(
        aws_sdk_memorydb.types.reset_parameter_group_request.serialize_aws_json_1_1(
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


def reset_parameter_group(
    options: OperationOptions,
    input_: aws_sdk_memorydb.types.reset_parameter_group_request.ResetParameterGroupRequest,
) -> tuple[
    aws_sdk_memorydb.types.reset_parameter_group_response.ResetParameterGroupResponse,
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


async def async_reset_parameter_group(
    options: AsyncOperationOptions,
    input_: aws_sdk_memorydb.types.reset_parameter_group_request.ResetParameterGroupRequest,
) -> tuple[
    aws_sdk_memorydb.types.reset_parameter_group_response.ResetParameterGroupResponse,
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
