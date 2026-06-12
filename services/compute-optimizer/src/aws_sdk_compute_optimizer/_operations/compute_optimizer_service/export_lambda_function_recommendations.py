"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportLambdaFunctionRecommendations``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_compute_optimizer._auth._signers
import aws_sdk_compute_optimizer._auth._sigv4
from aws_sdk_compute_optimizer._protocol.errors import parse_error_metadata_json
from aws_sdk_compute_optimizer._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_compute_optimizer._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_compute_optimizer.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.export_lambda_function_recommendations_request
    import aws_sdk_compute_optimizer.types.export_lambda_function_recommendations_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_compute_optimizer.errors.access_denied_exception

            raise aws_sdk_compute_optimizer.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_0(
                data
            )
        case "InternalServerException":
            import aws_sdk_compute_optimizer.errors.internal_server_exception

            raise aws_sdk_compute_optimizer.errors.internal_server_exception.InternalServerException.from_aws_json_1_0(
                data
            )
        case "InvalidParameterValueException":
            import aws_sdk_compute_optimizer.errors.invalid_parameter_value_exception

            raise aws_sdk_compute_optimizer.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_aws_json_1_0(
                data
            )
        case "LimitExceededException":
            import aws_sdk_compute_optimizer.errors.limit_exceeded_exception

            raise aws_sdk_compute_optimizer.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_0(
                data
            )
        case "MissingAuthenticationToken":
            import aws_sdk_compute_optimizer.errors.missing_authentication_token

            raise aws_sdk_compute_optimizer.errors.missing_authentication_token.MissingAuthenticationToken.from_aws_json_1_0(
                data
            )
        case "OptInRequiredException":
            import aws_sdk_compute_optimizer.errors.opt_in_required_exception

            raise aws_sdk_compute_optimizer.errors.opt_in_required_exception.OptInRequiredException.from_aws_json_1_0(
                data
            )
        case "ServiceUnavailableException":
            import aws_sdk_compute_optimizer.errors.service_unavailable_exception

            raise aws_sdk_compute_optimizer.errors.service_unavailable_exception.ServiceUnavailableException.from_aws_json_1_0(
                data
            )
        case "ThrottlingException":
            import aws_sdk_compute_optimizer.errors.throttling_exception

            raise aws_sdk_compute_optimizer.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_compute_optimizer.types.export_lambda_function_recommendations_response.ExportLambdaFunctionRecommendationsResponse:
    import aws_sdk_compute_optimizer.types.export_lambda_function_recommendations_response

    out: aws_sdk_compute_optimizer.types.export_lambda_function_recommendations_response.ExportLambdaFunctionRecommendationsResponse = aws_sdk_compute_optimizer.types.export_lambda_function_recommendations_response.deserialize_aws_json_1_0(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_compute_optimizer._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_compute_optimizer._auth._sigv4.build_sigv4_auth_scheme(
                "compute-optimizer", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_compute_optimizer._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_compute_optimizer.types.export_lambda_function_recommendations_request.ExportLambdaFunctionRecommendationsRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = (
        "ComputeOptimizerService.ExportLambdaFunctionRecommendations"
    )
    import aws_sdk_compute_optimizer.types.export_lambda_function_recommendations_request

    body: bytes | None = json.dumps(
        aws_sdk_compute_optimizer.types.export_lambda_function_recommendations_request.serialize_aws_json_1_0(
            input
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def export_lambda_function_recommendations(
    options: OperationOptions,
    input: aws_sdk_compute_optimizer.types.export_lambda_function_recommendations_request.ExportLambdaFunctionRecommendationsRequest,
) -> tuple[
    aws_sdk_compute_optimizer.types.export_lambda_function_recommendations_response.ExportLambdaFunctionRecommendationsResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_export_lambda_function_recommendations(
    options: AsyncOperationOptions,
    input: aws_sdk_compute_optimizer.types.export_lambda_function_recommendations_request.ExportLambdaFunctionRecommendationsRequest,
) -> tuple[
    aws_sdk_compute_optimizer.types.export_lambda_function_recommendations_response.ExportLambdaFunctionRecommendationsResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
