"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#SendSerialConsoleSSHPublicKey``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_ec2_instance_connect._auth._signers
import aws_sdk_ec2_instance_connect._auth._sigv4
from aws_sdk_ec2_instance_connect._protocol.errors import parse_error_metadata_json
from aws_sdk_ec2_instance_connect._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_ec2_instance_connect._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_ec2_instance_connect.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_ec2_instance_connect.types.send_serial_console_ssh_public_key_request
    import aws_sdk_ec2_instance_connect.types.send_serial_console_ssh_public_key_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AuthException":
            import aws_sdk_ec2_instance_connect.errors.auth_exception

            raise aws_sdk_ec2_instance_connect.errors.auth_exception.AuthException.from_aws_json_1_1(
                data
            )
        case "EC2InstanceNotFoundException":
            import aws_sdk_ec2_instance_connect.errors.ec2_instance_not_found_exception

            raise aws_sdk_ec2_instance_connect.errors.ec2_instance_not_found_exception.EC2InstanceNotFoundException.from_aws_json_1_1(
                data
            )
        case "EC2InstanceStateInvalidException":
            import aws_sdk_ec2_instance_connect.errors.ec2_instance_state_invalid_exception

            raise aws_sdk_ec2_instance_connect.errors.ec2_instance_state_invalid_exception.EC2InstanceStateInvalidException.from_aws_json_1_1(
                data
            )
        case "EC2InstanceTypeInvalidException":
            import aws_sdk_ec2_instance_connect.errors.ec2_instance_type_invalid_exception

            raise aws_sdk_ec2_instance_connect.errors.ec2_instance_type_invalid_exception.EC2InstanceTypeInvalidException.from_aws_json_1_1(
                data
            )
        case "EC2InstanceUnavailableException":
            import aws_sdk_ec2_instance_connect.errors.ec2_instance_unavailable_exception

            raise aws_sdk_ec2_instance_connect.errors.ec2_instance_unavailable_exception.EC2InstanceUnavailableException.from_aws_json_1_1(
                data
            )
        case "InvalidArgsException":
            import aws_sdk_ec2_instance_connect.errors.invalid_args_exception

            raise aws_sdk_ec2_instance_connect.errors.invalid_args_exception.InvalidArgsException.from_aws_json_1_1(
                data
            )
        case "SerialConsoleAccessDisabledException":
            import aws_sdk_ec2_instance_connect.errors.serial_console_access_disabled_exception

            raise aws_sdk_ec2_instance_connect.errors.serial_console_access_disabled_exception.SerialConsoleAccessDisabledException.from_aws_json_1_1(
                data
            )
        case "SerialConsoleSessionLimitExceededException":
            import aws_sdk_ec2_instance_connect.errors.serial_console_session_limit_exceeded_exception

            raise aws_sdk_ec2_instance_connect.errors.serial_console_session_limit_exceeded_exception.SerialConsoleSessionLimitExceededException.from_aws_json_1_1(
                data
            )
        case "SerialConsoleSessionUnavailableException":
            import aws_sdk_ec2_instance_connect.errors.serial_console_session_unavailable_exception

            raise aws_sdk_ec2_instance_connect.errors.serial_console_session_unavailable_exception.SerialConsoleSessionUnavailableException.from_aws_json_1_1(
                data
            )
        case "SerialConsoleSessionUnsupportedException":
            import aws_sdk_ec2_instance_connect.errors.serial_console_session_unsupported_exception

            raise aws_sdk_ec2_instance_connect.errors.serial_console_session_unsupported_exception.SerialConsoleSessionUnsupportedException.from_aws_json_1_1(
                data
            )
        case "ServiceException":
            import aws_sdk_ec2_instance_connect.errors.service_exception

            raise aws_sdk_ec2_instance_connect.errors.service_exception.ServiceException.from_aws_json_1_1(
                data
            )
        case "ThrottlingException":
            import aws_sdk_ec2_instance_connect.errors.throttling_exception

            raise aws_sdk_ec2_instance_connect.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_ec2_instance_connect.types.send_serial_console_ssh_public_key_response.SendSerialConsoleSSHPublicKeyResponse:
    import aws_sdk_ec2_instance_connect.types.send_serial_console_ssh_public_key_response

    out: aws_sdk_ec2_instance_connect.types.send_serial_console_ssh_public_key_response.SendSerialConsoleSSHPublicKeyResponse = aws_sdk_ec2_instance_connect.types.send_serial_console_ssh_public_key_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_ec2_instance_connect._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_ec2_instance_connect._auth._sigv4.build_sigv4_auth_scheme(
                "ec2-instance-connect", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_ec2_instance_connect._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_ec2_instance_connect.types.send_serial_console_ssh_public_key_request.SendSerialConsoleSSHPublicKeyRequest,
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
    headers["X-Amz-Target"] = (
        "AWSEC2InstanceConnectService.SendSerialConsoleSSHPublicKey"
    )
    import aws_sdk_ec2_instance_connect.types.send_serial_console_ssh_public_key_request

    body: bytes | None = json.dumps(
        aws_sdk_ec2_instance_connect.types.send_serial_console_ssh_public_key_request.serialize_aws_json_1_1(
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


def send_serial_console_ssh_public_key(
    options: OperationOptions,
    input_: aws_sdk_ec2_instance_connect.types.send_serial_console_ssh_public_key_request.SendSerialConsoleSSHPublicKeyRequest,
) -> tuple[
    aws_sdk_ec2_instance_connect.types.send_serial_console_ssh_public_key_response.SendSerialConsoleSSHPublicKeyResponse,
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


async def async_send_serial_console_ssh_public_key(
    options: AsyncOperationOptions,
    input_: aws_sdk_ec2_instance_connect.types.send_serial_console_ssh_public_key_request.SendSerialConsoleSSHPublicKeyRequest,
) -> tuple[
    aws_sdk_ec2_instance_connect.types.send_serial_console_ssh_public_key_response.SendSerialConsoleSSHPublicKeyResponse,
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
