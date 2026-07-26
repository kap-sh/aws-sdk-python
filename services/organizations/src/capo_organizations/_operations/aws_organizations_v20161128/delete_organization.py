"""Generated from Smithy shape ``com.amazonaws.organizations#DeleteOrganization``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_organizations._auth._signers
import capo_organizations._auth._sigv4
import capo_organizations.errors.access_denied_exception
import capo_organizations.errors.aws_organizations_not_in_use_exception
import capo_organizations.errors.concurrent_modification_exception
import capo_organizations.errors.constraint_violation_exception
import capo_organizations.errors.invalid_input_exception
import capo_organizations.errors.organization_not_empty_exception
import capo_organizations.errors.service_exception
import capo_organizations.errors.too_many_requests_exception
from capo_organizations._protocol.errors import parse_error_metadata_json
from capo_organizations._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_organizations._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_organizations.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_organizations.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "AWSOrganizationsNotInUseException":
            raise capo_organizations.errors.aws_organizations_not_in_use_exception.AWSOrganizationsNotInUseException.from_aws_json_1_1(
                data
            )
        case "ConcurrentModificationException":
            raise capo_organizations.errors.concurrent_modification_exception.ConcurrentModificationException.from_aws_json_1_1(
                data
            )
        case "ConstraintViolationException":
            raise capo_organizations.errors.constraint_violation_exception.ConstraintViolationException.from_aws_json_1_1(
                data
            )
        case "InvalidInputException":
            raise capo_organizations.errors.invalid_input_exception.InvalidInputException.from_aws_json_1_1(
                data
            )
        case "OrganizationNotEmptyException":
            raise capo_organizations.errors.organization_not_empty_exception.OrganizationNotEmptyException.from_aws_json_1_1(
                data
            )
        case "ServiceException":
            raise capo_organizations.errors.service_exception.ServiceException.from_aws_json_1_1(
                data
            )
        case "TooManyRequestsException":
            raise capo_organizations.errors.too_many_requests_exception.TooManyRequestsException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_organizations._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_organizations._auth._sigv4.build_sigv4_auth_scheme(
                "organizations", options.region
            )
        )
        if sigv4_config is not None:
            return capo_organizations._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(options: OperationOptions | AsyncOperationOptions) -> zapros.Request:
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
    headers["X-Amz-Target"] = "AWSOrganizationsV20161128.DeleteOrganization"
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def delete_organization(options: OperationOptions) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_delete_organization(
    options: AsyncOperationOptions,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
