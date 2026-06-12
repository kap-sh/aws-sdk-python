"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CreateTheme``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any
from typing import cast
from aws_sdk_amplifyuibuilder._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_amplifyuibuilder._rule_engine._endpoint_runtime import apply_label
import zapros
from urllib.parse import quote
from aws_sdk_amplifyuibuilder.errors import ServiceError, UnknownServiceError
from aws_sdk_amplifyuibuilder._protocol.errors import parse_error_metadata_json
import json
import aws_sdk_amplifyuibuilder._auth._signers
import aws_sdk_amplifyuibuilder._auth._sigv4
from aws_sdk_amplifyuibuilder._services._pipeline import AsyncOperationOptions, OperationOptions
if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.create_theme_request
    import aws_sdk_amplifyuibuilder.types.create_theme_response

def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            import aws_sdk_amplifyuibuilder.errors.internal_server_exception
            raise aws_sdk_amplifyuibuilder.errors.internal_server_exception.InternalServerException.from_json(data)
        case "InvalidParameterException":
            import aws_sdk_amplifyuibuilder.errors.invalid_parameter_exception
            raise aws_sdk_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException.from_json(data)
        case "ResourceConflictException":
            import aws_sdk_amplifyuibuilder.errors.resource_conflict_exception
            raise aws_sdk_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException.from_json(data)
        case "ServiceQuotaExceededException":
            import aws_sdk_amplifyuibuilder.errors.service_quota_exceeded_exception
            raise aws_sdk_amplifyuibuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(data)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)

def handle_response(response: zapros.Response, is_async: bool) -> aws_sdk_amplifyuibuilder.types.create_theme_response.CreateThemeResponse:
    import aws_sdk_amplifyuibuilder.types.theme
    out: aws_sdk_amplifyuibuilder.types.create_theme_response.CreateThemeResponse = {"entity": aws_sdk_amplifyuibuilder.types.theme.deserialize_json(json.loads(response.read()))}  # type: ignore[typeddict-item]
    return out

def get_signer(options: AsyncOperationOptions | OperationOptions, auth_schemes: list[dict[str, Any]] | None = None) -> aws_sdk_amplifyuibuilder._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = name_to_schema.get("sigv4") or name_to_schema.get("sigv4a") or name_to_schema.get("sigv4-s3express") or aws_sdk_amplifyuibuilder._auth._sigv4.build_sigv4_auth_scheme('amplifyuibuilder', options.region)
        if sigv4_config is not None:
            return aws_sdk_amplifyuibuilder._auth._signers.SigV4Signer(options.credentials_provider, auth_scheme=sigv4_config)
    raise RuntimeError("Auth was not resolved")

def build_request(options: OperationOptions | AsyncOperationOptions, input: aws_sdk_amplifyuibuilder.types.create_theme_request.CreateThemeRequest) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/app/{appId}/environment/{environmentName}/themes"
    url = url.replace("{appId}", quote(str(input["app_id"]), safe=""))
    url = url.replace("{environmentName}", quote(str(input["environment_name"]), safe=""))
    params: dict[str, str] = {}
    if "client_token" in input:
        params["clientToken"] = str(input["client_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "theme_to_create" in input:
        import aws_sdk_amplifyuibuilder.types.create_theme_data
        body: bytes | None = json.dumps(aws_sdk_amplifyuibuilder.types.create_theme_data.serialize_json(input["theme_to_create"])).encode()
        headers["content-type"] = "application/json"
    else:
        body = b""
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

def create_theme(options: OperationOptions, input: aws_sdk_amplifyuibuilder.types.create_theme_request.CreateThemeRequest) -> tuple[aws_sdk_amplifyuibuilder.types.create_theme_response.CreateThemeResponse, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise

async def async_create_theme(options: AsyncOperationOptions, input: aws_sdk_amplifyuibuilder.types.create_theme_request.CreateThemeRequest) -> tuple[aws_sdk_amplifyuibuilder.types.create_theme_response.CreateThemeResponse, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise