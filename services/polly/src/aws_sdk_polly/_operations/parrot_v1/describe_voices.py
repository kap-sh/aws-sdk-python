"""Generated from Smithy shape ``com.amazonaws.polly#DescribeVoices``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_polly._auth._signers
import aws_sdk_polly._auth._sigv4
from aws_sdk_polly._protocol.errors import parse_error_metadata_json
from aws_sdk_polly._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_polly._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_polly.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_polly.types.describe_voices_input
    import aws_sdk_polly.types.describe_voices_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidNextTokenException":
            import aws_sdk_polly.errors.invalid_next_token_exception

            raise aws_sdk_polly.errors.invalid_next_token_exception.InvalidNextTokenException.from_json(
                data
            )
        case "ServiceFailureException":
            import aws_sdk_polly.errors.service_failure_exception

            raise aws_sdk_polly.errors.service_failure_exception.ServiceFailureException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_polly.types.describe_voices_output.DescribeVoicesOutput:
    import aws_sdk_polly.types.describe_voices_output

    out: aws_sdk_polly.types.describe_voices_output.DescribeVoicesOutput = (
        aws_sdk_polly.types.describe_voices_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_polly._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_polly._auth._sigv4.build_sigv4_auth_scheme(
                "polly", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_polly._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_polly.types.describe_voices_input.DescribeVoicesInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/voices"
    params: dict[str, str] = {}
    if "engine" in input_:
        params["Engine"] = str(input_["engine"])
    if "language_code" in input_:
        params["LanguageCode"] = str(input_["language_code"])
    params["IncludeAdditionalLanguageCodes"] = str(
        input_.get("include_additional_language_codes", False)
    )
    if "next_token" in input_:
        params["NextToken"] = str(input_["next_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def describe_voices(
    options: OperationOptions,
    input_: aws_sdk_polly.types.describe_voices_input.DescribeVoicesInput,
) -> tuple[
    aws_sdk_polly.types.describe_voices_output.DescribeVoicesOutput, zapros.Response
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


async def async_describe_voices(
    options: AsyncOperationOptions,
    input_: aws_sdk_polly.types.describe_voices_input.DescribeVoicesInput,
) -> tuple[
    aws_sdk_polly.types.describe_voices_output.DescribeVoicesOutput, zapros.Response
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
