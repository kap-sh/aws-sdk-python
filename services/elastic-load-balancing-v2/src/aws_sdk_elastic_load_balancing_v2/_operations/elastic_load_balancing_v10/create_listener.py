"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CreateListener``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_elastic_load_balancing_v2._auth._signers
import aws_sdk_elastic_load_balancing_v2._auth._sigv4
import aws_sdk_elastic_load_balancing_v2.errors.alpn_policy_not_supported_exception
import aws_sdk_elastic_load_balancing_v2.errors.certificate_not_found_exception
import aws_sdk_elastic_load_balancing_v2.errors.duplicate_listener_exception
import aws_sdk_elastic_load_balancing_v2.errors.incompatible_protocols_exception
import aws_sdk_elastic_load_balancing_v2.errors.invalid_configuration_request_exception
import aws_sdk_elastic_load_balancing_v2.errors.invalid_load_balancer_action_exception
import aws_sdk_elastic_load_balancing_v2.errors.load_balancer_not_found_exception
import aws_sdk_elastic_load_balancing_v2.errors.ssl_policy_not_found_exception
import aws_sdk_elastic_load_balancing_v2.errors.target_group_association_limit_exception
import aws_sdk_elastic_load_balancing_v2.errors.target_group_not_found_exception
import aws_sdk_elastic_load_balancing_v2.errors.too_many_actions_exception
import aws_sdk_elastic_load_balancing_v2.errors.too_many_certificates_exception
import aws_sdk_elastic_load_balancing_v2.errors.too_many_listeners_exception
import aws_sdk_elastic_load_balancing_v2.errors.too_many_registrations_for_target_id_exception
import aws_sdk_elastic_load_balancing_v2.errors.too_many_tags_exception
import aws_sdk_elastic_load_balancing_v2.errors.too_many_targets_exception
import aws_sdk_elastic_load_balancing_v2.errors.too_many_unique_target_groups_per_load_balancer_exception
import aws_sdk_elastic_load_balancing_v2.errors.trust_store_not_found_exception
import aws_sdk_elastic_load_balancing_v2.errors.trust_store_not_ready_exception
import aws_sdk_elastic_load_balancing_v2.errors.unsupported_protocol_exception
import aws_sdk_elastic_load_balancing_v2.types.actions
import aws_sdk_elastic_load_balancing_v2.types.alpn_policy_name
import aws_sdk_elastic_load_balancing_v2.types.certificate_list
import aws_sdk_elastic_load_balancing_v2.types.create_listener_input
import aws_sdk_elastic_load_balancing_v2.types.create_listener_output
import aws_sdk_elastic_load_balancing_v2.types.listeners
import aws_sdk_elastic_load_balancing_v2.types.mutual_authentication_attributes
import aws_sdk_elastic_load_balancing_v2.types.protocol_enum
import aws_sdk_elastic_load_balancing_v2.types.tag_list
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


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "ALPNPolicyNotSupportedException":
            raise aws_sdk_elastic_load_balancing_v2.errors.alpn_policy_not_supported_exception.ALPNPolicyNotSupportedException.from_query(
                root
            )
        case "CertificateNotFoundException":
            raise aws_sdk_elastic_load_balancing_v2.errors.certificate_not_found_exception.CertificateNotFoundException.from_query(
                root
            )
        case "DuplicateListenerException":
            raise aws_sdk_elastic_load_balancing_v2.errors.duplicate_listener_exception.DuplicateListenerException.from_query(
                root
            )
        case "IncompatibleProtocolsException":
            raise aws_sdk_elastic_load_balancing_v2.errors.incompatible_protocols_exception.IncompatibleProtocolsException.from_query(
                root
            )
        case "InvalidConfigurationRequestException":
            raise aws_sdk_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException.from_query(
                root
            )
        case "InvalidLoadBalancerActionException":
            raise aws_sdk_elastic_load_balancing_v2.errors.invalid_load_balancer_action_exception.InvalidLoadBalancerActionException.from_query(
                root
            )
        case "LoadBalancerNotFoundException":
            raise aws_sdk_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException.from_query(
                root
            )
        case "SSLPolicyNotFoundException":
            raise aws_sdk_elastic_load_balancing_v2.errors.ssl_policy_not_found_exception.SSLPolicyNotFoundException.from_query(
                root
            )
        case "TargetGroupAssociationLimitException":
            raise aws_sdk_elastic_load_balancing_v2.errors.target_group_association_limit_exception.TargetGroupAssociationLimitException.from_query(
                root
            )
        case "TargetGroupNotFoundException":
            raise aws_sdk_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException.from_query(
                root
            )
        case "TooManyActionsException":
            raise aws_sdk_elastic_load_balancing_v2.errors.too_many_actions_exception.TooManyActionsException.from_query(
                root
            )
        case "TooManyCertificatesException":
            raise aws_sdk_elastic_load_balancing_v2.errors.too_many_certificates_exception.TooManyCertificatesException.from_query(
                root
            )
        case "TooManyListenersException":
            raise aws_sdk_elastic_load_balancing_v2.errors.too_many_listeners_exception.TooManyListenersException.from_query(
                root
            )
        case "TooManyRegistrationsForTargetIdException":
            raise aws_sdk_elastic_load_balancing_v2.errors.too_many_registrations_for_target_id_exception.TooManyRegistrationsForTargetIdException.from_query(
                root
            )
        case "TooManyTagsException":
            raise aws_sdk_elastic_load_balancing_v2.errors.too_many_tags_exception.TooManyTagsException.from_query(
                root
            )
        case "TooManyTargetsException":
            raise aws_sdk_elastic_load_balancing_v2.errors.too_many_targets_exception.TooManyTargetsException.from_query(
                root
            )
        case "TooManyUniqueTargetGroupsPerLoadBalancerException":
            raise aws_sdk_elastic_load_balancing_v2.errors.too_many_unique_target_groups_per_load_balancer_exception.TooManyUniqueTargetGroupsPerLoadBalancerException.from_query(
                root
            )
        case "TrustStoreNotFoundException":
            raise aws_sdk_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException.from_query(
                root
            )
        case "TrustStoreNotReadyException":
            raise aws_sdk_elastic_load_balancing_v2.errors.trust_store_not_ready_exception.TrustStoreNotReadyException.from_query(
                root
            )
        case "UnsupportedProtocolException":
            raise aws_sdk_elastic_load_balancing_v2.errors.unsupported_protocol_exception.UnsupportedProtocolException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_elastic_load_balancing_v2.types.create_listener_output.CreateListenerOutput
):
    root = fromstring(response.read())
    result = root.find("CreateListenerResult")
    out: aws_sdk_elastic_load_balancing_v2.types.create_listener_output.CreateListenerOutput = aws_sdk_elastic_load_balancing_v2.types.create_listener_output.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_elastic_load_balancing_v2.types.create_listener_output.CreateListenerOutput
):
    root = fromstring(await response.aread())
    result = root.find("CreateListenerResult")
    out: aws_sdk_elastic_load_balancing_v2.types.create_listener_output.CreateListenerOutput = aws_sdk_elastic_load_balancing_v2.types.create_listener_output.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_elastic_load_balancing_v2._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_elastic_load_balancing_v2.types.create_listener_input.CreateListenerInput,
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
    pairs.append(("Action", "CreateListener"))
    pairs.append(("Version", "2015-12-01"))
    import aws_sdk_elastic_load_balancing_v2.types.create_listener_input

    aws_sdk_elastic_load_balancing_v2.types.create_listener_input.serialize_query(
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


def create_listener(
    options: OperationOptions,
    input_: aws_sdk_elastic_load_balancing_v2.types.create_listener_input.CreateListenerInput,
) -> tuple[
    aws_sdk_elastic_load_balancing_v2.types.create_listener_output.CreateListenerOutput,
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


async def async_create_listener(
    options: AsyncOperationOptions,
    input_: aws_sdk_elastic_load_balancing_v2.types.create_listener_input.CreateListenerInput,
) -> tuple[
    aws_sdk_elastic_load_balancing_v2.types.create_listener_output.CreateListenerOutput,
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
