"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#AssociateEnvironmentOperationsRole``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_elastic_beanstalk._auth._signers
import aws_sdk_elastic_beanstalk._auth._sigv4
import aws_sdk_elastic_beanstalk.errors.insufficient_privileges_exception
import aws_sdk_elastic_beanstalk.types.associate_environment_operations_role_message
from aws_sdk_elastic_beanstalk._protocol.errors import parse_error_metadata
from aws_sdk_elastic_beanstalk._protocol.xml import (
    fromstring,
)
from aws_sdk_elastic_beanstalk._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_elastic_beanstalk._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_elastic_beanstalk.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InsufficientPrivilegesException":
            raise aws_sdk_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_elastic_beanstalk._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_elastic_beanstalk._auth._sigv4.build_sigv4_auth_scheme(
                "elasticbeanstalk", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_elastic_beanstalk._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_elastic_beanstalk.types.associate_environment_operations_role_message.AssociateEnvironmentOperationsRoleMessage,
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
    pairs.append(("Action", "AssociateEnvironmentOperationsRole"))
    pairs.append(("Version", "2010-12-01"))
    aws_sdk_elastic_beanstalk.types.associate_environment_operations_role_message.serialize_query(
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


def associate_environment_operations_role(
    options: OperationOptions,
    input_: aws_sdk_elastic_beanstalk.types.associate_environment_operations_role_message.AssociateEnvironmentOperationsRoleMessage,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_associate_environment_operations_role(
    options: AsyncOperationOptions,
    input_: aws_sdk_elastic_beanstalk.types.associate_environment_operations_role_message.AssociateEnvironmentOperationsRoleMessage,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
