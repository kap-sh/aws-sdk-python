"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTargetGroupAttributes``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_elastic_load_balancing_v2._auth._signers
import capo_elastic_load_balancing_v2._auth._sigv4
import capo_elastic_load_balancing_v2.errors.target_group_not_found_exception
import capo_elastic_load_balancing_v2.types.describe_target_group_attributes_input
import capo_elastic_load_balancing_v2.types.describe_target_group_attributes_output
import capo_elastic_load_balancing_v2.types.target_group_attributes
from capo_elastic_load_balancing_v2._protocol.errors import parse_error_metadata
from capo_elastic_load_balancing_v2._protocol.xml import (
    fromstring,
)
from capo_elastic_load_balancing_v2._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_elastic_load_balancing_v2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_elastic_load_balancing_v2.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "TargetGroupNotFoundException":
            raise capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_elastic_load_balancing_v2.types.describe_target_group_attributes_output.DescribeTargetGroupAttributesOutput:
    root = fromstring(response.read())
    result = root.find("DescribeTargetGroupAttributesResult")
    out: capo_elastic_load_balancing_v2.types.describe_target_group_attributes_output.DescribeTargetGroupAttributesOutput = capo_elastic_load_balancing_v2.types.describe_target_group_attributes_output.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_elastic_load_balancing_v2.types.describe_target_group_attributes_output.DescribeTargetGroupAttributesOutput:
    root = fromstring(await response.aread())
    result = root.find("DescribeTargetGroupAttributesResult")
    out: capo_elastic_load_balancing_v2.types.describe_target_group_attributes_output.DescribeTargetGroupAttributesOutput = capo_elastic_load_balancing_v2.types.describe_target_group_attributes_output.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_elastic_load_balancing_v2._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_elastic_load_balancing_v2._auth._sigv4.build_sigv4_auth_scheme(
                "elasticloadbalancing", options.region
            )
        )
        if sigv4_config is not None:
            return capo_elastic_load_balancing_v2._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_elastic_load_balancing_v2.types.describe_target_group_attributes_input.DescribeTargetGroupAttributesInput,
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
    pairs.append(("Action", "DescribeTargetGroupAttributes"))
    pairs.append(("Version", "2015-12-01"))
    capo_elastic_load_balancing_v2.types.describe_target_group_attributes_input.serialize_query(
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


def describe_target_group_attributes(
    options: OperationOptions,
    input_: capo_elastic_load_balancing_v2.types.describe_target_group_attributes_input.DescribeTargetGroupAttributesInput,
) -> tuple[
    capo_elastic_load_balancing_v2.types.describe_target_group_attributes_output.DescribeTargetGroupAttributesOutput,
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


async def async_describe_target_group_attributes(
    options: AsyncOperationOptions,
    input_: capo_elastic_load_balancing_v2.types.describe_target_group_attributes_input.DescribeTargetGroupAttributesInput,
) -> tuple[
    capo_elastic_load_balancing_v2.types.describe_target_group_attributes_output.DescribeTargetGroupAttributesOutput,
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
