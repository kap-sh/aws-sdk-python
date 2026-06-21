"""Generated from Smithy shape ``com.amazonaws.s3control#CreateStorageLensGroup``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_s3_control._auth._signers
import aws_sdk_s3_control._auth._sigv4
import aws_sdk_s3_control.types.create_storage_lens_group_request
import aws_sdk_s3_control.types.storage_lens_group
import aws_sdk_s3_control.types.tag_list
from aws_sdk_s3_control._protocol.errors import parse_error_metadata
from aws_sdk_s3_control._protocol.xml import Element, fromstring, tostring
from aws_sdk_s3_control._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3_control._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_s3_control.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_s3_control._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_s3_control._auth._sigv4.build_sigv4_auth_scheme(
                "s3", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_s3_control._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_s3_control.types.create_storage_lens_group_request.CreateStorageLensGroupRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
            AccountId=input_.get("account_id"),
            RequiresAccountId=True,
            OutpostId=options.outpost_id,
            Bucket=options.bucket,
            AccessPointName=options.access_point_name,
            UseArnRegion=options.use_arn_region,
            ResourceArn=options.resource_arn,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v20180820/storagelensgroup"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "account_id" in input_:
        headers["x-amz-account-id"] = str(input_["account_id"])
    root = Element("CreateStorageLensGroupRequest")
    if "storage_lens_group" in input_:
        import aws_sdk_s3_control.types.storage_lens_group

        aws_sdk_s3_control.types.storage_lens_group.serialize_xml(
            input_["storage_lens_group"], root, "StorageLensGroup"
        )
    if "tags" in input_:
        import aws_sdk_s3_control.types.tag_list

        aws_sdk_s3_control.types.tag_list.serialize_xml(input_["tags"], root, "Tags")
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_storage_lens_group(
    options: OperationOptions,
    input_: aws_sdk_s3_control.types.create_storage_lens_group_request.CreateStorageLensGroupRequest,
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


async def async_create_storage_lens_group(
    options: AsyncOperationOptions,
    input_: aws_sdk_s3_control.types.create_storage_lens_group_request.CreateStorageLensGroupRequest,
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
