"""Generated from Smithy shape ``com.amazonaws.eks#UpdateEksAnywhereSubscription``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_eks._auth._signers
import capo_eks._auth._sigv4
import capo_eks.errors.client_exception
import capo_eks.errors.invalid_parameter_exception
import capo_eks.errors.invalid_request_exception
import capo_eks.errors.resource_not_found_exception
import capo_eks.errors.server_exception
import capo_eks.types.eks_anywhere_subscription
import capo_eks.types.update_eks_anywhere_subscription_request
import capo_eks.types.update_eks_anywhere_subscription_response
from capo_eks._protocol.errors import parse_error_metadata_json
from capo_eks._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_eks._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_eks.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ClientException":
            raise capo_eks.errors.client_exception.ClientException.from_json(data)
        case "InvalidParameterException":
            raise capo_eks.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case "InvalidRequestException":
            raise capo_eks.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_eks.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServerException":
            raise capo_eks.errors.server_exception.ServerException.from_json(data)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_eks.types.update_eks_anywhere_subscription_response.UpdateEksAnywhereSubscriptionResponse:
    out: capo_eks.types.update_eks_anywhere_subscription_response.UpdateEksAnywhereSubscriptionResponse = capo_eks.types.update_eks_anywhere_subscription_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_eks.types.update_eks_anywhere_subscription_response.UpdateEksAnywhereSubscriptionResponse:
    out: capo_eks.types.update_eks_anywhere_subscription_response.UpdateEksAnywhereSubscriptionResponse = capo_eks.types.update_eks_anywhere_subscription_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_eks._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_eks._auth._sigv4.build_sigv4_auth_scheme("eks", options.region)
        )
        if sigv4_config is not None:
            return capo_eks._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_eks.types.update_eks_anywhere_subscription_request.UpdateEksAnywhereSubscriptionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/eks-anywhere-subscriptions/{id}"
    url = url.replace("{id}", quote(str(input_["id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_eks.types.update_eks_anywhere_subscription_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def update_eks_anywhere_subscription(
    options: OperationOptions,
    input_: capo_eks.types.update_eks_anywhere_subscription_request.UpdateEksAnywhereSubscriptionRequest,
) -> tuple[
    capo_eks.types.update_eks_anywhere_subscription_response.UpdateEksAnywhereSubscriptionResponse,
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


async def async_update_eks_anywhere_subscription(
    options: AsyncOperationOptions,
    input_: capo_eks.types.update_eks_anywhere_subscription_request.UpdateEksAnywhereSubscriptionRequest,
) -> tuple[
    capo_eks.types.update_eks_anywhere_subscription_response.UpdateEksAnywhereSubscriptionResponse,
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
