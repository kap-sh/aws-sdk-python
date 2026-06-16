"""Generated from Smithy shape ``com.amazonaws.ssm#CreateAssociationBatch``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_ssm._auth._signers
import aws_sdk_ssm._auth._sigv4
from aws_sdk_ssm._protocol.errors import parse_error_metadata_json
from aws_sdk_ssm._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_ssm._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_ssm.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.create_association_batch_request
    import aws_sdk_ssm.types.create_association_batch_result


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AssociationLimitExceeded":
            import aws_sdk_ssm.errors.association_limit_exceeded

            raise aws_sdk_ssm.errors.association_limit_exceeded.AssociationLimitExceeded.from_aws_json_1_1(
                data
            )
        case "DuplicateInstanceId":
            import aws_sdk_ssm.errors.duplicate_instance_id

            raise aws_sdk_ssm.errors.duplicate_instance_id.DuplicateInstanceId.from_aws_json_1_1(
                data
            )
        case "InternalServerError":
            import aws_sdk_ssm.errors.internal_server_error

            raise aws_sdk_ssm.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data
            )
        case "InvalidDocument":
            import aws_sdk_ssm.errors.invalid_document

            raise aws_sdk_ssm.errors.invalid_document.InvalidDocument.from_aws_json_1_1(
                data
            )
        case "InvalidDocumentVersion":
            import aws_sdk_ssm.errors.invalid_document_version

            raise aws_sdk_ssm.errors.invalid_document_version.InvalidDocumentVersion.from_aws_json_1_1(
                data
            )
        case "InvalidInstanceId":
            import aws_sdk_ssm.errors.invalid_instance_id

            raise aws_sdk_ssm.errors.invalid_instance_id.InvalidInstanceId.from_aws_json_1_1(
                data
            )
        case "InvalidOutputLocation":
            import aws_sdk_ssm.errors.invalid_output_location

            raise aws_sdk_ssm.errors.invalid_output_location.InvalidOutputLocation.from_aws_json_1_1(
                data
            )
        case "InvalidParameters":
            import aws_sdk_ssm.errors.invalid_parameters

            raise aws_sdk_ssm.errors.invalid_parameters.InvalidParameters.from_aws_json_1_1(
                data
            )
        case "InvalidSchedule":
            import aws_sdk_ssm.errors.invalid_schedule

            raise aws_sdk_ssm.errors.invalid_schedule.InvalidSchedule.from_aws_json_1_1(
                data
            )
        case "InvalidTarget":
            import aws_sdk_ssm.errors.invalid_target

            raise aws_sdk_ssm.errors.invalid_target.InvalidTarget.from_aws_json_1_1(
                data
            )
        case "InvalidTargetMaps":
            import aws_sdk_ssm.errors.invalid_target_maps

            raise aws_sdk_ssm.errors.invalid_target_maps.InvalidTargetMaps.from_aws_json_1_1(
                data
            )
        case "UnsupportedPlatformType":
            import aws_sdk_ssm.errors.unsupported_platform_type

            raise aws_sdk_ssm.errors.unsupported_platform_type.UnsupportedPlatformType.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_ssm.types.create_association_batch_result.CreateAssociationBatchResult:
    import aws_sdk_ssm.types.create_association_batch_result

    out: aws_sdk_ssm.types.create_association_batch_result.CreateAssociationBatchResult = aws_sdk_ssm.types.create_association_batch_result.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_ssm._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_ssm._auth._sigv4.build_sigv4_auth_scheme("ssm", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_ssm._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_ssm.types.create_association_batch_request.CreateAssociationBatchRequest,
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
    headers["X-Amz-Target"] = "AmazonSSM.CreateAssociationBatch"
    import aws_sdk_ssm.types.create_association_batch_request

    body: bytes | None = json.dumps(
        aws_sdk_ssm.types.create_association_batch_request.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_association_batch(
    options: OperationOptions,
    input_: aws_sdk_ssm.types.create_association_batch_request.CreateAssociationBatchRequest,
) -> tuple[
    aws_sdk_ssm.types.create_association_batch_result.CreateAssociationBatchResult,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_create_association_batch(
    options: AsyncOperationOptions,
    input_: aws_sdk_ssm.types.create_association_batch_request.CreateAssociationBatchRequest,
) -> tuple[
    aws_sdk_ssm.types.create_association_batch_result.CreateAssociationBatchResult,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
