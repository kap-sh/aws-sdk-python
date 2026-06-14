"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListResourcesForTagOption``."""

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
    import aws_sdk_service_catalog.types.list_resources_for_tag_option_input
    import aws_sdk_service_catalog.types.list_resources_for_tag_option_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParametersException":
            import aws_sdk_service_catalog.errors.invalid_parameters_exception

            raise aws_sdk_service_catalog.errors.invalid_parameters_exception.InvalidParametersException.from_aws_json_1_1(
                data
            )
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
) -> aws_sdk_service_catalog.types.list_resources_for_tag_option_output.ListResourcesForTagOptionOutput:
    import aws_sdk_service_catalog.types.list_resources_for_tag_option_output

    out: aws_sdk_service_catalog.types.list_resources_for_tag_option_output.ListResourcesForTagOptionOutput = aws_sdk_service_catalog.types.list_resources_for_tag_option_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_service_catalog._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_service_catalog.types.list_resources_for_tag_option_input.ListResourcesForTagOptionInput,
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
    if "tag_option_id" in input_:
        params["tagOptionId"] = str(input_["tag_option_id"])
    if "resource_type" in input_:
        params["resourceType"] = str(input_["resource_type"])
    params["pageSize"] = str(input_.get("page_size", 0))
    if "page_token" in input_:
        params["pageToken"] = str(input_["page_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWS242ServiceCatalogService.ListResourcesForTagOption"
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def list_resources_for_tag_option(
    options: OperationOptions,
    input_: aws_sdk_service_catalog.types.list_resources_for_tag_option_input.ListResourcesForTagOptionInput,
) -> tuple[
    aws_sdk_service_catalog.types.list_resources_for_tag_option_output.ListResourcesForTagOptionOutput,
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


async def async_list_resources_for_tag_option(
    options: AsyncOperationOptions,
    input_: aws_sdk_service_catalog.types.list_resources_for_tag_option_input.ListResourcesForTagOptionInput,
) -> tuple[
    aws_sdk_service_catalog.types.list_resources_for_tag_option_output.ListResourcesForTagOptionOutput,
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
