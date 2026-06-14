"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#GetMediaForFragmentList``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never, cast

import zapros

import aws_sdk_kinesis_video_archived_media._auth._signers
import aws_sdk_kinesis_video_archived_media._auth._sigv4
from aws_sdk_kinesis_video_archived_media._protocol.errors import (
    parse_error_metadata_json,
)
from aws_sdk_kinesis_video_archived_media._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_kinesis_video_archived_media._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_kinesis_video_archived_media.errors import (
    UnknownServiceError,
)

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.get_media_for_fragment_list_input
    import aws_sdk_kinesis_video_archived_media.types.get_media_for_fragment_list_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ClientLimitExceededException":
            import aws_sdk_kinesis_video_archived_media.errors.client_limit_exceeded_exception

            raise aws_sdk_kinesis_video_archived_media.errors.client_limit_exceeded_exception.ClientLimitExceededException.from_json(
                data
            )
        case "InvalidArgumentException":
            import aws_sdk_kinesis_video_archived_media.errors.invalid_argument_exception

            raise aws_sdk_kinesis_video_archived_media.errors.invalid_argument_exception.InvalidArgumentException.from_json(
                data
            )
        case "NotAuthorizedException":
            import aws_sdk_kinesis_video_archived_media.errors.not_authorized_exception

            raise aws_sdk_kinesis_video_archived_media.errors.not_authorized_exception.NotAuthorizedException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_kinesis_video_archived_media.errors.resource_not_found_exception

            raise aws_sdk_kinesis_video_archived_media.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_kinesis_video_archived_media.types.get_media_for_fragment_list_output.GetMediaForFragmentListOutput:
    _iter = cast(
        Any, response.async_iter_bytes() if is_async else response.iter_bytes()
    )
    out: aws_sdk_kinesis_video_archived_media.types.get_media_for_fragment_list_output.GetMediaForFragmentListOutput = {
        "payload": _iter
    }  # type: ignore[reportAssignmentType]
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_kinesis_video_archived_media._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_kinesis_video_archived_media._auth._sigv4.build_sigv4_auth_scheme(
                "kinesisvideo", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_kinesis_video_archived_media._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_kinesis_video_archived_media.types.get_media_for_fragment_list_input.GetMediaForFragmentListInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/getMediaForFragmentList"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_kinesis_video_archived_media.types.get_media_for_fragment_list_input

    body: bytes | None = json.dumps(
        aws_sdk_kinesis_video_archived_media.types.get_media_for_fragment_list_input.serialize_json(
            input_
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def get_media_for_fragment_list(
    options: OperationOptions,
    input_: aws_sdk_kinesis_video_archived_media.types.get_media_for_fragment_list_input.GetMediaForFragmentListInput,
) -> tuple[
    aws_sdk_kinesis_video_archived_media.types.get_media_for_fragment_list_output.GetMediaForFragmentListOutput,
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


async def async_get_media_for_fragment_list(
    options: AsyncOperationOptions,
    input_: aws_sdk_kinesis_video_archived_media.types.get_media_for_fragment_list_input.GetMediaForFragmentListInput,
) -> tuple[
    aws_sdk_kinesis_video_archived_media.types.get_media_for_fragment_list_output.GetMediaForFragmentListOutput,
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
