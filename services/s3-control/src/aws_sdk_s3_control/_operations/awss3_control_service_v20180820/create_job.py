"""Generated from Smithy shape ``com.amazonaws.s3control#CreateJob``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_s3_control._auth._signers
import aws_sdk_s3_control._auth._sigv4
from aws_sdk_s3_control._protocol.errors import parse_error_metadata
from aws_sdk_s3_control._protocol.xml import Element, SubElement, fromstring, tostring
from aws_sdk_s3_control._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3_control._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_s3_control.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.create_job_request
    import aws_sdk_s3_control.types.create_job_result


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "BadRequestException":
            import aws_sdk_s3_control.errors.bad_request_exception

            raise aws_sdk_s3_control.errors.bad_request_exception.BadRequestException.from_xml(
                root
            )
        case "IdempotencyException":
            import aws_sdk_s3_control.errors.idempotency_exception

            raise aws_sdk_s3_control.errors.idempotency_exception.IdempotencyException.from_xml(
                root
            )
        case "InternalServiceException":
            import aws_sdk_s3_control.errors.internal_service_exception

            raise aws_sdk_s3_control.errors.internal_service_exception.InternalServiceException.from_xml(
                root
            )
        case "TooManyRequestsException":
            import aws_sdk_s3_control.errors.too_many_requests_exception

            raise aws_sdk_s3_control.errors.too_many_requests_exception.TooManyRequestsException.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_s3_control.types.create_job_result.CreateJobResult:
    import aws_sdk_s3_control.types.create_job_result

    out: aws_sdk_s3_control.types.create_job_result.CreateJobResult = (
        aws_sdk_s3_control.types.create_job_result.deserialize_xml(
            fromstring(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_s3_control._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_s3_control._auth._sigv4.build_sigv4_auth_scheme(
                "s3", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_s3_control._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_s3_control.types.create_job_request.CreateJobRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
            AccountId=input_.get("account_id"),
            RequiresAccountId=True,
            OutpostId=options.outpost_id,
            Bucket=options.bucket,
            AccessPointName=options.access_point_name,
            UseArnRegion=options.use_arn_region,
            ResourceArn=options.resource_arn,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v20180820/jobs"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "account_id" in input_:
        headers["x-amz-account-id"] = str(input_["account_id"])
    root = Element("CreateJobRequest")
    if "confirmation_required" in input_:
        SubElement(root, "ConfirmationRequired").text = str(
            input_["confirmation_required"]
        )
    if "operation" in input_:
        import aws_sdk_s3_control.types.job_operation

        aws_sdk_s3_control.types.job_operation.serialize_xml(
            input_["operation"], root, "Operation"
        )
    if "report" in input_:
        import aws_sdk_s3_control.types.job_report

        aws_sdk_s3_control.types.job_report.serialize_xml(
            input_["report"], root, "Report"
        )
    if "client_request_token" in input_:
        SubElement(root, "ClientRequestToken").text = str(
            input_["client_request_token"]
        )
    if "manifest" in input_:
        import aws_sdk_s3_control.types.job_manifest

        aws_sdk_s3_control.types.job_manifest.serialize_xml(
            input_["manifest"], root, "Manifest"
        )
    if "description" in input_:
        SubElement(root, "Description").text = str(input_["description"])
    if "priority" in input_:
        SubElement(root, "Priority").text = str(input_["priority"])
    if "role_arn" in input_:
        SubElement(root, "RoleArn").text = str(input_["role_arn"])
    if "tags" in input_:
        import aws_sdk_s3_control.types.s3_tag_set

        aws_sdk_s3_control.types.s3_tag_set.serialize_xml(input_["tags"], root, "Tags")
    if "manifest_generator" in input_:
        import aws_sdk_s3_control.types.job_manifest_generator

        aws_sdk_s3_control.types.job_manifest_generator.serialize_xml(
            input_["manifest_generator"], root, "ManifestGenerator"
        )
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_job(
    options: OperationOptions,
    input_: aws_sdk_s3_control.types.create_job_request.CreateJobRequest,
) -> tuple[aws_sdk_s3_control.types.create_job_result.CreateJobResult, zapros.Response]:
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


async def async_create_job(
    options: AsyncOperationOptions,
    input_: aws_sdk_s3_control.types.create_job_request.CreateJobRequest,
) -> tuple[aws_sdk_s3_control.types.create_job_result.CreateJobResult, zapros.Response]:
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
