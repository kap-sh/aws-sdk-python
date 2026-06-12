"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyCapacityReservation``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never
from urllib.parse import urlencode

import zapros

import aws_sdk_elastic_load_balancing_v2._auth._signers
import aws_sdk_elastic_load_balancing_v2._auth._sigv4
from aws_sdk_elastic_load_balancing_v2._protocol.errors import parse_error_metadata
from aws_sdk_elastic_load_balancing_v2._protocol.xml import (
    fromstring,
)
from aws_sdk_elastic_load_balancing_v2._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_elastic_load_balancing_v2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_elastic_load_balancing_v2.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.modify_capacity_reservation_input
    import aws_sdk_elastic_load_balancing_v2.types.modify_capacity_reservation_output


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "CapacityDecreaseRequestsLimitExceededException":
            import aws_sdk_elastic_load_balancing_v2.errors.capacity_decrease_requests_limit_exceeded_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.capacity_decrease_requests_limit_exceeded_exception.CapacityDecreaseRequestsLimitExceededException.from_query(
                root
            )
        case "CapacityReservationPendingException":
            import aws_sdk_elastic_load_balancing_v2.errors.capacity_reservation_pending_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.capacity_reservation_pending_exception.CapacityReservationPendingException.from_query(
                root
            )
        case "CapacityUnitsLimitExceededException":
            import aws_sdk_elastic_load_balancing_v2.errors.capacity_units_limit_exceeded_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.capacity_units_limit_exceeded_exception.CapacityUnitsLimitExceededException.from_query(
                root
            )
        case "InsufficientCapacityException":
            import aws_sdk_elastic_load_balancing_v2.errors.insufficient_capacity_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.insufficient_capacity_exception.InsufficientCapacityException.from_query(
                root
            )
        case "InvalidConfigurationRequestException":
            import aws_sdk_elastic_load_balancing_v2.errors.invalid_configuration_request_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException.from_query(
                root
            )
        case "LoadBalancerNotFoundException":
            import aws_sdk_elastic_load_balancing_v2.errors.load_balancer_not_found_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException.from_query(
                root
            )
        case "OperationNotPermittedException":
            import aws_sdk_elastic_load_balancing_v2.errors.operation_not_permitted_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.operation_not_permitted_exception.OperationNotPermittedException.from_query(
                root
            )
        case "PriorRequestNotCompleteException":
            import aws_sdk_elastic_load_balancing_v2.errors.prior_request_not_complete_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.prior_request_not_complete_exception.PriorRequestNotCompleteException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_elastic_load_balancing_v2.types.modify_capacity_reservation_output.ModifyCapacityReservationOutput:
    import aws_sdk_elastic_load_balancing_v2.types.modify_capacity_reservation_output

    root = fromstring(response.read())
    result = root.find("ModifyCapacityReservationResult")
    out: aws_sdk_elastic_load_balancing_v2.types.modify_capacity_reservation_output.ModifyCapacityReservationOutput = aws_sdk_elastic_load_balancing_v2.types.modify_capacity_reservation_output.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_elastic_load_balancing_v2._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_elastic_load_balancing_v2._auth._sigv4.build_sigv4_auth_scheme(
                "elasticloadbalancing", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_elastic_load_balancing_v2._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_elastic_load_balancing_v2.types.modify_capacity_reservation_input.ModifyCapacityReservationInput,
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
    pairs.append(("Action", "ModifyCapacityReservation"))
    pairs.append(("Version", "2015-12-01"))
    import aws_sdk_elastic_load_balancing_v2.types.modify_capacity_reservation_input

    aws_sdk_elastic_load_balancing_v2.types.modify_capacity_reservation_input.serialize_query(
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


def modify_capacity_reservation(
    options: OperationOptions,
    input: aws_sdk_elastic_load_balancing_v2.types.modify_capacity_reservation_input.ModifyCapacityReservationInput,
) -> tuple[
    aws_sdk_elastic_load_balancing_v2.types.modify_capacity_reservation_output.ModifyCapacityReservationOutput,
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


async def async_modify_capacity_reservation(
    options: AsyncOperationOptions,
    input: aws_sdk_elastic_load_balancing_v2.types.modify_capacity_reservation_input.ModifyCapacityReservationInput,
) -> tuple[
    aws_sdk_elastic_load_balancing_v2.types.modify_capacity_reservation_output.ModifyCapacityReservationOutput,
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
