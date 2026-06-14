"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeReservedNodeOfferings``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never
from urllib.parse import urlencode

import zapros

import aws_sdk_redshift._auth._signers
import aws_sdk_redshift._auth._sigv4
from aws_sdk_redshift._protocol.errors import parse_error_metadata
from aws_sdk_redshift._protocol.xml import fromstring
from aws_sdk_redshift._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_redshift._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_redshift.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.describe_reserved_node_offerings_message
    import aws_sdk_redshift.types.reserved_node_offerings_message


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "DependentServiceUnavailableFault":
            import aws_sdk_redshift.errors.dependent_service_unavailable_fault

            raise aws_sdk_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault.from_query(
                root
            )
        case "ReservedNodeOfferingNotFoundFault":
            import aws_sdk_redshift.errors.reserved_node_offering_not_found_fault

            raise aws_sdk_redshift.errors.reserved_node_offering_not_found_fault.ReservedNodeOfferingNotFoundFault.from_query(
                root
            )
        case "UnsupportedOperationFault":
            import aws_sdk_redshift.errors.unsupported_operation_fault

            raise aws_sdk_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> (
    aws_sdk_redshift.types.reserved_node_offerings_message.ReservedNodeOfferingsMessage
):
    import aws_sdk_redshift.types.reserved_node_offerings_message

    root = fromstring(response.read())
    result = root.find("DescribeReservedNodeOfferingsResult")
    out: aws_sdk_redshift.types.reserved_node_offerings_message.ReservedNodeOfferingsMessage = aws_sdk_redshift.types.reserved_node_offerings_message.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_redshift._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_redshift._auth._sigv4.build_sigv4_auth_scheme(
                "redshift", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_redshift._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_redshift.types.describe_reserved_node_offerings_message.DescribeReservedNodeOfferingsMessage,
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
    pairs.append(("Action", "DescribeReservedNodeOfferings"))
    pairs.append(("Version", "2012-12-01"))
    import aws_sdk_redshift.types.describe_reserved_node_offerings_message

    aws_sdk_redshift.types.describe_reserved_node_offerings_message.serialize_query(
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


def describe_reserved_node_offerings(
    options: OperationOptions,
    input_: aws_sdk_redshift.types.describe_reserved_node_offerings_message.DescribeReservedNodeOfferingsMessage,
) -> tuple[
    aws_sdk_redshift.types.reserved_node_offerings_message.ReservedNodeOfferingsMessage,
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


async def async_describe_reserved_node_offerings(
    options: AsyncOperationOptions,
    input_: aws_sdk_redshift.types.describe_reserved_node_offerings_message.DescribeReservedNodeOfferingsMessage,
) -> tuple[
    aws_sdk_redshift.types.reserved_node_offerings_message.ReservedNodeOfferingsMessage,
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
