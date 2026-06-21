"""Generated from Smithy shape ``com.amazonaws.xray#PutResourcePolicy``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_xray._auth._signers
import aws_sdk_xray._auth._sigv4
import aws_sdk_xray.errors.invalid_policy_revision_id_exception
import aws_sdk_xray.errors.lockout_prevention_exception
import aws_sdk_xray.errors.malformed_policy_document_exception
import aws_sdk_xray.errors.policy_count_limit_exceeded_exception
import aws_sdk_xray.errors.policy_size_limit_exceeded_exception
import aws_sdk_xray.errors.throttled_exception
import aws_sdk_xray.types.put_resource_policy_request
import aws_sdk_xray.types.put_resource_policy_result
import aws_sdk_xray.types.resource_policy
from aws_sdk_xray._protocol.errors import parse_error_metadata_json
from aws_sdk_xray._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_xray._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_xray.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidPolicyRevisionIdException":
            raise aws_sdk_xray.errors.invalid_policy_revision_id_exception.InvalidPolicyRevisionIdException.from_json(
                data
            )
        case "LockoutPreventionException":
            raise aws_sdk_xray.errors.lockout_prevention_exception.LockoutPreventionException.from_json(
                data
            )
        case "MalformedPolicyDocumentException":
            raise aws_sdk_xray.errors.malformed_policy_document_exception.MalformedPolicyDocumentException.from_json(
                data
            )
        case "PolicyCountLimitExceededException":
            raise aws_sdk_xray.errors.policy_count_limit_exceeded_exception.PolicyCountLimitExceededException.from_json(
                data
            )
        case "PolicySizeLimitExceededException":
            raise aws_sdk_xray.errors.policy_size_limit_exceeded_exception.PolicySizeLimitExceededException.from_json(
                data
            )
        case "ThrottledException":
            raise aws_sdk_xray.errors.throttled_exception.ThrottledException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_xray.types.put_resource_policy_result.PutResourcePolicyResult:
    out: aws_sdk_xray.types.put_resource_policy_result.PutResourcePolicyResult = (
        aws_sdk_xray.types.put_resource_policy_result.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_xray.types.put_resource_policy_result.PutResourcePolicyResult:
    out: aws_sdk_xray.types.put_resource_policy_result.PutResourcePolicyResult = (
        aws_sdk_xray.types.put_resource_policy_result.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_xray._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_xray._auth._sigv4.build_sigv4_auth_scheme("xray", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_xray._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_xray.types.put_resource_policy_request.PutResourcePolicyRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/PutResourcePolicy"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_xray.types.put_resource_policy_request

    body: bytes | None = json.dumps(
        aws_sdk_xray.types.put_resource_policy_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def put_resource_policy(
    options: OperationOptions,
    input_: aws_sdk_xray.types.put_resource_policy_request.PutResourcePolicyRequest,
) -> tuple[
    aws_sdk_xray.types.put_resource_policy_result.PutResourcePolicyResult,
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


async def async_put_resource_policy(
    options: AsyncOperationOptions,
    input_: aws_sdk_xray.types.put_resource_policy_request.PutResourcePolicyRequest,
) -> tuple[
    aws_sdk_xray.types.put_resource_policy_result.PutResourcePolicyResult,
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
