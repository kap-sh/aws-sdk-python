"""Generated from Smithy shape ``com.amazonaws.elasticache#RemoveTagsFromResource``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never
from urllib.parse import urlencode

import zapros

import aws_sdk_elasticache._auth._signers
import aws_sdk_elasticache._auth._sigv4
from aws_sdk_elasticache._protocol.errors import parse_error_metadata
from aws_sdk_elasticache._protocol.xml import fromstring
from aws_sdk_elasticache._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_elasticache._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_elasticache.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.remove_tags_from_resource_message
    import aws_sdk_elasticache.types.tag_list_message


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "CacheClusterNotFoundFault":
            import aws_sdk_elasticache.errors.cache_cluster_not_found_fault

            raise aws_sdk_elasticache.errors.cache_cluster_not_found_fault.CacheClusterNotFoundFault.from_query(
                root
            )
        case "CacheParameterGroupNotFoundFault":
            import aws_sdk_elasticache.errors.cache_parameter_group_not_found_fault

            raise aws_sdk_elasticache.errors.cache_parameter_group_not_found_fault.CacheParameterGroupNotFoundFault.from_query(
                root
            )
        case "CacheSecurityGroupNotFoundFault":
            import aws_sdk_elasticache.errors.cache_security_group_not_found_fault

            raise aws_sdk_elasticache.errors.cache_security_group_not_found_fault.CacheSecurityGroupNotFoundFault.from_query(
                root
            )
        case "CacheSubnetGroupNotFoundFault":
            import aws_sdk_elasticache.errors.cache_subnet_group_not_found_fault

            raise aws_sdk_elasticache.errors.cache_subnet_group_not_found_fault.CacheSubnetGroupNotFoundFault.from_query(
                root
            )
        case "InvalidARNFault":
            import aws_sdk_elasticache.errors.invalid_arn_fault

            raise aws_sdk_elasticache.errors.invalid_arn_fault.InvalidARNFault.from_query(
                root
            )
        case "InvalidReplicationGroupStateFault":
            import aws_sdk_elasticache.errors.invalid_replication_group_state_fault

            raise aws_sdk_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault.from_query(
                root
            )
        case "InvalidServerlessCacheSnapshotStateFault":
            import aws_sdk_elasticache.errors.invalid_serverless_cache_snapshot_state_fault

            raise aws_sdk_elasticache.errors.invalid_serverless_cache_snapshot_state_fault.InvalidServerlessCacheSnapshotStateFault.from_query(
                root
            )
        case "InvalidServerlessCacheStateFault":
            import aws_sdk_elasticache.errors.invalid_serverless_cache_state_fault

            raise aws_sdk_elasticache.errors.invalid_serverless_cache_state_fault.InvalidServerlessCacheStateFault.from_query(
                root
            )
        case "ReplicationGroupNotFoundFault":
            import aws_sdk_elasticache.errors.replication_group_not_found_fault

            raise aws_sdk_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault.from_query(
                root
            )
        case "ReservedCacheNodeNotFoundFault":
            import aws_sdk_elasticache.errors.reserved_cache_node_not_found_fault

            raise aws_sdk_elasticache.errors.reserved_cache_node_not_found_fault.ReservedCacheNodeNotFoundFault.from_query(
                root
            )
        case "ServerlessCacheNotFoundFault":
            import aws_sdk_elasticache.errors.serverless_cache_not_found_fault

            raise aws_sdk_elasticache.errors.serverless_cache_not_found_fault.ServerlessCacheNotFoundFault.from_query(
                root
            )
        case "ServerlessCacheSnapshotNotFoundFault":
            import aws_sdk_elasticache.errors.serverless_cache_snapshot_not_found_fault

            raise aws_sdk_elasticache.errors.serverless_cache_snapshot_not_found_fault.ServerlessCacheSnapshotNotFoundFault.from_query(
                root
            )
        case "SnapshotNotFoundFault":
            import aws_sdk_elasticache.errors.snapshot_not_found_fault

            raise aws_sdk_elasticache.errors.snapshot_not_found_fault.SnapshotNotFoundFault.from_query(
                root
            )
        case "TagNotFoundFault":
            import aws_sdk_elasticache.errors.tag_not_found_fault

            raise aws_sdk_elasticache.errors.tag_not_found_fault.TagNotFoundFault.from_query(
                root
            )
        case "UserGroupNotFoundFault":
            import aws_sdk_elasticache.errors.user_group_not_found_fault

            raise aws_sdk_elasticache.errors.user_group_not_found_fault.UserGroupNotFoundFault.from_query(
                root
            )
        case "UserNotFoundFault":
            import aws_sdk_elasticache.errors.user_not_found_fault

            raise aws_sdk_elasticache.errors.user_not_found_fault.UserNotFoundFault.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_elasticache.types.tag_list_message.TagListMessage:
    import aws_sdk_elasticache.types.tag_list_message

    root = fromstring(response.read())
    result = root.find("RemoveTagsFromResourceResult")
    out: aws_sdk_elasticache.types.tag_list_message.TagListMessage = (
        aws_sdk_elasticache.types.tag_list_message.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_elasticache._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_elasticache._auth._sigv4.build_sigv4_auth_scheme(
                "elasticache", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_elasticache._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_elasticache.types.remove_tags_from_resource_message.RemoveTagsFromResourceMessage,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "RemoveTagsFromResource"))
    pairs.append(("Version", "2015-02-02"))
    import aws_sdk_elasticache.types.remove_tags_from_resource_message

    aws_sdk_elasticache.types.remove_tags_from_resource_message.serialize_query(
        input, pairs, ""
    )
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def remove_tags_from_resource(
    options: OperationOptions,
    input: aws_sdk_elasticache.types.remove_tags_from_resource_message.RemoveTagsFromResourceMessage,
) -> tuple[aws_sdk_elasticache.types.tag_list_message.TagListMessage, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_remove_tags_from_resource(
    options: AsyncOperationOptions,
    input: aws_sdk_elasticache.types.remove_tags_from_resource_message.RemoveTagsFromResourceMessage,
) -> tuple[aws_sdk_elasticache.types.tag_list_message.TagListMessage, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
