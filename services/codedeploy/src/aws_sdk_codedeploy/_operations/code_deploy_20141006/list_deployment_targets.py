"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListDeploymentTargets``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_codedeploy._auth._signers
import aws_sdk_codedeploy._auth._sigv4
from aws_sdk_codedeploy._protocol.errors import parse_error_metadata_json
from aws_sdk_codedeploy._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_codedeploy._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codedeploy.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.list_deployment_targets_input
    import aws_sdk_codedeploy.types.list_deployment_targets_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "DeploymentDoesNotExistException":
            import aws_sdk_codedeploy.errors.deployment_does_not_exist_exception

            raise aws_sdk_codedeploy.errors.deployment_does_not_exist_exception.DeploymentDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "DeploymentIdRequiredException":
            import aws_sdk_codedeploy.errors.deployment_id_required_exception

            raise aws_sdk_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException.from_aws_json_1_1(
                data
            )
        case "DeploymentNotStartedException":
            import aws_sdk_codedeploy.errors.deployment_not_started_exception

            raise aws_sdk_codedeploy.errors.deployment_not_started_exception.DeploymentNotStartedException.from_aws_json_1_1(
                data
            )
        case "InvalidDeploymentIdException":
            import aws_sdk_codedeploy.errors.invalid_deployment_id_exception

            raise aws_sdk_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException.from_aws_json_1_1(
                data
            )
        case "InvalidDeploymentInstanceTypeException":
            import aws_sdk_codedeploy.errors.invalid_deployment_instance_type_exception

            raise aws_sdk_codedeploy.errors.invalid_deployment_instance_type_exception.InvalidDeploymentInstanceTypeException.from_aws_json_1_1(
                data
            )
        case "InvalidInstanceStatusException":
            import aws_sdk_codedeploy.errors.invalid_instance_status_exception

            raise aws_sdk_codedeploy.errors.invalid_instance_status_exception.InvalidInstanceStatusException.from_aws_json_1_1(
                data
            )
        case "InvalidInstanceTypeException":
            import aws_sdk_codedeploy.errors.invalid_instance_type_exception

            raise aws_sdk_codedeploy.errors.invalid_instance_type_exception.InvalidInstanceTypeException.from_aws_json_1_1(
                data
            )
        case "InvalidNextTokenException":
            import aws_sdk_codedeploy.errors.invalid_next_token_exception

            raise aws_sdk_codedeploy.errors.invalid_next_token_exception.InvalidNextTokenException.from_aws_json_1_1(
                data
            )
        case "InvalidTargetFilterNameException":
            import aws_sdk_codedeploy.errors.invalid_target_filter_name_exception

            raise aws_sdk_codedeploy.errors.invalid_target_filter_name_exception.InvalidTargetFilterNameException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> (
    aws_sdk_codedeploy.types.list_deployment_targets_output.ListDeploymentTargetsOutput
):
    import aws_sdk_codedeploy.types.list_deployment_targets_output

    out: aws_sdk_codedeploy.types.list_deployment_targets_output.ListDeploymentTargetsOutput = aws_sdk_codedeploy.types.list_deployment_targets_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_codedeploy._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_codedeploy._auth._sigv4.build_sigv4_auth_scheme(
                "codedeploy", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_codedeploy._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_codedeploy.types.list_deployment_targets_input.ListDeploymentTargetsInput,
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
    headers["X-Amz-Target"] = "CodeDeploy_20141006.ListDeploymentTargets"
    import aws_sdk_codedeploy.types.list_deployment_targets_input

    body: bytes | None = json.dumps(
        aws_sdk_codedeploy.types.list_deployment_targets_input.serialize_aws_json_1_1(
            input
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
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


def list_deployment_targets(
    options: OperationOptions,
    input: aws_sdk_codedeploy.types.list_deployment_targets_input.ListDeploymentTargetsInput,
) -> tuple[
    aws_sdk_codedeploy.types.list_deployment_targets_output.ListDeploymentTargetsOutput,
    zapros.Response,
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


async def async_list_deployment_targets(
    options: AsyncOperationOptions,
    input: aws_sdk_codedeploy.types.list_deployment_targets_input.ListDeploymentTargetsInput,
) -> tuple[
    aws_sdk_codedeploy.types.list_deployment_targets_output.ListDeploymentTargetsOutput,
    zapros.Response,
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
