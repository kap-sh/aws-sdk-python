"""Generated from Smithy shape ``com.amazonaws.configservice#PutConfigurationAggregator``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_config_service._auth._signers
import aws_sdk_config_service._auth._sigv4
import aws_sdk_config_service.errors.invalid_parameter_value_exception
import aws_sdk_config_service.errors.invalid_role_exception
import aws_sdk_config_service.errors.limit_exceeded_exception
import aws_sdk_config_service.errors.no_available_organization_exception
import aws_sdk_config_service.errors.organization_access_denied_exception
import aws_sdk_config_service.errors.organization_all_features_not_enabled_exception
import aws_sdk_config_service.types.account_aggregation_source_list
import aws_sdk_config_service.types.aggregator_filters
import aws_sdk_config_service.types.configuration_aggregator
import aws_sdk_config_service.types.organization_aggregation_source
import aws_sdk_config_service.types.put_configuration_aggregator_request
import aws_sdk_config_service.types.put_configuration_aggregator_response
import aws_sdk_config_service.types.tags_list
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


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            raise aws_sdk_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_aws_json_1_1(
                data
            )
        case "InvalidRoleException":
            raise aws_sdk_config_service.errors.invalid_role_exception.InvalidRoleException.from_aws_json_1_1(
                data
            )
        case "LimitExceededException":
            raise aws_sdk_config_service.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case "NoAvailableOrganizationException":
            raise aws_sdk_config_service.errors.no_available_organization_exception.NoAvailableOrganizationException.from_aws_json_1_1(
                data
            )
        case "OrganizationAccessDeniedException":
            raise aws_sdk_config_service.errors.organization_access_denied_exception.OrganizationAccessDeniedException.from_aws_json_1_1(
                data
            )
        case "OrganizationAllFeaturesNotEnabledException":
            raise aws_sdk_config_service.errors.organization_all_features_not_enabled_exception.OrganizationAllFeaturesNotEnabledException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_config_service.types.put_configuration_aggregator_response.PutConfigurationAggregatorResponse:
    out: aws_sdk_config_service.types.put_configuration_aggregator_response.PutConfigurationAggregatorResponse = aws_sdk_config_service.types.put_configuration_aggregator_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_config_service.types.put_configuration_aggregator_response.PutConfigurationAggregatorResponse:
    out: aws_sdk_config_service.types.put_configuration_aggregator_response.PutConfigurationAggregatorResponse = aws_sdk_config_service.types.put_configuration_aggregator_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


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
    input_: aws_sdk_config_service.types.put_configuration_aggregator_request.PutConfigurationAggregatorRequest,
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
    headers["X-Amz-Target"] = "StarlingDoveService.PutConfigurationAggregator"
    body: bytes | None = json.dumps(
        aws_sdk_config_service.types.put_configuration_aggregator_request.serialize_aws_json_1_1(
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


def put_configuration_aggregator(
    options: OperationOptions,
    input_: aws_sdk_config_service.types.put_configuration_aggregator_request.PutConfigurationAggregatorRequest,
) -> tuple[
    aws_sdk_config_service.types.put_configuration_aggregator_response.PutConfigurationAggregatorResponse,
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


async def async_put_configuration_aggregator(
    options: AsyncOperationOptions,
    input_: aws_sdk_config_service.types.put_configuration_aggregator_request.PutConfigurationAggregatorRequest,
) -> tuple[
    aws_sdk_config_service.types.put_configuration_aggregator_response.PutConfigurationAggregatorResponse,
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
