"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateTemplateAlias``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_quicksight._auth._signers
import aws_sdk_quicksight._auth._sigv4
from aws_sdk_quicksight._protocol.errors import parse_error_metadata_json
from aws_sdk_quicksight._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_quicksight._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_quicksight.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.create_template_alias_request
    import aws_sdk_quicksight.types.create_template_alias_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConflictException":
            import aws_sdk_quicksight.errors.conflict_exception

            raise aws_sdk_quicksight.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalFailureException":
            import aws_sdk_quicksight.errors.internal_failure_exception

            raise aws_sdk_quicksight.errors.internal_failure_exception.InternalFailureException.from_json(
                data
            )
        case "LimitExceededException":
            import aws_sdk_quicksight.errors.limit_exceeded_exception

            raise aws_sdk_quicksight.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "ResourceExistsException":
            import aws_sdk_quicksight.errors.resource_exists_exception

            raise aws_sdk_quicksight.errors.resource_exists_exception.ResourceExistsException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_quicksight.errors.resource_not_found_exception

            raise aws_sdk_quicksight.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_quicksight.errors.throttling_exception

            raise aws_sdk_quicksight.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "UnsupportedUserEditionException":
            import aws_sdk_quicksight.errors.unsupported_user_edition_exception

            raise aws_sdk_quicksight.errors.unsupported_user_edition_exception.UnsupportedUserEditionException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> (
    aws_sdk_quicksight.types.create_template_alias_response.CreateTemplateAliasResponse
):
    import aws_sdk_quicksight.types.create_template_alias_response

    out: aws_sdk_quicksight.types.create_template_alias_response.CreateTemplateAliasResponse = aws_sdk_quicksight.types.create_template_alias_response.deserialize_json(
        json.loads(response.read())
    )
    out["status"] = response.status
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_quicksight._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_quicksight._auth._sigv4.build_sigv4_auth_scheme(
                "quicksight", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_quicksight._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_quicksight.types.create_template_alias_request.CreateTemplateAliasRequest,
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
        + "/accounts/{AwsAccountId}/templates/{TemplateId}/aliases/{AliasName}"
    )
    url = url.replace("{AwsAccountId}", quote(str(input["aws_account_id"]), safe=""))
    url = url.replace("{TemplateId}", quote(str(input["template_id"]), safe=""))
    url = url.replace("{AliasName}", quote(str(input["alias_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_quicksight.types.create_template_alias_request

    body: bytes | None = json.dumps(
        aws_sdk_quicksight.types.create_template_alias_request.serialize_json(input)
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


def create_template_alias(
    options: OperationOptions,
    input: aws_sdk_quicksight.types.create_template_alias_request.CreateTemplateAliasRequest,
) -> tuple[
    aws_sdk_quicksight.types.create_template_alias_response.CreateTemplateAliasResponse,
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


async def async_create_template_alias(
    options: AsyncOperationOptions,
    input: aws_sdk_quicksight.types.create_template_alias_request.CreateTemplateAliasRequest,
) -> tuple[
    aws_sdk_quicksight.types.create_template_alias_response.CreateTemplateAliasResponse,
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
