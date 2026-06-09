"""Generated from Smithy shape ``com.amazonaws.lambda#AddLayerVersionPermission``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_lambda._auth._signers
from aws_sdk_lambda._protocol.errors import parse_error_metadata_json
from aws_sdk_lambda._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_lambda._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_lambda.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.add_layer_version_permission_request
    import aws_sdk_lambda.types.add_layer_version_permission_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            import aws_sdk_lambda.errors.invalid_parameter_value_exception

            raise aws_sdk_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "PolicyLengthExceededException":
            import aws_sdk_lambda.errors.policy_length_exceeded_exception

            raise aws_sdk_lambda.errors.policy_length_exceeded_exception.PolicyLengthExceededException.from_json(
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
) -> aws_sdk_lambda.types.add_layer_version_permission_response.AddLayerVersionPermissionResponse:
    import aws_sdk_lambda.types.add_layer_version_permission_response

    out: aws_sdk_lambda.types.add_layer_version_permission_response.AddLayerVersionPermissionResponse = aws_sdk_lambda.types.add_layer_version_permission_response.deserialize_json(
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
    input: aws_sdk_lambda.types.add_layer_version_permission_request.AddLayerVersionPermissionRequest,
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
        + "/2018-10-31/layers/{LayerName}/versions/{VersionNumber}/policy"
    )
    url = url.replace("{LayerName}", quote(str(input["layer_name"]), safe=""))
    url = url.replace("{VersionNumber}", quote(str(input["version_number"]), safe=""))
    params: dict[str, str] = {}
    if "revision_id" in input:
        params["RevisionId"] = str(input["revision_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_lambda.types.add_layer_version_permission_request

    body: bytes | None = json.dumps(
        aws_sdk_lambda.types.add_layer_version_permission_request.serialize_json(input)
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


def add_layer_version_permission(
    options: OperationOptions,
    input: aws_sdk_lambda.types.add_layer_version_permission_request.AddLayerVersionPermissionRequest,
) -> tuple[
    aws_sdk_lambda.types.add_layer_version_permission_response.AddLayerVersionPermissionResponse,
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


async def async_add_layer_version_permission(
    options: AsyncOperationOptions,
    input: aws_sdk_lambda.types.add_layer_version_permission_request.AddLayerVersionPermissionRequest,
) -> tuple[
    aws_sdk_lambda.types.add_layer_version_permission_response.AddLayerVersionPermissionResponse,
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
