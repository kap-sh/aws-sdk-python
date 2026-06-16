"""Generated from Smithy shape ``com.amazonaws.configservice#PutDeliveryChannel``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_config_service._auth._signers
import aws_sdk_config_service._auth._sigv4
from aws_sdk_config_service._protocol.errors import parse_error_metadata_json
from aws_sdk_config_service._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_config_service._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_config_service.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.put_delivery_channel_request


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InsufficientDeliveryPolicyException":
            import aws_sdk_config_service.errors.insufficient_delivery_policy_exception

            raise aws_sdk_config_service.errors.insufficient_delivery_policy_exception.InsufficientDeliveryPolicyException.from_aws_json_1_1(
                data
            )
        case "InvalidDeliveryChannelNameException":
            import aws_sdk_config_service.errors.invalid_delivery_channel_name_exception

            raise aws_sdk_config_service.errors.invalid_delivery_channel_name_exception.InvalidDeliveryChannelNameException.from_aws_json_1_1(
                data
            )
        case "InvalidS3KeyPrefixException":
            import aws_sdk_config_service.errors.invalid_s3_key_prefix_exception

            raise aws_sdk_config_service.errors.invalid_s3_key_prefix_exception.InvalidS3KeyPrefixException.from_aws_json_1_1(
                data
            )
        case "InvalidS3KmsKeyArnException":
            import aws_sdk_config_service.errors.invalid_s3_kms_key_arn_exception

            raise aws_sdk_config_service.errors.invalid_s3_kms_key_arn_exception.InvalidS3KmsKeyArnException.from_aws_json_1_1(
                data
            )
        case "InvalidSNSTopicARNException":
            import aws_sdk_config_service.errors.invalid_sns_topic_arn_exception

            raise aws_sdk_config_service.errors.invalid_sns_topic_arn_exception.InvalidSNSTopicARNException.from_aws_json_1_1(
                data
            )
        case "MaxNumberOfDeliveryChannelsExceededException":
            import aws_sdk_config_service.errors.max_number_of_delivery_channels_exceeded_exception

            raise aws_sdk_config_service.errors.max_number_of_delivery_channels_exceeded_exception.MaxNumberOfDeliveryChannelsExceededException.from_aws_json_1_1(
                data
            )
        case "NoAvailableConfigurationRecorderException":
            import aws_sdk_config_service.errors.no_available_configuration_recorder_exception

            raise aws_sdk_config_service.errors.no_available_configuration_recorder_exception.NoAvailableConfigurationRecorderException.from_aws_json_1_1(
                data
            )
        case "NoSuchBucketException":
            import aws_sdk_config_service.errors.no_such_bucket_exception

            raise aws_sdk_config_service.errors.no_such_bucket_exception.NoSuchBucketException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_config_service._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_config_service._auth._sigv4.build_sigv4_auth_scheme(
                "config", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_config_service._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_config_service.types.put_delivery_channel_request.PutDeliveryChannelRequest,
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
    headers["X-Amz-Target"] = "StarlingDoveService.PutDeliveryChannel"
    import aws_sdk_config_service.types.put_delivery_channel_request

    body: bytes | None = json.dumps(
        aws_sdk_config_service.types.put_delivery_channel_request.serialize_aws_json_1_1(
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


def put_delivery_channel(
    options: OperationOptions,
    input_: aws_sdk_config_service.types.put_delivery_channel_request.PutDeliveryChannelRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return None, response
    except BaseException:
        response.close()
        raise


async def async_put_delivery_channel(
    options: AsyncOperationOptions,
    input_: aws_sdk_config_service.types.put_delivery_channel_request.PutDeliveryChannelRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return None, response
    except BaseException:
        await response.aclose()
        raise
