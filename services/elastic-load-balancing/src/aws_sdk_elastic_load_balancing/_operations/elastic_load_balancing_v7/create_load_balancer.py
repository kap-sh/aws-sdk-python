"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#CreateLoadBalancer``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never
from urllib.parse import urlencode

import zapros

import aws_sdk_elastic_load_balancing._auth._signers
import aws_sdk_elastic_load_balancing._auth._sigv4
from aws_sdk_elastic_load_balancing._protocol.errors import parse_error_metadata
from aws_sdk_elastic_load_balancing._protocol.xml import (
    fromstring,
)
from aws_sdk_elastic_load_balancing._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_elastic_load_balancing._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_elastic_load_balancing.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.create_access_point_input
    import aws_sdk_elastic_load_balancing.types.create_access_point_output


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "CertificateNotFoundException":
            import aws_sdk_elastic_load_balancing.errors.certificate_not_found_exception

            raise aws_sdk_elastic_load_balancing.errors.certificate_not_found_exception.CertificateNotFoundException.from_query(
                root
            )
        case "DuplicateAccessPointNameException":
            import aws_sdk_elastic_load_balancing.errors.duplicate_access_point_name_exception

            raise aws_sdk_elastic_load_balancing.errors.duplicate_access_point_name_exception.DuplicateAccessPointNameException.from_query(
                root
            )
        case "DuplicateTagKeysException":
            import aws_sdk_elastic_load_balancing.errors.duplicate_tag_keys_exception

            raise aws_sdk_elastic_load_balancing.errors.duplicate_tag_keys_exception.DuplicateTagKeysException.from_query(
                root
            )
        case "InvalidConfigurationRequestException":
            import aws_sdk_elastic_load_balancing.errors.invalid_configuration_request_exception

            raise aws_sdk_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException.from_query(
                root
            )
        case "InvalidSchemeException":
            import aws_sdk_elastic_load_balancing.errors.invalid_scheme_exception

            raise aws_sdk_elastic_load_balancing.errors.invalid_scheme_exception.InvalidSchemeException.from_query(
                root
            )
        case "InvalidSecurityGroupException":
            import aws_sdk_elastic_load_balancing.errors.invalid_security_group_exception

            raise aws_sdk_elastic_load_balancing.errors.invalid_security_group_exception.InvalidSecurityGroupException.from_query(
                root
            )
        case "InvalidSubnetException":
            import aws_sdk_elastic_load_balancing.errors.invalid_subnet_exception

            raise aws_sdk_elastic_load_balancing.errors.invalid_subnet_exception.InvalidSubnetException.from_query(
                root
            )
        case "OperationNotPermittedException":
            import aws_sdk_elastic_load_balancing.errors.operation_not_permitted_exception

            raise aws_sdk_elastic_load_balancing.errors.operation_not_permitted_exception.OperationNotPermittedException.from_query(
                root
            )
        case "SubnetNotFoundException":
            import aws_sdk_elastic_load_balancing.errors.subnet_not_found_exception

            raise aws_sdk_elastic_load_balancing.errors.subnet_not_found_exception.SubnetNotFoundException.from_query(
                root
            )
        case "TooManyAccessPointsException":
            import aws_sdk_elastic_load_balancing.errors.too_many_access_points_exception

            raise aws_sdk_elastic_load_balancing.errors.too_many_access_points_exception.TooManyAccessPointsException.from_query(
                root
            )
        case "TooManyTagsException":
            import aws_sdk_elastic_load_balancing.errors.too_many_tags_exception

            raise aws_sdk_elastic_load_balancing.errors.too_many_tags_exception.TooManyTagsException.from_query(
                root
            )
        case "UnsupportedProtocolException":
            import aws_sdk_elastic_load_balancing.errors.unsupported_protocol_exception

            raise aws_sdk_elastic_load_balancing.errors.unsupported_protocol_exception.UnsupportedProtocolException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_elastic_load_balancing.types.create_access_point_output.CreateAccessPointOutput:
    import aws_sdk_elastic_load_balancing.types.create_access_point_output

    root = fromstring(response.read())
    result = root.find("CreateLoadBalancerResult")
    out: aws_sdk_elastic_load_balancing.types.create_access_point_output.CreateAccessPointOutput = aws_sdk_elastic_load_balancing.types.create_access_point_output.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_elastic_load_balancing._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_elastic_load_balancing._auth._sigv4.build_sigv4_auth_scheme(
                "elasticloadbalancing", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_elastic_load_balancing._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_elastic_load_balancing.types.create_access_point_input.CreateAccessPointInput,
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
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "CreateLoadBalancer"))
    pairs.append(("Version", "2012-06-01"))
    import aws_sdk_elastic_load_balancing.types.create_access_point_input

    aws_sdk_elastic_load_balancing.types.create_access_point_input.serialize_query(
        input_, pairs, ""
    )
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_load_balancer(
    options: OperationOptions,
    input_: aws_sdk_elastic_load_balancing.types.create_access_point_input.CreateAccessPointInput,
) -> tuple[
    aws_sdk_elastic_load_balancing.types.create_access_point_output.CreateAccessPointOutput,
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


async def async_create_load_balancer(
    options: AsyncOperationOptions,
    input_: aws_sdk_elastic_load_balancing.types.create_access_point_input.CreateAccessPointInput,
) -> tuple[
    aws_sdk_elastic_load_balancing.types.create_access_point_output.CreateAccessPointOutput,
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
