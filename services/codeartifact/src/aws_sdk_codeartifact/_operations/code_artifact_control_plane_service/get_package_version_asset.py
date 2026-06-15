"""Generated from Smithy shape ``com.amazonaws.codeartifact#GetPackageVersionAsset``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never, cast

import zapros

import aws_sdk_codeartifact._auth._signers
import aws_sdk_codeartifact._auth._sigv4
from aws_sdk_codeartifact._protocol.errors import parse_error_metadata_json
from aws_sdk_codeartifact._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_codeartifact._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codeartifact.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.get_package_version_asset_request
    import aws_sdk_codeartifact.types.get_package_version_asset_result


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_codeartifact.errors.access_denied_exception

            raise aws_sdk_codeartifact.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            import aws_sdk_codeartifact.errors.conflict_exception

            raise aws_sdk_codeartifact.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_codeartifact.errors.internal_server_exception

            raise aws_sdk_codeartifact.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_codeartifact.errors.resource_not_found_exception

            raise aws_sdk_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_codeartifact.errors.throttling_exception

            raise aws_sdk_codeartifact.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_codeartifact.errors.validation_exception

            raise aws_sdk_codeartifact.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_codeartifact.types.get_package_version_asset_result.GetPackageVersionAssetResult:
    _iter = cast(
        Any, response.async_iter_bytes() if is_async else response.iter_bytes()
    )
    out: aws_sdk_codeartifact.types.get_package_version_asset_result.GetPackageVersionAssetResult = {
        "asset": _iter
    }  # type: ignore[reportAssignmentType]
    if "X-AssetName" in response.headers:
        out["asset_name"] = str(response.headers["X-AssetName"])
    if "X-PackageVersion" in response.headers:
        out["package_version"] = str(response.headers["X-PackageVersion"])
    if "X-PackageVersionRevision" in response.headers:
        out["package_version_revision"] = str(
            response.headers["X-PackageVersionRevision"]
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_codeartifact._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_codeartifact._auth._sigv4.build_sigv4_auth_scheme(
                "codeartifact", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_codeartifact._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_codeartifact.types.get_package_version_asset_request.GetPackageVersionAssetRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/package/version/asset"
    params: dict[str, str] = {}
    if "domain" in input_:
        params["domain"] = str(input_["domain"])
    if "domain_owner" in input_:
        params["domain-owner"] = str(input_["domain_owner"])
    if "repository" in input_:
        params["repository"] = str(input_["repository"])
    if "format" in input_:
        params["format"] = str(input_["format"])
    if "namespace" in input_:
        params["namespace"] = str(input_["namespace"])
    if "package" in input_:
        params["package"] = str(input_["package"])
    if "package_version" in input_:
        params["version"] = str(input_["package_version"])
    if "asset" in input_:
        params["asset"] = str(input_["asset"])
    if "package_version_revision" in input_:
        params["revision"] = str(input_["package_version_revision"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_package_version_asset(
    options: OperationOptions,
    input_: aws_sdk_codeartifact.types.get_package_version_asset_request.GetPackageVersionAssetRequest,
) -> tuple[
    aws_sdk_codeartifact.types.get_package_version_asset_result.GetPackageVersionAssetResult,
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


async def async_get_package_version_asset(
    options: AsyncOperationOptions,
    input_: aws_sdk_codeartifact.types.get_package_version_asset_request.GetPackageVersionAssetRequest,
) -> tuple[
    aws_sdk_codeartifact.types.get_package_version_asset_result.GetPackageVersionAssetResult,
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
