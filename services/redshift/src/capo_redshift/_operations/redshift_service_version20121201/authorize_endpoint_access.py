"""Generated from Smithy shape ``com.amazonaws.redshift#AuthorizeEndpointAccess``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_redshift._auth._signers
import capo_redshift._auth._sigv4
import capo_redshift.errors.cluster_not_found_fault
import capo_redshift.errors.endpoint_authorization_already_exists_fault
import capo_redshift.errors.endpoint_authorizations_per_cluster_limit_exceeded_fault
import capo_redshift.errors.invalid_authorization_state_fault
import capo_redshift.errors.invalid_cluster_state_fault
import capo_redshift.errors.unsupported_operation_fault
import capo_redshift.types.authorization_status
import capo_redshift.types.authorize_endpoint_access_message
import capo_redshift.types.endpoint_authorization
import capo_redshift.types.t_stamp
import capo_redshift.types.vpc_identifier_list
from capo_redshift._protocol.errors import parse_error_metadata
from capo_redshift._protocol.xml import fromstring
from capo_redshift._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_redshift._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_redshift.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "ClusterNotFoundFault":
            raise capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault.from_query(
                root
            )
        case "EndpointAuthorizationAlreadyExistsFault":
            raise capo_redshift.errors.endpoint_authorization_already_exists_fault.EndpointAuthorizationAlreadyExistsFault.from_query(
                root
            )
        case "EndpointAuthorizationsPerClusterLimitExceededFault":
            raise capo_redshift.errors.endpoint_authorizations_per_cluster_limit_exceeded_fault.EndpointAuthorizationsPerClusterLimitExceededFault.from_query(
                root
            )
        case "InvalidAuthorizationStateFault":
            raise capo_redshift.errors.invalid_authorization_state_fault.InvalidAuthorizationStateFault.from_query(
                root
            )
        case "InvalidClusterStateFault":
            raise capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault.from_query(
                root
            )
        case "UnsupportedOperationFault":
            raise capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_redshift.types.endpoint_authorization.EndpointAuthorization:
    root = fromstring(response.read())
    result = root.find("AuthorizeEndpointAccessResult")
    out: capo_redshift.types.endpoint_authorization.EndpointAuthorization = (
        capo_redshift.types.endpoint_authorization.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_redshift.types.endpoint_authorization.EndpointAuthorization:
    root = fromstring(await response.aread())
    result = root.find("AuthorizeEndpointAccessResult")
    out: capo_redshift.types.endpoint_authorization.EndpointAuthorization = (
        capo_redshift.types.endpoint_authorization.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_redshift._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_redshift._auth._sigv4.build_sigv4_auth_scheme(
                "redshift", options.region
            )
        )
        if sigv4_config is not None:
            return capo_redshift._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_redshift.types.authorize_endpoint_access_message.AuthorizeEndpointAccessMessage,
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
    pairs.append(("Action", "AuthorizeEndpointAccess"))
    pairs.append(("Version", "2012-12-01"))
    capo_redshift.types.authorize_endpoint_access_message.serialize_query(
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


def authorize_endpoint_access(
    options: OperationOptions,
    input_: capo_redshift.types.authorize_endpoint_access_message.AuthorizeEndpointAccessMessage,
) -> tuple[
    capo_redshift.types.endpoint_authorization.EndpointAuthorization, zapros.Response
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


async def async_authorize_endpoint_access(
    options: AsyncOperationOptions,
    input_: capo_redshift.types.authorize_endpoint_access_message.AuthorizeEndpointAccessMessage,
) -> tuple[
    capo_redshift.types.endpoint_authorization.EndpointAuthorization, zapros.Response
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
