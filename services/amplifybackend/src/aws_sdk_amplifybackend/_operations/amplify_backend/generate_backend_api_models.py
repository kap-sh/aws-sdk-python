"""Generated from Smithy shape ``com.amazonaws.amplifybackend#GenerateBackendAPIModels``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_amplifybackend._auth._signers
import aws_sdk_amplifybackend._auth._sigv4
from aws_sdk_amplifybackend._protocol.errors import parse_error_metadata_json
from aws_sdk_amplifybackend._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_amplifybackend._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_amplifybackend.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.generate_backend_api_models_request
    import aws_sdk_amplifybackend.types.generate_backend_api_models_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            import aws_sdk_amplifybackend.errors.bad_request_exception

            raise aws_sdk_amplifybackend.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "GatewayTimeoutException":
            import aws_sdk_amplifybackend.errors.gateway_timeout_exception

            raise aws_sdk_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException.from_json(
                data
            )
        case "NotFoundException":
            import aws_sdk_amplifybackend.errors.not_found_exception

            raise aws_sdk_amplifybackend.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_amplifybackend.errors.too_many_requests_exception

            raise aws_sdk_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_amplifybackend.types.generate_backend_api_models_response.GenerateBackendAPIModelsResponse:
    import aws_sdk_amplifybackend.types.generate_backend_api_models_response

    out: aws_sdk_amplifybackend.types.generate_backend_api_models_response.GenerateBackendAPIModelsResponse = aws_sdk_amplifybackend.types.generate_backend_api_models_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_amplifybackend._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_amplifybackend._auth._sigv4.build_sigv4_auth_scheme(
                "amplifybackend", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_amplifybackend._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_amplifybackend.types.generate_backend_api_models_request.GenerateBackendAPIModelsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/backend/{AppId}/api/{BackendEnvironmentName}/generateModels"
    )
    url = url.replace("{AppId}", quote(str(input_["app_id"]), safe=""))
    url = url.replace(
        "{BackendEnvironmentName}",
        quote(str(input_["backend_environment_name"]), safe=""),
    )
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_amplifybackend.types.generate_backend_api_models_request

    body: bytes | None = json.dumps(
        aws_sdk_amplifybackend.types.generate_backend_api_models_request.serialize_json(
            input_
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def generate_backend_api_models(
    options: OperationOptions,
    input_: aws_sdk_amplifybackend.types.generate_backend_api_models_request.GenerateBackendAPIModelsRequest,
) -> tuple[
    aws_sdk_amplifybackend.types.generate_backend_api_models_response.GenerateBackendAPIModelsResponse,
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


async def async_generate_backend_api_models(
    options: AsyncOperationOptions,
    input_: aws_sdk_amplifybackend.types.generate_backend_api_models_request.GenerateBackendAPIModelsRequest,
) -> tuple[
    aws_sdk_amplifybackend.types.generate_backend_api_models_response.GenerateBackendAPIModelsResponse,
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
