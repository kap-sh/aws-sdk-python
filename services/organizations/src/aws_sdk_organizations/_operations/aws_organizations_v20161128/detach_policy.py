"""Generated from Smithy shape ``com.amazonaws.organizations#DetachPolicy``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_organizations._auth._signers
import aws_sdk_organizations._auth._sigv4
import aws_sdk_organizations.errors.access_denied_exception
import aws_sdk_organizations.errors.aws_organizations_not_in_use_exception
import aws_sdk_organizations.errors.concurrent_modification_exception
import aws_sdk_organizations.errors.constraint_violation_exception
import aws_sdk_organizations.errors.invalid_input_exception
import aws_sdk_organizations.errors.policy_changes_in_progress_exception
import aws_sdk_organizations.errors.policy_not_attached_exception
import aws_sdk_organizations.errors.policy_not_found_exception
import aws_sdk_organizations.errors.service_exception
import aws_sdk_organizations.errors.target_not_found_exception
import aws_sdk_organizations.errors.too_many_requests_exception
import aws_sdk_organizations.errors.unsupported_api_endpoint_exception
import aws_sdk_organizations.types.detach_policy_request
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


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_organizations.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "AWSOrganizationsNotInUseException":
            raise aws_sdk_organizations.errors.aws_organizations_not_in_use_exception.AWSOrganizationsNotInUseException.from_aws_json_1_1(
                data
            )
        case "ConcurrentModificationException":
            raise aws_sdk_organizations.errors.concurrent_modification_exception.ConcurrentModificationException.from_aws_json_1_1(
                data
            )
        case "ConstraintViolationException":
            raise aws_sdk_organizations.errors.constraint_violation_exception.ConstraintViolationException.from_aws_json_1_1(
                data
            )
        case "InvalidInputException":
            raise aws_sdk_organizations.errors.invalid_input_exception.InvalidInputException.from_aws_json_1_1(
                data
            )
        case "PolicyChangesInProgressException":
            raise aws_sdk_organizations.errors.policy_changes_in_progress_exception.PolicyChangesInProgressException.from_aws_json_1_1(
                data
            )
        case "PolicyNotAttachedException":
            raise aws_sdk_organizations.errors.policy_not_attached_exception.PolicyNotAttachedException.from_aws_json_1_1(
                data
            )
        case "PolicyNotFoundException":
            raise aws_sdk_organizations.errors.policy_not_found_exception.PolicyNotFoundException.from_aws_json_1_1(
                data
            )
        case "ServiceException":
            raise aws_sdk_organizations.errors.service_exception.ServiceException.from_aws_json_1_1(
                data
            )
        case "TargetNotFoundException":
            raise aws_sdk_organizations.errors.target_not_found_exception.TargetNotFoundException.from_aws_json_1_1(
                data
            )
        case "TooManyRequestsException":
            raise aws_sdk_organizations.errors.too_many_requests_exception.TooManyRequestsException.from_aws_json_1_1(
                data
            )
        case "UnsupportedAPIEndpointException":
            raise aws_sdk_organizations.errors.unsupported_api_endpoint_exception.UnsupportedAPIEndpointException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_organizations._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_organizations.types.detach_policy_request.DetachPolicyRequest,
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
    headers["X-Amz-Target"] = "AWSOrganizationsV20161128.DetachPolicy"
    import aws_sdk_organizations.types.detach_policy_request

    body: bytes | None = json.dumps(
        aws_sdk_organizations.types.detach_policy_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def detach_policy(
    options: OperationOptions,
    input_: aws_sdk_organizations.types.detach_policy_request.DetachPolicyRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_detach_policy(
    options: AsyncOperationOptions,
    input_: aws_sdk_organizations.types.detach_policy_request.DetachPolicyRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
