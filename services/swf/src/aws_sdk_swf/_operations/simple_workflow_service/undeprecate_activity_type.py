"""Generated from Smithy shape ``com.amazonaws.swf#UndeprecateActivityType``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_swf._auth._signers
import aws_sdk_swf._auth._sigv4
from aws_sdk_swf._protocol.errors import parse_error_metadata_json
from aws_sdk_swf._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_swf._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_swf.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_swf.types.undeprecate_activity_type_input


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "OperationNotPermittedFault":
            import aws_sdk_swf.errors.operation_not_permitted_fault

            raise aws_sdk_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault.from_aws_json_1_0(
                data
            )
        case "TypeAlreadyExistsFault":
            import aws_sdk_swf.errors.type_already_exists_fault

            raise aws_sdk_swf.errors.type_already_exists_fault.TypeAlreadyExistsFault.from_aws_json_1_0(
                data
            )
        case "UnknownResourceFault":
            import aws_sdk_swf.errors.unknown_resource_fault

            raise aws_sdk_swf.errors.unknown_resource_fault.UnknownResourceFault.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_swf._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_swf._auth._sigv4.build_sigv4_auth_scheme("swf", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_swf._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_swf.types.undeprecate_activity_type_input.UndeprecateActivityTypeInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "SimpleWorkflowService.UndeprecateActivityType"
    import aws_sdk_swf.types.undeprecate_activity_type_input

    body: bytes | None = json.dumps(
        aws_sdk_swf.types.undeprecate_activity_type_input.serialize_aws_json_1_0(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def undeprecate_activity_type(
    options: OperationOptions,
    input_: aws_sdk_swf.types.undeprecate_activity_type_input.UndeprecateActivityTypeInput,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return None, response
    except BaseException:
        response.close()
        raise


async def async_undeprecate_activity_type(
    options: AsyncOperationOptions,
    input_: aws_sdk_swf.types.undeprecate_activity_type_input.UndeprecateActivityTypeInput,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return None, response
    except BaseException:
        await response.aclose()
        raise
