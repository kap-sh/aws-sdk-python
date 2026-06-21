"""Generated from Smithy shape ``com.amazonaws.codedeploy#UntagResource``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_codedeploy._auth._signers
import aws_sdk_codedeploy._auth._sigv4
import aws_sdk_codedeploy.errors.application_does_not_exist_exception
import aws_sdk_codedeploy.errors.arn_not_supported_exception
import aws_sdk_codedeploy.errors.deployment_config_does_not_exist_exception
import aws_sdk_codedeploy.errors.deployment_group_does_not_exist_exception
import aws_sdk_codedeploy.errors.invalid_arn_exception
import aws_sdk_codedeploy.errors.invalid_tags_to_add_exception
import aws_sdk_codedeploy.errors.resource_arn_required_exception
import aws_sdk_codedeploy.errors.tag_required_exception
import aws_sdk_codedeploy.types.tag_key_list
import aws_sdk_codedeploy.types.untag_resource_input
import aws_sdk_codedeploy.types.untag_resource_output
from aws_sdk_codedeploy._protocol.errors import parse_error_metadata_json
from aws_sdk_codedeploy._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_codedeploy._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codedeploy.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ApplicationDoesNotExistException":
            raise aws_sdk_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "ArnNotSupportedException":
            raise aws_sdk_codedeploy.errors.arn_not_supported_exception.ArnNotSupportedException.from_aws_json_1_1(
                data
            )
        case "DeploymentConfigDoesNotExistException":
            raise aws_sdk_codedeploy.errors.deployment_config_does_not_exist_exception.DeploymentConfigDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "DeploymentGroupDoesNotExistException":
            raise aws_sdk_codedeploy.errors.deployment_group_does_not_exist_exception.DeploymentGroupDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "InvalidArnException":
            raise aws_sdk_codedeploy.errors.invalid_arn_exception.InvalidArnException.from_aws_json_1_1(
                data
            )
        case "InvalidTagsToAddException":
            raise aws_sdk_codedeploy.errors.invalid_tags_to_add_exception.InvalidTagsToAddException.from_aws_json_1_1(
                data
            )
        case "ResourceArnRequiredException":
            raise aws_sdk_codedeploy.errors.resource_arn_required_exception.ResourceArnRequiredException.from_aws_json_1_1(
                data
            )
        case "TagRequiredException":
            raise aws_sdk_codedeploy.errors.tag_required_exception.TagRequiredException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_codedeploy.types.untag_resource_output.UntagResourceOutput:
    out: aws_sdk_codedeploy.types.untag_resource_output.UntagResourceOutput = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_codedeploy.types.untag_resource_output.UntagResourceOutput:
    out: aws_sdk_codedeploy.types.untag_resource_output.UntagResourceOutput = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_codedeploy._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_codedeploy._auth._sigv4.build_sigv4_auth_scheme(
                "codedeploy", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_codedeploy._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_codedeploy.types.untag_resource_input.UntagResourceInput,
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
    headers["X-Amz-Target"] = "CodeDeploy_20141006.UntagResource"
    import aws_sdk_codedeploy.types.untag_resource_input

    body: bytes | None = json.dumps(
        aws_sdk_codedeploy.types.untag_resource_input.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def untag_resource(
    options: OperationOptions,
    input_: aws_sdk_codedeploy.types.untag_resource_input.UntagResourceInput,
) -> tuple[
    aws_sdk_codedeploy.types.untag_resource_output.UntagResourceOutput, zapros.Response
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_untag_resource(
    options: AsyncOperationOptions,
    input_: aws_sdk_codedeploy.types.untag_resource_input.UntagResourceInput,
) -> tuple[
    aws_sdk_codedeploy.types.untag_resource_output.UntagResourceOutput, zapros.Response
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
