"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AssociateDatasetKmsKey``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import urlencode

import zapros

import aws_sdk_cloudwatch._auth._signers
import aws_sdk_cloudwatch._auth._sigv4
from aws_sdk_cloudwatch._protocol.errors import parse_error_metadata_json
from aws_sdk_cloudwatch._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloudwatch._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudwatch.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.associate_dataset_kms_key_input
    import aws_sdk_cloudwatch.types.associate_dataset_kms_key_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConflictException":
            import aws_sdk_cloudwatch.errors.conflict_exception

            raise aws_sdk_cloudwatch.errors.conflict_exception.ConflictException.from_aws_json_1_0(
                data
            )
        case "KmsAccessDeniedException":
            import aws_sdk_cloudwatch.errors.kms_access_denied_exception

            raise aws_sdk_cloudwatch.errors.kms_access_denied_exception.KmsAccessDeniedException.from_aws_json_1_0(
                data
            )
        case "KmsKeyDisabledException":
            import aws_sdk_cloudwatch.errors.kms_key_disabled_exception

            raise aws_sdk_cloudwatch.errors.kms_key_disabled_exception.KmsKeyDisabledException.from_aws_json_1_0(
                data
            )
        case "KmsKeyNotFoundException":
            import aws_sdk_cloudwatch.errors.kms_key_not_found_exception

            raise aws_sdk_cloudwatch.errors.kms_key_not_found_exception.KmsKeyNotFoundException.from_aws_json_1_0(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_cloudwatch.errors.resource_not_found_exception

            raise aws_sdk_cloudwatch.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cloudwatch.types.associate_dataset_kms_key_output.AssociateDatasetKmsKeyOutput:
    out: aws_sdk_cloudwatch.types.associate_dataset_kms_key_output.AssociateDatasetKmsKeyOutput = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloudwatch._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cloudwatch._auth._sigv4.build_sigv4_auth_scheme(
                "monitoring", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cloudwatch._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_cloudwatch.types.associate_dataset_kms_key_input.AssociateDatasetKmsKeyInput,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "GraniteServiceVersion20100801.AssociateDatasetKmsKey"
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "AssociateDatasetKmsKey"))
    pairs.append(("Version", "2010-08-01"))
    import aws_sdk_cloudwatch.types.associate_dataset_kms_key_input

    aws_sdk_cloudwatch.types.associate_dataset_kms_key_input.serialize_query(
        input, pairs, ""
    )
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
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


def associate_dataset_kms_key(
    options: OperationOptions,
    input: aws_sdk_cloudwatch.types.associate_dataset_kms_key_input.AssociateDatasetKmsKeyInput,
) -> tuple[
    aws_sdk_cloudwatch.types.associate_dataset_kms_key_output.AssociateDatasetKmsKeyOutput,
    zapros.Response,
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


async def async_associate_dataset_kms_key(
    options: AsyncOperationOptions,
    input: aws_sdk_cloudwatch.types.associate_dataset_kms_key_input.AssociateDatasetKmsKeyInput,
) -> tuple[
    aws_sdk_cloudwatch.types.associate_dataset_kms_key_output.AssociateDatasetKmsKeyOutput,
    zapros.Response,
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
