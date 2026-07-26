"""Generated from Smithy shape ``com.amazonaws.swf#UntagResource``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_swf._auth._signers
import capo_swf._auth._sigv4
import capo_swf.errors.limit_exceeded_fault
import capo_swf.errors.operation_not_permitted_fault
import capo_swf.errors.unknown_resource_fault
import capo_swf.types.resource_tag_key_list
import capo_swf.types.untag_resource_input
from capo_swf._protocol.errors import parse_error_metadata_json
from capo_swf._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_swf._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_swf.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "LimitExceededFault":
            raise capo_swf.errors.limit_exceeded_fault.LimitExceededFault.from_aws_json_1_0(
                data
            )
        case "OperationNotPermittedFault":
            raise capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault.from_aws_json_1_0(
                data
            )
        case "UnknownResourceFault":
            raise capo_swf.errors.unknown_resource_fault.UnknownResourceFault.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_swf._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_swf._auth._sigv4.build_sigv4_auth_scheme("swf", options.region)
        )
        if sigv4_config is not None:
            return capo_swf._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_swf.types.untag_resource_input.UntagResourceInput,
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
    headers["X-Amz-Target"] = "SimpleWorkflowService.UntagResource"
    body: bytes | None = json.dumps(
        capo_swf.types.untag_resource_input.serialize_aws_json_1_0(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def untag_resource(
    options: OperationOptions,
    input_: capo_swf.types.untag_resource_input.UntagResourceInput,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_untag_resource(
    options: AsyncOperationOptions,
    input_: capo_swf.types.untag_resource_input.UntagResourceInput,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
