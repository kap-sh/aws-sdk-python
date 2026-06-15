"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateContinuousDeploymentPolicy``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_cloudfront._auth._signers
import aws_sdk_cloudfront._auth._sigv4
from aws_sdk_cloudfront._protocol.errors import parse_error_metadata
from aws_sdk_cloudfront._protocol.xml import Element, fromstring, tostring
from aws_sdk_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloudfront._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudfront.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.create_continuous_deployment_policy_request
    import aws_sdk_cloudfront.types.create_continuous_deployment_policy_result


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AccessDenied":
            import aws_sdk_cloudfront.errors.access_denied

            raise aws_sdk_cloudfront.errors.access_denied.AccessDenied.from_xml(root)
        case "ContinuousDeploymentPolicyAlreadyExists":
            import aws_sdk_cloudfront.errors.continuous_deployment_policy_already_exists

            raise aws_sdk_cloudfront.errors.continuous_deployment_policy_already_exists.ContinuousDeploymentPolicyAlreadyExists.from_xml(
                root
            )
        case "InconsistentQuantities":
            import aws_sdk_cloudfront.errors.inconsistent_quantities

            raise aws_sdk_cloudfront.errors.inconsistent_quantities.InconsistentQuantities.from_xml(
                root
            )
        case "InvalidArgument":
            import aws_sdk_cloudfront.errors.invalid_argument

            raise aws_sdk_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                root
            )
        case "StagingDistributionInUse":
            import aws_sdk_cloudfront.errors.staging_distribution_in_use

            raise aws_sdk_cloudfront.errors.staging_distribution_in_use.StagingDistributionInUse.from_xml(
                root
            )
        case "TooManyContinuousDeploymentPolicies":
            import aws_sdk_cloudfront.errors.too_many_continuous_deployment_policies

            raise aws_sdk_cloudfront.errors.too_many_continuous_deployment_policies.TooManyContinuousDeploymentPolicies.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cloudfront.types.create_continuous_deployment_policy_result.CreateContinuousDeploymentPolicyResult:
    import aws_sdk_cloudfront.types.continuous_deployment_policy

    out: aws_sdk_cloudfront.types.create_continuous_deployment_policy_result.CreateContinuousDeploymentPolicyResult = {
        "continuous_deployment_policy": aws_sdk_cloudfront.types.continuous_deployment_policy.deserialize_xml(
            fromstring(response.read())
        )
    }  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = str(response.headers["Location"])
    if "ETag" in response.headers:
        out["e_tag"] = str(response.headers["ETag"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloudfront._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cloudfront._auth._sigv4.build_sigv4_auth_scheme(
                "cloudfront", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cloudfront._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_cloudfront.types.create_continuous_deployment_policy_request.CreateContinuousDeploymentPolicyRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/continuous-deployment-policy"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "continuous_deployment_policy_config" in input_:
        import aws_sdk_cloudfront.types.continuous_deployment_policy_config

        payload_root = Element("_")
        aws_sdk_cloudfront.types.continuous_deployment_policy_config.serialize_xml(
            input_["continuous_deployment_policy_config"],
            payload_root,
            "ContinuousDeploymentPolicyConfig",
        )
        body: bytes | None = tostring(payload_root[0])
        headers["content-type"] = "application/xml"
    else:
        body = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_continuous_deployment_policy(
    options: OperationOptions,
    input_: aws_sdk_cloudfront.types.create_continuous_deployment_policy_request.CreateContinuousDeploymentPolicyRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_continuous_deployment_policy_result.CreateContinuousDeploymentPolicyResult,
    zapros.Response,
]:
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


async def async_create_continuous_deployment_policy(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudfront.types.create_continuous_deployment_policy_request.CreateContinuousDeploymentPolicyRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_continuous_deployment_policy_result.CreateContinuousDeploymentPolicyResult,
    zapros.Response,
]:
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
