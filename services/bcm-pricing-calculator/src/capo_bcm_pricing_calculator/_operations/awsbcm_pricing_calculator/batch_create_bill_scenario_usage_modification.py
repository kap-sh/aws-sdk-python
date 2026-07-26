"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioUsageModification``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_bcm_pricing_calculator._auth._signers
import capo_bcm_pricing_calculator._auth._sigv4
import capo_bcm_pricing_calculator.errors.access_denied_exception
import capo_bcm_pricing_calculator.errors.conflict_exception
import capo_bcm_pricing_calculator.errors.data_unavailable_exception
import capo_bcm_pricing_calculator.errors.internal_server_exception
import capo_bcm_pricing_calculator.errors.resource_not_found_exception
import capo_bcm_pricing_calculator.errors.service_quota_exceeded_exception
import capo_bcm_pricing_calculator.errors.throttling_exception
import capo_bcm_pricing_calculator.errors.validation_exception
import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entries
import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_errors
import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_items
import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_request
import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_response
from capo_bcm_pricing_calculator._protocol.errors import parse_error_metadata_json
from capo_bcm_pricing_calculator._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_bcm_pricing_calculator._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_bcm_pricing_calculator.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_0(
                data
            )
        case "InternalServerException":
            raise capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException.from_aws_json_1_0(
                data
            )
        case "ThrottlingException":
            raise capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data
            )
        case "ValidationException":
            raise capo_bcm_pricing_calculator.errors.validation_exception.ValidationException.from_aws_json_1_0(
                data
            )
        case "ConflictException":
            raise capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException.from_aws_json_1_0(
                data
            )
        case "DataUnavailableException":
            raise capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException.from_aws_json_1_0(
                data
            )
        case "ResourceNotFoundException":
            raise capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data
            )
        case "ServiceQuotaExceededException":
            raise capo_bcm_pricing_calculator.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_response.BatchCreateBillScenarioUsageModificationResponse:
    out: capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_response.BatchCreateBillScenarioUsageModificationResponse = capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_response.deserialize_aws_json_1_0(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_response.BatchCreateBillScenarioUsageModificationResponse:
    out: capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_response.BatchCreateBillScenarioUsageModificationResponse = capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_response.deserialize_aws_json_1_0(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_bcm_pricing_calculator._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_bcm_pricing_calculator._auth._sigv4.build_sigv4_auth_scheme(
                "bcm-pricing-calculator", options.region
            )
        )
        if sigv4_config is not None:
            return capo_bcm_pricing_calculator._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_request.BatchCreateBillScenarioUsageModificationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = (
        "AWSBCMPricingCalculator.BatchCreateBillScenarioUsageModification"
    )
    if "client_token" in input_:
        headers["X-Amzn-Client-Token"] = str(input_["client_token"])
    body: bytes | None = json.dumps(
        capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_request.serialize_aws_json_1_0(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def batch_create_bill_scenario_usage_modification(
    options: OperationOptions,
    input_: capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_request.BatchCreateBillScenarioUsageModificationRequest,
) -> tuple[
    capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_response.BatchCreateBillScenarioUsageModificationResponse,
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


async def async_batch_create_bill_scenario_usage_modification(
    options: AsyncOperationOptions,
    input_: capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_request.BatchCreateBillScenarioUsageModificationRequest,
) -> tuple[
    capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_response.BatchCreateBillScenarioUsageModificationResponse,
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
