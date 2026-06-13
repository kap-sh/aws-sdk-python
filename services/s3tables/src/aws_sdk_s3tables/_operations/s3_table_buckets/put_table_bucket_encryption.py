"""Generated from Smithy shape ``com.amazonaws.s3tables#PutTableBucketEncryption``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_s3tables._auth._signers
import aws_sdk_s3tables._auth._sigv4
from aws_sdk_s3tables._protocol.errors import parse_error_metadata_json
from aws_sdk_s3tables._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3tables._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_s3tables.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.put_table_bucket_encryption_request


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            import aws_sdk_s3tables.errors.bad_request_exception

            raise aws_sdk_s3tables.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ConflictException":
            import aws_sdk_s3tables.errors.conflict_exception

            raise aws_sdk_s3tables.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "ForbiddenException":
            import aws_sdk_s3tables.errors.forbidden_exception

            raise aws_sdk_s3tables.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "InternalServerErrorException":
            import aws_sdk_s3tables.errors.internal_server_error_exception

            raise aws_sdk_s3tables.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "NotFoundException":
            import aws_sdk_s3tables.errors.not_found_exception

            raise aws_sdk_s3tables.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_s3tables.errors.too_many_requests_exception

            raise aws_sdk_s3tables.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_s3tables._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_s3tables._auth._sigv4.build_sigv4_auth_scheme(
                "s3tables", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_s3tables._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_s3tables.types.put_table_bucket_encryption_request.PutTableBucketEncryptionRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/buckets/{tableBucketARN}/encryption"
    url = url.replace(
        "{tableBucketARN}", quote(str(input["table_bucket_arn"]), safe="")
    )
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_s3tables.types.put_table_bucket_encryption_request

    body: bytes | None = json.dumps(
        aws_sdk_s3tables.types.put_table_bucket_encryption_request.serialize_json(input)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "PUT",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def put_table_bucket_encryption(
    options: OperationOptions,
    input: aws_sdk_s3tables.types.put_table_bucket_encryption_request.PutTableBucketEncryptionRequest,
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


async def async_put_table_bucket_encryption(
    options: AsyncOperationOptions,
    input: aws_sdk_s3tables.types.put_table_bucket_encryption_request.PutTableBucketEncryptionRequest,
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
