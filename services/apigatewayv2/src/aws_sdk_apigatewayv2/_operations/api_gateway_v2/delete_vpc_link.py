"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteVpcLink``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any, cast
from aws_sdk_apigatewayv2._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_apigatewayv2._rule_engine._endpoint_runtime import apply_label
import jmespath
import zapros
from urllib.parse import quote, urlencode
from aws_sdk_apigatewayv2.errors import ServiceError, UnknownServiceError
from aws_sdk_apigatewayv2._protocol.errors import parse_error_metadata_json
import json
import aws_sdk_apigatewayv2._auth._signers
import aws_sdk_apigatewayv2._auth._sigv4
from aws_sdk_apigatewayv2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
import datetime
from email.utils import parsedate_to_datetime as _parse_http_date

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.delete_vpc_link_request
    import aws_sdk_apigatewayv2.types.delete_vpc_link_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "NotFoundException":
            import aws_sdk_apigatewayv2.errors.not_found_exception

            raise aws_sdk_apigatewayv2.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_apigatewayv2.errors.too_many_requests_exception

            raise aws_sdk_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_apigatewayv2.types.delete_vpc_link_response.DeleteVpcLinkResponse:
    out: aws_sdk_apigatewayv2.types.delete_vpc_link_response.DeleteVpcLinkResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_apigatewayv2._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_apigatewayv2._auth._sigv4.build_sigv4_auth_scheme(
                "apigateway", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_apigatewayv2._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_apigatewayv2.types.delete_vpc_link_request.DeleteVpcLinkRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/v2/vpclinks/{VpcLinkId}"
    url = url.replace("{VpcLinkId}", quote(str(input["vpc_link_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "DELETE",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def delete_vpc_link(
    options: OperationOptions,
    input: aws_sdk_apigatewayv2.types.delete_vpc_link_request.DeleteVpcLinkRequest,
) -> tuple[
    aws_sdk_apigatewayv2.types.delete_vpc_link_response.DeleteVpcLinkResponse,
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


async def async_delete_vpc_link(
    options: AsyncOperationOptions,
    input: aws_sdk_apigatewayv2.types.delete_vpc_link_request.DeleteVpcLinkRequest,
) -> tuple[
    aws_sdk_apigatewayv2.types.delete_vpc_link_response.DeleteVpcLinkResponse,
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
