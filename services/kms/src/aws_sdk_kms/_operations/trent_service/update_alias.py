"""Generated from Smithy shape ``com.amazonaws.kms#UpdateAlias``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any
from aws_sdk_kms._rule_engine._endpoint_rule_set import EndpointParams, resolve
import zapros
from aws_sdk_kms.errors import UnknownServiceError
from aws_sdk_kms._protocol.errors import parse_error_metadata_json
import json
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.update_alias_request


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "DependencyTimeoutException":
            import aws_sdk_kms.errors.dependency_timeout_exception

            raise aws_sdk_kms.errors.dependency_timeout_exception.DependencyTimeoutException.from_aws_json_1_1(
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
        case "LimitExceededException":
            import aws_sdk_kms.errors.limit_exceeded_exception

            raise aws_sdk_kms.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case "NotFoundException":
            import aws_sdk_kms.errors.not_found_exception

            raise aws_sdk_kms.errors.not_found_exception.NotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


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
    input: aws_sdk_kms.types.update_alias_request.UpdateAliasRequest,
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
    headers["X-Amz-Target"] = "TrentService.UpdateAlias"
    import aws_sdk_kms.types.update_alias_request

    body: bytes | None = json.dumps(
        aws_sdk_kms.types.update_alias_request.serialize_aws_json_1_1(input)
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


def update_alias(
    options: OperationOptions,
    input: aws_sdk_kms.types.update_alias_request.UpdateAliasRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_update_alias(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.update_alias_request.UpdateAliasRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
