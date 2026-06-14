"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdatePullRequestApprovalRuleContent``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

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
    import aws_sdk_codecommit.types.update_pull_request_approval_rule_content_input
    import aws_sdk_codecommit.types.update_pull_request_approval_rule_content_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ApprovalRuleContentRequiredException":
            import aws_sdk_codecommit.errors.approval_rule_content_required_exception

            raise aws_sdk_codecommit.errors.approval_rule_content_required_exception.ApprovalRuleContentRequiredException.from_aws_json_1_1(
                data
            )
        case "ApprovalRuleDoesNotExistException":
            import aws_sdk_codecommit.errors.approval_rule_does_not_exist_exception

            raise aws_sdk_codecommit.errors.approval_rule_does_not_exist_exception.ApprovalRuleDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "ApprovalRuleNameRequiredException":
            import aws_sdk_codecommit.errors.approval_rule_name_required_exception

            raise aws_sdk_codecommit.errors.approval_rule_name_required_exception.ApprovalRuleNameRequiredException.from_aws_json_1_1(
                data
            )
        case "CannotModifyApprovalRuleFromTemplateException":
            import aws_sdk_codecommit.errors.cannot_modify_approval_rule_from_template_exception

            raise aws_sdk_codecommit.errors.cannot_modify_approval_rule_from_template_exception.CannotModifyApprovalRuleFromTemplateException.from_aws_json_1_1(
                data
            )
        case "EncryptionIntegrityChecksFailedException":
            import aws_sdk_codecommit.errors.encryption_integrity_checks_failed_exception

            raise aws_sdk_codecommit.errors.encryption_integrity_checks_failed_exception.EncryptionIntegrityChecksFailedException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyAccessDeniedException":
            import aws_sdk_codecommit.errors.encryption_key_access_denied_exception

            raise aws_sdk_codecommit.errors.encryption_key_access_denied_exception.EncryptionKeyAccessDeniedException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyDisabledException":
            import aws_sdk_codecommit.errors.encryption_key_disabled_exception

            raise aws_sdk_codecommit.errors.encryption_key_disabled_exception.EncryptionKeyDisabledException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyNotFoundException":
            import aws_sdk_codecommit.errors.encryption_key_not_found_exception

            raise aws_sdk_codecommit.errors.encryption_key_not_found_exception.EncryptionKeyNotFoundException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyUnavailableException":
            import aws_sdk_codecommit.errors.encryption_key_unavailable_exception

            raise aws_sdk_codecommit.errors.encryption_key_unavailable_exception.EncryptionKeyUnavailableException.from_aws_json_1_1(
                data
            )
        case "InvalidApprovalRuleContentException":
            import aws_sdk_codecommit.errors.invalid_approval_rule_content_exception

            raise aws_sdk_codecommit.errors.invalid_approval_rule_content_exception.InvalidApprovalRuleContentException.from_aws_json_1_1(
                data
            )
        case "InvalidApprovalRuleNameException":
            import aws_sdk_codecommit.errors.invalid_approval_rule_name_exception

            raise aws_sdk_codecommit.errors.invalid_approval_rule_name_exception.InvalidApprovalRuleNameException.from_aws_json_1_1(
                data
            )
        case "InvalidPullRequestIdException":
            import aws_sdk_codecommit.errors.invalid_pull_request_id_exception

            raise aws_sdk_codecommit.errors.invalid_pull_request_id_exception.InvalidPullRequestIdException.from_aws_json_1_1(
                data
            )
        case "InvalidRuleContentSha256Exception":
            import aws_sdk_codecommit.errors.invalid_rule_content_sha256_exception

            raise aws_sdk_codecommit.errors.invalid_rule_content_sha256_exception.InvalidRuleContentSha256Exception.from_aws_json_1_1(
                data
            )
        case "PullRequestAlreadyClosedException":
            import aws_sdk_codecommit.errors.pull_request_already_closed_exception

            raise aws_sdk_codecommit.errors.pull_request_already_closed_exception.PullRequestAlreadyClosedException.from_aws_json_1_1(
                data
            )
        case "PullRequestDoesNotExistException":
            import aws_sdk_codecommit.errors.pull_request_does_not_exist_exception

            raise aws_sdk_codecommit.errors.pull_request_does_not_exist_exception.PullRequestDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "PullRequestIdRequiredException":
            import aws_sdk_codecommit.errors.pull_request_id_required_exception

            raise aws_sdk_codecommit.errors.pull_request_id_required_exception.PullRequestIdRequiredException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_codecommit.types.update_pull_request_approval_rule_content_output.UpdatePullRequestApprovalRuleContentOutput:
    import aws_sdk_codecommit.types.update_pull_request_approval_rule_content_output

    out: aws_sdk_codecommit.types.update_pull_request_approval_rule_content_output.UpdatePullRequestApprovalRuleContentOutput = aws_sdk_codecommit.types.update_pull_request_approval_rule_content_output.deserialize_aws_json_1_1(
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
    input_: aws_sdk_codecommit.types.update_pull_request_approval_rule_content_input.UpdatePullRequestApprovalRuleContentInput,
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
    headers["X-Amz-Target"] = "CodeCommit_20150413.UpdatePullRequestApprovalRuleContent"
    import aws_sdk_codecommit.types.update_pull_request_approval_rule_content_input

    body: bytes | None = json.dumps(
        aws_sdk_codecommit.types.update_pull_request_approval_rule_content_input.serialize_aws_json_1_1(
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


def update_pull_request_approval_rule_content(
    options: OperationOptions,
    input_: aws_sdk_codecommit.types.update_pull_request_approval_rule_content_input.UpdatePullRequestApprovalRuleContentInput,
) -> tuple[
    aws_sdk_codecommit.types.update_pull_request_approval_rule_content_output.UpdatePullRequestApprovalRuleContentOutput,
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


async def async_update_pull_request_approval_rule_content(
    options: AsyncOperationOptions,
    input_: aws_sdk_codecommit.types.update_pull_request_approval_rule_content_input.UpdatePullRequestApprovalRuleContentInput,
) -> tuple[
    aws_sdk_codecommit.types.update_pull_request_approval_rule_content_output.UpdatePullRequestApprovalRuleContentOutput,
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
