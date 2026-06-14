"""Generated from Smithy shape ``com.amazonaws.route53#CreateVPCAssociationAuthorization``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_route_53._auth._signers
import aws_sdk_route_53._auth._sigv4
from aws_sdk_route_53._protocol.errors import parse_error_metadata
from aws_sdk_route_53._protocol.xml import Element, fromstring, tostring
from aws_sdk_route_53._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_route_53._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_route_53.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.create_vpc_association_authorization_request
    import aws_sdk_route_53.types.create_vpc_association_authorization_response


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "ConcurrentModification":
            import aws_sdk_route_53.errors.concurrent_modification

            raise aws_sdk_route_53.errors.concurrent_modification.ConcurrentModification.from_xml(
                root
            )
        case "InvalidInput":
            import aws_sdk_route_53.errors.invalid_input

            raise aws_sdk_route_53.errors.invalid_input.InvalidInput.from_xml(root)
        case "InvalidVPCId":
            import aws_sdk_route_53.errors.invalid_vpc_id

            raise aws_sdk_route_53.errors.invalid_vpc_id.InvalidVPCId.from_xml(root)
        case "NoSuchHostedZone":
            import aws_sdk_route_53.errors.no_such_hosted_zone

            raise aws_sdk_route_53.errors.no_such_hosted_zone.NoSuchHostedZone.from_xml(
                root
            )
        case "TooManyVPCAssociationAuthorizations":
            import aws_sdk_route_53.errors.too_many_vpc_association_authorizations

            raise aws_sdk_route_53.errors.too_many_vpc_association_authorizations.TooManyVPCAssociationAuthorizations.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_route_53.types.create_vpc_association_authorization_response.CreateVPCAssociationAuthorizationResponse:
    import aws_sdk_route_53.types.create_vpc_association_authorization_response

    out: aws_sdk_route_53.types.create_vpc_association_authorization_response.CreateVPCAssociationAuthorizationResponse = aws_sdk_route_53.types.create_vpc_association_authorization_response.deserialize_xml(
        fromstring(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_route_53._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_route_53._auth._sigv4.build_sigv4_auth_scheme(
                "route53", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_route_53._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_route_53.types.create_vpc_association_authorization_request.CreateVPCAssociationAuthorizationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/2013-04-01/hostedzone/{HostedZoneId}/authorizevpcassociation"
    )
    url = url.replace("{HostedZoneId}", quote(str(input_["hosted_zone_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    root = Element("CreateVPCAssociationAuthorizationRequest")
    if "vpc" in input_:
        import aws_sdk_route_53.types.vpc

        aws_sdk_route_53.types.vpc.serialize_xml(input_["vpc"], root, "VPC")
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_vpc_association_authorization(
    options: OperationOptions,
    input_: aws_sdk_route_53.types.create_vpc_association_authorization_request.CreateVPCAssociationAuthorizationRequest,
) -> tuple[
    aws_sdk_route_53.types.create_vpc_association_authorization_response.CreateVPCAssociationAuthorizationResponse,
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


async def async_create_vpc_association_authorization(
    options: AsyncOperationOptions,
    input_: aws_sdk_route_53.types.create_vpc_association_authorization_request.CreateVPCAssociationAuthorizationRequest,
) -> tuple[
    aws_sdk_route_53.types.create_vpc_association_authorization_response.CreateVPCAssociationAuthorizationResponse,
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
