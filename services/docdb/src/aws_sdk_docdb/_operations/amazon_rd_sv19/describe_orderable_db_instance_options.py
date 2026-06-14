"""Generated from Smithy shape ``com.amazonaws.docdb#DescribeOrderableDBInstanceOptions``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never
from urllib.parse import urlencode

import zapros

import aws_sdk_docdb._auth._signers
import aws_sdk_docdb._auth._sigv4
from aws_sdk_docdb._protocol.errors import parse_error_metadata
from aws_sdk_docdb._protocol.xml import fromstring
from aws_sdk_docdb._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_docdb._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_docdb.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_docdb.types.describe_orderable_db_instance_options_message
    import aws_sdk_docdb.types.orderable_db_instance_options_message


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_docdb.types.orderable_db_instance_options_message.OrderableDBInstanceOptionsMessage:
    import aws_sdk_docdb.types.orderable_db_instance_options_message

    root = fromstring(response.read())
    result = root.find("DescribeOrderableDBInstanceOptionsResult")
    out: aws_sdk_docdb.types.orderable_db_instance_options_message.OrderableDBInstanceOptionsMessage = aws_sdk_docdb.types.orderable_db_instance_options_message.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_docdb._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_docdb._auth._sigv4.build_sigv4_auth_scheme("rds", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_docdb._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_docdb.types.describe_orderable_db_instance_options_message.DescribeOrderableDBInstanceOptionsMessage,
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
    pairs.append(("Action", "DescribeOrderableDBInstanceOptions"))
    pairs.append(("Version", "2014-10-31"))
    import aws_sdk_docdb.types.describe_orderable_db_instance_options_message

    aws_sdk_docdb.types.describe_orderable_db_instance_options_message.serialize_query(
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


def describe_orderable_db_instance_options(
    options: OperationOptions,
    input_: aws_sdk_docdb.types.describe_orderable_db_instance_options_message.DescribeOrderableDBInstanceOptionsMessage,
) -> tuple[
    aws_sdk_docdb.types.orderable_db_instance_options_message.OrderableDBInstanceOptionsMessage,
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


async def async_describe_orderable_db_instance_options(
    options: AsyncOperationOptions,
    input_: aws_sdk_docdb.types.describe_orderable_db_instance_options_message.DescribeOrderableDBInstanceOptionsMessage,
) -> tuple[
    aws_sdk_docdb.types.orderable_db_instance_options_message.OrderableDBInstanceOptionsMessage,
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
