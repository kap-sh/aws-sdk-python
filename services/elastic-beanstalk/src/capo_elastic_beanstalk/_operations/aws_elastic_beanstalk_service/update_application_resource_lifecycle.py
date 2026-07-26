"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#UpdateApplicationResourceLifecycle``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_elastic_beanstalk._auth._signers
import capo_elastic_beanstalk._auth._sigv4
import capo_elastic_beanstalk.errors.insufficient_privileges_exception
import capo_elastic_beanstalk.types.application_resource_lifecycle_config
import capo_elastic_beanstalk.types.application_resource_lifecycle_description_message
import capo_elastic_beanstalk.types.update_application_resource_lifecycle_message
from capo_elastic_beanstalk._protocol.errors import parse_error_metadata
from capo_elastic_beanstalk._protocol.xml import (
    fromstring,
)
from capo_elastic_beanstalk._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_elastic_beanstalk._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_elastic_beanstalk.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InsufficientPrivilegesException":
            raise capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_elastic_beanstalk.types.application_resource_lifecycle_description_message.ApplicationResourceLifecycleDescriptionMessage:
    root = fromstring(response.read())
    result = root.find("UpdateApplicationResourceLifecycleResult")
    out: capo_elastic_beanstalk.types.application_resource_lifecycle_description_message.ApplicationResourceLifecycleDescriptionMessage = capo_elastic_beanstalk.types.application_resource_lifecycle_description_message.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_elastic_beanstalk.types.application_resource_lifecycle_description_message.ApplicationResourceLifecycleDescriptionMessage:
    root = fromstring(await response.aread())
    result = root.find("UpdateApplicationResourceLifecycleResult")
    out: capo_elastic_beanstalk.types.application_resource_lifecycle_description_message.ApplicationResourceLifecycleDescriptionMessage = capo_elastic_beanstalk.types.application_resource_lifecycle_description_message.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_elastic_beanstalk._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_elastic_beanstalk._auth._sigv4.build_sigv4_auth_scheme(
                "elasticbeanstalk", options.region
            )
        )
        if sigv4_config is not None:
            return capo_elastic_beanstalk._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_elastic_beanstalk.types.update_application_resource_lifecycle_message.UpdateApplicationResourceLifecycleMessage,
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
    pairs.append(("Action", "UpdateApplicationResourceLifecycle"))
    pairs.append(("Version", "2010-12-01"))
    capo_elastic_beanstalk.types.update_application_resource_lifecycle_message.serialize_query(
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


def update_application_resource_lifecycle(
    options: OperationOptions,
    input_: capo_elastic_beanstalk.types.update_application_resource_lifecycle_message.UpdateApplicationResourceLifecycleMessage,
) -> tuple[
    capo_elastic_beanstalk.types.application_resource_lifecycle_description_message.ApplicationResourceLifecycleDescriptionMessage,
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


async def async_update_application_resource_lifecycle(
    options: AsyncOperationOptions,
    input_: capo_elastic_beanstalk.types.update_application_resource_lifecycle_message.UpdateApplicationResourceLifecycleMessage,
) -> tuple[
    capo_elastic_beanstalk.types.application_resource_lifecycle_description_message.ApplicationResourceLifecycleDescriptionMessage,
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
