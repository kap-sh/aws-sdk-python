"""Generated from Smithy shape ``com.amazonaws.lambda#PutFunctionScalingConfig``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any
from aws_sdk_lambda._rule_engine._endpoint_rule_set import EndpointParams, resolve
import zapros
from urllib.parse import quote
from aws_sdk_lambda.errors import UnknownServiceError
from aws_sdk_lambda._protocol.errors import parse_error_metadata_json
import json
import aws_sdk_lambda._auth._signers
from aws_sdk_lambda._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_lambda.types.put_function_scaling_config_request
    import aws_sdk_lambda.types.put_function_scaling_config_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            import aws_sdk_lambda.errors.invalid_parameter_value_exception

            raise aws_sdk_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "ResourceConflictException":
            import aws_sdk_lambda.errors.resource_conflict_exception

            raise aws_sdk_lambda.errors.resource_conflict_exception.ResourceConflictException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_lambda.errors.resource_not_found_exception

            raise aws_sdk_lambda.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceException":
            import aws_sdk_lambda.errors.service_exception

            raise aws_sdk_lambda.errors.service_exception.ServiceException.from_json(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_lambda.errors.too_many_requests_exception

            raise aws_sdk_lambda.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_lambda.types.put_function_scaling_config_response.PutFunctionScalingConfigResponse:
    import aws_sdk_lambda.types.put_function_scaling_config_response

    out: aws_sdk_lambda.types.put_function_scaling_config_response.PutFunctionScalingConfigResponse = aws_sdk_lambda.types.put_function_scaling_config_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_lambda._auth._signers.Signer | None:
    if auth_schemes:
        for scheme in auth_schemes:
            match scheme["name"]:
                case "sigv4" | "sigv4a" | "sigv4-s3express" if (
                    options.credentials_provider is not None
                ):
                    return aws_sdk_lambda._auth._signers.SigV4Signer(
                        options.credentials_provider, auth_scheme=scheme
                    )
                case "none":
                    return None
                case _:
                    raise RuntimeError(
                        f"Could not find provider for auth scheme {scheme['name']!r}"
                    )
    if options.credentials_provider is not None:
        if options.region is None:
            raise RuntimeError("options.region is required for SigV4 signing")
        return aws_sdk_lambda._auth._signers.SigV4Signer(
            options.credentials_provider,
            auth_scheme={
                "name": "sigv4",
                "signingName": "lambda",
                "signingRegion": options.region,
                "disableDoubleEncoding": False,
                "disableNormalizePath": False,
            },
        )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_lambda.types.put_function_scaling_config_request.PutFunctionScalingConfigRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = (
        endpoint.url.rstrip("/")
        + "/2025-11-30/functions/{FunctionName}/function-scaling-config"
    )
    url = url.replace("{FunctionName}", quote(str(input["function_name"]), safe=""))
    params: dict[str, str] = {}
    if "qualifier" in input:
        params["Qualifier"] = str(input["qualifier"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_lambda.types.put_function_scaling_config_request

    body: bytes | None = json.dumps(
        aws_sdk_lambda.types.put_function_scaling_config_request.serialize_json(input)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "PUT",
        headers=headers,
        body=body,  # type: ignore
        context={"signer": signer},  # type: ignore
    )


def put_function_scaling_config(
    options: OperationOptions,
    input: aws_sdk_lambda.types.put_function_scaling_config_request.PutFunctionScalingConfigRequest,
) -> tuple[
    aws_sdk_lambda.types.put_function_scaling_config_response.PutFunctionScalingConfigResponse,
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


async def async_put_function_scaling_config(
    options: AsyncOperationOptions,
    input: aws_sdk_lambda.types.put_function_scaling_config_request.PutFunctionScalingConfigRequest,
) -> tuple[
    aws_sdk_lambda.types.put_function_scaling_config_response.PutFunctionScalingConfigResponse,
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
