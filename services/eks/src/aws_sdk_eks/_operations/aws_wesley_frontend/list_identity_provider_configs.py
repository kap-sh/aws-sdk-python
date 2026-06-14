"""Generated from Smithy shape ``com.amazonaws.eks#ListIdentityProviderConfigs``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_eks._auth._signers
import aws_sdk_eks._auth._sigv4
from aws_sdk_eks._protocol.errors import parse_error_metadata_json
from aws_sdk_eks._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_eks._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_eks.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_eks.types.list_identity_provider_configs_request
    import aws_sdk_eks.types.list_identity_provider_configs_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ClientException":
            import aws_sdk_eks.errors.client_exception

            raise aws_sdk_eks.errors.client_exception.ClientException.from_json(data)
        case "InvalidParameterException":
            import aws_sdk_eks.errors.invalid_parameter_exception

            raise aws_sdk_eks.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_eks.errors.resource_not_found_exception

            raise aws_sdk_eks.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServerException":
            import aws_sdk_eks.errors.server_exception

            raise aws_sdk_eks.errors.server_exception.ServerException.from_json(data)
        case "ServiceUnavailableException":
            import aws_sdk_eks.errors.service_unavailable_exception

            raise aws_sdk_eks.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_eks.types.list_identity_provider_configs_response.ListIdentityProviderConfigsResponse:
    import aws_sdk_eks.types.list_identity_provider_configs_response

    out: aws_sdk_eks.types.list_identity_provider_configs_response.ListIdentityProviderConfigsResponse = aws_sdk_eks.types.list_identity_provider_configs_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_eks._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_eks._auth._sigv4.build_sigv4_auth_scheme("eks", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_eks._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_eks.types.list_identity_provider_configs_request.ListIdentityProviderConfigsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/clusters/{clusterName}/identity-provider-configs"
    url = url.replace("{clusterName}", quote(str(input_["cluster_name"]), safe=""))
    params: dict[str, str] = {}
    if "max_results" in input_:
        params["maxResults"] = str(input_["max_results"])
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_identity_provider_configs(
    options: OperationOptions,
    input_: aws_sdk_eks.types.list_identity_provider_configs_request.ListIdentityProviderConfigsRequest,
) -> tuple[
    aws_sdk_eks.types.list_identity_provider_configs_response.ListIdentityProviderConfigsResponse,
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


async def async_list_identity_provider_configs(
    options: AsyncOperationOptions,
    input_: aws_sdk_eks.types.list_identity_provider_configs_request.ListIdentityProviderConfigsRequest,
) -> tuple[
    aws_sdk_eks.types.list_identity_provider_configs_response.ListIdentityProviderConfigsResponse,
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
