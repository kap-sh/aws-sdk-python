"""Generated from Smithy shape ``com.amazonaws.neptunedata#ListLoaderJobs``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_neptunedata._auth._signers
import capo_neptunedata._auth._sigv4
import capo_neptunedata.errors.bad_request_exception
import capo_neptunedata.errors.bulk_load_id_not_found_exception
import capo_neptunedata.errors.client_timeout_exception
import capo_neptunedata.errors.constraint_violation_exception
import capo_neptunedata.errors.illegal_argument_exception
import capo_neptunedata.errors.internal_failure_exception
import capo_neptunedata.errors.invalid_argument_exception
import capo_neptunedata.errors.invalid_parameter_exception
import capo_neptunedata.errors.load_url_access_denied_exception
import capo_neptunedata.errors.preconditions_failed_exception
import capo_neptunedata.errors.too_many_requests_exception
import capo_neptunedata.errors.unsupported_operation_exception
import capo_neptunedata.types.list_loader_jobs_input
import capo_neptunedata.types.list_loader_jobs_output
import capo_neptunedata.types.loader_id_result
from capo_neptunedata._protocol.errors import parse_error_metadata_json
from capo_neptunedata._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_neptunedata._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_neptunedata.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise capo_neptunedata.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "BulkLoadIdNotFoundException":
            raise capo_neptunedata.errors.bulk_load_id_not_found_exception.BulkLoadIdNotFoundException.from_json(
                data
            )
        case "ClientTimeoutException":
            raise capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException.from_json(
                data
            )
        case "ConstraintViolationException":
            raise capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException.from_json(
                data
            )
        case "IllegalArgumentException":
            raise capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException.from_json(
                data
            )
        case "InternalFailureException":
            raise capo_neptunedata.errors.internal_failure_exception.InternalFailureException.from_json(
                data
            )
        case "InvalidArgumentException":
            raise capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException.from_json(
                data
            )
        case "InvalidParameterException":
            raise capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case "LoadUrlAccessDeniedException":
            raise capo_neptunedata.errors.load_url_access_denied_exception.LoadUrlAccessDeniedException.from_json(
                data
            )
        case "PreconditionsFailedException":
            raise capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException.from_json(
                data
            )
        case "TooManyRequestsException":
            raise capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case "UnsupportedOperationException":
            raise capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_neptunedata.types.list_loader_jobs_output.ListLoaderJobsOutput:
    out: capo_neptunedata.types.list_loader_jobs_output.ListLoaderJobsOutput = (
        capo_neptunedata.types.list_loader_jobs_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_neptunedata.types.list_loader_jobs_output.ListLoaderJobsOutput:
    out: capo_neptunedata.types.list_loader_jobs_output.ListLoaderJobsOutput = (
        capo_neptunedata.types.list_loader_jobs_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_neptunedata._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_neptunedata._auth._sigv4.build_sigv4_auth_scheme(
                "neptune-db", options.region
            )
        )
        if sigv4_config is not None:
            return capo_neptunedata._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_neptunedata.types.list_loader_jobs_input.ListLoaderJobsInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/loader"
    params: dict[str, str] = {}
    if "limit" in input_:
        params["limit"] = str(input_["limit"])
    if "include_queued_loads" in input_:
        params["includeQueuedLoads"] = str(input_["include_queued_loads"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_loader_jobs(
    options: OperationOptions,
    input_: capo_neptunedata.types.list_loader_jobs_input.ListLoaderJobsInput,
) -> tuple[
    capo_neptunedata.types.list_loader_jobs_output.ListLoaderJobsOutput, zapros.Response
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


async def async_list_loader_jobs(
    options: AsyncOperationOptions,
    input_: capo_neptunedata.types.list_loader_jobs_input.ListLoaderJobsInput,
) -> tuple[
    capo_neptunedata.types.list_loader_jobs_output.ListLoaderJobsOutput, zapros.Response
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
