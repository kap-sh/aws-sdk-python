"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetMatchingWorkflow``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_entityresolution._auth._signers
import aws_sdk_entityresolution._auth._sigv4
from aws_sdk_entityresolution._protocol.errors import parse_error_metadata_json
from aws_sdk_entityresolution._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_entityresolution._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_entityresolution.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.get_matching_workflow_input
    import aws_sdk_entityresolution.types.get_matching_workflow_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_entityresolution.errors.access_denied_exception

            raise aws_sdk_entityresolution.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_entityresolution.errors.internal_server_exception

            raise aws_sdk_entityresolution.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_entityresolution.errors.resource_not_found_exception

            raise aws_sdk_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_entityresolution.errors.throttling_exception

            raise aws_sdk_entityresolution.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_entityresolution.errors.validation_exception

            raise aws_sdk_entityresolution.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_entityresolution.types.get_matching_workflow_output.GetMatchingWorkflowOutput:
    import aws_sdk_entityresolution.types.get_matching_workflow_output

    out: aws_sdk_entityresolution.types.get_matching_workflow_output.GetMatchingWorkflowOutput = aws_sdk_entityresolution.types.get_matching_workflow_output.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_entityresolution._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_entityresolution._auth._sigv4.build_sigv4_auth_scheme(
                "entityresolution", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_entityresolution._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_entityresolution.types.get_matching_workflow_input.GetMatchingWorkflowInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/matchingworkflows/{workflowName}"
    url = url.replace("{workflowName}", quote(str(input_["workflow_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_matching_workflow(
    options: OperationOptions,
    input_: aws_sdk_entityresolution.types.get_matching_workflow_input.GetMatchingWorkflowInput,
) -> tuple[
    aws_sdk_entityresolution.types.get_matching_workflow_output.GetMatchingWorkflowOutput,
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


async def async_get_matching_workflow(
    options: AsyncOperationOptions,
    input_: aws_sdk_entityresolution.types.get_matching_workflow_input.GetMatchingWorkflowInput,
) -> tuple[
    aws_sdk_entityresolution.types.get_matching_workflow_output.GetMatchingWorkflowOutput,
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
