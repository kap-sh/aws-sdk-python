"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetImageFrame``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never, cast
from urllib.parse import quote

import zapros

import aws_sdk_medical_imaging._auth._signers
import aws_sdk_medical_imaging._auth._sigv4
from aws_sdk_medical_imaging._protocol.errors import parse_error_metadata_json
from aws_sdk_medical_imaging._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_medical_imaging._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_medical_imaging.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.get_image_frame_request
    import aws_sdk_medical_imaging.types.get_image_frame_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_medical_imaging.errors.access_denied_exception

            raise aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "BadRequestException":
            import aws_sdk_medical_imaging.errors.bad_request_exception

            raise aws_sdk_medical_imaging.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ConflictException":
            import aws_sdk_medical_imaging.errors.conflict_exception

            raise aws_sdk_medical_imaging.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_medical_imaging.errors.internal_server_exception

            raise aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "NotAcceptableException":
            import aws_sdk_medical_imaging.errors.not_acceptable_exception

            raise aws_sdk_medical_imaging.errors.not_acceptable_exception.NotAcceptableException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_medical_imaging.errors.resource_not_found_exception

            raise aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_medical_imaging.errors.throttling_exception

            raise aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_medical_imaging.errors.validation_exception

            raise aws_sdk_medical_imaging.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_medical_imaging.types.get_image_frame_response.GetImageFrameResponse:
    _iter = cast(
        Any, response.async_iter_bytes() if is_async else response.iter_bytes()
    )
    out: aws_sdk_medical_imaging.types.get_image_frame_response.GetImageFrameResponse = {
        "image_frame_blob": _iter
    }
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_medical_imaging._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_medical_imaging._auth._sigv4.build_sigv4_auth_scheme(
                "medical-imaging", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_medical_imaging._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_medical_imaging.types.get_image_frame_request.GetImageFrameRequest,
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
        + "/datastore/{datastoreId}/imageSet/{imageSetId}/getImageFrame"
    )
    url = url.replace("{datastoreId}", quote(str(input_["datastore_id"]), safe=""))
    url = url.replace("{imageSetId}", quote(str(input_["image_set_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "image_frame_information" in input_:
        import aws_sdk_medical_imaging.types.image_frame_information

        body: bytes | None = json.dumps(
            aws_sdk_medical_imaging.types.image_frame_information.serialize_json(
                input_["image_frame_information"]
            )
        ).encode()
        headers["content-type"] = "application/json"
    else:
        body = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def get_image_frame(
    options: OperationOptions,
    input_: aws_sdk_medical_imaging.types.get_image_frame_request.GetImageFrameRequest,
) -> tuple[
    aws_sdk_medical_imaging.types.get_image_frame_response.GetImageFrameResponse,
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


async def async_get_image_frame(
    options: AsyncOperationOptions,
    input_: aws_sdk_medical_imaging.types.get_image_frame_request.GetImageFrameRequest,
) -> tuple[
    aws_sdk_medical_imaging.types.get_image_frame_response.GetImageFrameResponse,
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
