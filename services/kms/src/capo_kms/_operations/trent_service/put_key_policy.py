"""Generated from Smithy shape ``com.amazonaws.kms#PutKeyPolicy``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_kms._auth._signers
import capo_kms._auth._sigv4
import capo_kms.errors.dependency_timeout_exception
import capo_kms.errors.invalid_arn_exception
import capo_kms.errors.kms_internal_exception
import capo_kms.errors.kms_invalid_state_exception
import capo_kms.errors.limit_exceeded_exception
import capo_kms.errors.malformed_policy_document_exception
import capo_kms.errors.not_found_exception
import capo_kms.errors.unsupported_operation_exception
import capo_kms.types.put_key_policy_request
from capo_kms._protocol.errors import parse_error_metadata_json
from capo_kms._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_kms._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_kms.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "DependencyTimeoutException":
            raise capo_kms.errors.dependency_timeout_exception.DependencyTimeoutException.from_aws_json_1_1(
                data
            )
        case "InvalidArnException":
            raise capo_kms.errors.invalid_arn_exception.InvalidArnException.from_aws_json_1_1(
                data
            )
        case "KMSInternalException":
            raise capo_kms.errors.kms_internal_exception.KMSInternalException.from_aws_json_1_1(
                data
            )
        case "KMSInvalidStateException":
            raise capo_kms.errors.kms_invalid_state_exception.KMSInvalidStateException.from_aws_json_1_1(
                data
            )
        case "LimitExceededException":
            raise capo_kms.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case "MalformedPolicyDocumentException":
            raise capo_kms.errors.malformed_policy_document_exception.MalformedPolicyDocumentException.from_aws_json_1_1(
                data
            )
        case "NotFoundException":
            raise capo_kms.errors.not_found_exception.NotFoundException.from_aws_json_1_1(
                data
            )
        case "UnsupportedOperationException":
            raise capo_kms.errors.unsupported_operation_exception.UnsupportedOperationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_kms._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_kms._auth._sigv4.build_sigv4_auth_scheme("kms", options.region)
        )
        if sigv4_config is not None:
            return capo_kms._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_kms.types.put_key_policy_request.PutKeyPolicyRequest,
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
    headers["X-Amz-Target"] = "TrentService.PutKeyPolicy"
    body: bytes | None = json.dumps(
        capo_kms.types.put_key_policy_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def put_key_policy(
    options: OperationOptions,
    input_: capo_kms.types.put_key_policy_request.PutKeyPolicyRequest,
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


async def async_put_key_policy(
    options: AsyncOperationOptions,
    input_: capo_kms.types.put_key_policy_request.PutKeyPolicyRequest,
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
