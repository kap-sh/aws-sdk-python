"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#UpdateCloudConnector``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_iot_managed_integrations._auth._signers
import capo_iot_managed_integrations._auth._sigv4
import capo_iot_managed_integrations.errors.access_denied_exception
import capo_iot_managed_integrations.errors.internal_server_exception
import capo_iot_managed_integrations.errors.resource_not_found_exception
import capo_iot_managed_integrations.errors.throttling_exception
import capo_iot_managed_integrations.errors.unauthorized_exception
import capo_iot_managed_integrations.errors.validation_exception
import capo_iot_managed_integrations.types.update_cloud_connector_request
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
        case "ResourceNotFoundException":
            raise capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
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
    input_: capo_iot_managed_integrations.types.update_cloud_connector_request.UpdateCloudConnectorRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/cloud-connectors/{Identifier}"
    url = url.replace("{Identifier}", quote(str(input_["identifier"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_iot_managed_integrations.types.update_cloud_connector_request.serialize_json(
            input_
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def update_cloud_connector(
    options: OperationOptions,
    input_: capo_iot_managed_integrations.types.update_cloud_connector_request.UpdateCloudConnectorRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_update_cloud_connector(
    options: AsyncOperationOptions,
    input_: capo_iot_managed_integrations.types.update_cloud_connector_request.UpdateCloudConnectorRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
