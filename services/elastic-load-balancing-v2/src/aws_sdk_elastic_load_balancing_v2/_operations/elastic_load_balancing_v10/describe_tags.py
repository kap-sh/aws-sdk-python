"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTags``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

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
    import aws_sdk_elastic_load_balancing_v2.types.describe_tags_input
    import aws_sdk_elastic_load_balancing_v2.types.describe_tags_output


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "ListenerNotFoundException":
            import aws_sdk_elastic_load_balancing_v2.errors.listener_not_found_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.listener_not_found_exception.ListenerNotFoundException.from_query(
                root
            )
        case "LoadBalancerNotFoundException":
            import aws_sdk_elastic_load_balancing_v2.errors.load_balancer_not_found_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException.from_query(
                root
            )
        case "RuleNotFoundException":
            import aws_sdk_elastic_load_balancing_v2.errors.rule_not_found_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.rule_not_found_exception.RuleNotFoundException.from_query(
                root
            )
        case "TargetGroupNotFoundException":
            import aws_sdk_elastic_load_balancing_v2.errors.target_group_not_found_exception

            raise aws_sdk_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException.from_query(
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
) -> aws_sdk_elastic_load_balancing_v2.types.describe_tags_output.DescribeTagsOutput:
    import aws_sdk_elastic_load_balancing_v2.types.describe_tags_output

    root = fromstring(response.read())
    result = root.find("DescribeTagsResult")
    out: aws_sdk_elastic_load_balancing_v2.types.describe_tags_output.DescribeTagsOutput = aws_sdk_elastic_load_balancing_v2.types.describe_tags_output.deserialize_query(
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
    input_: aws_sdk_elastic_load_balancing_v2.types.describe_tags_input.DescribeTagsInput,
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
    pairs.append(("Action", "DescribeTags"))
    pairs.append(("Version", "2015-12-01"))
    import aws_sdk_elastic_load_balancing_v2.types.describe_tags_input

    aws_sdk_elastic_load_balancing_v2.types.describe_tags_input.serialize_query(
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


def describe_tags(
    options: OperationOptions,
    input_: aws_sdk_elastic_load_balancing_v2.types.describe_tags_input.DescribeTagsInput,
) -> tuple[
    aws_sdk_elastic_load_balancing_v2.types.describe_tags_output.DescribeTagsOutput,
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


async def async_describe_tags(
    options: AsyncOperationOptions,
    input_: aws_sdk_elastic_load_balancing_v2.types.describe_tags_input.DescribeTagsInput,
) -> tuple[
    aws_sdk_elastic_load_balancing_v2.types.describe_tags_output.DescribeTagsOutput,
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
