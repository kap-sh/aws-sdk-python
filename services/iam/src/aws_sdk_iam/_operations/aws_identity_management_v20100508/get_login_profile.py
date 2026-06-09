"""Generated from Smithy shape ``com.amazonaws.iam#GetLoginProfile``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never
from urllib.parse import urlencode

import zapros

import aws_sdk_iam._auth._signers
from aws_sdk_iam._protocol.errors import parse_error_metadata
from aws_sdk_iam._protocol.xml import fromstring
from aws_sdk_iam._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_iam.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_login_profile_request
    import aws_sdk_iam.types.get_login_profile_response


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "NoSuchEntityException":
            import aws_sdk_iam.errors.no_such_entity_exception

            raise aws_sdk_iam.errors.no_such_entity_exception.NoSuchEntityException.from_query(
                root
            )
        case "ServiceFailureException":
            import aws_sdk_iam.errors.service_failure_exception

            raise aws_sdk_iam.errors.service_failure_exception.ServiceFailureException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_iam.types.get_login_profile_response.GetLoginProfileResponse:
    import aws_sdk_iam.types.get_login_profile_response

    root = fromstring(response.read())
    result = root.find("GetLoginProfileResult")
    out: aws_sdk_iam.types.get_login_profile_response.GetLoginProfileResponse = (
        aws_sdk_iam.types.get_login_profile_response.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_iam._auth._signers.Signer | None:
    if auth_schemes:
        for scheme in auth_schemes:
            match scheme["name"]:
                case "sigv4" | "sigv4a" | "sigv4-s3express" if (
                    options.credentials_provider is not None
                ):
                    return aws_sdk_iam._auth._signers.SigV4Signer(
                        options.credentials_provider, auth_scheme=scheme
                    )
                case "none":
                    return None
                case _:
                    raise RuntimeError(
                        f"Could not find provider for auth scheme {scheme['name']!r}"
                    )
    if options.credentials_provider is not None:
        if options.region is None:
            raise RuntimeError("options.region is required for SigV4 signing")
        return aws_sdk_iam._auth._signers.SigV4Signer(
            options.credentials_provider,
            auth_scheme={
                "name": "sigv4",
                "signingName": "iam",
                "signingRegion": options.region,
                "disableDoubleEncoding": False,
                "disableNormalizePath": False,
            },
        )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_iam.types.get_login_profile_request.GetLoginProfileRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "GetLoginProfile"))
    pairs.append(("Version", "2010-05-08"))
    import aws_sdk_iam.types.get_login_profile_request

    aws_sdk_iam.types.get_login_profile_request.serialize_query(input, pairs, "")
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def get_login_profile(
    options: OperationOptions,
    input: aws_sdk_iam.types.get_login_profile_request.GetLoginProfileRequest,
) -> tuple[
    aws_sdk_iam.types.get_login_profile_response.GetLoginProfileResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_get_login_profile(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_login_profile_request.GetLoginProfileRequest,
) -> tuple[
    aws_sdk_iam.types.get_login_profile_response.GetLoginProfileResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
