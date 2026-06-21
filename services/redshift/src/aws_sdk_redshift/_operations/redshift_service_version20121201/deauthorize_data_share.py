"""Generated from Smithy shape ``com.amazonaws.redshift#DeauthorizeDataShare``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_redshift._auth._signers
import aws_sdk_redshift._auth._sigv4
import aws_sdk_redshift.errors.invalid_data_share_fault
import aws_sdk_redshift.types.data_share
import aws_sdk_redshift.types.data_share_association_list
import aws_sdk_redshift.types.data_share_type
import aws_sdk_redshift.types.deauthorize_data_share_message
from aws_sdk_redshift._protocol.errors import parse_error_metadata
from aws_sdk_redshift._protocol.xml import fromstring
from aws_sdk_redshift._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_redshift._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_redshift.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InvalidDataShareFault":
            raise aws_sdk_redshift.errors.invalid_data_share_fault.InvalidDataShareFault.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_redshift.types.data_share.DataShare:
    root = fromstring(response.read())
    result = root.find("DeauthorizeDataShareResult")
    out: aws_sdk_redshift.types.data_share.DataShare = (
        aws_sdk_redshift.types.data_share.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_redshift.types.data_share.DataShare:
    root = fromstring(await response.aread())
    result = root.find("DeauthorizeDataShareResult")
    out: aws_sdk_redshift.types.data_share.DataShare = (
        aws_sdk_redshift.types.data_share.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_redshift._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_redshift.types.deauthorize_data_share_message.DeauthorizeDataShareMessage,
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
    pairs.append(("Action", "DeauthorizeDataShare"))
    pairs.append(("Version", "2012-12-01"))
    import aws_sdk_redshift.types.deauthorize_data_share_message

    aws_sdk_redshift.types.deauthorize_data_share_message.serialize_query(
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


def deauthorize_data_share(
    options: OperationOptions,
    input_: aws_sdk_redshift.types.deauthorize_data_share_message.DeauthorizeDataShareMessage,
) -> tuple[aws_sdk_redshift.types.data_share.DataShare, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_deauthorize_data_share(
    options: AsyncOperationOptions,
    input_: aws_sdk_redshift.types.deauthorize_data_share_message.DeauthorizeDataShareMessage,
) -> tuple[aws_sdk_redshift.types.data_share.DataShare, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
