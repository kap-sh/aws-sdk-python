"""Generated from Smithy shape ``com.amazonaws.lambda#PublishVersion``."""

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
    import aws_sdk_lambda.types.publish_version_request
    import aws_sdk_lambda.types.function_configuration


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CodeStorageExceededException":
            import aws_sdk_lambda.errors.code_storage_exceeded_exception

            raise aws_sdk_lambda.errors.code_storage_exceeded_exception.CodeStorageExceededException.from_json(
                data
            )
        case "FunctionVersionsPerCapacityProviderLimitExceededException":
            import aws_sdk_lambda.errors.function_versions_per_capacity_provider_limit_exceeded_exception

            raise aws_sdk_lambda.errors.function_versions_per_capacity_provider_limit_exceeded_exception.FunctionVersionsPerCapacityProviderLimitExceededException.from_json(
                data
            )
        case "InvalidParameterValueException":
            import aws_sdk_lambda.errors.invalid_parameter_value_exception

            raise aws_sdk_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "PreconditionFailedException":
            import aws_sdk_lambda.errors.precondition_failed_exception

            raise aws_sdk_lambda.errors.precondition_failed_exception.PreconditionFailedException.from_json(
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
) -> aws_sdk_lambda.types.function_configuration.FunctionConfiguration:
    import aws_sdk_lambda.types.function_configuration

    out: aws_sdk_lambda.types.function_configuration.FunctionConfiguration = (
        aws_sdk_lambda.types.function_configuration.deserialize_json(
            json.loads(response.read())
        )
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
    input: aws_sdk_lambda.types.publish_version_request.PublishVersionRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/2015-03-31/functions/{FunctionName}/versions"
    url = url.replace("{FunctionName}", quote(str(input["function_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_lambda.types.publish_version_request

    body: bytes | None = json.dumps(
        aws_sdk_lambda.types.publish_version_request.serialize_json(input)
    ).encode()
    headers["content-type"] = "application/json"
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


def publish_version(
    options: OperationOptions,
    input: aws_sdk_lambda.types.publish_version_request.PublishVersionRequest,
) -> tuple[
    aws_sdk_lambda.types.function_configuration.FunctionConfiguration, zapros.Response
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


async def async_publish_version(
    options: AsyncOperationOptions,
    input: aws_sdk_lambda.types.publish_version_request.PublishVersionRequest,
) -> tuple[
    aws_sdk_lambda.types.function_configuration.FunctionConfiguration, zapros.Response
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
