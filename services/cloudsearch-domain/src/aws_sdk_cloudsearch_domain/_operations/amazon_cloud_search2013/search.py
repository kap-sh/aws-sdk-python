"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#Search``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_cloudsearch_domain._auth._signers
import aws_sdk_cloudsearch_domain._auth._sigv4
from aws_sdk_cloudsearch_domain._protocol.errors import parse_error_metadata_json
from aws_sdk_cloudsearch_domain._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_cloudsearch_domain._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudsearch_domain.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.search_request
    import aws_sdk_cloudsearch_domain.types.search_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "SearchException":
            import aws_sdk_cloudsearch_domain.errors.search_exception

            raise aws_sdk_cloudsearch_domain.errors.search_exception.SearchException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cloudsearch_domain.types.search_response.SearchResponse:
    import aws_sdk_cloudsearch_domain.types.search_response

    out: aws_sdk_cloudsearch_domain.types.search_response.SearchResponse = (
        aws_sdk_cloudsearch_domain.types.search_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloudsearch_domain._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cloudsearch_domain._auth._sigv4.build_sigv4_auth_scheme(
                "cloudsearch", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cloudsearch_domain._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_cloudsearch_domain.types.search_request.SearchRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2013-01-01/search?format=sdk&pretty=true"
    params: dict[str, str] = {}
    if "cursor" in input_:
        params["cursor"] = str(input_["cursor"])
    if "expr" in input_:
        params["expr"] = str(input_["expr"])
    if "facet" in input_:
        params["facet"] = str(input_["facet"])
    if "filter_query" in input_:
        params["fq"] = str(input_["filter_query"])
    if "highlight" in input_:
        params["highlight"] = str(input_["highlight"])
    params["partial"] = str(input_.get("partial", False))
    if "query" in input_:
        params["q"] = str(input_["query"])
    if "query_options" in input_:
        params["q.options"] = str(input_["query_options"])
    if "query_parser" in input_:
        params["q.parser"] = str(input_["query_parser"])
    if "return" in input_:
        params["return"] = str(input_["return"])
    params["size"] = str(input_.get("size", 0))
    if "sort" in input_:
        params["sort"] = str(input_["sort"])
    params["start"] = str(input_.get("start", 0))
    if "stats" in input_:
        params["stats"] = str(input_["stats"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def search(
    options: OperationOptions,
    input_: aws_sdk_cloudsearch_domain.types.search_request.SearchRequest,
) -> tuple[
    aws_sdk_cloudsearch_domain.types.search_response.SearchResponse, zapros.Response
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


async def async_search(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudsearch_domain.types.search_request.SearchRequest,
) -> tuple[
    aws_sdk_cloudsearch_domain.types.search_response.SearchResponse, zapros.Response
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
