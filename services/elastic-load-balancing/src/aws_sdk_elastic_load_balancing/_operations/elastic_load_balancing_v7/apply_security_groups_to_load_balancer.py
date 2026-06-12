"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#ApplySecurityGroupsToLoadBalancer``."""

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
    import aws_sdk_elastic_load_balancing.types.apply_security_groups_to_load_balancer_input
    import aws_sdk_elastic_load_balancing.types.apply_security_groups_to_load_balancer_output


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AccessPointNotFoundException":
            import aws_sdk_elastic_load_balancing.errors.access_point_not_found_exception

            raise aws_sdk_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException.from_query(
                root
            )
        case "InvalidConfigurationRequestException":
            import aws_sdk_elastic_load_balancing.errors.invalid_configuration_request_exception

            raise aws_sdk_elastic_load_balancing.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException.from_query(
                root
            )
        case "InvalidSecurityGroupException":
            import aws_sdk_elastic_load_balancing.errors.invalid_security_group_exception

            raise aws_sdk_elastic_load_balancing.errors.invalid_security_group_exception.InvalidSecurityGroupException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_elastic_load_balancing.types.apply_security_groups_to_load_balancer_output.ApplySecurityGroupsToLoadBalancerOutput:
    import aws_sdk_elastic_load_balancing.types.apply_security_groups_to_load_balancer_output

    root = fromstring(response.read())
    result = root.find("ApplySecurityGroupsToLoadBalancerResult")
    out: aws_sdk_elastic_load_balancing.types.apply_security_groups_to_load_balancer_output.ApplySecurityGroupsToLoadBalancerOutput = aws_sdk_elastic_load_balancing.types.apply_security_groups_to_load_balancer_output.deserialize_query(
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
    input: aws_sdk_elastic_load_balancing.types.apply_security_groups_to_load_balancer_input.ApplySecurityGroupsToLoadBalancerInput,
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
    pairs.append(("Action", "ApplySecurityGroupsToLoadBalancer"))
    pairs.append(("Version", "2012-06-01"))
    import aws_sdk_elastic_load_balancing.types.apply_security_groups_to_load_balancer_input

    aws_sdk_elastic_load_balancing.types.apply_security_groups_to_load_balancer_input.serialize_query(
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


def apply_security_groups_to_load_balancer(
    options: OperationOptions,
    input: aws_sdk_elastic_load_balancing.types.apply_security_groups_to_load_balancer_input.ApplySecurityGroupsToLoadBalancerInput,
) -> tuple[
    aws_sdk_elastic_load_balancing.types.apply_security_groups_to_load_balancer_output.ApplySecurityGroupsToLoadBalancerOutput,
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


async def async_apply_security_groups_to_load_balancer(
    options: AsyncOperationOptions,
    input: aws_sdk_elastic_load_balancing.types.apply_security_groups_to_load_balancer_input.ApplySecurityGroupsToLoadBalancerInput,
) -> tuple[
    aws_sdk_elastic_load_balancing.types.apply_security_groups_to_load_balancer_output.ApplySecurityGroupsToLoadBalancerOutput,
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
