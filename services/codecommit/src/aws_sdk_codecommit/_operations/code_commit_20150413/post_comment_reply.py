"""Generated from Smithy shape ``com.amazonaws.codecommit#PostCommentReply``."""

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
    import aws_sdk_codecommit.types.post_comment_reply_input
    import aws_sdk_codecommit.types.post_comment_reply_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ClientRequestTokenRequiredException":
            import aws_sdk_codecommit.errors.client_request_token_required_exception

            raise aws_sdk_codecommit.errors.client_request_token_required_exception.ClientRequestTokenRequiredException.from_aws_json_1_1(
                data
            )
        case "CommentContentRequiredException":
            import aws_sdk_codecommit.errors.comment_content_required_exception

            raise aws_sdk_codecommit.errors.comment_content_required_exception.CommentContentRequiredException.from_aws_json_1_1(
                data
            )
        case "CommentContentSizeLimitExceededException":
            import aws_sdk_codecommit.errors.comment_content_size_limit_exceeded_exception

            raise aws_sdk_codecommit.errors.comment_content_size_limit_exceeded_exception.CommentContentSizeLimitExceededException.from_aws_json_1_1(
                data
            )
        case "CommentDoesNotExistException":
            import aws_sdk_codecommit.errors.comment_does_not_exist_exception

            raise aws_sdk_codecommit.errors.comment_does_not_exist_exception.CommentDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "CommentIdRequiredException":
            import aws_sdk_codecommit.errors.comment_id_required_exception

            raise aws_sdk_codecommit.errors.comment_id_required_exception.CommentIdRequiredException.from_aws_json_1_1(
                data
            )
        case "IdempotencyParameterMismatchException":
            import aws_sdk_codecommit.errors.idempotency_parameter_mismatch_exception

            raise aws_sdk_codecommit.errors.idempotency_parameter_mismatch_exception.IdempotencyParameterMismatchException.from_aws_json_1_1(
                data
            )
        case "InvalidClientRequestTokenException":
            import aws_sdk_codecommit.errors.invalid_client_request_token_exception

            raise aws_sdk_codecommit.errors.invalid_client_request_token_exception.InvalidClientRequestTokenException.from_aws_json_1_1(
                data
            )
        case "InvalidCommentIdException":
            import aws_sdk_codecommit.errors.invalid_comment_id_exception

            raise aws_sdk_codecommit.errors.invalid_comment_id_exception.InvalidCommentIdException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_codecommit.types.post_comment_reply_output.PostCommentReplyOutput:
    import aws_sdk_codecommit.types.post_comment_reply_output

    out: aws_sdk_codecommit.types.post_comment_reply_output.PostCommentReplyOutput = (
        aws_sdk_codecommit.types.post_comment_reply_output.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
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
    input_: aws_sdk_codecommit.types.post_comment_reply_input.PostCommentReplyInput,
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
    headers["X-Amz-Target"] = "CodeCommit_20150413.PostCommentReply"
    import aws_sdk_codecommit.types.post_comment_reply_input

    body: bytes | None = json.dumps(
        aws_sdk_codecommit.types.post_comment_reply_input.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def post_comment_reply(
    options: OperationOptions,
    input_: aws_sdk_codecommit.types.post_comment_reply_input.PostCommentReplyInput,
) -> tuple[
    aws_sdk_codecommit.types.post_comment_reply_output.PostCommentReplyOutput,
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


async def async_post_comment_reply(
    options: AsyncOperationOptions,
    input_: aws_sdk_codecommit.types.post_comment_reply_input.PostCommentReplyInput,
) -> tuple[
    aws_sdk_codecommit.types.post_comment_reply_output.PostCommentReplyOutput,
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
