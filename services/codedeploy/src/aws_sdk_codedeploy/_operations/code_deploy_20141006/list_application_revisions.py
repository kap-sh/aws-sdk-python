"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListApplicationRevisions``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_codedeploy._auth._signers
import aws_sdk_codedeploy._auth._sigv4
import aws_sdk_codedeploy.errors.application_does_not_exist_exception
import aws_sdk_codedeploy.errors.application_name_required_exception
import aws_sdk_codedeploy.errors.bucket_name_filter_required_exception
import aws_sdk_codedeploy.errors.invalid_application_name_exception
import aws_sdk_codedeploy.errors.invalid_bucket_name_filter_exception
import aws_sdk_codedeploy.errors.invalid_deployed_state_filter_exception
import aws_sdk_codedeploy.errors.invalid_key_prefix_filter_exception
import aws_sdk_codedeploy.errors.invalid_next_token_exception
import aws_sdk_codedeploy.errors.invalid_sort_by_exception
import aws_sdk_codedeploy.errors.invalid_sort_order_exception
import aws_sdk_codedeploy.types.application_revision_sort_by
import aws_sdk_codedeploy.types.list_application_revisions_input
import aws_sdk_codedeploy.types.list_application_revisions_output
import aws_sdk_codedeploy.types.list_state_filter_action
import aws_sdk_codedeploy.types.revision_location_list
import aws_sdk_codedeploy.types.sort_order
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
        case "ApplicationNameRequiredException":
            raise aws_sdk_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException.from_aws_json_1_1(
                data
            )
        case "BucketNameFilterRequiredException":
            raise aws_sdk_codedeploy.errors.bucket_name_filter_required_exception.BucketNameFilterRequiredException.from_aws_json_1_1(
                data
            )
        case "InvalidApplicationNameException":
            raise aws_sdk_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException.from_aws_json_1_1(
                data
            )
        case "InvalidBucketNameFilterException":
            raise aws_sdk_codedeploy.errors.invalid_bucket_name_filter_exception.InvalidBucketNameFilterException.from_aws_json_1_1(
                data
            )
        case "InvalidDeployedStateFilterException":
            raise aws_sdk_codedeploy.errors.invalid_deployed_state_filter_exception.InvalidDeployedStateFilterException.from_aws_json_1_1(
                data
            )
        case "InvalidKeyPrefixFilterException":
            raise aws_sdk_codedeploy.errors.invalid_key_prefix_filter_exception.InvalidKeyPrefixFilterException.from_aws_json_1_1(
                data
            )
        case "InvalidNextTokenException":
            raise aws_sdk_codedeploy.errors.invalid_next_token_exception.InvalidNextTokenException.from_aws_json_1_1(
                data
            )
        case "InvalidSortByException":
            raise aws_sdk_codedeploy.errors.invalid_sort_by_exception.InvalidSortByException.from_aws_json_1_1(
                data
            )
        case "InvalidSortOrderException":
            raise aws_sdk_codedeploy.errors.invalid_sort_order_exception.InvalidSortOrderException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_codedeploy.types.list_application_revisions_output.ListApplicationRevisionsOutput:
    out: aws_sdk_codedeploy.types.list_application_revisions_output.ListApplicationRevisionsOutput = aws_sdk_codedeploy.types.list_application_revisions_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_codedeploy.types.list_application_revisions_output.ListApplicationRevisionsOutput:
    out: aws_sdk_codedeploy.types.list_application_revisions_output.ListApplicationRevisionsOutput = aws_sdk_codedeploy.types.list_application_revisions_output.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
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
    input_: aws_sdk_codedeploy.types.list_application_revisions_input.ListApplicationRevisionsInput,
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
    headers["X-Amz-Target"] = "CodeDeploy_20141006.ListApplicationRevisions"
    import aws_sdk_codedeploy.types.list_application_revisions_input

    body: bytes | None = json.dumps(
        aws_sdk_codedeploy.types.list_application_revisions_input.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def list_application_revisions(
    options: OperationOptions,
    input_: aws_sdk_codedeploy.types.list_application_revisions_input.ListApplicationRevisionsInput,
) -> tuple[
    aws_sdk_codedeploy.types.list_application_revisions_output.ListApplicationRevisionsOutput,
    zapros.Response,
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


async def async_list_application_revisions(
    options: AsyncOperationOptions,
    input_: aws_sdk_codedeploy.types.list_application_revisions_input.ListApplicationRevisionsInput,
) -> tuple[
    aws_sdk_codedeploy.types.list_application_revisions_output.ListApplicationRevisionsOutput,
    zapros.Response,
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
