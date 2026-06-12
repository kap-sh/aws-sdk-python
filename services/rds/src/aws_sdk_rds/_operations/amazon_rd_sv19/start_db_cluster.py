"""Generated from Smithy shape ``com.amazonaws.rds#StartDBCluster``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never
from urllib.parse import urlencode

import zapros

import aws_sdk_rds._auth._signers
import aws_sdk_rds._auth._sigv4
from aws_sdk_rds._protocol.errors import parse_error_metadata
from aws_sdk_rds._protocol.xml import fromstring
from aws_sdk_rds._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_rds._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_rds.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_rds.types.start_db_cluster_message
    import aws_sdk_rds.types.start_db_cluster_result


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "DBClusterNotFoundFault":
            import aws_sdk_rds.errors.db_cluster_not_found_fault

            raise aws_sdk_rds.errors.db_cluster_not_found_fault.DBClusterNotFoundFault.from_query(
                root
            )
        case "InvalidDBClusterStateFault":
            import aws_sdk_rds.errors.invalid_db_cluster_state_fault

            raise aws_sdk_rds.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault.from_query(
                root
            )
        case "InvalidDBInstanceStateFault":
            import aws_sdk_rds.errors.invalid_db_instance_state_fault

            raise aws_sdk_rds.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault.from_query(
                root
            )
        case "InvalidDBShardGroupStateFault":
            import aws_sdk_rds.errors.invalid_db_shard_group_state_fault

            raise aws_sdk_rds.errors.invalid_db_shard_group_state_fault.InvalidDBShardGroupStateFault.from_query(
                root
            )
        case "KMSKeyNotAccessibleFault":
            import aws_sdk_rds.errors.kms_key_not_accessible_fault

            raise aws_sdk_rds.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault.from_query(
                root
            )
        case "VpcEncryptionControlViolationException":
            import aws_sdk_rds.errors.vpc_encryption_control_violation_exception

            raise aws_sdk_rds.errors.vpc_encryption_control_violation_exception.VpcEncryptionControlViolationException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_rds.types.start_db_cluster_result.StartDBClusterResult:
    import aws_sdk_rds.types.start_db_cluster_result

    root = fromstring(response.read())
    result = root.find("StartDBClusterResult")
    out: aws_sdk_rds.types.start_db_cluster_result.StartDBClusterResult = (
        aws_sdk_rds.types.start_db_cluster_result.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_rds._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
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
    input: aws_sdk_rds.types.start_db_cluster_message.StartDBClusterMessage,
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
    pairs.append(("Action", "StartDBCluster"))
    pairs.append(("Version", "2014-10-31"))
    import aws_sdk_rds.types.start_db_cluster_message

    aws_sdk_rds.types.start_db_cluster_message.serialize_query(input, pairs, "")
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


def start_db_cluster(
    options: OperationOptions,
    input: aws_sdk_rds.types.start_db_cluster_message.StartDBClusterMessage,
) -> tuple[
    aws_sdk_rds.types.start_db_cluster_result.StartDBClusterResult, zapros.Response
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_start_db_cluster(
    options: AsyncOperationOptions,
    input: aws_sdk_rds.types.start_db_cluster_message.StartDBClusterMessage,
) -> tuple[
    aws_sdk_rds.types.start_db_cluster_result.StartDBClusterResult, zapros.Response
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
