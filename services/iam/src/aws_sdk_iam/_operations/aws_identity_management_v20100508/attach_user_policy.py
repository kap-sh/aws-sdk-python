"""Generated from Smithy shape ``com.amazonaws.iam#AttachUserPolicy``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never
from urllib.parse import urlencode

import zapros

import aws_sdk_iam._auth._signers
import aws_sdk_iam._auth._sigv4
from aws_sdk_iam._protocol.errors import parse_error_metadata
from aws_sdk_iam._protocol.xml import fromstring
from aws_sdk_iam._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_iam.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.attach_user_policy_request


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InvalidInputException":
            import aws_sdk_iam.errors.invalid_input_exception

            raise aws_sdk_iam.errors.invalid_input_exception.InvalidInputException.from_query(
                root
            )
        case "LimitExceededException":
            import aws_sdk_iam.errors.limit_exceeded_exception

            raise aws_sdk_iam.errors.limit_exceeded_exception.LimitExceededException.from_query(
                root
            )
        case "NoSuchEntityException":
            import aws_sdk_iam.errors.no_such_entity_exception

            raise aws_sdk_iam.errors.no_such_entity_exception.NoSuchEntityException.from_query(
                root
            )
        case "PolicyNotAttachableException":
            import aws_sdk_iam.errors.policy_not_attachable_exception

            raise aws_sdk_iam.errors.policy_not_attachable_exception.PolicyNotAttachableException.from_query(
                root
            )
        case "ServiceFailureException":
            import aws_sdk_iam.errors.service_failure_exception

            raise aws_sdk_iam.errors.service_failure_exception.ServiceFailureException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_iam._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_iam._auth._sigv4.build_sigv4_auth_scheme("iam", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_iam._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_iam.types.attach_user_policy_request.AttachUserPolicyRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "AttachUserPolicy"))
    pairs.append(("Version", "2010-05-08"))
    import aws_sdk_iam.types.attach_user_policy_request

    aws_sdk_iam.types.attach_user_policy_request.serialize_query(input_, pairs, "")
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def attach_user_policy(
    options: OperationOptions,
    input_: aws_sdk_iam.types.attach_user_policy_request.AttachUserPolicyRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return None, response
    except BaseException:
        response.close()
        raise


async def async_attach_user_policy(
    options: AsyncOperationOptions,
    input_: aws_sdk_iam.types.attach_user_policy_request.AttachUserPolicyRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return None, response
    except BaseException:
        await response.aclose()
        raise
