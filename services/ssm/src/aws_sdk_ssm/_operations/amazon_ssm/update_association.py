"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateAssociation``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_ssm._auth._signers
import aws_sdk_ssm._auth._sigv4
import aws_sdk_ssm.errors.association_does_not_exist
import aws_sdk_ssm.errors.association_version_limit_exceeded
import aws_sdk_ssm.errors.internal_server_error
import aws_sdk_ssm.errors.invalid_association_version
import aws_sdk_ssm.errors.invalid_document
import aws_sdk_ssm.errors.invalid_document_version
import aws_sdk_ssm.errors.invalid_output_location
import aws_sdk_ssm.errors.invalid_parameters
import aws_sdk_ssm.errors.invalid_schedule
import aws_sdk_ssm.errors.invalid_target
import aws_sdk_ssm.errors.invalid_target_maps
import aws_sdk_ssm.errors.invalid_update
import aws_sdk_ssm.errors.too_many_updates
import aws_sdk_ssm.types.alarm_configuration
import aws_sdk_ssm.types.association_compliance_severity
import aws_sdk_ssm.types.association_description
import aws_sdk_ssm.types.association_sync_compliance
import aws_sdk_ssm.types.calendar_name_or_arn_list
import aws_sdk_ssm.types.instance_association_output_location
import aws_sdk_ssm.types.parameters
import aws_sdk_ssm.types.target_locations
import aws_sdk_ssm.types.target_maps
import aws_sdk_ssm.types.targets
import aws_sdk_ssm.types.update_association_request
import aws_sdk_ssm.types.update_association_result
from aws_sdk_ssm._protocol.errors import parse_error_metadata_json
from aws_sdk_ssm._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_ssm._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_ssm.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AssociationDoesNotExist":
            raise aws_sdk_ssm.errors.association_does_not_exist.AssociationDoesNotExist.from_aws_json_1_1(
                data
            )
        case "AssociationVersionLimitExceeded":
            raise aws_sdk_ssm.errors.association_version_limit_exceeded.AssociationVersionLimitExceeded.from_aws_json_1_1(
                data
            )
        case "InternalServerError":
            raise aws_sdk_ssm.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data
            )
        case "InvalidAssociationVersion":
            raise aws_sdk_ssm.errors.invalid_association_version.InvalidAssociationVersion.from_aws_json_1_1(
                data
            )
        case "InvalidDocument":
            raise aws_sdk_ssm.errors.invalid_document.InvalidDocument.from_aws_json_1_1(
                data
            )
        case "InvalidDocumentVersion":
            raise aws_sdk_ssm.errors.invalid_document_version.InvalidDocumentVersion.from_aws_json_1_1(
                data
            )
        case "InvalidOutputLocation":
            raise aws_sdk_ssm.errors.invalid_output_location.InvalidOutputLocation.from_aws_json_1_1(
                data
            )
        case "InvalidParameters":
            raise aws_sdk_ssm.errors.invalid_parameters.InvalidParameters.from_aws_json_1_1(
                data
            )
        case "InvalidSchedule":
            raise aws_sdk_ssm.errors.invalid_schedule.InvalidSchedule.from_aws_json_1_1(
                data
            )
        case "InvalidTarget":
            raise aws_sdk_ssm.errors.invalid_target.InvalidTarget.from_aws_json_1_1(
                data
            )
        case "InvalidTargetMaps":
            raise aws_sdk_ssm.errors.invalid_target_maps.InvalidTargetMaps.from_aws_json_1_1(
                data
            )
        case "InvalidUpdate":
            raise aws_sdk_ssm.errors.invalid_update.InvalidUpdate.from_aws_json_1_1(
                data
            )
        case "TooManyUpdates":
            raise aws_sdk_ssm.errors.too_many_updates.TooManyUpdates.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_ssm.types.update_association_result.UpdateAssociationResult:
    out: aws_sdk_ssm.types.update_association_result.UpdateAssociationResult = (
        aws_sdk_ssm.types.update_association_result.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_ssm.types.update_association_result.UpdateAssociationResult:
    out: aws_sdk_ssm.types.update_association_result.UpdateAssociationResult = (
        aws_sdk_ssm.types.update_association_result.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
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
    input_: aws_sdk_ssm.types.update_association_request.UpdateAssociationRequest,
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
    headers["X-Amz-Target"] = "AmazonSSM.UpdateAssociation"
    body: bytes | None = json.dumps(
        aws_sdk_ssm.types.update_association_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def update_association(
    options: OperationOptions,
    input_: aws_sdk_ssm.types.update_association_request.UpdateAssociationRequest,
) -> tuple[
    aws_sdk_ssm.types.update_association_result.UpdateAssociationResult, zapros.Response
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


async def async_update_association(
    options: AsyncOperationOptions,
    input_: aws_sdk_ssm.types.update_association_request.UpdateAssociationRequest,
) -> tuple[
    aws_sdk_ssm.types.update_association_result.UpdateAssociationResult, zapros.Response
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
