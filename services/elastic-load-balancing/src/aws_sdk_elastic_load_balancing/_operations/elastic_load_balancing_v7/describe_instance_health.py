"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DescribeInstanceHealth``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_elastic_load_balancing._auth._signers
import aws_sdk_elastic_load_balancing._auth._sigv4
import aws_sdk_elastic_load_balancing.errors.access_point_not_found_exception
import aws_sdk_elastic_load_balancing.errors.invalid_end_point_exception
import aws_sdk_elastic_load_balancing.types.describe_end_point_state_input
import aws_sdk_elastic_load_balancing.types.describe_end_point_state_output
import aws_sdk_elastic_load_balancing.types.instance_states
import aws_sdk_elastic_load_balancing.types.instances
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


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AccessPointNotFoundException":
            raise aws_sdk_elastic_load_balancing.errors.access_point_not_found_exception.AccessPointNotFoundException.from_query(
                root
            )
        case "InvalidEndPointException":
            raise aws_sdk_elastic_load_balancing.errors.invalid_end_point_exception.InvalidEndPointException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_elastic_load_balancing.types.describe_end_point_state_output.DescribeEndPointStateOutput:
    root = fromstring(response.read())
    result = root.find("DescribeInstanceHealthResult")
    out: aws_sdk_elastic_load_balancing.types.describe_end_point_state_output.DescribeEndPointStateOutput = aws_sdk_elastic_load_balancing.types.describe_end_point_state_output.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_elastic_load_balancing.types.describe_end_point_state_output.DescribeEndPointStateOutput:
    root = fromstring(await response.aread())
    result = root.find("DescribeInstanceHealthResult")
    out: aws_sdk_elastic_load_balancing.types.describe_end_point_state_output.DescribeEndPointStateOutput = aws_sdk_elastic_load_balancing.types.describe_end_point_state_output.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_elastic_load_balancing._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_elastic_load_balancing.types.describe_end_point_state_input.DescribeEndPointStateInput,
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
    pairs.append(("Action", "DescribeInstanceHealth"))
    pairs.append(("Version", "2012-06-01"))
    import aws_sdk_elastic_load_balancing.types.describe_end_point_state_input

    aws_sdk_elastic_load_balancing.types.describe_end_point_state_input.serialize_query(
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


def describe_instance_health(
    options: OperationOptions,
    input_: aws_sdk_elastic_load_balancing.types.describe_end_point_state_input.DescribeEndPointStateInput,
) -> tuple[
    aws_sdk_elastic_load_balancing.types.describe_end_point_state_output.DescribeEndPointStateOutput,
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


async def async_describe_instance_health(
    options: AsyncOperationOptions,
    input_: aws_sdk_elastic_load_balancing.types.describe_end_point_state_input.DescribeEndPointStateInput,
) -> tuple[
    aws_sdk_elastic_load_balancing.types.describe_end_point_state_output.DescribeEndPointStateOutput,
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
