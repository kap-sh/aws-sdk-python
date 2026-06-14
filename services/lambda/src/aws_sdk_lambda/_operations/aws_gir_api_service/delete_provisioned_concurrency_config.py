"""Generated from Smithy shape ``com.amazonaws.lambda#DeleteProvisionedConcurrencyConfig``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_lambda._auth._signers
import aws_sdk_lambda._auth._sigv4
from aws_sdk_lambda._protocol.errors import parse_error_metadata_json
from aws_sdk_lambda._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_lambda._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_lambda.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.delete_provisioned_concurrency_config_request


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


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_lambda._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_lambda._auth._sigv4.build_sigv4_auth_scheme(
                "lambda", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_lambda._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_lambda.types.delete_provisioned_concurrency_config_request.DeleteProvisionedConcurrencyConfigRequest,
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
        + "/2019-09-30/functions/{FunctionName}/provisioned-concurrency"
    )
    url = url.replace("{FunctionName}", quote(str(input_["function_name"]), safe=""))
    params: dict[str, str] = {}
    if "qualifier" in input_:
        params["Qualifier"] = str(input_["qualifier"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_provisioned_concurrency_config(
    options: OperationOptions,
    input_: aws_sdk_lambda.types.delete_provisioned_concurrency_config_request.DeleteProvisionedConcurrencyConfigRequest,
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


async def async_delete_provisioned_concurrency_config(
    options: AsyncOperationOptions,
    input_: aws_sdk_lambda.types.delete_provisioned_concurrency_config_request.DeleteProvisionedConcurrencyConfigRequest,
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
