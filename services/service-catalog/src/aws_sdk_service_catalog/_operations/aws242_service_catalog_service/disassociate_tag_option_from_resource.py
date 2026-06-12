"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DisassociateTagOptionFromResource``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_service_catalog._auth._signers
import aws_sdk_service_catalog._auth._sigv4
from aws_sdk_service_catalog._protocol.errors import parse_error_metadata_json
from aws_sdk_service_catalog._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_service_catalog._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_service_catalog.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.disassociate_tag_option_from_resource_input
    import aws_sdk_service_catalog.types.disassociate_tag_option_from_resource_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ResourceNotFoundException":
            import aws_sdk_service_catalog.errors.resource_not_found_exception

            raise aws_sdk_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case "TagOptionNotMigratedException":
            import aws_sdk_service_catalog.errors.tag_option_not_migrated_exception

            raise aws_sdk_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_service_catalog.types.disassociate_tag_option_from_resource_output.DisassociateTagOptionFromResourceOutput:
    out: aws_sdk_service_catalog.types.disassociate_tag_option_from_resource_output.DisassociateTagOptionFromResourceOutput = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_service_catalog._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_service_catalog._auth._sigv4.build_sigv4_auth_scheme(
                "servicecatalog", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_service_catalog._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_service_catalog.types.disassociate_tag_option_from_resource_input.DisassociateTagOptionFromResourceInput,
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
    if "resource_id" in input:
        params["resourceId"] = str(input["resource_id"])
    if "tag_option_id" in input:
        params["tagOptionId"] = str(input["tag_option_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = (
        "AWS242ServiceCatalogService.DisassociateTagOptionFromResource"
    )
    body: bytes | None = b""
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


def disassociate_tag_option_from_resource(
    options: OperationOptions,
    input: aws_sdk_service_catalog.types.disassociate_tag_option_from_resource_input.DisassociateTagOptionFromResourceInput,
) -> tuple[
    aws_sdk_service_catalog.types.disassociate_tag_option_from_resource_output.DisassociateTagOptionFromResourceOutput,
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


async def async_disassociate_tag_option_from_resource(
    options: AsyncOperationOptions,
    input: aws_sdk_service_catalog.types.disassociate_tag_option_from_resource_input.DisassociateTagOptionFromResourceInput,
) -> tuple[
    aws_sdk_service_catalog.types.disassociate_tag_option_from_resource_output.DisassociateTagOptionFromResourceOutput,
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
