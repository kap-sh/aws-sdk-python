"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListManagedThings``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_iot_managed_integrations._auth._signers
import capo_iot_managed_integrations._auth._sigv4
import capo_iot_managed_integrations.errors.access_denied_exception
import capo_iot_managed_integrations.errors.internal_server_exception
import capo_iot_managed_integrations.errors.service_unavailable_exception
import capo_iot_managed_integrations.errors.throttling_exception
import capo_iot_managed_integrations.errors.unauthorized_exception
import capo_iot_managed_integrations.errors.validation_exception
import capo_iot_managed_integrations.types.list_managed_things_request
import capo_iot_managed_integrations.types.list_managed_things_response
import capo_iot_managed_integrations.types.managed_thing_list_definition
import capo_iot_managed_integrations.types.provisioning_status
import capo_iot_managed_integrations.types.role
from capo_iot_managed_integrations._protocol.errors import parse_error_metadata_json
from capo_iot_managed_integrations._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_iot_managed_integrations._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_iot_managed_integrations.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "UnauthorizedException":
            raise capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException.from_json(
                data
            )
        case "ValidationException":
            raise capo_iot_managed_integrations.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_iot_managed_integrations.types.list_managed_things_response.ListManagedThingsResponse:
    out: capo_iot_managed_integrations.types.list_managed_things_response.ListManagedThingsResponse = capo_iot_managed_integrations.types.list_managed_things_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_iot_managed_integrations.types.list_managed_things_response.ListManagedThingsResponse:
    out: capo_iot_managed_integrations.types.list_managed_things_response.ListManagedThingsResponse = capo_iot_managed_integrations.types.list_managed_things_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_iot_managed_integrations._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_iot_managed_integrations._auth._sigv4.build_sigv4_auth_scheme(
                "iotmanagedintegrations", options.region
            )
        )
        if sigv4_config is not None:
            return capo_iot_managed_integrations._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_iot_managed_integrations.types.list_managed_things_request.ListManagedThingsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/managed-things"
    params: dict[str, str] = {}
    if "owner_filter" in input_:
        params["OwnerFilter"] = str(input_["owner_filter"])
    if "credential_locker_filter" in input_:
        params["CredentialLockerFilter"] = str(input_["credential_locker_filter"])
    if "role_filter" in input_:
        params["RoleFilter"] = str(input_["role_filter"])
    if "parent_controller_identifier_filter" in input_:
        params["ParentControllerIdentifierFilter"] = str(
            input_["parent_controller_identifier_filter"]
        )
    if "connector_policy_id_filter" in input_:
        params["ConnectorPolicyIdFilter"] = str(input_["connector_policy_id_filter"])
    if "connector_destination_id_filter" in input_:
        params["ConnectorDestinationIdFilter"] = str(
            input_["connector_destination_id_filter"]
        )
    if "connector_device_id_filter" in input_:
        params["ConnectorDeviceIdFilter"] = str(input_["connector_device_id_filter"])
    if "serial_number_filter" in input_:
        params["SerialNumberFilter"] = str(input_["serial_number_filter"])
    if "provisioning_status_filter" in input_:
        params["ProvisioningStatusFilter"] = str(input_["provisioning_status_filter"])
    if "next_token" in input_:
        params["NextToken"] = str(input_["next_token"])
    if "max_results" in input_:
        params["MaxResults"] = str(input_["max_results"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_managed_things(
    options: OperationOptions,
    input_: capo_iot_managed_integrations.types.list_managed_things_request.ListManagedThingsRequest,
) -> tuple[
    capo_iot_managed_integrations.types.list_managed_things_response.ListManagedThingsResponse,
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


async def async_list_managed_things(
    options: AsyncOperationOptions,
    input_: capo_iot_managed_integrations.types.list_managed_things_request.ListManagedThingsRequest,
) -> tuple[
    capo_iot_managed_integrations.types.list_managed_things_response.ListManagedThingsResponse,
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
