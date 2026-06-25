"""Generated from Smithy shape ``com.amazonaws.rds#AddTagsToResource``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_rds._auth._signers
import aws_sdk_rds._auth._sigv4
import aws_sdk_rds.errors.blue_green_deployment_not_found_fault
import aws_sdk_rds.errors.db_cluster_not_found_fault
import aws_sdk_rds.errors.db_instance_not_found_fault
import aws_sdk_rds.errors.db_proxy_endpoint_not_found_fault
import aws_sdk_rds.errors.db_proxy_not_found_fault
import aws_sdk_rds.errors.db_proxy_target_group_not_found_fault
import aws_sdk_rds.errors.db_shard_group_not_found_fault
import aws_sdk_rds.errors.db_snapshot_not_found_fault
import aws_sdk_rds.errors.db_snapshot_tenant_database_not_found_fault
import aws_sdk_rds.errors.integration_not_found_fault
import aws_sdk_rds.errors.invalid_db_cluster_endpoint_state_fault
import aws_sdk_rds.errors.invalid_db_cluster_state_fault
import aws_sdk_rds.errors.invalid_db_instance_state_fault
import aws_sdk_rds.errors.tenant_database_not_found_fault
import aws_sdk_rds.types.add_tags_to_resource_message
import aws_sdk_rds.types.tag_list
from aws_sdk_rds._protocol.errors import parse_error_metadata
from aws_sdk_rds._protocol.xml import fromstring
from aws_sdk_rds._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_rds._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_rds.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "BlueGreenDeploymentNotFoundFault":
            raise aws_sdk_rds.errors.blue_green_deployment_not_found_fault.BlueGreenDeploymentNotFoundFault.from_query(
                root
            )
        case "DBClusterNotFoundFault":
            raise aws_sdk_rds.errors.db_cluster_not_found_fault.DBClusterNotFoundFault.from_query(
                root
            )
        case "DBInstanceNotFoundFault":
            raise aws_sdk_rds.errors.db_instance_not_found_fault.DBInstanceNotFoundFault.from_query(
                root
            )
        case "DBProxyEndpointNotFoundFault":
            raise aws_sdk_rds.errors.db_proxy_endpoint_not_found_fault.DBProxyEndpointNotFoundFault.from_query(
                root
            )
        case "DBProxyNotFoundFault":
            raise aws_sdk_rds.errors.db_proxy_not_found_fault.DBProxyNotFoundFault.from_query(
                root
            )
        case "DBProxyTargetGroupNotFoundFault":
            raise aws_sdk_rds.errors.db_proxy_target_group_not_found_fault.DBProxyTargetGroupNotFoundFault.from_query(
                root
            )
        case "DBShardGroupNotFoundFault":
            raise aws_sdk_rds.errors.db_shard_group_not_found_fault.DBShardGroupNotFoundFault.from_query(
                root
            )
        case "DBSnapshotNotFoundFault":
            raise aws_sdk_rds.errors.db_snapshot_not_found_fault.DBSnapshotNotFoundFault.from_query(
                root
            )
        case "DBSnapshotTenantDatabaseNotFoundFault":
            raise aws_sdk_rds.errors.db_snapshot_tenant_database_not_found_fault.DBSnapshotTenantDatabaseNotFoundFault.from_query(
                root
            )
        case "IntegrationNotFoundFault":
            raise aws_sdk_rds.errors.integration_not_found_fault.IntegrationNotFoundFault.from_query(
                root
            )
        case "InvalidDBClusterEndpointStateFault":
            raise aws_sdk_rds.errors.invalid_db_cluster_endpoint_state_fault.InvalidDBClusterEndpointStateFault.from_query(
                root
            )
        case "InvalidDBClusterStateFault":
            raise aws_sdk_rds.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault.from_query(
                root
            )
        case "InvalidDBInstanceStateFault":
            raise aws_sdk_rds.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault.from_query(
                root
            )
        case "TenantDatabaseNotFoundFault":
            raise aws_sdk_rds.errors.tenant_database_not_found_fault.TenantDatabaseNotFoundFault.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_rds._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_rds._auth._sigv4.build_sigv4_auth_scheme("rds", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_rds._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_rds.types.add_tags_to_resource_message.AddTagsToResourceMessage,
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
    pairs.append(("Action", "AddTagsToResource"))
    pairs.append(("Version", "2014-10-31"))
    aws_sdk_rds.types.add_tags_to_resource_message.serialize_query(input_, pairs, "")
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def add_tags_to_resource(
    options: OperationOptions,
    input_: aws_sdk_rds.types.add_tags_to_resource_message.AddTagsToResourceMessage,
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


async def async_add_tags_to_resource(
    options: AsyncOperationOptions,
    input_: aws_sdk_rds.types.add_tags_to_resource_message.AddTagsToResourceMessage,
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
