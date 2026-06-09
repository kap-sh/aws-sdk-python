"""Generated from Smithy shape ``com.amazonaws.kms#GetKeyPolicy``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_kms._auth._signers
from aws_sdk_kms._protocol.errors import parse_error_metadata_json
from aws_sdk_kms._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_kms.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.get_key_policy_request
    import aws_sdk_kms.types.get_key_policy_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "DependencyTimeoutException":
            import aws_sdk_kms.errors.dependency_timeout_exception

            raise aws_sdk_kms.errors.dependency_timeout_exception.DependencyTimeoutException.from_aws_json_1_1(
                data
            )
        case "InvalidArnException":
            import aws_sdk_kms.errors.invalid_arn_exception

            raise aws_sdk_kms.errors.invalid_arn_exception.InvalidArnException.from_aws_json_1_1(
                data
            )
        case "KMSInternalException":
            import aws_sdk_kms.errors.kms_internal_exception

            raise aws_sdk_kms.errors.kms_internal_exception.KMSInternalException.from_aws_json_1_1(
                data
            )
        case "KMSInvalidStateException":
            import aws_sdk_kms.errors.kms_invalid_state_exception

            raise aws_sdk_kms.errors.kms_invalid_state_exception.KMSInvalidStateException.from_aws_json_1_1(
                data
            )
        case "NotFoundException":
            import aws_sdk_kms.errors.not_found_exception

            raise aws_sdk_kms.errors.not_found_exception.NotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_kms.types.get_key_policy_response.GetKeyPolicyResponse:
    import aws_sdk_kms.types.get_key_policy_response

    out: aws_sdk_kms.types.get_key_policy_response.GetKeyPolicyResponse = (
        aws_sdk_kms.types.get_key_policy_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_kms._auth._signers.Signer | None:
    if auth_schemes:
        for scheme in auth_schemes:
            match scheme["name"]:
                case "sigv4" | "sigv4a" | "sigv4-s3express" if (
                    options.credentials_provider is not None
                ):
                    return aws_sdk_kms._auth._signers.SigV4Signer(
                        options.credentials_provider, auth_scheme=scheme
                    )
                case "none":
                    return None
                case _:
                    raise RuntimeError(
                        f"Could not find provider for auth scheme {scheme['name']!r}"
                    )
    if options.credentials_provider is not None:
        if options.region is None:
            raise RuntimeError("options.region is required for SigV4 signing")
        return aws_sdk_kms._auth._signers.SigV4Signer(
            options.credentials_provider,
            auth_scheme={
                "name": "sigv4",
                "signingName": "kms",
                "signingRegion": options.region,
                "disableDoubleEncoding": False,
                "disableNormalizePath": False,
            },
        )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_kms.types.get_key_policy_request.GetKeyPolicyRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "TrentService.GetKeyPolicy"
    import aws_sdk_kms.types.get_key_policy_request

    body: bytes | None = json.dumps(
        aws_sdk_kms.types.get_key_policy_request.serialize_aws_json_1_1(input)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
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


def get_key_policy(
    options: OperationOptions,
    input: aws_sdk_kms.types.get_key_policy_request.GetKeyPolicyRequest,
) -> tuple[
    aws_sdk_kms.types.get_key_policy_response.GetKeyPolicyResponse, zapros.Response
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


async def async_get_key_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.get_key_policy_request.GetKeyPolicyRequest,
) -> tuple[
    aws_sdk_kms.types.get_key_policy_response.GetKeyPolicyResponse, zapros.Response
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
