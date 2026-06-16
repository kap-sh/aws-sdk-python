"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateApprovalRuleTemplateName``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_codecommit._auth._signers
import aws_sdk_codecommit._auth._sigv4
from aws_sdk_codecommit._protocol.errors import parse_error_metadata_json
from aws_sdk_codecommit._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_codecommit._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codecommit.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.update_approval_rule_template_name_input
    import aws_sdk_codecommit.types.update_approval_rule_template_name_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ApprovalRuleTemplateDoesNotExistException":
            import aws_sdk_codecommit.errors.approval_rule_template_does_not_exist_exception

            raise aws_sdk_codecommit.errors.approval_rule_template_does_not_exist_exception.ApprovalRuleTemplateDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "ApprovalRuleTemplateNameAlreadyExistsException":
            import aws_sdk_codecommit.errors.approval_rule_template_name_already_exists_exception

            raise aws_sdk_codecommit.errors.approval_rule_template_name_already_exists_exception.ApprovalRuleTemplateNameAlreadyExistsException.from_aws_json_1_1(
                data
            )
        case "ApprovalRuleTemplateNameRequiredException":
            import aws_sdk_codecommit.errors.approval_rule_template_name_required_exception

            raise aws_sdk_codecommit.errors.approval_rule_template_name_required_exception.ApprovalRuleTemplateNameRequiredException.from_aws_json_1_1(
                data
            )
        case "InvalidApprovalRuleTemplateNameException":
            import aws_sdk_codecommit.errors.invalid_approval_rule_template_name_exception

            raise aws_sdk_codecommit.errors.invalid_approval_rule_template_name_exception.InvalidApprovalRuleTemplateNameException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_codecommit.types.update_approval_rule_template_name_output.UpdateApprovalRuleTemplateNameOutput:
    import aws_sdk_codecommit.types.update_approval_rule_template_name_output

    out: aws_sdk_codecommit.types.update_approval_rule_template_name_output.UpdateApprovalRuleTemplateNameOutput = aws_sdk_codecommit.types.update_approval_rule_template_name_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


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
    input_: aws_sdk_codecommit.types.update_approval_rule_template_name_input.UpdateApprovalRuleTemplateNameInput,
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
    headers["X-Amz-Target"] = "CodeCommit_20150413.UpdateApprovalRuleTemplateName"
    import aws_sdk_codecommit.types.update_approval_rule_template_name_input

    body: bytes | None = json.dumps(
        aws_sdk_codecommit.types.update_approval_rule_template_name_input.serialize_aws_json_1_1(
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


def update_approval_rule_template_name(
    options: OperationOptions,
    input_: aws_sdk_codecommit.types.update_approval_rule_template_name_input.UpdateApprovalRuleTemplateNameInput,
) -> tuple[
    aws_sdk_codecommit.types.update_approval_rule_template_name_output.UpdateApprovalRuleTemplateNameOutput,
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


async def async_update_approval_rule_template_name(
    options: AsyncOperationOptions,
    input_: aws_sdk_codecommit.types.update_approval_rule_template_name_input.UpdateApprovalRuleTemplateNameInput,
) -> tuple[
    aws_sdk_codecommit.types.update_approval_rule_template_name_output.UpdateApprovalRuleTemplateNameOutput,
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
