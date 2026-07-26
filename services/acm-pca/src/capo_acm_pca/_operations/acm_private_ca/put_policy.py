"""Generated from Smithy shape ``com.amazonaws.acmpca#PutPolicy``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_acm_pca._auth._signers
import capo_acm_pca._auth._sigv4
import capo_acm_pca.errors.concurrent_modification_exception
import capo_acm_pca.errors.invalid_arn_exception
import capo_acm_pca.errors.invalid_policy_exception
import capo_acm_pca.errors.invalid_state_exception
import capo_acm_pca.errors.lockout_prevented_exception
import capo_acm_pca.errors.request_failed_exception
import capo_acm_pca.errors.resource_not_found_exception
import capo_acm_pca.types.put_policy_request
from capo_acm_pca._protocol.errors import parse_error_metadata_json
from capo_acm_pca._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_acm_pca._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_acm_pca.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConcurrentModificationException":
            raise capo_acm_pca.errors.concurrent_modification_exception.ConcurrentModificationException.from_aws_json_1_1(
                data
            )
        case "InvalidArnException":
            raise capo_acm_pca.errors.invalid_arn_exception.InvalidArnException.from_aws_json_1_1(
                data
            )
        case "InvalidPolicyException":
            raise capo_acm_pca.errors.invalid_policy_exception.InvalidPolicyException.from_aws_json_1_1(
                data
            )
        case "InvalidStateException":
            raise capo_acm_pca.errors.invalid_state_exception.InvalidStateException.from_aws_json_1_1(
                data
            )
        case "LockoutPreventedException":
            raise capo_acm_pca.errors.lockout_prevented_exception.LockoutPreventedException.from_aws_json_1_1(
                data
            )
        case "RequestFailedException":
            raise capo_acm_pca.errors.request_failed_exception.RequestFailedException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            raise capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_acm_pca._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_acm_pca._auth._sigv4.build_sigv4_auth_scheme(
                "acm-pca", options.region
            )
        )
        if sigv4_config is not None:
            return capo_acm_pca._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_acm_pca.types.put_policy_request.PutPolicyRequest,
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
    headers["X-Amz-Target"] = "ACMPrivateCA.PutPolicy"
    body: bytes | None = json.dumps(
        capo_acm_pca.types.put_policy_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def put_policy(
    options: OperationOptions,
    input_: capo_acm_pca.types.put_policy_request.PutPolicyRequest,
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


async def async_put_policy(
    options: AsyncOperationOptions,
    input_: capo_acm_pca.types.put_policy_request.PutPolicyRequest,
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
