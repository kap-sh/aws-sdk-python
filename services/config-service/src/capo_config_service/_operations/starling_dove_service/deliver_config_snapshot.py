"""Generated from Smithy shape ``com.amazonaws.configservice#DeliverConfigSnapshot``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_config_service._auth._signers
import capo_config_service._auth._sigv4
import capo_config_service.errors.no_available_configuration_recorder_exception
import capo_config_service.errors.no_running_configuration_recorder_exception
import capo_config_service.errors.no_such_delivery_channel_exception
import capo_config_service.types.deliver_config_snapshot_request
import capo_config_service.types.deliver_config_snapshot_response
from capo_config_service._protocol.errors import parse_error_metadata_json
from capo_config_service._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_config_service._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_config_service.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "NoAvailableConfigurationRecorderException":
            raise capo_config_service.errors.no_available_configuration_recorder_exception.NoAvailableConfigurationRecorderException.from_aws_json_1_1(
                data
            )
        case "NoRunningConfigurationRecorderException":
            raise capo_config_service.errors.no_running_configuration_recorder_exception.NoRunningConfigurationRecorderException.from_aws_json_1_1(
                data
            )
        case "NoSuchDeliveryChannelException":
            raise capo_config_service.errors.no_such_delivery_channel_exception.NoSuchDeliveryChannelException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_config_service.types.deliver_config_snapshot_response.DeliverConfigSnapshotResponse:
    out: capo_config_service.types.deliver_config_snapshot_response.DeliverConfigSnapshotResponse = capo_config_service.types.deliver_config_snapshot_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_config_service.types.deliver_config_snapshot_response.DeliverConfigSnapshotResponse:
    out: capo_config_service.types.deliver_config_snapshot_response.DeliverConfigSnapshotResponse = capo_config_service.types.deliver_config_snapshot_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_config_service._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_config_service._auth._sigv4.build_sigv4_auth_scheme(
                "config", options.region
            )
        )
        if sigv4_config is not None:
            return capo_config_service._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_config_service.types.deliver_config_snapshot_request.DeliverConfigSnapshotRequest,
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
    headers["X-Amz-Target"] = "StarlingDoveService.DeliverConfigSnapshot"
    body: bytes | None = json.dumps(
        capo_config_service.types.deliver_config_snapshot_request.serialize_aws_json_1_1(
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


def deliver_config_snapshot(
    options: OperationOptions,
    input_: capo_config_service.types.deliver_config_snapshot_request.DeliverConfigSnapshotRequest,
) -> tuple[
    capo_config_service.types.deliver_config_snapshot_response.DeliverConfigSnapshotResponse,
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


async def async_deliver_config_snapshot(
    options: AsyncOperationOptions,
    input_: capo_config_service.types.deliver_config_snapshot_request.DeliverConfigSnapshotRequest,
) -> tuple[
    capo_config_service.types.deliver_config_snapshot_response.DeliverConfigSnapshotResponse,
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
