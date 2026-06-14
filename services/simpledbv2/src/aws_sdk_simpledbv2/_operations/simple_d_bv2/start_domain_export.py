"""Generated from Smithy shape ``com.amazonaws.simpledbv2#StartDomainExport``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_simpledbv2._auth._signers
import aws_sdk_simpledbv2._auth._sigv4
from aws_sdk_simpledbv2._protocol.errors import parse_error_metadata_json
from aws_sdk_simpledbv2._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_simpledbv2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_simpledbv2.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_simpledbv2.types.start_domain_export_request
    import aws_sdk_simpledbv2.types.start_domain_export_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConflictException":
            import aws_sdk_simpledbv2.errors.conflict_exception

            raise aws_sdk_simpledbv2.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InvalidParameterCombinationException":
            import aws_sdk_simpledbv2.errors.invalid_parameter_combination_exception

            raise aws_sdk_simpledbv2.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException.from_json(
                data
            )
        case "InvalidParameterValueException":
            import aws_sdk_simpledbv2.errors.invalid_parameter_value_exception

            raise aws_sdk_simpledbv2.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "NoSuchDomainException":
            import aws_sdk_simpledbv2.errors.no_such_domain_exception

            raise aws_sdk_simpledbv2.errors.no_such_domain_exception.NoSuchDomainException.from_json(
                data
            )
        case "NumberExportsLimitExceeded":
            import aws_sdk_simpledbv2.errors.number_exports_limit_exceeded

            raise aws_sdk_simpledbv2.errors.number_exports_limit_exceeded.NumberExportsLimitExceeded.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_simpledbv2.types.start_domain_export_response.StartDomainExportResponse:
    import aws_sdk_simpledbv2.types.start_domain_export_response

    out: aws_sdk_simpledbv2.types.start_domain_export_response.StartDomainExportResponse = aws_sdk_simpledbv2.types.start_domain_export_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_simpledbv2._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_simpledbv2._auth._sigv4.build_sigv4_auth_scheme(
                "sdb", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_simpledbv2._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_simpledbv2.types.start_domain_export_request.StartDomainExportRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v2/StartDomainExport"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_simpledbv2.types.start_domain_export_request

    body: bytes | None = json.dumps(
        aws_sdk_simpledbv2.types.start_domain_export_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def start_domain_export(
    options: OperationOptions,
    input_: aws_sdk_simpledbv2.types.start_domain_export_request.StartDomainExportRequest,
) -> tuple[
    aws_sdk_simpledbv2.types.start_domain_export_response.StartDomainExportResponse,
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


async def async_start_domain_export(
    options: AsyncOperationOptions,
    input_: aws_sdk_simpledbv2.types.start_domain_export_request.StartDomainExportRequest,
) -> tuple[
    aws_sdk_simpledbv2.types.start_domain_export_response.StartDomainExportResponse,
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
