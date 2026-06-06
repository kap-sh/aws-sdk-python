"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateIpamResourceDiscovery``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any
from aws_sdk_ec2._rule_engine._endpoint_rule_set import EndpointParams, resolve
import zapros
from aws_sdk_ec2.errors import UnknownServiceError
from aws_sdk_ec2._protocol.errors import parse_error_metadata
from aws_sdk_ec2._protocol.xml import fromstring
from urllib.parse import urlencode
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associate_ipam_resource_discovery_request
    import aws_sdk_ec2.types.associate_ipam_resource_discovery_result


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_ec2.types.associate_ipam_resource_discovery_result.AssociateIpamResourceDiscoveryResult:
    import aws_sdk_ec2.types.associate_ipam_resource_discovery_result

    out: aws_sdk_ec2.types.associate_ipam_resource_discovery_result.AssociateIpamResourceDiscoveryResult = aws_sdk_ec2.types.associate_ipam_resource_discovery_result.deserialize_ec2_query(
        fromstring(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_ec2._auth._signers.Signer | None:
    if auth_schemes:
        for scheme in auth_schemes:
            match scheme["name"]:
                case "sigv4" | "sigv4a" | "sigv4-s3express" if (
                    options.credentials_provider is not None
                ):
                    return aws_sdk_ec2._auth._signers.SigV4Signer(
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
        return aws_sdk_ec2._auth._signers.SigV4Signer(
            options.credentials_provider,
            auth_scheme={
                "name": "sigv4",
                "signingName": "ec2",
                "signingRegion": options.region,
                "disableDoubleEncoding": False,
                "disableNormalizePath": False,
            },
        )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_ec2.types.associate_ipam_resource_discovery_request.AssociateIpamResourceDiscoveryRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "AssociateIpamResourceDiscovery"))
    pairs.append(("Version", "2016-11-15"))
    import aws_sdk_ec2.types.associate_ipam_resource_discovery_request

    aws_sdk_ec2.types.associate_ipam_resource_discovery_request.serialize_ec2_query(
        input, pairs, ""
    )
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


def associate_ipam_resource_discovery(
    options: OperationOptions,
    input: aws_sdk_ec2.types.associate_ipam_resource_discovery_request.AssociateIpamResourceDiscoveryRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_ipam_resource_discovery_result.AssociateIpamResourceDiscoveryResult,
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


async def async_associate_ipam_resource_discovery(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.associate_ipam_resource_discovery_request.AssociateIpamResourceDiscoveryRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_ipam_resource_discovery_result.AssociateIpamResourceDiscoveryResult,
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
