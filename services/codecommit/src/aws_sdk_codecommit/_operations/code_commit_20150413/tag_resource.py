"""Generated from Smithy shape ``com.amazonaws.codecommit#TagResource``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_codecommit._auth._signers
import aws_sdk_codecommit._auth._sigv4
import aws_sdk_codecommit.errors.invalid_repository_name_exception
import aws_sdk_codecommit.errors.invalid_resource_arn_exception
import aws_sdk_codecommit.errors.invalid_system_tag_usage_exception
import aws_sdk_codecommit.errors.invalid_tags_map_exception
import aws_sdk_codecommit.errors.repository_does_not_exist_exception
import aws_sdk_codecommit.errors.resource_arn_required_exception
import aws_sdk_codecommit.errors.tag_policy_exception
import aws_sdk_codecommit.errors.tags_map_required_exception
import aws_sdk_codecommit.errors.too_many_tags_exception
import aws_sdk_codecommit.types.tag_resource_input
import aws_sdk_codecommit.types.tags_map
from aws_sdk_codecommit._protocol.errors import parse_error_metadata_json
from aws_sdk_codecommit._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_codecommit._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codecommit.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidRepositoryNameException":
            raise aws_sdk_codecommit.errors.invalid_repository_name_exception.InvalidRepositoryNameException.from_aws_json_1_1(
                data
            )
        case "InvalidResourceArnException":
            raise aws_sdk_codecommit.errors.invalid_resource_arn_exception.InvalidResourceArnException.from_aws_json_1_1(
                data
            )
        case "InvalidSystemTagUsageException":
            raise aws_sdk_codecommit.errors.invalid_system_tag_usage_exception.InvalidSystemTagUsageException.from_aws_json_1_1(
                data
            )
        case "InvalidTagsMapException":
            raise aws_sdk_codecommit.errors.invalid_tags_map_exception.InvalidTagsMapException.from_aws_json_1_1(
                data
            )
        case "RepositoryDoesNotExistException":
            raise aws_sdk_codecommit.errors.repository_does_not_exist_exception.RepositoryDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "ResourceArnRequiredException":
            raise aws_sdk_codecommit.errors.resource_arn_required_exception.ResourceArnRequiredException.from_aws_json_1_1(
                data
            )
        case "TagPolicyException":
            raise aws_sdk_codecommit.errors.tag_policy_exception.TagPolicyException.from_aws_json_1_1(
                data
            )
        case "TagsMapRequiredException":
            raise aws_sdk_codecommit.errors.tags_map_required_exception.TagsMapRequiredException.from_aws_json_1_1(
                data
            )
        case "TooManyTagsException":
            raise aws_sdk_codecommit.errors.too_many_tags_exception.TooManyTagsException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_codecommit._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_codecommit._auth._sigv4.build_sigv4_auth_scheme(
                "codecommit", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_codecommit._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_codecommit.types.tag_resource_input.TagResourceInput,
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
    headers["X-Amz-Target"] = "CodeCommit_20150413.TagResource"
    body: bytes | None = json.dumps(
        aws_sdk_codecommit.types.tag_resource_input.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def tag_resource(
    options: OperationOptions,
    input_: aws_sdk_codecommit.types.tag_resource_input.TagResourceInput,
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


async def async_tag_resource(
    options: AsyncOperationOptions,
    input_: aws_sdk_codecommit.types.tag_resource_input.TagResourceInput,
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
