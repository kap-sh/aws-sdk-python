"""Generated from Smithy shape ``com.amazonaws.bedrock#ListProvisionedModelThroughputs``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any
from typing import cast
from aws_sdk_bedrock._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_bedrock._rule_engine._endpoint_runtime import apply_label
import zapros
from urllib.parse import quote
from aws_sdk_bedrock.errors import ServiceError, UnknownServiceError
from aws_sdk_bedrock._protocol.errors import parse_error_metadata_json
import json
import aws_sdk_bedrock._auth._signers
import aws_sdk_bedrock._auth._sigv4
from aws_sdk_bedrock._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.list_provisioned_model_throughputs_request
    import aws_sdk_bedrock.types.list_provisioned_model_throughputs_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_bedrock.errors.access_denied_exception

            raise aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_bedrock.errors.internal_server_exception

            raise aws_sdk_bedrock.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_bedrock.errors.throttling_exception

            raise aws_sdk_bedrock.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_bedrock.errors.validation_exception

            raise aws_sdk_bedrock.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_bedrock.types.list_provisioned_model_throughputs_response.ListProvisionedModelThroughputsResponse:
    import aws_sdk_bedrock.types.list_provisioned_model_throughputs_response

    out: aws_sdk_bedrock.types.list_provisioned_model_throughputs_response.ListProvisionedModelThroughputsResponse = aws_sdk_bedrock.types.list_provisioned_model_throughputs_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_bedrock._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_bedrock._auth._sigv4.build_sigv4_auth_scheme(
                "bedrock", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_bedrock._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    if options.bearer_provider is not None:
        return aws_sdk_bedrock._auth._signers.HttpBearerSigner(options.bearer_provider)
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_bedrock.types.list_provisioned_model_throughputs_request.ListProvisionedModelThroughputsRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/provisioned-model-throughputs"
    params: dict[str, str] = {}
    if "creation_time_after" in input:
        params["creationTimeAfter"] = str(input["creation_time_after"])
    if "creation_time_before" in input:
        params["creationTimeBefore"] = str(input["creation_time_before"])
    if "status_equals" in input:
        params["statusEquals"] = str(input["status_equals"])
    if "model_arn_equals" in input:
        params["modelArnEquals"] = str(input["model_arn_equals"])
    if "name_contains" in input:
        params["nameContains"] = str(input["name_contains"])
    if "max_results" in input:
        params["maxResults"] = str(input["max_results"])
    if "next_token" in input:
        params["nextToken"] = str(input["next_token"])
    if "sort_by" in input:
        params["sortBy"] = str(input["sort_by"])
    if "sort_order" in input:
        params["sortOrder"] = str(input["sort_order"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "GET",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def list_provisioned_model_throughputs(
    options: OperationOptions,
    input: aws_sdk_bedrock.types.list_provisioned_model_throughputs_request.ListProvisionedModelThroughputsRequest,
) -> tuple[
    aws_sdk_bedrock.types.list_provisioned_model_throughputs_response.ListProvisionedModelThroughputsResponse,
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


async def async_list_provisioned_model_throughputs(
    options: AsyncOperationOptions,
    input: aws_sdk_bedrock.types.list_provisioned_model_throughputs_request.ListProvisionedModelThroughputsRequest,
) -> tuple[
    aws_sdk_bedrock.types.list_provisioned_model_throughputs_response.ListProvisionedModelThroughputsResponse,
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
