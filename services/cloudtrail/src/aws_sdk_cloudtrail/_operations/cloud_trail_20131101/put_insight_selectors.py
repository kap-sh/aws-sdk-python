"""Generated from Smithy shape ``com.amazonaws.cloudtrail#PutInsightSelectors``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_cloudtrail._auth._signers
import aws_sdk_cloudtrail._auth._sigv4
import aws_sdk_cloudtrail.errors.cloud_trail_arn_invalid_exception
import aws_sdk_cloudtrail.errors.insufficient_encryption_policy_exception
import aws_sdk_cloudtrail.errors.insufficient_s3_bucket_policy_exception
import aws_sdk_cloudtrail.errors.invalid_home_region_exception
import aws_sdk_cloudtrail.errors.invalid_insight_selectors_exception
import aws_sdk_cloudtrail.errors.invalid_parameter_combination_exception
import aws_sdk_cloudtrail.errors.invalid_parameter_exception
import aws_sdk_cloudtrail.errors.invalid_trail_name_exception
import aws_sdk_cloudtrail.errors.kms_exception
import aws_sdk_cloudtrail.errors.no_management_account_slr_exists_exception
import aws_sdk_cloudtrail.errors.not_organization_master_account_exception
import aws_sdk_cloudtrail.errors.operation_not_permitted_exception
import aws_sdk_cloudtrail.errors.s3_bucket_does_not_exist_exception
import aws_sdk_cloudtrail.errors.throttling_exception
import aws_sdk_cloudtrail.errors.trail_not_found_exception
import aws_sdk_cloudtrail.errors.unsupported_operation_exception
import aws_sdk_cloudtrail.types.insight_selectors
import aws_sdk_cloudtrail.types.put_insight_selectors_request
import aws_sdk_cloudtrail.types.put_insight_selectors_response
from aws_sdk_cloudtrail._protocol.errors import parse_error_metadata_json
from aws_sdk_cloudtrail._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloudtrail._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudtrail.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CloudTrailARNInvalidException":
            raise aws_sdk_cloudtrail.errors.cloud_trail_arn_invalid_exception.CloudTrailARNInvalidException.from_aws_json_1_1(
                data
            )
        case "InsufficientEncryptionPolicyException":
            raise aws_sdk_cloudtrail.errors.insufficient_encryption_policy_exception.InsufficientEncryptionPolicyException.from_aws_json_1_1(
                data
            )
        case "InsufficientS3BucketPolicyException":
            raise aws_sdk_cloudtrail.errors.insufficient_s3_bucket_policy_exception.InsufficientS3BucketPolicyException.from_aws_json_1_1(
                data
            )
        case "InvalidHomeRegionException":
            raise aws_sdk_cloudtrail.errors.invalid_home_region_exception.InvalidHomeRegionException.from_aws_json_1_1(
                data
            )
        case "InvalidInsightSelectorsException":
            raise aws_sdk_cloudtrail.errors.invalid_insight_selectors_exception.InvalidInsightSelectorsException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterCombinationException":
            raise aws_sdk_cloudtrail.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            raise aws_sdk_cloudtrail.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "InvalidTrailNameException":
            raise aws_sdk_cloudtrail.errors.invalid_trail_name_exception.InvalidTrailNameException.from_aws_json_1_1(
                data
            )
        case "KmsException":
            raise aws_sdk_cloudtrail.errors.kms_exception.KmsException.from_aws_json_1_1(
                data
            )
        case "NoManagementAccountSLRExistsException":
            raise aws_sdk_cloudtrail.errors.no_management_account_slr_exists_exception.NoManagementAccountSLRExistsException.from_aws_json_1_1(
                data
            )
        case "NotOrganizationMasterAccountException":
            raise aws_sdk_cloudtrail.errors.not_organization_master_account_exception.NotOrganizationMasterAccountException.from_aws_json_1_1(
                data
            )
        case "OperationNotPermittedException":
            raise aws_sdk_cloudtrail.errors.operation_not_permitted_exception.OperationNotPermittedException.from_aws_json_1_1(
                data
            )
        case "S3BucketDoesNotExistException":
            raise aws_sdk_cloudtrail.errors.s3_bucket_does_not_exist_exception.S3BucketDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_cloudtrail.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data
            )
        case "TrailNotFoundException":
            raise aws_sdk_cloudtrail.errors.trail_not_found_exception.TrailNotFoundException.from_aws_json_1_1(
                data
            )
        case "UnsupportedOperationException":
            raise aws_sdk_cloudtrail.errors.unsupported_operation_exception.UnsupportedOperationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_cloudtrail.types.put_insight_selectors_response.PutInsightSelectorsResponse
):
    out: aws_sdk_cloudtrail.types.put_insight_selectors_response.PutInsightSelectorsResponse = aws_sdk_cloudtrail.types.put_insight_selectors_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_cloudtrail.types.put_insight_selectors_response.PutInsightSelectorsResponse
):
    out: aws_sdk_cloudtrail.types.put_insight_selectors_response.PutInsightSelectorsResponse = aws_sdk_cloudtrail.types.put_insight_selectors_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloudtrail._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_cloudtrail.types.put_insight_selectors_request.PutInsightSelectorsRequest,
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
    headers["X-Amz-Target"] = "CloudTrail_20131101.PutInsightSelectors"
    import aws_sdk_cloudtrail.types.put_insight_selectors_request

    body: bytes | None = json.dumps(
        aws_sdk_cloudtrail.types.put_insight_selectors_request.serialize_aws_json_1_1(
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


def put_insight_selectors(
    options: OperationOptions,
    input_: aws_sdk_cloudtrail.types.put_insight_selectors_request.PutInsightSelectorsRequest,
) -> tuple[
    aws_sdk_cloudtrail.types.put_insight_selectors_response.PutInsightSelectorsResponse,
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


async def async_put_insight_selectors(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudtrail.types.put_insight_selectors_request.PutInsightSelectorsRequest,
) -> tuple[
    aws_sdk_cloudtrail.types.put_insight_selectors_response.PutInsightSelectorsResponse,
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
