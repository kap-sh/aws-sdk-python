"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#PostContent``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_lex_runtime_service._auth._signers
import aws_sdk_lex_runtime_service._auth._sigv4
from aws_sdk_lex_runtime_service._protocol.errors import parse_error_metadata_json
from aws_sdk_lex_runtime_service._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_lex_runtime_service._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_lex_runtime_service.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_service.types.post_content_request
    import aws_sdk_lex_runtime_service.types.post_content_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadGatewayException":
            import aws_sdk_lex_runtime_service.errors.bad_gateway_exception

            raise aws_sdk_lex_runtime_service.errors.bad_gateway_exception.BadGatewayException.from_json(
                data
            )
        case "BadRequestException":
            import aws_sdk_lex_runtime_service.errors.bad_request_exception

            raise aws_sdk_lex_runtime_service.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ConflictException":
            import aws_sdk_lex_runtime_service.errors.conflict_exception

            raise aws_sdk_lex_runtime_service.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "DependencyFailedException":
            import aws_sdk_lex_runtime_service.errors.dependency_failed_exception

            raise aws_sdk_lex_runtime_service.errors.dependency_failed_exception.DependencyFailedException.from_json(
                data
            )
        case "InternalFailureException":
            import aws_sdk_lex_runtime_service.errors.internal_failure_exception

            raise aws_sdk_lex_runtime_service.errors.internal_failure_exception.InternalFailureException.from_json(
                data
            )
        case "LimitExceededException":
            import aws_sdk_lex_runtime_service.errors.limit_exceeded_exception

            raise aws_sdk_lex_runtime_service.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "LoopDetectedException":
            import aws_sdk_lex_runtime_service.errors.loop_detected_exception

            raise aws_sdk_lex_runtime_service.errors.loop_detected_exception.LoopDetectedException.from_json(
                data
            )
        case "NotAcceptableException":
            import aws_sdk_lex_runtime_service.errors.not_acceptable_exception

            raise aws_sdk_lex_runtime_service.errors.not_acceptable_exception.NotAcceptableException.from_json(
                data
            )
        case "NotFoundException":
            import aws_sdk_lex_runtime_service.errors.not_found_exception

            raise aws_sdk_lex_runtime_service.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "RequestTimeoutException":
            import aws_sdk_lex_runtime_service.errors.request_timeout_exception

            raise aws_sdk_lex_runtime_service.errors.request_timeout_exception.RequestTimeoutException.from_json(
                data
            )
        case "UnsupportedMediaTypeException":
            import aws_sdk_lex_runtime_service.errors.unsupported_media_type_exception

            raise aws_sdk_lex_runtime_service.errors.unsupported_media_type_exception.UnsupportedMediaTypeException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_lex_runtime_service.types.post_content_response.PostContentResponse:
    _iter = cast(
        Any, response.async_iter_bytes() if is_async else response.iter_bytes()
    )
    out: aws_sdk_lex_runtime_service.types.post_content_response.PostContentResponse = {
        "audio_stream": _iter
    }  # type: ignore[reportAssignmentType]
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    if "x-amz-lex-intent-name" in response.headers:
        out["intent_name"] = str(response.headers["x-amz-lex-intent-name"])
    if "x-amz-lex-nlu-intent-confidence" in response.headers:
        out["nlu_intent_confidence"] = str(
            response.headers["x-amz-lex-nlu-intent-confidence"]
        )
    if "x-amz-lex-alternative-intents" in response.headers:
        out["alternative_intents"] = str(
            response.headers["x-amz-lex-alternative-intents"]
        )
    if "x-amz-lex-slots" in response.headers:
        out["slots"] = str(response.headers["x-amz-lex-slots"])
    if "x-amz-lex-session-attributes" in response.headers:
        out["session_attributes"] = str(
            response.headers["x-amz-lex-session-attributes"]
        )
    if "x-amz-lex-sentiment" in response.headers:
        out["sentiment_response"] = str(response.headers["x-amz-lex-sentiment"])
    if "x-amz-lex-message" in response.headers:
        out["message"] = str(response.headers["x-amz-lex-message"])
    if "x-amz-lex-encoded-message" in response.headers:
        out["encoded_message"] = str(response.headers["x-amz-lex-encoded-message"])
    if "x-amz-lex-message-format" in response.headers:
        import aws_sdk_lex_runtime_service.types.message_format_type

        out["message_format"] = (
            aws_sdk_lex_runtime_service.types.message_format_type.deserialize_json(
                response.headers["x-amz-lex-message-format"]
            )
        )
    if "x-amz-lex-dialog-state" in response.headers:
        import aws_sdk_lex_runtime_service.types.dialog_state

        out["dialog_state"] = (
            aws_sdk_lex_runtime_service.types.dialog_state.deserialize_json(
                response.headers["x-amz-lex-dialog-state"]
            )
        )
    if "x-amz-lex-slot-to-elicit" in response.headers:
        out["slot_to_elicit"] = str(response.headers["x-amz-lex-slot-to-elicit"])
    if "x-amz-lex-input-transcript" in response.headers:
        out["input_transcript"] = str(response.headers["x-amz-lex-input-transcript"])
    if "x-amz-lex-encoded-input-transcript" in response.headers:
        out["encoded_input_transcript"] = str(
            response.headers["x-amz-lex-encoded-input-transcript"]
        )
    if "x-amz-lex-bot-version" in response.headers:
        out["bot_version"] = str(response.headers["x-amz-lex-bot-version"])
    if "x-amz-lex-session-id" in response.headers:
        out["session_id"] = str(response.headers["x-amz-lex-session-id"])
    if "x-amz-lex-active-contexts" in response.headers:
        out["active_contexts"] = str(response.headers["x-amz-lex-active-contexts"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_lex_runtime_service._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_lex_runtime_service._auth._sigv4.build_sigv4_auth_scheme(
                "lex", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_lex_runtime_service._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_lex_runtime_service.types.post_content_request.PostContentRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/bot/{botName}/alias/{botAlias}/user/{userId}/content"
    )
    url = url.replace("{botName}", quote(str(input_["bot_name"]), safe=""))
    url = url.replace("{botAlias}", quote(str(input_["bot_alias"]), safe=""))
    url = url.replace("{userId}", quote(str(input_["user_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "session_attributes" in input_:
        headers["x-amz-lex-session-attributes"] = str(input_["session_attributes"])
    if "request_attributes" in input_:
        headers["x-amz-lex-request-attributes"] = str(input_["request_attributes"])
    if "content_type" in input_:
        headers["Content-Type"] = str(input_["content_type"])
    if "accept" in input_:
        headers["Accept"] = str(input_["accept"])
    if "active_contexts" in input_:
        headers["x-amz-lex-active-contexts"] = str(input_["active_contexts"])
    body = input_["input_stream"]
    if not isinstance(body, bytes) and "content-length" not in [
        header.lower() for header in headers
    ]:
        raise ValueError("Content-Length is required for streaming input")
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def post_content(
    options: OperationOptions,
    input_: aws_sdk_lex_runtime_service.types.post_content_request.PostContentRequest,
) -> tuple[
    aws_sdk_lex_runtime_service.types.post_content_response.PostContentResponse,
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


async def async_post_content(
    options: AsyncOperationOptions,
    input_: aws_sdk_lex_runtime_service.types.post_content_request.PostContentRequest,
) -> tuple[
    aws_sdk_lex_runtime_service.types.post_content_response.PostContentResponse,
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
