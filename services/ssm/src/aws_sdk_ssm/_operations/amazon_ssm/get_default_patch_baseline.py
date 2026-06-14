"""Generated from Smithy shape ``com.amazonaws.ssm#GetDefaultPatchBaseline``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_ssm._auth._signers
import aws_sdk_ssm._auth._sigv4
from aws_sdk_ssm._protocol.errors import parse_error_metadata_json
from aws_sdk_ssm._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_ssm._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_ssm.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.get_default_patch_baseline_request
    import aws_sdk_ssm.types.get_default_patch_baseline_result


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerError":
            import aws_sdk_ssm.errors.internal_server_error

            raise aws_sdk_ssm.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_ssm.types.get_default_patch_baseline_result.GetDefaultPatchBaselineResult:
    import aws_sdk_ssm.types.get_default_patch_baseline_result

    out: aws_sdk_ssm.types.get_default_patch_baseline_result.GetDefaultPatchBaselineResult = aws_sdk_ssm.types.get_default_patch_baseline_result.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_ssm._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_ssm._auth._sigv4.build_sigv4_auth_scheme("ssm", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_ssm._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_ssm.types.get_default_patch_baseline_request.GetDefaultPatchBaselineRequest,
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
    headers["X-Amz-Target"] = "AmazonSSM.GetDefaultPatchBaseline"
    import aws_sdk_ssm.types.get_default_patch_baseline_request

    body: bytes | None = json.dumps(
        aws_sdk_ssm.types.get_default_patch_baseline_request.serialize_aws_json_1_1(
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


def get_default_patch_baseline(
    options: OperationOptions,
    input_: aws_sdk_ssm.types.get_default_patch_baseline_request.GetDefaultPatchBaselineRequest,
) -> tuple[
    aws_sdk_ssm.types.get_default_patch_baseline_result.GetDefaultPatchBaselineResult,
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


async def async_get_default_patch_baseline(
    options: AsyncOperationOptions,
    input_: aws_sdk_ssm.types.get_default_patch_baseline_request.GetDefaultPatchBaselineRequest,
) -> tuple[
    aws_sdk_ssm.types.get_default_patch_baseline_result.GetDefaultPatchBaselineResult,
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
