"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AddTrustStoreRevocations``."""

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
    import aws_sdk_elastic_load_balancing_v2.types.add_trust_store_revocations_input
    import aws_sdk_elastic_load_balancing_v2.types.add_trust_store_revocations_output


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InvalidRevocationContentException":
            import aws_sdk_elastic_load_balancing_v2.errors.invalid_revocation_content_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.invalid_revocation_content_exception.InvalidRevocationContentException.from_query(
                root
            )
        case "RevocationContentNotFoundException":
            import aws_sdk_elastic_load_balancing_v2.errors.revocation_content_not_found_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.revocation_content_not_found_exception.RevocationContentNotFoundException.from_query(
                root
            )
        case "TooManyTrustStoreRevocationEntriesException":
            import aws_sdk_elastic_load_balancing_v2.errors.too_many_trust_store_revocation_entries_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.too_many_trust_store_revocation_entries_exception.TooManyTrustStoreRevocationEntriesException.from_query(
                root
            )
        case "TrustStoreNotFoundException":
            import aws_sdk_elastic_load_balancing_v2.errors.trust_store_not_found_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_elastic_load_balancing_v2.types.add_trust_store_revocations_output.AddTrustStoreRevocationsOutput:
    import aws_sdk_elastic_load_balancing_v2.types.add_trust_store_revocations_output

    root = fromstring(response.read())
    result = root.find("AddTrustStoreRevocationsResult")
    out: aws_sdk_elastic_load_balancing_v2.types.add_trust_store_revocations_output.AddTrustStoreRevocationsOutput = aws_sdk_elastic_load_balancing_v2.types.add_trust_store_revocations_output.deserialize_query(
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
    input_: aws_sdk_elastic_load_balancing_v2.types.add_trust_store_revocations_input.AddTrustStoreRevocationsInput,
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
    pairs.append(("Action", "AddTrustStoreRevocations"))
    pairs.append(("Version", "2015-12-01"))
    import aws_sdk_elastic_load_balancing_v2.types.add_trust_store_revocations_input

    aws_sdk_elastic_load_balancing_v2.types.add_trust_store_revocations_input.serialize_query(
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


def add_trust_store_revocations(
    options: OperationOptions,
    input_: aws_sdk_elastic_load_balancing_v2.types.add_trust_store_revocations_input.AddTrustStoreRevocationsInput,
) -> tuple[
    aws_sdk_elastic_load_balancing_v2.types.add_trust_store_revocations_output.AddTrustStoreRevocationsOutput,
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


async def async_add_trust_store_revocations(
    options: AsyncOperationOptions,
    input_: aws_sdk_elastic_load_balancing_v2.types.add_trust_store_revocations_input.AddTrustStoreRevocationsInput,
) -> tuple[
    aws_sdk_elastic_load_balancing_v2.types.add_trust_store_revocations_output.AddTrustStoreRevocationsOutput,
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
