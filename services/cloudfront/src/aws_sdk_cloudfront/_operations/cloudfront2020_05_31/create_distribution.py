"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateDistribution``."""

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
    import aws_sdk_cloudfront.types.create_distribution_request
    import aws_sdk_cloudfront.types.create_distribution_result


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AccessDenied":
            import aws_sdk_cloudfront.errors.access_denied

            raise aws_sdk_cloudfront.errors.access_denied.AccessDenied.from_xml(root)
        case "CNAMEAlreadyExists":
            import aws_sdk_cloudfront.errors.cname_already_exists

            raise aws_sdk_cloudfront.errors.cname_already_exists.CNAMEAlreadyExists.from_xml(
                root
            )
        case "ContinuousDeploymentPolicyInUse":
            import aws_sdk_cloudfront.errors.continuous_deployment_policy_in_use

            raise aws_sdk_cloudfront.errors.continuous_deployment_policy_in_use.ContinuousDeploymentPolicyInUse.from_xml(
                root
            )
        case "DistributionAlreadyExists":
            import aws_sdk_cloudfront.errors.distribution_already_exists

            raise aws_sdk_cloudfront.errors.distribution_already_exists.DistributionAlreadyExists.from_xml(
                root
            )
        case "EntityLimitExceeded":
            import aws_sdk_cloudfront.errors.entity_limit_exceeded

            raise aws_sdk_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded.from_xml(
                root
            )
        case "EntityNotFound":
            import aws_sdk_cloudfront.errors.entity_not_found

            raise aws_sdk_cloudfront.errors.entity_not_found.EntityNotFound.from_xml(
                root
            )
        case "IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior":
            import aws_sdk_cloudfront.errors.illegal_field_level_encryption_config_association_with_cache_behavior

            raise aws_sdk_cloudfront.errors.illegal_field_level_encryption_config_association_with_cache_behavior.IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior.from_xml(
                root
            )
        case "IllegalOriginAccessConfiguration":
            import aws_sdk_cloudfront.errors.illegal_origin_access_configuration

            raise aws_sdk_cloudfront.errors.illegal_origin_access_configuration.IllegalOriginAccessConfiguration.from_xml(
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
        case "InvalidDefaultRootObject":
            import aws_sdk_cloudfront.errors.invalid_default_root_object

            raise aws_sdk_cloudfront.errors.invalid_default_root_object.InvalidDefaultRootObject.from_xml(
                root
            )
        case "InvalidDomainNameForOriginAccessControl":
            import aws_sdk_cloudfront.errors.invalid_domain_name_for_origin_access_control

            raise aws_sdk_cloudfront.errors.invalid_domain_name_for_origin_access_control.InvalidDomainNameForOriginAccessControl.from_xml(
                root
            )
        case "InvalidErrorCode":
            import aws_sdk_cloudfront.errors.invalid_error_code

            raise aws_sdk_cloudfront.errors.invalid_error_code.InvalidErrorCode.from_xml(
                root
            )
        case "InvalidForwardCookies":
            import aws_sdk_cloudfront.errors.invalid_forward_cookies

            raise aws_sdk_cloudfront.errors.invalid_forward_cookies.InvalidForwardCookies.from_xml(
                root
            )
        case "InvalidFunctionAssociation":
            import aws_sdk_cloudfront.errors.invalid_function_association

            raise aws_sdk_cloudfront.errors.invalid_function_association.InvalidFunctionAssociation.from_xml(
                root
            )
        case "InvalidGeoRestrictionParameter":
            import aws_sdk_cloudfront.errors.invalid_geo_restriction_parameter

            raise aws_sdk_cloudfront.errors.invalid_geo_restriction_parameter.InvalidGeoRestrictionParameter.from_xml(
                root
            )
        case "InvalidHeadersForS3Origin":
            import aws_sdk_cloudfront.errors.invalid_headers_for_s3_origin

            raise aws_sdk_cloudfront.errors.invalid_headers_for_s3_origin.InvalidHeadersForS3Origin.from_xml(
                root
            )
        case "InvalidLambdaFunctionAssociation":
            import aws_sdk_cloudfront.errors.invalid_lambda_function_association

            raise aws_sdk_cloudfront.errors.invalid_lambda_function_association.InvalidLambdaFunctionAssociation.from_xml(
                root
            )
        case "InvalidLocationCode":
            import aws_sdk_cloudfront.errors.invalid_location_code

            raise aws_sdk_cloudfront.errors.invalid_location_code.InvalidLocationCode.from_xml(
                root
            )
        case "InvalidMinimumProtocolVersion":
            import aws_sdk_cloudfront.errors.invalid_minimum_protocol_version

            raise aws_sdk_cloudfront.errors.invalid_minimum_protocol_version.InvalidMinimumProtocolVersion.from_xml(
                root
            )
        case "InvalidOrigin":
            import aws_sdk_cloudfront.errors.invalid_origin

            raise aws_sdk_cloudfront.errors.invalid_origin.InvalidOrigin.from_xml(root)
        case "InvalidOriginAccessControl":
            import aws_sdk_cloudfront.errors.invalid_origin_access_control

            raise aws_sdk_cloudfront.errors.invalid_origin_access_control.InvalidOriginAccessControl.from_xml(
                root
            )
        case "InvalidOriginAccessIdentity":
            import aws_sdk_cloudfront.errors.invalid_origin_access_identity

            raise aws_sdk_cloudfront.errors.invalid_origin_access_identity.InvalidOriginAccessIdentity.from_xml(
                root
            )
        case "InvalidOriginKeepaliveTimeout":
            import aws_sdk_cloudfront.errors.invalid_origin_keepalive_timeout

            raise aws_sdk_cloudfront.errors.invalid_origin_keepalive_timeout.InvalidOriginKeepaliveTimeout.from_xml(
                root
            )
        case "InvalidOriginReadTimeout":
            import aws_sdk_cloudfront.errors.invalid_origin_read_timeout

            raise aws_sdk_cloudfront.errors.invalid_origin_read_timeout.InvalidOriginReadTimeout.from_xml(
                root
            )
        case "InvalidProtocolSettings":
            import aws_sdk_cloudfront.errors.invalid_protocol_settings

            raise aws_sdk_cloudfront.errors.invalid_protocol_settings.InvalidProtocolSettings.from_xml(
                root
            )
        case "InvalidQueryStringParameters":
            import aws_sdk_cloudfront.errors.invalid_query_string_parameters

            raise aws_sdk_cloudfront.errors.invalid_query_string_parameters.InvalidQueryStringParameters.from_xml(
                root
            )
        case "InvalidRelativePath":
            import aws_sdk_cloudfront.errors.invalid_relative_path

            raise aws_sdk_cloudfront.errors.invalid_relative_path.InvalidRelativePath.from_xml(
                root
            )
        case "InvalidRequiredProtocol":
            import aws_sdk_cloudfront.errors.invalid_required_protocol

            raise aws_sdk_cloudfront.errors.invalid_required_protocol.InvalidRequiredProtocol.from_xml(
                root
            )
        case "InvalidResponseCode":
            import aws_sdk_cloudfront.errors.invalid_response_code

            raise aws_sdk_cloudfront.errors.invalid_response_code.InvalidResponseCode.from_xml(
                root
            )
        case "InvalidTTLOrder":
            import aws_sdk_cloudfront.errors.invalid_ttl_order

            raise aws_sdk_cloudfront.errors.invalid_ttl_order.InvalidTTLOrder.from_xml(
                root
            )
        case "InvalidViewerCertificate":
            import aws_sdk_cloudfront.errors.invalid_viewer_certificate

            raise aws_sdk_cloudfront.errors.invalid_viewer_certificate.InvalidViewerCertificate.from_xml(
                root
            )
        case "InvalidWebACLId":
            import aws_sdk_cloudfront.errors.invalid_web_acl_id

            raise aws_sdk_cloudfront.errors.invalid_web_acl_id.InvalidWebACLId.from_xml(
                root
            )
        case "MissingBody":
            import aws_sdk_cloudfront.errors.missing_body

            raise aws_sdk_cloudfront.errors.missing_body.MissingBody.from_xml(root)
        case "NoSuchCachePolicy":
            import aws_sdk_cloudfront.errors.no_such_cache_policy

            raise aws_sdk_cloudfront.errors.no_such_cache_policy.NoSuchCachePolicy.from_xml(
                root
            )
        case "NoSuchContinuousDeploymentPolicy":
            import aws_sdk_cloudfront.errors.no_such_continuous_deployment_policy

            raise aws_sdk_cloudfront.errors.no_such_continuous_deployment_policy.NoSuchContinuousDeploymentPolicy.from_xml(
                root
            )
        case "NoSuchFieldLevelEncryptionConfig":
            import aws_sdk_cloudfront.errors.no_such_field_level_encryption_config

            raise aws_sdk_cloudfront.errors.no_such_field_level_encryption_config.NoSuchFieldLevelEncryptionConfig.from_xml(
                root
            )
        case "NoSuchOrigin":
            import aws_sdk_cloudfront.errors.no_such_origin

            raise aws_sdk_cloudfront.errors.no_such_origin.NoSuchOrigin.from_xml(root)
        case "NoSuchOriginRequestPolicy":
            import aws_sdk_cloudfront.errors.no_such_origin_request_policy

            raise aws_sdk_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy.from_xml(
                root
            )
        case "NoSuchRealtimeLogConfig":
            import aws_sdk_cloudfront.errors.no_such_realtime_log_config

            raise aws_sdk_cloudfront.errors.no_such_realtime_log_config.NoSuchRealtimeLogConfig.from_xml(
                root
            )
        case "NoSuchResponseHeadersPolicy":
            import aws_sdk_cloudfront.errors.no_such_response_headers_policy

            raise aws_sdk_cloudfront.errors.no_such_response_headers_policy.NoSuchResponseHeadersPolicy.from_xml(
                root
            )
        case "RealtimeLogConfigOwnerMismatch":
            import aws_sdk_cloudfront.errors.realtime_log_config_owner_mismatch

            raise aws_sdk_cloudfront.errors.realtime_log_config_owner_mismatch.RealtimeLogConfigOwnerMismatch.from_xml(
                root
            )
        case "TooManyCacheBehaviors":
            import aws_sdk_cloudfront.errors.too_many_cache_behaviors

            raise aws_sdk_cloudfront.errors.too_many_cache_behaviors.TooManyCacheBehaviors.from_xml(
                root
            )
        case "TooManyCertificates":
            import aws_sdk_cloudfront.errors.too_many_certificates

            raise aws_sdk_cloudfront.errors.too_many_certificates.TooManyCertificates.from_xml(
                root
            )
        case "TooManyCookieNamesInWhiteList":
            import aws_sdk_cloudfront.errors.too_many_cookie_names_in_white_list

            raise aws_sdk_cloudfront.errors.too_many_cookie_names_in_white_list.TooManyCookieNamesInWhiteList.from_xml(
                root
            )
        case "TooManyDistributionCNAMEs":
            import aws_sdk_cloudfront.errors.too_many_distribution_cnam_es

            raise aws_sdk_cloudfront.errors.too_many_distribution_cnam_es.TooManyDistributionCNAMEs.from_xml(
                root
            )
        case "TooManyDistributions":
            import aws_sdk_cloudfront.errors.too_many_distributions

            raise aws_sdk_cloudfront.errors.too_many_distributions.TooManyDistributions.from_xml(
                root
            )
        case "TooManyDistributionsAssociatedToCachePolicy":
            import aws_sdk_cloudfront.errors.too_many_distributions_associated_to_cache_policy

            raise aws_sdk_cloudfront.errors.too_many_distributions_associated_to_cache_policy.TooManyDistributionsAssociatedToCachePolicy.from_xml(
                root
            )
        case "TooManyDistributionsAssociatedToFieldLevelEncryptionConfig":
            import aws_sdk_cloudfront.errors.too_many_distributions_associated_to_field_level_encryption_config

            raise aws_sdk_cloudfront.errors.too_many_distributions_associated_to_field_level_encryption_config.TooManyDistributionsAssociatedToFieldLevelEncryptionConfig.from_xml(
                root
            )
        case "TooManyDistributionsAssociatedToKeyGroup":
            import aws_sdk_cloudfront.errors.too_many_distributions_associated_to_key_group

            raise aws_sdk_cloudfront.errors.too_many_distributions_associated_to_key_group.TooManyDistributionsAssociatedToKeyGroup.from_xml(
                root
            )
        case "TooManyDistributionsAssociatedToOriginAccessControl":
            import aws_sdk_cloudfront.errors.too_many_distributions_associated_to_origin_access_control

            raise aws_sdk_cloudfront.errors.too_many_distributions_associated_to_origin_access_control.TooManyDistributionsAssociatedToOriginAccessControl.from_xml(
                root
            )
        case "TooManyDistributionsAssociatedToOriginRequestPolicy":
            import aws_sdk_cloudfront.errors.too_many_distributions_associated_to_origin_request_policy

            raise aws_sdk_cloudfront.errors.too_many_distributions_associated_to_origin_request_policy.TooManyDistributionsAssociatedToOriginRequestPolicy.from_xml(
                root
            )
        case "TooManyDistributionsAssociatedToResponseHeadersPolicy":
            import aws_sdk_cloudfront.errors.too_many_distributions_associated_to_response_headers_policy

            raise aws_sdk_cloudfront.errors.too_many_distributions_associated_to_response_headers_policy.TooManyDistributionsAssociatedToResponseHeadersPolicy.from_xml(
                root
            )
        case "TooManyDistributionsWithFunctionAssociations":
            import aws_sdk_cloudfront.errors.too_many_distributions_with_function_associations

            raise aws_sdk_cloudfront.errors.too_many_distributions_with_function_associations.TooManyDistributionsWithFunctionAssociations.from_xml(
                root
            )
        case "TooManyDistributionsWithLambdaAssociations":
            import aws_sdk_cloudfront.errors.too_many_distributions_with_lambda_associations

            raise aws_sdk_cloudfront.errors.too_many_distributions_with_lambda_associations.TooManyDistributionsWithLambdaAssociations.from_xml(
                root
            )
        case "TooManyDistributionsWithSingleFunctionARN":
            import aws_sdk_cloudfront.errors.too_many_distributions_with_single_function_arn

            raise aws_sdk_cloudfront.errors.too_many_distributions_with_single_function_arn.TooManyDistributionsWithSingleFunctionARN.from_xml(
                root
            )
        case "TooManyFunctionAssociations":
            import aws_sdk_cloudfront.errors.too_many_function_associations

            raise aws_sdk_cloudfront.errors.too_many_function_associations.TooManyFunctionAssociations.from_xml(
                root
            )
        case "TooManyHeadersInForwardedValues":
            import aws_sdk_cloudfront.errors.too_many_headers_in_forwarded_values

            raise aws_sdk_cloudfront.errors.too_many_headers_in_forwarded_values.TooManyHeadersInForwardedValues.from_xml(
                root
            )
        case "TooManyKeyGroupsAssociatedToDistribution":
            import aws_sdk_cloudfront.errors.too_many_key_groups_associated_to_distribution

            raise aws_sdk_cloudfront.errors.too_many_key_groups_associated_to_distribution.TooManyKeyGroupsAssociatedToDistribution.from_xml(
                root
            )
        case "TooManyLambdaFunctionAssociations":
            import aws_sdk_cloudfront.errors.too_many_lambda_function_associations

            raise aws_sdk_cloudfront.errors.too_many_lambda_function_associations.TooManyLambdaFunctionAssociations.from_xml(
                root
            )
        case "TooManyOriginCustomHeaders":
            import aws_sdk_cloudfront.errors.too_many_origin_custom_headers

            raise aws_sdk_cloudfront.errors.too_many_origin_custom_headers.TooManyOriginCustomHeaders.from_xml(
                root
            )
        case "TooManyOriginGroupsPerDistribution":
            import aws_sdk_cloudfront.errors.too_many_origin_groups_per_distribution

            raise aws_sdk_cloudfront.errors.too_many_origin_groups_per_distribution.TooManyOriginGroupsPerDistribution.from_xml(
                root
            )
        case "TooManyOrigins":
            import aws_sdk_cloudfront.errors.too_many_origins

            raise aws_sdk_cloudfront.errors.too_many_origins.TooManyOrigins.from_xml(
                root
            )
        case "TooManyQueryStringParameters":
            import aws_sdk_cloudfront.errors.too_many_query_string_parameters

            raise aws_sdk_cloudfront.errors.too_many_query_string_parameters.TooManyQueryStringParameters.from_xml(
                root
            )
        case "TooManyTrustedSigners":
            import aws_sdk_cloudfront.errors.too_many_trusted_signers

            raise aws_sdk_cloudfront.errors.too_many_trusted_signers.TooManyTrustedSigners.from_xml(
                root
            )
        case "TrustedKeyGroupDoesNotExist":
            import aws_sdk_cloudfront.errors.trusted_key_group_does_not_exist

            raise aws_sdk_cloudfront.errors.trusted_key_group_does_not_exist.TrustedKeyGroupDoesNotExist.from_xml(
                root
            )
        case "TrustedSignerDoesNotExist":
            import aws_sdk_cloudfront.errors.trusted_signer_does_not_exist

            raise aws_sdk_cloudfront.errors.trusted_signer_does_not_exist.TrustedSignerDoesNotExist.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cloudfront.types.create_distribution_result.CreateDistributionResult:
    import aws_sdk_cloudfront.types.distribution

    out: aws_sdk_cloudfront.types.create_distribution_result.CreateDistributionResult = {
        "distribution": aws_sdk_cloudfront.types.distribution.deserialize_xml(
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
    input_: aws_sdk_cloudfront.types.create_distribution_request.CreateDistributionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/distribution"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "distribution_config" in input_:
        import aws_sdk_cloudfront.types.distribution_config

        payload_root = Element("_")
        aws_sdk_cloudfront.types.distribution_config.serialize_xml(
            input_["distribution_config"], payload_root, "DistributionConfig"
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


def create_distribution(
    options: OperationOptions,
    input_: aws_sdk_cloudfront.types.create_distribution_request.CreateDistributionRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_distribution_result.CreateDistributionResult,
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


async def async_create_distribution(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudfront.types.create_distribution_request.CreateDistributionRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_distribution_result.CreateDistributionResult,
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
