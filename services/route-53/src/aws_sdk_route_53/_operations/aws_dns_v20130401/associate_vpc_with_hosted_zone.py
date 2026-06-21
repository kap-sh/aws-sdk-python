"""Generated from Smithy shape ``com.amazonaws.route53#AssociateVPCWithHostedZone``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_route_53._auth._signers
import aws_sdk_route_53._auth._sigv4
import aws_sdk_route_53.errors.conflicting_domain_exists
import aws_sdk_route_53.errors.invalid_input
import aws_sdk_route_53.errors.invalid_vpc_id
import aws_sdk_route_53.errors.limits_exceeded
import aws_sdk_route_53.errors.no_such_hosted_zone
import aws_sdk_route_53.errors.not_authorized_exception
import aws_sdk_route_53.errors.prior_request_not_complete
import aws_sdk_route_53.errors.public_zone_vpc_association
import aws_sdk_route_53.types.associate_vpc_with_hosted_zone_request
import aws_sdk_route_53.types.associate_vpc_with_hosted_zone_response
import aws_sdk_route_53.types.change_info
import aws_sdk_route_53.types.vpc
from aws_sdk_route_53._protocol.errors import parse_error_metadata
from aws_sdk_route_53._protocol.xml import Element, SubElement, fromstring, tostring
from aws_sdk_route_53._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_route_53._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_route_53.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "ConflictingDomainExists":
            raise aws_sdk_route_53.errors.conflicting_domain_exists.ConflictingDomainExists.from_xml(
                root
            )
        case "InvalidInput":
            raise aws_sdk_route_53.errors.invalid_input.InvalidInput.from_xml(root)
        case "InvalidVPCId":
            raise aws_sdk_route_53.errors.invalid_vpc_id.InvalidVPCId.from_xml(root)
        case "LimitsExceeded":
            raise aws_sdk_route_53.errors.limits_exceeded.LimitsExceeded.from_xml(root)
        case "NoSuchHostedZone":
            raise aws_sdk_route_53.errors.no_such_hosted_zone.NoSuchHostedZone.from_xml(
                root
            )
        case "NotAuthorizedException":
            raise aws_sdk_route_53.errors.not_authorized_exception.NotAuthorizedException.from_xml(
                root
            )
        case "PriorRequestNotComplete":
            raise aws_sdk_route_53.errors.prior_request_not_complete.PriorRequestNotComplete.from_xml(
                root
            )
        case "PublicZoneVPCAssociation":
            raise aws_sdk_route_53.errors.public_zone_vpc_association.PublicZoneVPCAssociation.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_route_53.types.associate_vpc_with_hosted_zone_response.AssociateVPCWithHostedZoneResponse:
    out: aws_sdk_route_53.types.associate_vpc_with_hosted_zone_response.AssociateVPCWithHostedZoneResponse = aws_sdk_route_53.types.associate_vpc_with_hosted_zone_response.deserialize_xml(
        fromstring(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_route_53.types.associate_vpc_with_hosted_zone_response.AssociateVPCWithHostedZoneResponse:
    out: aws_sdk_route_53.types.associate_vpc_with_hosted_zone_response.AssociateVPCWithHostedZoneResponse = aws_sdk_route_53.types.associate_vpc_with_hosted_zone_response.deserialize_xml(
        fromstring(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_route_53._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_route_53.types.associate_vpc_with_hosted_zone_request.AssociateVPCWithHostedZoneRequest,
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
        endpoint.url.rstrip("/") + "/2013-04-01/hostedzone/{HostedZoneId}/associatevpc"
    )
    url = url.replace("{HostedZoneId}", quote(str(input_["hosted_zone_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    root = Element("AssociateVPCWithHostedZoneRequest")
    if "vpc" in input_:
        import aws_sdk_route_53.types.vpc

        aws_sdk_route_53.types.vpc.serialize_xml(input_["vpc"], root, "VPC")
    if "comment" in input_:
        SubElement(root, "Comment").text = str(input_["comment"])
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def associate_vpc_with_hosted_zone(
    options: OperationOptions,
    input_: aws_sdk_route_53.types.associate_vpc_with_hosted_zone_request.AssociateVPCWithHostedZoneRequest,
) -> tuple[
    aws_sdk_route_53.types.associate_vpc_with_hosted_zone_response.AssociateVPCWithHostedZoneResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_associate_vpc_with_hosted_zone(
    options: AsyncOperationOptions,
    input_: aws_sdk_route_53.types.associate_vpc_with_hosted_zone_request.AssociateVPCWithHostedZoneRequest,
) -> tuple[
    aws_sdk_route_53.types.associate_vpc_with_hosted_zone_response.AssociateVPCWithHostedZoneResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
