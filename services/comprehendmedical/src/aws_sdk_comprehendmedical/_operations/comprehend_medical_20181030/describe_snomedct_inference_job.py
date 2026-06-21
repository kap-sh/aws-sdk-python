"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#DescribeSNOMEDCTInferenceJob``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_comprehendmedical._auth._signers
import aws_sdk_comprehendmedical._auth._sigv4
import aws_sdk_comprehendmedical.errors.internal_server_exception
import aws_sdk_comprehendmedical.errors.invalid_request_exception
import aws_sdk_comprehendmedical.errors.resource_not_found_exception
import aws_sdk_comprehendmedical.errors.too_many_requests_exception
import aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties
import aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_request
import aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_response
from aws_sdk_comprehendmedical._protocol.errors import parse_error_metadata_json
from aws_sdk_comprehendmedical._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_comprehendmedical._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_comprehendmedical.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            raise aws_sdk_comprehendmedical.errors.internal_server_exception.InternalServerException.from_aws_json_1_1(
                data
            )
        case "InvalidRequestException":
            raise aws_sdk_comprehendmedical.errors.invalid_request_exception.InvalidRequestException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_comprehendmedical.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case "TooManyRequestsException":
            raise aws_sdk_comprehendmedical.errors.too_many_requests_exception.TooManyRequestsException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_response.DescribeSNOMEDCTInferenceJobResponse:
    out: aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_response.DescribeSNOMEDCTInferenceJobResponse = aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_response.DescribeSNOMEDCTInferenceJobResponse:
    out: aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_response.DescribeSNOMEDCTInferenceJobResponse = aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_comprehendmedical._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_comprehendmedical._auth._sigv4.build_sigv4_auth_scheme(
                "comprehendmedical", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_comprehendmedical._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_request.DescribeSNOMEDCTInferenceJobRequest,
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
    headers["X-Amz-Target"] = "ComprehendMedical_20181030.DescribeSNOMEDCTInferenceJob"
    import aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_request

    body: bytes | None = json.dumps(
        aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_request.serialize_aws_json_1_1(
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


def describe_snomedct_inference_job(
    options: OperationOptions,
    input_: aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_request.DescribeSNOMEDCTInferenceJobRequest,
) -> tuple[
    aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_response.DescribeSNOMEDCTInferenceJobResponse,
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


async def async_describe_snomedct_inference_job(
    options: AsyncOperationOptions,
    input_: aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_request.DescribeSNOMEDCTInferenceJobRequest,
) -> tuple[
    aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_response.DescribeSNOMEDCTInferenceJobResponse,
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
