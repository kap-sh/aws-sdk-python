"""Generated from Smithy shape ``com.amazonaws.datazone#ListRules``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_datazone._auth._signers
import aws_sdk_datazone._auth._sigv4
from aws_sdk_datazone._protocol.errors import parse_error_metadata_json
from aws_sdk_datazone._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_datazone._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_datazone.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.list_rules_input
    import aws_sdk_datazone.types.list_rules_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_datazone.errors.access_denied_exception

            raise aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_datazone.errors.throttling_exception

            raise aws_sdk_datazone.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "UnauthorizedException":
            import aws_sdk_datazone.errors.unauthorized_exception

            raise aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_datazone.errors.internal_server_exception

            raise aws_sdk_datazone.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_datazone.errors.resource_not_found_exception

            raise aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_datazone.errors.validation_exception

            raise aws_sdk_datazone.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_datazone.types.list_rules_output.ListRulesOutput:
    import aws_sdk_datazone.types.list_rules_output

    out: aws_sdk_datazone.types.list_rules_output.ListRulesOutput = (
        aws_sdk_datazone.types.list_rules_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_datazone._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_datazone._auth._sigv4.build_sigv4_auth_scheme(
                "datazone", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_datazone._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_datazone.types.list_rules_input.ListRulesInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region, UseFIPS=options.use_fips, Endpoint=options.endpoint
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/v2/domains/{domainIdentifier}/list-rules/{targetType}/{targetIdentifier}"
    )
    url = url.replace(
        "{domainIdentifier}", quote(str(input_["domain_identifier"]), safe="")
    )
    url = url.replace("{targetType}", quote(str(input_["target_type"]), safe=""))
    url = url.replace(
        "{targetIdentifier}", quote(str(input_["target_identifier"]), safe="")
    )
    params: dict[str, str] = {}
    if "rule_type" in input_:
        params["ruleType"] = str(input_["rule_type"])
    if "action" in input_:
        params["ruleAction"] = str(input_["action"])
    if "project_ids" in input_:
        params["projectIds"] = str(input_["project_ids"])
    if "asset_types" in input_:
        params["assetTypes"] = str(input_["asset_types"])
    if "data_product" in input_:
        params["dataProduct"] = str(input_["data_product"])
    if "include_cascaded" in input_:
        params["includeCascaded"] = str(input_["include_cascaded"])
    if "max_results" in input_:
        params["maxResults"] = str(input_["max_results"])
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_rules(
    options: OperationOptions,
    input_: aws_sdk_datazone.types.list_rules_input.ListRulesInput,
) -> tuple[aws_sdk_datazone.types.list_rules_output.ListRulesOutput, zapros.Response]:
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


async def async_list_rules(
    options: AsyncOperationOptions,
    input_: aws_sdk_datazone.types.list_rules_input.ListRulesInput,
) -> tuple[aws_sdk_datazone.types.list_rules_output.ListRulesOutput, zapros.Response]:
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
