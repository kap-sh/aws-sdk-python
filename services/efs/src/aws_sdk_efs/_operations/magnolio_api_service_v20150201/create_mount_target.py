"""Generated from Smithy shape ``com.amazonaws.efs#CreateMountTarget``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_efs._auth._signers
import aws_sdk_efs._auth._sigv4
import aws_sdk_efs.errors.availability_zones_mismatch
import aws_sdk_efs.errors.bad_request
import aws_sdk_efs.errors.file_system_not_found
import aws_sdk_efs.errors.incorrect_file_system_life_cycle_state
import aws_sdk_efs.errors.internal_server_error
import aws_sdk_efs.errors.ip_address_in_use
import aws_sdk_efs.errors.mount_target_conflict
import aws_sdk_efs.errors.network_interface_limit_exceeded
import aws_sdk_efs.errors.no_free_addresses_in_subnet
import aws_sdk_efs.errors.security_group_limit_exceeded
import aws_sdk_efs.errors.security_group_not_found
import aws_sdk_efs.errors.subnet_not_found
import aws_sdk_efs.errors.unsupported_availability_zone
import aws_sdk_efs.types.create_mount_target_request
import aws_sdk_efs.types.ip_address_type
import aws_sdk_efs.types.life_cycle_state
import aws_sdk_efs.types.mount_target_description
import aws_sdk_efs.types.security_groups
from aws_sdk_efs._protocol.errors import parse_error_metadata_json
from aws_sdk_efs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_efs._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_efs.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AvailabilityZonesMismatch":
            raise aws_sdk_efs.errors.availability_zones_mismatch.AvailabilityZonesMismatch.from_json(
                data
            )
        case "BadRequest":
            raise aws_sdk_efs.errors.bad_request.BadRequest.from_json(data)
        case "FileSystemNotFound":
            raise aws_sdk_efs.errors.file_system_not_found.FileSystemNotFound.from_json(
                data
            )
        case "IncorrectFileSystemLifeCycleState":
            raise aws_sdk_efs.errors.incorrect_file_system_life_cycle_state.IncorrectFileSystemLifeCycleState.from_json(
                data
            )
        case "InternalServerError":
            raise aws_sdk_efs.errors.internal_server_error.InternalServerError.from_json(
                data
            )
        case "IpAddressInUse":
            raise aws_sdk_efs.errors.ip_address_in_use.IpAddressInUse.from_json(data)
        case "MountTargetConflict":
            raise aws_sdk_efs.errors.mount_target_conflict.MountTargetConflict.from_json(
                data
            )
        case "NetworkInterfaceLimitExceeded":
            raise aws_sdk_efs.errors.network_interface_limit_exceeded.NetworkInterfaceLimitExceeded.from_json(
                data
            )
        case "NoFreeAddressesInSubnet":
            raise aws_sdk_efs.errors.no_free_addresses_in_subnet.NoFreeAddressesInSubnet.from_json(
                data
            )
        case "SecurityGroupLimitExceeded":
            raise aws_sdk_efs.errors.security_group_limit_exceeded.SecurityGroupLimitExceeded.from_json(
                data
            )
        case "SecurityGroupNotFound":
            raise aws_sdk_efs.errors.security_group_not_found.SecurityGroupNotFound.from_json(
                data
            )
        case "SubnetNotFound":
            raise aws_sdk_efs.errors.subnet_not_found.SubnetNotFound.from_json(data)
        case "UnsupportedAvailabilityZone":
            raise aws_sdk_efs.errors.unsupported_availability_zone.UnsupportedAvailabilityZone.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_efs.types.mount_target_description.MountTargetDescription:
    out: aws_sdk_efs.types.mount_target_description.MountTargetDescription = (
        aws_sdk_efs.types.mount_target_description.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_efs.types.mount_target_description.MountTargetDescription:
    out: aws_sdk_efs.types.mount_target_description.MountTargetDescription = (
        aws_sdk_efs.types.mount_target_description.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_efs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_efs._auth._sigv4.build_sigv4_auth_scheme(
                "elasticfilesystem", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_efs._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_efs.types.create_mount_target_request.CreateMountTargetRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2015-02-01/mount-targets"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_efs.types.create_mount_target_request

    body: bytes | None = json.dumps(
        aws_sdk_efs.types.create_mount_target_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_mount_target(
    options: OperationOptions,
    input_: aws_sdk_efs.types.create_mount_target_request.CreateMountTargetRequest,
) -> tuple[
    aws_sdk_efs.types.mount_target_description.MountTargetDescription, zapros.Response
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


async def async_create_mount_target(
    options: AsyncOperationOptions,
    input_: aws_sdk_efs.types.create_mount_target_request.CreateMountTargetRequest,
) -> tuple[
    aws_sdk_efs.types.mount_target_description.MountTargetDescription, zapros.Response
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
