"""Generated from Smithy shape ``com.amazonaws.codepipeline#PutThirdPartyJobSuccessResult``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_codepipeline._auth._signers
import aws_sdk_codepipeline._auth._sigv4
from aws_sdk_codepipeline._protocol.errors import parse_error_metadata_json
from aws_sdk_codepipeline._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_codepipeline._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codepipeline.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.put_third_party_job_success_result_input


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidClientTokenException":
            import aws_sdk_codepipeline.errors.invalid_client_token_exception

            raise aws_sdk_codepipeline.errors.invalid_client_token_exception.InvalidClientTokenException.from_aws_json_1_1(
                data
            )
        case "InvalidJobStateException":
            import aws_sdk_codepipeline.errors.invalid_job_state_exception

            raise aws_sdk_codepipeline.errors.invalid_job_state_exception.InvalidJobStateException.from_aws_json_1_1(
                data
            )
        case "JobNotFoundException":
            import aws_sdk_codepipeline.errors.job_not_found_exception

            raise aws_sdk_codepipeline.errors.job_not_found_exception.JobNotFoundException.from_aws_json_1_1(
                data
            )
        case "ValidationException":
            import aws_sdk_codepipeline.errors.validation_exception

            raise aws_sdk_codepipeline.errors.validation_exception.ValidationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_codepipeline._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_codepipeline._auth._sigv4.build_sigv4_auth_scheme(
                "codepipeline", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_codepipeline._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_codepipeline.types.put_third_party_job_success_result_input.PutThirdPartyJobSuccessResultInput,
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
    headers["X-Amz-Target"] = "CodePipeline_20150709.PutThirdPartyJobSuccessResult"
    import aws_sdk_codepipeline.types.put_third_party_job_success_result_input

    body: bytes | None = json.dumps(
        aws_sdk_codepipeline.types.put_third_party_job_success_result_input.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def put_third_party_job_success_result(
    options: OperationOptions,
    input_: aws_sdk_codepipeline.types.put_third_party_job_success_result_input.PutThirdPartyJobSuccessResultInput,
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


async def async_put_third_party_job_success_result(
    options: AsyncOperationOptions,
    input_: aws_sdk_codepipeline.types.put_third_party_job_success_result_input.PutThirdPartyJobSuccessResultInput,
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
