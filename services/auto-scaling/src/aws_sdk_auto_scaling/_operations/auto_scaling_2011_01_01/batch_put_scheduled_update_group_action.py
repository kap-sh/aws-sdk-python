"""Generated from Smithy shape ``com.amazonaws.autoscaling#BatchPutScheduledUpdateGroupAction``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_auto_scaling._auth._signers
import aws_sdk_auto_scaling._auth._sigv4
import aws_sdk_auto_scaling.errors.already_exists_fault
import aws_sdk_auto_scaling.errors.limit_exceeded_fault
import aws_sdk_auto_scaling.errors.resource_contention_fault
import aws_sdk_auto_scaling.types.batch_put_scheduled_update_group_action_answer
import aws_sdk_auto_scaling.types.batch_put_scheduled_update_group_action_type
import aws_sdk_auto_scaling.types.failed_scheduled_update_group_action_requests
import aws_sdk_auto_scaling.types.scheduled_update_group_action_requests
from aws_sdk_auto_scaling._protocol.errors import parse_error_metadata
from aws_sdk_auto_scaling._protocol.xml import fromstring
from aws_sdk_auto_scaling._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_auto_scaling._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_auto_scaling.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AlreadyExistsFault":
            raise aws_sdk_auto_scaling.errors.already_exists_fault.AlreadyExistsFault.from_query(
                root
            )
        case "LimitExceededFault":
            raise aws_sdk_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault.from_query(
                root
            )
        case "ResourceContentionFault":
            raise aws_sdk_auto_scaling.errors.resource_contention_fault.ResourceContentionFault.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_auto_scaling.types.batch_put_scheduled_update_group_action_answer.BatchPutScheduledUpdateGroupActionAnswer:
    root = fromstring(response.read())
    result = root.find("BatchPutScheduledUpdateGroupActionResult")
    out: aws_sdk_auto_scaling.types.batch_put_scheduled_update_group_action_answer.BatchPutScheduledUpdateGroupActionAnswer = aws_sdk_auto_scaling.types.batch_put_scheduled_update_group_action_answer.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_auto_scaling.types.batch_put_scheduled_update_group_action_answer.BatchPutScheduledUpdateGroupActionAnswer:
    root = fromstring(await response.aread())
    result = root.find("BatchPutScheduledUpdateGroupActionResult")
    out: aws_sdk_auto_scaling.types.batch_put_scheduled_update_group_action_answer.BatchPutScheduledUpdateGroupActionAnswer = aws_sdk_auto_scaling.types.batch_put_scheduled_update_group_action_answer.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_auto_scaling._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_auto_scaling._auth._sigv4.build_sigv4_auth_scheme(
                "autoscaling", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_auto_scaling._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_auto_scaling.types.batch_put_scheduled_update_group_action_type.BatchPutScheduledUpdateGroupActionType,
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
    pairs.append(("Action", "BatchPutScheduledUpdateGroupAction"))
    pairs.append(("Version", "2011-01-01"))
    aws_sdk_auto_scaling.types.batch_put_scheduled_update_group_action_type.serialize_query(
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


def batch_put_scheduled_update_group_action(
    options: OperationOptions,
    input_: aws_sdk_auto_scaling.types.batch_put_scheduled_update_group_action_type.BatchPutScheduledUpdateGroupActionType,
) -> tuple[
    aws_sdk_auto_scaling.types.batch_put_scheduled_update_group_action_answer.BatchPutScheduledUpdateGroupActionAnswer,
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


async def async_batch_put_scheduled_update_group_action(
    options: AsyncOperationOptions,
    input_: aws_sdk_auto_scaling.types.batch_put_scheduled_update_group_action_type.BatchPutScheduledUpdateGroupActionType,
) -> tuple[
    aws_sdk_auto_scaling.types.batch_put_scheduled_update_group_action_answer.BatchPutScheduledUpdateGroupActionAnswer,
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
