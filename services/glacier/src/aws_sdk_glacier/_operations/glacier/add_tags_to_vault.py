"""Generated from Smithy shape ``com.amazonaws.glacier#AddTagsToVault``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_glacier._auth._signers
import aws_sdk_glacier._auth._sigv4
from aws_sdk_glacier._protocol.errors import parse_error_metadata_json
from aws_sdk_glacier._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_glacier._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_glacier.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_glacier.types.add_tags_to_vault_input


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            import aws_sdk_glacier.errors.invalid_parameter_value_exception

            raise aws_sdk_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "LimitExceededException":
            import aws_sdk_glacier.errors.limit_exceeded_exception

            raise aws_sdk_glacier.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "MissingParameterValueException":
            import aws_sdk_glacier.errors.missing_parameter_value_exception

            raise aws_sdk_glacier.errors.missing_parameter_value_exception.MissingParameterValueException.from_json(
                data
            )
        case "NoLongerSupportedException":
            import aws_sdk_glacier.errors.no_longer_supported_exception

            raise aws_sdk_glacier.errors.no_longer_supported_exception.NoLongerSupportedException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_glacier.errors.resource_not_found_exception

            raise aws_sdk_glacier.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceUnavailableException":
            import aws_sdk_glacier.errors.service_unavailable_exception

            raise aws_sdk_glacier.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_glacier._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_glacier._auth._sigv4.build_sigv4_auth_scheme(
                "glacier", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_glacier._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_glacier.types.add_tags_to_vault_input.AddTagsToVaultInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/") + "/{accountId}/vaults/{vaultName}/tags?operation=add"
    )
    url = url.replace("{accountId}", quote(str(input_["account_id"]), safe=""))
    url = url.replace("{vaultName}", quote(str(input_["vault_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_glacier.types.add_tags_to_vault_input

    body: bytes | None = json.dumps(
        aws_sdk_glacier.types.add_tags_to_vault_input.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def add_tags_to_vault(
    options: OperationOptions,
    input_: aws_sdk_glacier.types.add_tags_to_vault_input.AddTagsToVaultInput,
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


async def async_add_tags_to_vault(
    options: AsyncOperationOptions,
    input_: aws_sdk_glacier.types.add_tags_to_vault_input.AddTagsToVaultInput,
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
