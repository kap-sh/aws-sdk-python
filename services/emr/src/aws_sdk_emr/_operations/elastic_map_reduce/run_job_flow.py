"""Generated from Smithy shape ``com.amazonaws.emr#RunJobFlow``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_emr._auth._signers
import aws_sdk_emr._auth._sigv4
import aws_sdk_emr.errors.internal_server_error
import aws_sdk_emr.types.application_list
import aws_sdk_emr.types.auto_termination_policy
import aws_sdk_emr.types.bootstrap_action_config_list
import aws_sdk_emr.types.configuration_list
import aws_sdk_emr.types.job_flow_instances_config
import aws_sdk_emr.types.kerberos_attributes
import aws_sdk_emr.types.managed_scaling_policy
import aws_sdk_emr.types.monitoring_configuration
import aws_sdk_emr.types.new_supported_products_list
import aws_sdk_emr.types.placement_group_config_list
import aws_sdk_emr.types.repo_upgrade_on_boot
import aws_sdk_emr.types.run_job_flow_input
import aws_sdk_emr.types.run_job_flow_output
import aws_sdk_emr.types.scale_down_behavior
import aws_sdk_emr.types.step_config_list
import aws_sdk_emr.types.supported_products_list
import aws_sdk_emr.types.tag_list
from aws_sdk_emr._protocol.errors import parse_error_metadata_json
from aws_sdk_emr._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_emr._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_emr.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerError":
            raise aws_sdk_emr.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_emr.types.run_job_flow_output.RunJobFlowOutput:
    out: aws_sdk_emr.types.run_job_flow_output.RunJobFlowOutput = (
        aws_sdk_emr.types.run_job_flow_output.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_emr.types.run_job_flow_output.RunJobFlowOutput:
    out: aws_sdk_emr.types.run_job_flow_output.RunJobFlowOutput = (
        aws_sdk_emr.types.run_job_flow_output.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_emr._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_emr._auth._sigv4.build_sigv4_auth_scheme(
                "elasticmapreduce", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_emr._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_emr.types.run_job_flow_input.RunJobFlowInput,
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
    headers["X-Amz-Target"] = "ElasticMapReduce.RunJobFlow"
    import aws_sdk_emr.types.run_job_flow_input

    body: bytes | None = json.dumps(
        aws_sdk_emr.types.run_job_flow_input.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def run_job_flow(
    options: OperationOptions,
    input_: aws_sdk_emr.types.run_job_flow_input.RunJobFlowInput,
) -> tuple[aws_sdk_emr.types.run_job_flow_output.RunJobFlowOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_run_job_flow(
    options: AsyncOperationOptions,
    input_: aws_sdk_emr.types.run_job_flow_input.RunJobFlowInput,
) -> tuple[aws_sdk_emr.types.run_job_flow_output.RunJobFlowOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
