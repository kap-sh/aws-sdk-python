"""Generated from Smithy shape ``com.amazonaws.ssm#PutInventory``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_ssm._auth._signers
import aws_sdk_ssm._auth._sigv4
from aws_sdk_ssm._protocol.errors import parse_error_metadata_json
from aws_sdk_ssm._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_ssm._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_ssm.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.put_inventory_request
    import aws_sdk_ssm.types.put_inventory_result


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CustomSchemaCountLimitExceededException":
            import aws_sdk_ssm.errors.custom_schema_count_limit_exceeded_exception

            raise aws_sdk_ssm.errors.custom_schema_count_limit_exceeded_exception.CustomSchemaCountLimitExceededException.from_aws_json_1_1(
                data
            )
        case "InternalServerError":
            import aws_sdk_ssm.errors.internal_server_error

            raise aws_sdk_ssm.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data
            )
        case "InvalidInstanceId":
            import aws_sdk_ssm.errors.invalid_instance_id

            raise aws_sdk_ssm.errors.invalid_instance_id.InvalidInstanceId.from_aws_json_1_1(
                data
            )
        case "InvalidInventoryItemContextException":
            import aws_sdk_ssm.errors.invalid_inventory_item_context_exception

            raise aws_sdk_ssm.errors.invalid_inventory_item_context_exception.InvalidInventoryItemContextException.from_aws_json_1_1(
                data
            )
        case "InvalidItemContentException":
            import aws_sdk_ssm.errors.invalid_item_content_exception

            raise aws_sdk_ssm.errors.invalid_item_content_exception.InvalidItemContentException.from_aws_json_1_1(
                data
            )
        case "InvalidTypeNameException":
            import aws_sdk_ssm.errors.invalid_type_name_exception

            raise aws_sdk_ssm.errors.invalid_type_name_exception.InvalidTypeNameException.from_aws_json_1_1(
                data
            )
        case "ItemContentMismatchException":
            import aws_sdk_ssm.errors.item_content_mismatch_exception

            raise aws_sdk_ssm.errors.item_content_mismatch_exception.ItemContentMismatchException.from_aws_json_1_1(
                data
            )
        case "ItemSizeLimitExceededException":
            import aws_sdk_ssm.errors.item_size_limit_exceeded_exception

            raise aws_sdk_ssm.errors.item_size_limit_exceeded_exception.ItemSizeLimitExceededException.from_aws_json_1_1(
                data
            )
        case "SubTypeCountLimitExceededException":
            import aws_sdk_ssm.errors.sub_type_count_limit_exceeded_exception

            raise aws_sdk_ssm.errors.sub_type_count_limit_exceeded_exception.SubTypeCountLimitExceededException.from_aws_json_1_1(
                data
            )
        case "TotalSizeLimitExceededException":
            import aws_sdk_ssm.errors.total_size_limit_exceeded_exception

            raise aws_sdk_ssm.errors.total_size_limit_exceeded_exception.TotalSizeLimitExceededException.from_aws_json_1_1(
                data
            )
        case "UnsupportedInventoryItemContextException":
            import aws_sdk_ssm.errors.unsupported_inventory_item_context_exception

            raise aws_sdk_ssm.errors.unsupported_inventory_item_context_exception.UnsupportedInventoryItemContextException.from_aws_json_1_1(
                data
            )
        case "UnsupportedInventorySchemaVersionException":
            import aws_sdk_ssm.errors.unsupported_inventory_schema_version_exception

            raise aws_sdk_ssm.errors.unsupported_inventory_schema_version_exception.UnsupportedInventorySchemaVersionException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_ssm.types.put_inventory_result.PutInventoryResult:
    import aws_sdk_ssm.types.put_inventory_result

    out: aws_sdk_ssm.types.put_inventory_result.PutInventoryResult = (
        aws_sdk_ssm.types.put_inventory_result.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_ssm._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_ssm._auth._sigv4.build_sigv4_auth_scheme("ssm", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_ssm._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_ssm.types.put_inventory_request.PutInventoryRequest,
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
    headers["X-Amz-Target"] = "AmazonSSM.PutInventory"
    import aws_sdk_ssm.types.put_inventory_request

    body: bytes | None = json.dumps(
        aws_sdk_ssm.types.put_inventory_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def put_inventory(
    options: OperationOptions,
    input_: aws_sdk_ssm.types.put_inventory_request.PutInventoryRequest,
) -> tuple[aws_sdk_ssm.types.put_inventory_result.PutInventoryResult, zapros.Response]:
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


async def async_put_inventory(
    options: AsyncOperationOptions,
    input_: aws_sdk_ssm.types.put_inventory_request.PutInventoryRequest,
) -> tuple[aws_sdk_ssm.types.put_inventory_result.PutInventoryResult, zapros.Response]:
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
