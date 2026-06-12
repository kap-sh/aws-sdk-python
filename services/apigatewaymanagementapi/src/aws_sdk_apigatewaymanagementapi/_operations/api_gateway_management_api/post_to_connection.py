"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#PostToConnection``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_apigatewaymanagementapi._auth._signers
import aws_sdk_apigatewaymanagementapi._auth._sigv4
from aws_sdk_apigatewaymanagementapi._protocol.errors import parse_error_metadata_json
from aws_sdk_apigatewaymanagementapi._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_apigatewaymanagementapi._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_apigatewaymanagementapi.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_apigatewaymanagementapi.types.post_to_connection_request


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ForbiddenException":
            import aws_sdk_apigatewaymanagementapi.errors.forbidden_exception

            raise aws_sdk_apigatewaymanagementapi.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "GoneException":
            import aws_sdk_apigatewaymanagementapi.errors.gone_exception

            raise aws_sdk_apigatewaymanagementapi.errors.gone_exception.GoneException.from_json(
                data
            )
        case "LimitExceededException":
            import aws_sdk_apigatewaymanagementapi.errors.limit_exceeded_exception

            raise aws_sdk_apigatewaymanagementapi.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "PayloadTooLargeException":
            import aws_sdk_apigatewaymanagementapi.errors.payload_too_large_exception

            raise aws_sdk_apigatewaymanagementapi.errors.payload_too_large_exception.PayloadTooLargeException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_apigatewaymanagementapi._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_apigatewaymanagementapi._auth._sigv4.build_sigv4_auth_scheme(
                "execute-api", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_apigatewaymanagementapi._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_apigatewaymanagementapi.types.post_to_connection_request.PostToConnectionRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/@connections/{ConnectionId}"
    url = url.replace("{ConnectionId}", quote(str(input["connection_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "data" in input:
        import aws_sdk_apigatewaymanagementapi.types.data

        body: bytes | None = json.dumps(
            aws_sdk_apigatewaymanagementapi.types.data.serialize_json(input["data"])
        ).encode()
        headers["content-type"] = "application/json"
    else:
        body = b""
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


def post_to_connection(
    options: OperationOptions,
    input: aws_sdk_apigatewaymanagementapi.types.post_to_connection_request.PostToConnectionRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_post_to_connection(
    options: AsyncOperationOptions,
    input: aws_sdk_apigatewaymanagementapi.types.post_to_connection_request.PostToConnectionRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
