"""Generated from Smithy shape ``com.amazonaws.ssm#PutParameter``."""

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
    import aws_sdk_ssm.types.put_parameter_request
    import aws_sdk_ssm.types.put_parameter_result


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "HierarchyLevelLimitExceededException":
            import aws_sdk_ssm.errors.hierarchy_level_limit_exceeded_exception

            raise aws_sdk_ssm.errors.hierarchy_level_limit_exceeded_exception.HierarchyLevelLimitExceededException.from_aws_json_1_1(
                data
            )
        case "HierarchyTypeMismatchException":
            import aws_sdk_ssm.errors.hierarchy_type_mismatch_exception

            raise aws_sdk_ssm.errors.hierarchy_type_mismatch_exception.HierarchyTypeMismatchException.from_aws_json_1_1(
                data
            )
        case "IncompatiblePolicyException":
            import aws_sdk_ssm.errors.incompatible_policy_exception

            raise aws_sdk_ssm.errors.incompatible_policy_exception.IncompatiblePolicyException.from_aws_json_1_1(
                data
            )
        case "InternalServerError":
            import aws_sdk_ssm.errors.internal_server_error

            raise aws_sdk_ssm.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data
            )
        case "InvalidAllowedPatternException":
            import aws_sdk_ssm.errors.invalid_allowed_pattern_exception

            raise aws_sdk_ssm.errors.invalid_allowed_pattern_exception.InvalidAllowedPatternException.from_aws_json_1_1(
                data
            )
        case "InvalidKeyId":
            import aws_sdk_ssm.errors.invalid_key_id

            raise aws_sdk_ssm.errors.invalid_key_id.InvalidKeyId.from_aws_json_1_1(data)
        case "InvalidPolicyAttributeException":
            import aws_sdk_ssm.errors.invalid_policy_attribute_exception

            raise aws_sdk_ssm.errors.invalid_policy_attribute_exception.InvalidPolicyAttributeException.from_aws_json_1_1(
                data
            )
        case "InvalidPolicyTypeException":
            import aws_sdk_ssm.errors.invalid_policy_type_exception

            raise aws_sdk_ssm.errors.invalid_policy_type_exception.InvalidPolicyTypeException.from_aws_json_1_1(
                data
            )
        case "ParameterAlreadyExists":
            import aws_sdk_ssm.errors.parameter_already_exists

            raise aws_sdk_ssm.errors.parameter_already_exists.ParameterAlreadyExists.from_aws_json_1_1(
                data
            )
        case "ParameterLimitExceeded":
            import aws_sdk_ssm.errors.parameter_limit_exceeded

            raise aws_sdk_ssm.errors.parameter_limit_exceeded.ParameterLimitExceeded.from_aws_json_1_1(
                data
            )
        case "ParameterMaxVersionLimitExceeded":
            import aws_sdk_ssm.errors.parameter_max_version_limit_exceeded

            raise aws_sdk_ssm.errors.parameter_max_version_limit_exceeded.ParameterMaxVersionLimitExceeded.from_aws_json_1_1(
                data
            )
        case "ParameterPatternMismatchException":
            import aws_sdk_ssm.errors.parameter_pattern_mismatch_exception

            raise aws_sdk_ssm.errors.parameter_pattern_mismatch_exception.ParameterPatternMismatchException.from_aws_json_1_1(
                data
            )
        case "PoliciesLimitExceededException":
            import aws_sdk_ssm.errors.policies_limit_exceeded_exception

            raise aws_sdk_ssm.errors.policies_limit_exceeded_exception.PoliciesLimitExceededException.from_aws_json_1_1(
                data
            )
        case "TooManyUpdates":
            import aws_sdk_ssm.errors.too_many_updates

            raise aws_sdk_ssm.errors.too_many_updates.TooManyUpdates.from_aws_json_1_1(
                data
            )
        case "UnsupportedParameterType":
            import aws_sdk_ssm.errors.unsupported_parameter_type

            raise aws_sdk_ssm.errors.unsupported_parameter_type.UnsupportedParameterType.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_ssm.types.put_parameter_result.PutParameterResult:
    import aws_sdk_ssm.types.put_parameter_result

    out: aws_sdk_ssm.types.put_parameter_result.PutParameterResult = (
        aws_sdk_ssm.types.put_parameter_result.deserialize_aws_json_1_1(
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
    input_: aws_sdk_ssm.types.put_parameter_request.PutParameterRequest,
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
    headers["X-Amz-Target"] = "AmazonSSM.PutParameter"
    import aws_sdk_ssm.types.put_parameter_request

    body: bytes | None = json.dumps(
        aws_sdk_ssm.types.put_parameter_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def put_parameter(
    options: OperationOptions,
    input_: aws_sdk_ssm.types.put_parameter_request.PutParameterRequest,
) -> tuple[aws_sdk_ssm.types.put_parameter_result.PutParameterResult, zapros.Response]:
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


async def async_put_parameter(
    options: AsyncOperationOptions,
    input_: aws_sdk_ssm.types.put_parameter_request.PutParameterRequest,
) -> tuple[aws_sdk_ssm.types.put_parameter_result.PutParameterResult, zapros.Response]:
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
