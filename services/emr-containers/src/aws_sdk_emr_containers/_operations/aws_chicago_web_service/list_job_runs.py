"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ListJobRuns``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_emr_containers._auth._signers
import aws_sdk_emr_containers._auth._sigv4
from aws_sdk_emr_containers._protocol.errors import parse_error_metadata_json
from aws_sdk_emr_containers._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_emr_containers._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_emr_containers.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.list_job_runs_request
    import aws_sdk_emr_containers.types.list_job_runs_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            import aws_sdk_emr_containers.errors.internal_server_exception

            raise aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_emr_containers.errors.validation_exception

            raise aws_sdk_emr_containers.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_emr_containers.types.list_job_runs_response.ListJobRunsResponse:
    import aws_sdk_emr_containers.types.list_job_runs_response

    out: aws_sdk_emr_containers.types.list_job_runs_response.ListJobRunsResponse = (
        aws_sdk_emr_containers.types.list_job_runs_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_emr_containers._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_emr_containers._auth._sigv4.build_sigv4_auth_scheme(
                "emr-containers", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_emr_containers._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_emr_containers.types.list_job_runs_request.ListJobRunsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/virtualclusters/{virtualClusterId}/jobruns"
    url = url.replace(
        "{virtualClusterId}", quote(str(input_["virtual_cluster_id"]), safe="")
    )
    params: dict[str, str] = {}
    if "created_before" in input_:
        params["createdBefore"] = str(input_["created_before"])
    if "created_after" in input_:
        params["createdAfter"] = str(input_["created_after"])
    if "name" in input_:
        params["name"] = str(input_["name"])
    if "states" in input_:
        params["states"] = str(input_["states"])
    if "max_results" in input_:
        params["maxResults"] = str(input_["max_results"])
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_job_runs(
    options: OperationOptions,
    input_: aws_sdk_emr_containers.types.list_job_runs_request.ListJobRunsRequest,
) -> tuple[
    aws_sdk_emr_containers.types.list_job_runs_response.ListJobRunsResponse,
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


async def async_list_job_runs(
    options: AsyncOperationOptions,
    input_: aws_sdk_emr_containers.types.list_job_runs_request.ListJobRunsRequest,
) -> tuple[
    aws_sdk_emr_containers.types.list_job_runs_response.ListJobRunsResponse,
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
