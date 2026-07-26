"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#UploadDocuments``."""

from __future__ import annotations

import json
from typing import Any, cast

import zapros
from typing_extensions import Never

import capo_cloudsearch_domain._auth._signers
import capo_cloudsearch_domain._auth._sigv4
import capo_cloudsearch_domain.errors.document_service_exception
import capo_cloudsearch_domain.types.blob
import capo_cloudsearch_domain.types.content_type
import capo_cloudsearch_domain.types.document_service_warnings
import capo_cloudsearch_domain.types.upload_documents_request
import capo_cloudsearch_domain.types.upload_documents_response
from capo_cloudsearch_domain._protocol.errors import parse_error_metadata_json
from capo_cloudsearch_domain._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_cloudsearch_domain._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_cloudsearch_domain.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "DocumentServiceException":
            raise capo_cloudsearch_domain.errors.document_service_exception.DocumentServiceException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudsearch_domain.types.upload_documents_response.UploadDocumentsResponse:
    out: capo_cloudsearch_domain.types.upload_documents_response.UploadDocumentsResponse = capo_cloudsearch_domain.types.upload_documents_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudsearch_domain.types.upload_documents_response.UploadDocumentsResponse:
    out: capo_cloudsearch_domain.types.upload_documents_response.UploadDocumentsResponse = capo_cloudsearch_domain.types.upload_documents_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudsearch_domain._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_cloudsearch_domain._auth._sigv4.build_sigv4_auth_scheme(
                "cloudsearch", options.region
            )
        )
        if sigv4_config is not None:
            return capo_cloudsearch_domain._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudsearch_domain.types.upload_documents_request.UploadDocumentsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2013-01-01/documents/batch?format=sdk"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "content_type" in input_:
        headers["Content-Type"] = str(input_["content_type"])
    body = input_["documents"]
    if isinstance(body, capo_cloudsearch_domain._iter.StaticAnyIterator):
        body = cast(bytes, body.content)
    if not isinstance(body, bytes) and "content-length" not in [
        header.lower() for header in headers
    ]:
        raise ValueError("Content-Length is required for streaming input")
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def upload_documents(
    options: OperationOptions,
    input_: capo_cloudsearch_domain.types.upload_documents_request.UploadDocumentsRequest,
) -> tuple[
    capo_cloudsearch_domain.types.upload_documents_response.UploadDocumentsResponse,
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


async def async_upload_documents(
    options: AsyncOperationOptions,
    input_: capo_cloudsearch_domain.types.upload_documents_request.UploadDocumentsRequest,
) -> tuple[
    capo_cloudsearch_domain.types.upload_documents_response.UploadDocumentsResponse,
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
