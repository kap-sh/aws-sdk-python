"""Generated from Smithy shape ``com.amazonaws.oam#CreateSink``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_oam._auth._signers
import capo_oam._auth._sigv4
import capo_oam.errors.conflict_exception
import capo_oam.errors.internal_service_fault
import capo_oam.errors.invalid_parameter_exception
import capo_oam.errors.missing_required_parameter_exception
import capo_oam.errors.service_quota_exceeded_exception
import capo_oam.types.create_sink_input
import capo_oam.types.create_sink_output
import capo_oam.types.tag_map_input
import capo_oam.types.tag_map_output
from capo_oam._protocol.errors import parse_error_metadata_json
from capo_oam._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_oam._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_oam.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConflictException":
            raise capo_oam.errors.conflict_exception.ConflictException.from_json(data)
        case "InternalServiceFault":
            raise capo_oam.errors.internal_service_fault.InternalServiceFault.from_json(
                data
            )
        case "InvalidParameterException":
            raise capo_oam.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case "MissingRequiredParameterException":
            raise capo_oam.errors.missing_required_parameter_exception.MissingRequiredParameterException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise capo_oam.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_oam.types.create_sink_output.CreateSinkOutput:
    out: capo_oam.types.create_sink_output.CreateSinkOutput = (
        capo_oam.types.create_sink_output.deserialize_json(json.loads(response.read()))
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_oam.types.create_sink_output.CreateSinkOutput:
    out: capo_oam.types.create_sink_output.CreateSinkOutput = (
        capo_oam.types.create_sink_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_oam._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_oam._auth._sigv4.build_sigv4_auth_scheme("oam", options.region)
        )
        if sigv4_config is not None:
            return capo_oam._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_oam.types.create_sink_input.CreateSinkInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/CreateSink"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_oam.types.create_sink_input.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_sink(
    options: OperationOptions, input_: capo_oam.types.create_sink_input.CreateSinkInput
) -> tuple[capo_oam.types.create_sink_output.CreateSinkOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_create_sink(
    options: AsyncOperationOptions,
    input_: capo_oam.types.create_sink_input.CreateSinkInput,
) -> tuple[capo_oam.types.create_sink_output.CreateSinkOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
