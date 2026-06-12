"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EnableFederation``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_cloudtrail._auth._signers
import aws_sdk_cloudtrail._auth._sigv4
from aws_sdk_cloudtrail._protocol.errors import parse_error_metadata_json
from aws_sdk_cloudtrail._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloudtrail._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudtrail.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.enable_federation_request
    import aws_sdk_cloudtrail.types.enable_federation_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_cloudtrail.errors.access_denied_exception

            raise aws_sdk_cloudtrail.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "CloudTrailAccessNotEnabledException":
            import aws_sdk_cloudtrail.errors.cloud_trail_access_not_enabled_exception

            raise aws_sdk_cloudtrail.errors.cloud_trail_access_not_enabled_exception.CloudTrailAccessNotEnabledException.from_aws_json_1_1(
                data
            )
        case "ConcurrentModificationException":
            import aws_sdk_cloudtrail.errors.concurrent_modification_exception

            raise aws_sdk_cloudtrail.errors.concurrent_modification_exception.ConcurrentModificationException.from_aws_json_1_1(
                data
            )
        case "EventDataStoreARNInvalidException":
            import aws_sdk_cloudtrail.errors.event_data_store_arn_invalid_exception

            raise aws_sdk_cloudtrail.errors.event_data_store_arn_invalid_exception.EventDataStoreARNInvalidException.from_aws_json_1_1(
                data
            )
        case "EventDataStoreFederationEnabledException":
            import aws_sdk_cloudtrail.errors.event_data_store_federation_enabled_exception

            raise aws_sdk_cloudtrail.errors.event_data_store_federation_enabled_exception.EventDataStoreFederationEnabledException.from_aws_json_1_1(
                data
            )
        case "EventDataStoreNotFoundException":
            import aws_sdk_cloudtrail.errors.event_data_store_not_found_exception

            raise aws_sdk_cloudtrail.errors.event_data_store_not_found_exception.EventDataStoreNotFoundException.from_aws_json_1_1(
                data
            )
        case "InactiveEventDataStoreException":
            import aws_sdk_cloudtrail.errors.inactive_event_data_store_exception

            raise aws_sdk_cloudtrail.errors.inactive_event_data_store_exception.InactiveEventDataStoreException.from_aws_json_1_1(
                data
            )
        case "InsufficientDependencyServiceAccessPermissionException":
            import aws_sdk_cloudtrail.errors.insufficient_dependency_service_access_permission_exception

            raise aws_sdk_cloudtrail.errors.insufficient_dependency_service_access_permission_exception.InsufficientDependencyServiceAccessPermissionException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            import aws_sdk_cloudtrail.errors.invalid_parameter_exception

            raise aws_sdk_cloudtrail.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "NoManagementAccountSLRExistsException":
            import aws_sdk_cloudtrail.errors.no_management_account_slr_exists_exception

            raise aws_sdk_cloudtrail.errors.no_management_account_slr_exists_exception.NoManagementAccountSLRExistsException.from_aws_json_1_1(
                data
            )
        case "NotOrganizationMasterAccountException":
            import aws_sdk_cloudtrail.errors.not_organization_master_account_exception

            raise aws_sdk_cloudtrail.errors.not_organization_master_account_exception.NotOrganizationMasterAccountException.from_aws_json_1_1(
                data
            )
        case "OperationNotPermittedException":
            import aws_sdk_cloudtrail.errors.operation_not_permitted_exception

            raise aws_sdk_cloudtrail.errors.operation_not_permitted_exception.OperationNotPermittedException.from_aws_json_1_1(
                data
            )
        case "OrganizationNotInAllFeaturesModeException":
            import aws_sdk_cloudtrail.errors.organization_not_in_all_features_mode_exception

            raise aws_sdk_cloudtrail.errors.organization_not_in_all_features_mode_exception.OrganizationNotInAllFeaturesModeException.from_aws_json_1_1(
                data
            )
        case "OrganizationsNotInUseException":
            import aws_sdk_cloudtrail.errors.organizations_not_in_use_exception

            raise aws_sdk_cloudtrail.errors.organizations_not_in_use_exception.OrganizationsNotInUseException.from_aws_json_1_1(
                data
            )
        case "UnsupportedOperationException":
            import aws_sdk_cloudtrail.errors.unsupported_operation_exception

            raise aws_sdk_cloudtrail.errors.unsupported_operation_exception.UnsupportedOperationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cloudtrail.types.enable_federation_response.EnableFederationResponse:
    import aws_sdk_cloudtrail.types.enable_federation_response

    out: aws_sdk_cloudtrail.types.enable_federation_response.EnableFederationResponse = aws_sdk_cloudtrail.types.enable_federation_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloudtrail._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cloudtrail._auth._sigv4.build_sigv4_auth_scheme(
                "cloudtrail", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cloudtrail._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_cloudtrail.types.enable_federation_request.EnableFederationRequest,
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
    headers["X-Amz-Target"] = "CloudTrail_20131101.EnableFederation"
    import aws_sdk_cloudtrail.types.enable_federation_request

    body: bytes | None = json.dumps(
        aws_sdk_cloudtrail.types.enable_federation_request.serialize_aws_json_1_1(input)
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


def enable_federation(
    options: OperationOptions,
    input: aws_sdk_cloudtrail.types.enable_federation_request.EnableFederationRequest,
) -> tuple[
    aws_sdk_cloudtrail.types.enable_federation_response.EnableFederationResponse,
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


async def async_enable_federation(
    options: AsyncOperationOptions,
    input: aws_sdk_cloudtrail.types.enable_federation_request.EnableFederationRequest,
) -> tuple[
    aws_sdk_cloudtrail.types.enable_federation_response.EnableFederationResponse,
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
