"""Generated from Smithy shape ``com.amazonaws.codecommit#PutCommentReaction``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_codecommit._auth._signers
import capo_codecommit._auth._sigv4
import capo_codecommit.errors.comment_deleted_exception
import capo_codecommit.errors.comment_does_not_exist_exception
import capo_codecommit.errors.comment_id_required_exception
import capo_codecommit.errors.invalid_comment_id_exception
import capo_codecommit.errors.invalid_reaction_value_exception
import capo_codecommit.errors.reaction_limit_exceeded_exception
import capo_codecommit.errors.reaction_value_required_exception
import capo_codecommit.types.put_comment_reaction_input
from capo_codecommit._protocol.errors import parse_error_metadata_json
from capo_codecommit._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_codecommit._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_codecommit.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CommentDeletedException":
            raise capo_codecommit.errors.comment_deleted_exception.CommentDeletedException.from_aws_json_1_1(
                data
            )
        case "CommentDoesNotExistException":
            raise capo_codecommit.errors.comment_does_not_exist_exception.CommentDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "CommentIdRequiredException":
            raise capo_codecommit.errors.comment_id_required_exception.CommentIdRequiredException.from_aws_json_1_1(
                data
            )
        case "InvalidCommentIdException":
            raise capo_codecommit.errors.invalid_comment_id_exception.InvalidCommentIdException.from_aws_json_1_1(
                data
            )
        case "InvalidReactionValueException":
            raise capo_codecommit.errors.invalid_reaction_value_exception.InvalidReactionValueException.from_aws_json_1_1(
                data
            )
        case "ReactionLimitExceededException":
            raise capo_codecommit.errors.reaction_limit_exceeded_exception.ReactionLimitExceededException.from_aws_json_1_1(
                data
            )
        case "ReactionValueRequiredException":
            raise capo_codecommit.errors.reaction_value_required_exception.ReactionValueRequiredException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_codecommit._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_codecommit._auth._sigv4.build_sigv4_auth_scheme(
                "codecommit", options.region
            )
        )
        if sigv4_config is not None:
            return capo_codecommit._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_codecommit.types.put_comment_reaction_input.PutCommentReactionInput,
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
    headers["X-Amz-Target"] = "CodeCommit_20150413.PutCommentReaction"
    body: bytes | None = json.dumps(
        capo_codecommit.types.put_comment_reaction_input.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def put_comment_reaction(
    options: OperationOptions,
    input_: capo_codecommit.types.put_comment_reaction_input.PutCommentReactionInput,
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


async def async_put_comment_reaction(
    options: AsyncOperationOptions,
    input_: capo_codecommit.types.put_comment_reaction_input.PutCommentReactionInput,
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
