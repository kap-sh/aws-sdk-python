"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ExchangeCodeForToken``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_amplifyuibuilder._auth._signers
import aws_sdk_amplifyuibuilder._auth._sigv4
from aws_sdk_amplifyuibuilder._protocol.errors import parse_error_metadata_json
from aws_sdk_amplifyuibuilder._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_amplifyuibuilder._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_amplifyuibuilder.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.exchange_code_for_token_request
    import aws_sdk_amplifyuibuilder.types.exchange_code_for_token_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterException":
            import aws_sdk_amplifyuibuilder.errors.invalid_parameter_exception

            raise aws_sdk_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_amplifyuibuilder.types.exchange_code_for_token_response.ExchangeCodeForTokenResponse:
    import aws_sdk_amplifyuibuilder.types.exchange_code_for_token_response

    out: aws_sdk_amplifyuibuilder.types.exchange_code_for_token_response.ExchangeCodeForTokenResponse = aws_sdk_amplifyuibuilder.types.exchange_code_for_token_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_amplifyuibuilder._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_amplifyuibuilder._auth._sigv4.build_sigv4_auth_scheme(
                "amplifyuibuilder", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_amplifyuibuilder._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_amplifyuibuilder.types.exchange_code_for_token_request.ExchangeCodeForTokenRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/tokens/{provider}"
    url = url.replace("{provider}", quote(str(input["provider"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "request" in input:
        import aws_sdk_amplifyuibuilder.types.exchange_code_for_token_request_body

        body: bytes | None = json.dumps(
            aws_sdk_amplifyuibuilder.types.exchange_code_for_token_request_body.serialize_json(
                input["request"]
            )
        ).encode()
        headers["content-type"] = "application/json"
    else:
        body = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def exchange_code_for_token(
    options: OperationOptions,
    input: aws_sdk_amplifyuibuilder.types.exchange_code_for_token_request.ExchangeCodeForTokenRequest,
) -> tuple[
    aws_sdk_amplifyuibuilder.types.exchange_code_for_token_response.ExchangeCodeForTokenResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_exchange_code_for_token(
    options: AsyncOperationOptions,
    input: aws_sdk_amplifyuibuilder.types.exchange_code_for_token_request.ExchangeCodeForTokenRequest,
) -> tuple[
    aws_sdk_amplifyuibuilder.types.exchange_code_for_token_response.ExchangeCodeForTokenResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
