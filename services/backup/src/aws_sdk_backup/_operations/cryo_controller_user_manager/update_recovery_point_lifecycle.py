"""Generated from Smithy shape ``com.amazonaws.backup#UpdateRecoveryPointLifecycle``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_backup._auth._signers
import aws_sdk_backup._auth._sigv4
import aws_sdk_backup.errors.invalid_parameter_value_exception
import aws_sdk_backup.errors.invalid_request_exception
import aws_sdk_backup.errors.missing_parameter_value_exception
import aws_sdk_backup.errors.resource_not_found_exception
import aws_sdk_backup.errors.service_unavailable_exception
import aws_sdk_backup.types.calculated_lifecycle
import aws_sdk_backup.types.lifecycle
import aws_sdk_backup.types.update_recovery_point_lifecycle_input
import aws_sdk_backup.types.update_recovery_point_lifecycle_output
from aws_sdk_backup._protocol.errors import parse_error_metadata_json
from aws_sdk_backup._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_backup._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_backup.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            raise aws_sdk_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "InvalidRequestException":
            raise aws_sdk_backup.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "MissingParameterValueException":
            raise aws_sdk_backup.errors.missing_parameter_value_exception.MissingParameterValueException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_backup.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_backup.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_backup.types.update_recovery_point_lifecycle_output.UpdateRecoveryPointLifecycleOutput:
    out: aws_sdk_backup.types.update_recovery_point_lifecycle_output.UpdateRecoveryPointLifecycleOutput = aws_sdk_backup.types.update_recovery_point_lifecycle_output.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_backup.types.update_recovery_point_lifecycle_output.UpdateRecoveryPointLifecycleOutput:
    out: aws_sdk_backup.types.update_recovery_point_lifecycle_output.UpdateRecoveryPointLifecycleOutput = aws_sdk_backup.types.update_recovery_point_lifecycle_output.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_backup._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_backup._auth._sigv4.build_sigv4_auth_scheme(
                "backup", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_backup._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_backup.types.update_recovery_point_lifecycle_input.UpdateRecoveryPointLifecycleInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/backup-vaults/{BackupVaultName}/recovery-points/{RecoveryPointArn}"
    )
    url = url.replace(
        "{BackupVaultName}", quote(str(input_["backup_vault_name"]), safe="")
    )
    url = url.replace(
        "{RecoveryPointArn}", quote(str(input_["recovery_point_arn"]), safe="")
    )
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_backup.types.update_recovery_point_lifecycle_input

    body: bytes | None = json.dumps(
        aws_sdk_backup.types.update_recovery_point_lifecycle_input.serialize_json(
            input_
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def update_recovery_point_lifecycle(
    options: OperationOptions,
    input_: aws_sdk_backup.types.update_recovery_point_lifecycle_input.UpdateRecoveryPointLifecycleInput,
) -> tuple[
    aws_sdk_backup.types.update_recovery_point_lifecycle_output.UpdateRecoveryPointLifecycleOutput,
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


async def async_update_recovery_point_lifecycle(
    options: AsyncOperationOptions,
    input_: aws_sdk_backup.types.update_recovery_point_lifecycle_input.UpdateRecoveryPointLifecycleInput,
) -> tuple[
    aws_sdk_backup.types.update_recovery_point_lifecycle_output.UpdateRecoveryPointLifecycleOutput,
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
