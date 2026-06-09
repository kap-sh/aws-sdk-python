"""Generated from Smithy shape ``com.amazonaws.kms#CreateKey``."""

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
    import aws_sdk_kms.types.create_key_request
    import aws_sdk_kms.types.create_key_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CloudHsmClusterInvalidConfigurationException":
            import aws_sdk_kms.errors.cloud_hsm_cluster_invalid_configuration_exception

            raise aws_sdk_kms.errors.cloud_hsm_cluster_invalid_configuration_exception.CloudHsmClusterInvalidConfigurationException.from_aws_json_1_1(
                data
            )
        case "CustomKeyStoreInvalidStateException":
            import aws_sdk_kms.errors.custom_key_store_invalid_state_exception

            raise aws_sdk_kms.errors.custom_key_store_invalid_state_exception.CustomKeyStoreInvalidStateException.from_aws_json_1_1(
                data
            )
        case "CustomKeyStoreNotFoundException":
            import aws_sdk_kms.errors.custom_key_store_not_found_exception

            raise aws_sdk_kms.errors.custom_key_store_not_found_exception.CustomKeyStoreNotFoundException.from_aws_json_1_1(
                data
            )
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
        case "LimitExceededException":
            import aws_sdk_kms.errors.limit_exceeded_exception

            raise aws_sdk_kms.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case "MalformedPolicyDocumentException":
            import aws_sdk_kms.errors.malformed_policy_document_exception

            raise aws_sdk_kms.errors.malformed_policy_document_exception.MalformedPolicyDocumentException.from_aws_json_1_1(
                data
            )
        case "TagException":
            import aws_sdk_kms.errors.tag_exception

            raise aws_sdk_kms.errors.tag_exception.TagException.from_aws_json_1_1(data)
        case "UnsupportedOperationException":
            import aws_sdk_kms.errors.unsupported_operation_exception

            raise aws_sdk_kms.errors.unsupported_operation_exception.UnsupportedOperationException.from_aws_json_1_1(
                data
            )
        case "XksKeyAlreadyInUseException":
            import aws_sdk_kms.errors.xks_key_already_in_use_exception

            raise aws_sdk_kms.errors.xks_key_already_in_use_exception.XksKeyAlreadyInUseException.from_aws_json_1_1(
                data
            )
        case "XksKeyInvalidConfigurationException":
            import aws_sdk_kms.errors.xks_key_invalid_configuration_exception

            raise aws_sdk_kms.errors.xks_key_invalid_configuration_exception.XksKeyInvalidConfigurationException.from_aws_json_1_1(
                data
            )
        case "XksKeyNotFoundException":
            import aws_sdk_kms.errors.xks_key_not_found_exception

            raise aws_sdk_kms.errors.xks_key_not_found_exception.XksKeyNotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_kms.types.create_key_response.CreateKeyResponse:
    import aws_sdk_kms.types.create_key_response

    out: aws_sdk_kms.types.create_key_response.CreateKeyResponse = (
        aws_sdk_kms.types.create_key_response.deserialize_aws_json_1_1(
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
    input: aws_sdk_kms.types.create_key_request.CreateKeyRequest,
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
    headers["X-Amz-Target"] = "TrentService.CreateKey"
    import aws_sdk_kms.types.create_key_request

    body: bytes | None = json.dumps(
        aws_sdk_kms.types.create_key_request.serialize_aws_json_1_1(input)
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


def create_key(
    options: OperationOptions,
    input: aws_sdk_kms.types.create_key_request.CreateKeyRequest,
) -> tuple[aws_sdk_kms.types.create_key_response.CreateKeyResponse, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_create_key(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.create_key_request.CreateKeyRequest,
) -> tuple[aws_sdk_kms.types.create_key_response.CreateKeyResponse, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
