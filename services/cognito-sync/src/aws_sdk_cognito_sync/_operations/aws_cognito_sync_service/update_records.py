"""Generated from Smithy shape ``com.amazonaws.cognitosync#UpdateRecords``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_cognito_sync._auth._signers
import aws_sdk_cognito_sync._auth._sigv4
from aws_sdk_cognito_sync._protocol.errors import parse_error_metadata_json
from aws_sdk_cognito_sync._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cognito_sync._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cognito_sync.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.update_records_request
    import aws_sdk_cognito_sync.types.update_records_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalErrorException":
            import aws_sdk_cognito_sync.errors.internal_error_exception

            raise aws_sdk_cognito_sync.errors.internal_error_exception.InternalErrorException.from_json(
                data
            )
        case "InvalidLambdaFunctionOutputException":
            import aws_sdk_cognito_sync.errors.invalid_lambda_function_output_exception

            raise aws_sdk_cognito_sync.errors.invalid_lambda_function_output_exception.InvalidLambdaFunctionOutputException.from_json(
                data
            )
        case "InvalidParameterException":
            import aws_sdk_cognito_sync.errors.invalid_parameter_exception

            raise aws_sdk_cognito_sync.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case "LambdaThrottledException":
            import aws_sdk_cognito_sync.errors.lambda_throttled_exception

            raise aws_sdk_cognito_sync.errors.lambda_throttled_exception.LambdaThrottledException.from_json(
                data
            )
        case "LimitExceededException":
            import aws_sdk_cognito_sync.errors.limit_exceeded_exception

            raise aws_sdk_cognito_sync.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "NotAuthorizedException":
            import aws_sdk_cognito_sync.errors.not_authorized_exception

            raise aws_sdk_cognito_sync.errors.not_authorized_exception.NotAuthorizedException.from_json(
                data
            )
        case "ResourceConflictException":
            import aws_sdk_cognito_sync.errors.resource_conflict_exception

            raise aws_sdk_cognito_sync.errors.resource_conflict_exception.ResourceConflictException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_cognito_sync.errors.resource_not_found_exception

            raise aws_sdk_cognito_sync.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_cognito_sync.errors.too_many_requests_exception

            raise aws_sdk_cognito_sync.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cognito_sync.types.update_records_response.UpdateRecordsResponse:
    import aws_sdk_cognito_sync.types.update_records_response

    out: aws_sdk_cognito_sync.types.update_records_response.UpdateRecordsResponse = (
        aws_sdk_cognito_sync.types.update_records_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cognito_sync._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cognito_sync._auth._sigv4.build_sigv4_auth_scheme(
                "cognito-sync", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cognito_sync._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_cognito_sync.types.update_records_request.UpdateRecordsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/identitypools/{IdentityPoolId}/identities/{IdentityId}/datasets/{DatasetName}"
    )
    url = url.replace(
        "{IdentityPoolId}", quote(str(input_["identity_pool_id"]), safe="")
    )
    url = url.replace("{IdentityId}", quote(str(input_["identity_id"]), safe=""))
    url = url.replace("{DatasetName}", quote(str(input_["dataset_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "client_context" in input_:
        headers["x-amz-Client-Context"] = str(input_["client_context"])
    import aws_sdk_cognito_sync.types.update_records_request

    body: bytes | None = json.dumps(
        aws_sdk_cognito_sync.types.update_records_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def update_records(
    options: OperationOptions,
    input_: aws_sdk_cognito_sync.types.update_records_request.UpdateRecordsRequest,
) -> tuple[
    aws_sdk_cognito_sync.types.update_records_response.UpdateRecordsResponse,
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


async def async_update_records(
    options: AsyncOperationOptions,
    input_: aws_sdk_cognito_sync.types.update_records_request.UpdateRecordsRequest,
) -> tuple[
    aws_sdk_cognito_sync.types.update_records_response.UpdateRecordsResponse,
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
