"""Generated from Smithy shape ``com.amazonaws.organizations#DescribeResponsibilityTransfer``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_organizations._auth._signers
import aws_sdk_organizations._auth._sigv4
from aws_sdk_organizations._protocol.errors import parse_error_metadata_json
from aws_sdk_organizations._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_organizations._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_organizations.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.describe_responsibility_transfer_request
    import aws_sdk_organizations.types.describe_responsibility_transfer_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_organizations.errors.access_denied_exception

            raise aws_sdk_organizations.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "AWSOrganizationsNotInUseException":
            import aws_sdk_organizations.errors.aws_organizations_not_in_use_exception

            raise aws_sdk_organizations.errors.aws_organizations_not_in_use_exception.AWSOrganizationsNotInUseException.from_aws_json_1_1(
                data
            )
        case "InvalidInputException":
            import aws_sdk_organizations.errors.invalid_input_exception

            raise aws_sdk_organizations.errors.invalid_input_exception.InvalidInputException.from_aws_json_1_1(
                data
            )
        case "ResponsibilityTransferNotFoundException":
            import aws_sdk_organizations.errors.responsibility_transfer_not_found_exception

            raise aws_sdk_organizations.errors.responsibility_transfer_not_found_exception.ResponsibilityTransferNotFoundException.from_aws_json_1_1(
                data
            )
        case "ServiceException":
            import aws_sdk_organizations.errors.service_exception

            raise aws_sdk_organizations.errors.service_exception.ServiceException.from_aws_json_1_1(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_organizations.errors.too_many_requests_exception

            raise aws_sdk_organizations.errors.too_many_requests_exception.TooManyRequestsException.from_aws_json_1_1(
                data
            )
        case "UnsupportedAPIEndpointException":
            import aws_sdk_organizations.errors.unsupported_api_endpoint_exception

            raise aws_sdk_organizations.errors.unsupported_api_endpoint_exception.UnsupportedAPIEndpointException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_organizations.types.describe_responsibility_transfer_response.DescribeResponsibilityTransferResponse:
    import aws_sdk_organizations.types.describe_responsibility_transfer_response

    out: aws_sdk_organizations.types.describe_responsibility_transfer_response.DescribeResponsibilityTransferResponse = aws_sdk_organizations.types.describe_responsibility_transfer_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_organizations._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_organizations._auth._sigv4.build_sigv4_auth_scheme(
                "organizations", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_organizations._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_organizations.types.describe_responsibility_transfer_request.DescribeResponsibilityTransferRequest,
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
    headers["X-Amz-Target"] = "AWSOrganizationsV20161128.DescribeResponsibilityTransfer"
    import aws_sdk_organizations.types.describe_responsibility_transfer_request

    body: bytes | None = json.dumps(
        aws_sdk_organizations.types.describe_responsibility_transfer_request.serialize_aws_json_1_1(
            input
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
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


def describe_responsibility_transfer(
    options: OperationOptions,
    input: aws_sdk_organizations.types.describe_responsibility_transfer_request.DescribeResponsibilityTransferRequest,
) -> tuple[
    aws_sdk_organizations.types.describe_responsibility_transfer_response.DescribeResponsibilityTransferResponse,
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


async def async_describe_responsibility_transfer(
    options: AsyncOperationOptions,
    input: aws_sdk_organizations.types.describe_responsibility_transfer_request.DescribeResponsibilityTransferRequest,
) -> tuple[
    aws_sdk_organizations.types.describe_responsibility_transfer_response.DescribeResponsibilityTransferResponse,
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
