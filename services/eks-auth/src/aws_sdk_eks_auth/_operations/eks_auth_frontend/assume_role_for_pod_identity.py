"""Generated from Smithy shape ``com.amazonaws.eksauth#AssumeRoleForPodIdentity``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_eks_auth._auth._signers
import aws_sdk_eks_auth._auth._sigv4
from aws_sdk_eks_auth._protocol.errors import parse_error_metadata_json
from aws_sdk_eks_auth._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_eks_auth._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_eks_auth.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_eks_auth.types.assume_role_for_pod_identity_request
    import aws_sdk_eks_auth.types.assume_role_for_pod_identity_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_eks_auth.errors.access_denied_exception

            raise aws_sdk_eks_auth.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ExpiredTokenException":
            import aws_sdk_eks_auth.errors.expired_token_exception

            raise aws_sdk_eks_auth.errors.expired_token_exception.ExpiredTokenException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_eks_auth.errors.internal_server_exception

            raise aws_sdk_eks_auth.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "InvalidParameterException":
            import aws_sdk_eks_auth.errors.invalid_parameter_exception

            raise aws_sdk_eks_auth.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case "InvalidRequestException":
            import aws_sdk_eks_auth.errors.invalid_request_exception

            raise aws_sdk_eks_auth.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "InvalidTokenException":
            import aws_sdk_eks_auth.errors.invalid_token_exception

            raise aws_sdk_eks_auth.errors.invalid_token_exception.InvalidTokenException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_eks_auth.errors.resource_not_found_exception

            raise aws_sdk_eks_auth.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceUnavailableException":
            import aws_sdk_eks_auth.errors.service_unavailable_exception

            raise aws_sdk_eks_auth.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_eks_auth.errors.throttling_exception

            raise aws_sdk_eks_auth.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_eks_auth.types.assume_role_for_pod_identity_response.AssumeRoleForPodIdentityResponse:
    import aws_sdk_eks_auth.types.assume_role_for_pod_identity_response

    out: aws_sdk_eks_auth.types.assume_role_for_pod_identity_response.AssumeRoleForPodIdentityResponse = aws_sdk_eks_auth.types.assume_role_for_pod_identity_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_eks_auth._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_eks_auth._auth._sigv4.build_sigv4_auth_scheme(
                "eks-auth", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_eks_auth._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_eks_auth.types.assume_role_for_pod_identity_request.AssumeRoleForPodIdentityRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region, UseFIPS=options.use_fips, Endpoint=options.endpoint
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/clusters/{clusterName}/assume-role-for-pod-identity"
    )
    url = url.replace("{clusterName}", quote(str(input_["cluster_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_eks_auth.types.assume_role_for_pod_identity_request

    body: bytes | None = json.dumps(
        aws_sdk_eks_auth.types.assume_role_for_pod_identity_request.serialize_json(
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


def assume_role_for_pod_identity(
    options: OperationOptions,
    input_: aws_sdk_eks_auth.types.assume_role_for_pod_identity_request.AssumeRoleForPodIdentityRequest,
) -> tuple[
    aws_sdk_eks_auth.types.assume_role_for_pod_identity_response.AssumeRoleForPodIdentityResponse,
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


async def async_assume_role_for_pod_identity(
    options: AsyncOperationOptions,
    input_: aws_sdk_eks_auth.types.assume_role_for_pod_identity_request.AssumeRoleForPodIdentityRequest,
) -> tuple[
    aws_sdk_eks_auth.types.assume_role_for_pod_identity_response.AssumeRoleForPodIdentityResponse,
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
