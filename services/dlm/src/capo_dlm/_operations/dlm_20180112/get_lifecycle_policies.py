"""Generated from Smithy shape ``com.amazonaws.dlm#GetLifecyclePolicies``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_dlm._auth._signers
import capo_dlm._auth._sigv4
import capo_dlm.errors.internal_server_exception
import capo_dlm.errors.invalid_request_exception
import capo_dlm.errors.limit_exceeded_exception
import capo_dlm.errors.resource_not_found_exception
import capo_dlm.types.default_policies_type_values
import capo_dlm.types.get_lifecycle_policies_request
import capo_dlm.types.get_lifecycle_policies_response
import capo_dlm.types.gettable_policy_state_values
import capo_dlm.types.lifecycle_policy_summary_list
import capo_dlm.types.policy_id_list
import capo_dlm.types.resource_type_values_list
import capo_dlm.types.tags_to_add_filter_list
import capo_dlm.types.target_tags_filter_list
from capo_dlm._protocol.errors import parse_error_metadata_json
from capo_dlm._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_dlm._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_dlm.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            raise capo_dlm.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "InvalidRequestException":
            raise capo_dlm.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "LimitExceededException":
            raise capo_dlm.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_dlm.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_dlm.types.get_lifecycle_policies_response.GetLifecyclePoliciesResponse:
    out: capo_dlm.types.get_lifecycle_policies_response.GetLifecyclePoliciesResponse = (
        capo_dlm.types.get_lifecycle_policies_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_dlm.types.get_lifecycle_policies_response.GetLifecyclePoliciesResponse:
    out: capo_dlm.types.get_lifecycle_policies_response.GetLifecyclePoliciesResponse = (
        capo_dlm.types.get_lifecycle_policies_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_dlm._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_dlm._auth._sigv4.build_sigv4_auth_scheme("dlm", options.region)
        )
        if sigv4_config is not None:
            return capo_dlm._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_dlm.types.get_lifecycle_policies_request.GetLifecyclePoliciesRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/policies"
    params: dict[str, str] = {}
    if "policy_ids" in input_:
        params["policyIds"] = str(input_["policy_ids"])
    if "state" in input_:
        params["state"] = str(input_["state"])
    if "resource_types" in input_:
        params["resourceTypes"] = str(input_["resource_types"])
    if "target_tags" in input_:
        params["targetTags"] = str(input_["target_tags"])
    if "tags_to_add" in input_:
        params["tagsToAdd"] = str(input_["tags_to_add"])
    if "default_policy_type" in input_:
        params["defaultPolicyType"] = str(input_["default_policy_type"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_lifecycle_policies(
    options: OperationOptions,
    input_: capo_dlm.types.get_lifecycle_policies_request.GetLifecyclePoliciesRequest,
) -> tuple[
    capo_dlm.types.get_lifecycle_policies_response.GetLifecyclePoliciesResponse,
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


async def async_get_lifecycle_policies(
    options: AsyncOperationOptions,
    input_: capo_dlm.types.get_lifecycle_policies_request.GetLifecyclePoliciesRequest,
) -> tuple[
    capo_dlm.types.get_lifecycle_policies_response.GetLifecyclePoliciesResponse,
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
