"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StartEventDataStoreIngestion``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudtrail._auth._signers
import capo_cloudtrail._auth._sigv4
import capo_cloudtrail.errors.conflict_exception
import capo_cloudtrail.errors.event_data_store_arn_invalid_exception
import capo_cloudtrail.errors.event_data_store_not_found_exception
import capo_cloudtrail.errors.insufficient_dependency_service_access_permission_exception
import capo_cloudtrail.errors.invalid_event_data_store_category_exception
import capo_cloudtrail.errors.invalid_event_data_store_status_exception
import capo_cloudtrail.errors.invalid_parameter_exception
import capo_cloudtrail.errors.no_management_account_slr_exists_exception
import capo_cloudtrail.errors.not_organization_master_account_exception
import capo_cloudtrail.errors.operation_not_permitted_exception
import capo_cloudtrail.errors.unsupported_operation_exception
import capo_cloudtrail.types.start_event_data_store_ingestion_request
import capo_cloudtrail.types.start_event_data_store_ingestion_response
from capo_cloudtrail._protocol.errors import parse_error_metadata_json
from capo_cloudtrail._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudtrail._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_cloudtrail.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConflictException":
            raise capo_cloudtrail.errors.conflict_exception.ConflictException.from_aws_json_1_1(
                data
            )
        case "EventDataStoreARNInvalidException":
            raise capo_cloudtrail.errors.event_data_store_arn_invalid_exception.EventDataStoreARNInvalidException.from_aws_json_1_1(
                data
            )
        case "EventDataStoreNotFoundException":
            raise capo_cloudtrail.errors.event_data_store_not_found_exception.EventDataStoreNotFoundException.from_aws_json_1_1(
                data
            )
        case "InsufficientDependencyServiceAccessPermissionException":
            raise capo_cloudtrail.errors.insufficient_dependency_service_access_permission_exception.InsufficientDependencyServiceAccessPermissionException.from_aws_json_1_1(
                data
            )
        case "InvalidEventDataStoreCategoryException":
            raise capo_cloudtrail.errors.invalid_event_data_store_category_exception.InvalidEventDataStoreCategoryException.from_aws_json_1_1(
                data
            )
        case "InvalidEventDataStoreStatusException":
            raise capo_cloudtrail.errors.invalid_event_data_store_status_exception.InvalidEventDataStoreStatusException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            raise capo_cloudtrail.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "NoManagementAccountSLRExistsException":
            raise capo_cloudtrail.errors.no_management_account_slr_exists_exception.NoManagementAccountSLRExistsException.from_aws_json_1_1(
                data
            )
        case "NotOrganizationMasterAccountException":
            raise capo_cloudtrail.errors.not_organization_master_account_exception.NotOrganizationMasterAccountException.from_aws_json_1_1(
                data
            )
        case "OperationNotPermittedException":
            raise capo_cloudtrail.errors.operation_not_permitted_exception.OperationNotPermittedException.from_aws_json_1_1(
                data
            )
        case "UnsupportedOperationException":
            raise capo_cloudtrail.errors.unsupported_operation_exception.UnsupportedOperationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudtrail.types.start_event_data_store_ingestion_response.StartEventDataStoreIngestionResponse:
    out: capo_cloudtrail.types.start_event_data_store_ingestion_response.StartEventDataStoreIngestionResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudtrail.types.start_event_data_store_ingestion_response.StartEventDataStoreIngestionResponse:
    out: capo_cloudtrail.types.start_event_data_store_ingestion_response.StartEventDataStoreIngestionResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudtrail._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_cloudtrail._auth._sigv4.build_sigv4_auth_scheme(
                "cloudtrail", options.region
            )
        )
        if sigv4_config is not None:
            return capo_cloudtrail._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudtrail.types.start_event_data_store_ingestion_request.StartEventDataStoreIngestionRequest,
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
    headers["X-Amz-Target"] = "CloudTrail_20131101.StartEventDataStoreIngestion"
    body: bytes | None = json.dumps(
        capo_cloudtrail.types.start_event_data_store_ingestion_request.serialize_aws_json_1_1(
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


def start_event_data_store_ingestion(
    options: OperationOptions,
    input_: capo_cloudtrail.types.start_event_data_store_ingestion_request.StartEventDataStoreIngestionRequest,
) -> tuple[
    capo_cloudtrail.types.start_event_data_store_ingestion_response.StartEventDataStoreIngestionResponse,
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


async def async_start_event_data_store_ingestion(
    options: AsyncOperationOptions,
    input_: capo_cloudtrail.types.start_event_data_store_ingestion_request.StartEventDataStoreIngestionRequest,
) -> tuple[
    capo_cloudtrail.types.start_event_data_store_ingestion_response.StartEventDataStoreIngestionResponse,
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
