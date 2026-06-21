"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateDistribution``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_cloudfront._auth._signers
import aws_sdk_cloudfront._auth._sigv4
import aws_sdk_cloudfront.errors.access_denied
import aws_sdk_cloudfront.errors.cname_already_exists
import aws_sdk_cloudfront.errors.continuous_deployment_policy_in_use
import aws_sdk_cloudfront.errors.distribution_already_exists
import aws_sdk_cloudfront.errors.entity_limit_exceeded
import aws_sdk_cloudfront.errors.entity_not_found
import aws_sdk_cloudfront.errors.illegal_field_level_encryption_config_association_with_cache_behavior
import aws_sdk_cloudfront.errors.illegal_origin_access_configuration
import aws_sdk_cloudfront.errors.inconsistent_quantities
import aws_sdk_cloudfront.errors.invalid_argument
import aws_sdk_cloudfront.errors.invalid_default_root_object
import aws_sdk_cloudfront.errors.invalid_domain_name_for_origin_access_control
import aws_sdk_cloudfront.errors.invalid_error_code
import aws_sdk_cloudfront.errors.invalid_forward_cookies
import aws_sdk_cloudfront.errors.invalid_function_association
import aws_sdk_cloudfront.errors.invalid_geo_restriction_parameter
import aws_sdk_cloudfront.errors.invalid_headers_for_s3_origin
import aws_sdk_cloudfront.errors.invalid_lambda_function_association
import aws_sdk_cloudfront.errors.invalid_location_code
import aws_sdk_cloudfront.errors.invalid_minimum_protocol_version
import aws_sdk_cloudfront.errors.invalid_origin
import aws_sdk_cloudfront.errors.invalid_origin_access_control
import aws_sdk_cloudfront.errors.invalid_origin_access_identity
import aws_sdk_cloudfront.errors.invalid_origin_keepalive_timeout
import aws_sdk_cloudfront.errors.invalid_origin_read_timeout
import aws_sdk_cloudfront.errors.invalid_protocol_settings
import aws_sdk_cloudfront.errors.invalid_query_string_parameters
import aws_sdk_cloudfront.errors.invalid_relative_path
import aws_sdk_cloudfront.errors.invalid_required_protocol
import aws_sdk_cloudfront.errors.invalid_response_code
import aws_sdk_cloudfront.errors.invalid_ttl_order
import aws_sdk_cloudfront.errors.invalid_viewer_certificate
import aws_sdk_cloudfront.errors.invalid_web_acl_id
import aws_sdk_cloudfront.errors.missing_body
import aws_sdk_cloudfront.errors.no_such_cache_policy
import aws_sdk_cloudfront.errors.no_such_continuous_deployment_policy
import aws_sdk_cloudfront.errors.no_such_field_level_encryption_config
import aws_sdk_cloudfront.errors.no_such_origin
import aws_sdk_cloudfront.errors.no_such_origin_request_policy
import aws_sdk_cloudfront.errors.no_such_realtime_log_config
import aws_sdk_cloudfront.errors.no_such_response_headers_policy
import aws_sdk_cloudfront.errors.realtime_log_config_owner_mismatch
import aws_sdk_cloudfront.errors.too_many_cache_behaviors
import aws_sdk_cloudfront.errors.too_many_certificates
import aws_sdk_cloudfront.errors.too_many_cookie_names_in_white_list
import aws_sdk_cloudfront.errors.too_many_distribution_cnam_es
import aws_sdk_cloudfront.errors.too_many_distributions
import aws_sdk_cloudfront.errors.too_many_distributions_associated_to_cache_policy
import aws_sdk_cloudfront.errors.too_many_distributions_associated_to_field_level_encryption_config
import aws_sdk_cloudfront.errors.too_many_distributions_associated_to_key_group
import aws_sdk_cloudfront.errors.too_many_distributions_associated_to_origin_access_control
import aws_sdk_cloudfront.errors.too_many_distributions_associated_to_origin_request_policy
import aws_sdk_cloudfront.errors.too_many_distributions_associated_to_response_headers_policy
import aws_sdk_cloudfront.errors.too_many_distributions_with_function_associations
import aws_sdk_cloudfront.errors.too_many_distributions_with_lambda_associations
import aws_sdk_cloudfront.errors.too_many_distributions_with_single_function_arn
import aws_sdk_cloudfront.errors.too_many_function_associations
import aws_sdk_cloudfront.errors.too_many_headers_in_forwarded_values
import aws_sdk_cloudfront.errors.too_many_key_groups_associated_to_distribution
import aws_sdk_cloudfront.errors.too_many_lambda_function_associations
import aws_sdk_cloudfront.errors.too_many_origin_custom_headers
import aws_sdk_cloudfront.errors.too_many_origin_groups_per_distribution
import aws_sdk_cloudfront.errors.too_many_origins
import aws_sdk_cloudfront.errors.too_many_query_string_parameters
import aws_sdk_cloudfront.errors.too_many_trusted_signers
import aws_sdk_cloudfront.errors.trusted_key_group_does_not_exist
import aws_sdk_cloudfront.errors.trusted_signer_does_not_exist
import aws_sdk_cloudfront.types.create_distribution_request
import aws_sdk_cloudfront.types.create_distribution_result
import aws_sdk_cloudfront.types.distribution
import aws_sdk_cloudfront.types.distribution_config
from aws_sdk_cloudfront._protocol.errors import parse_error_metadata
from aws_sdk_cloudfront._protocol.xml import Element, fromstring, tostring
from aws_sdk_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloudfront._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudfront.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AccessDenied":
            raise aws_sdk_cloudfront.errors.access_denied.AccessDenied.from_xml(root)
        case "CNAMEAlreadyExists":
            raise aws_sdk_cloudfront.errors.cname_already_exists.CNAMEAlreadyExists.from_xml(
                root
            )
        case "ContinuousDeploymentPolicyInUse":
            raise aws_sdk_cloudfront.errors.continuous_deployment_policy_in_use.ContinuousDeploymentPolicyInUse.from_xml(
                root
            )
        case "DistributionAlreadyExists":
            raise aws_sdk_cloudfront.errors.distribution_already_exists.DistributionAlreadyExists.from_xml(
                root
            )
        case "EntityLimitExceeded":
            raise aws_sdk_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded.from_xml(
                root
            )
        case "EntityNotFound":
            raise aws_sdk_cloudfront.errors.entity_not_found.EntityNotFound.from_xml(
                root
            )
        case "IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior":
            raise aws_sdk_cloudfront.errors.illegal_field_level_encryption_config_association_with_cache_behavior.IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior.from_xml(
                root
            )
        case "IllegalOriginAccessConfiguration":
            raise aws_sdk_cloudfront.errors.illegal_origin_access_configuration.IllegalOriginAccessConfiguration.from_xml(
                root
            )
        case "InconsistentQuantities":
            raise aws_sdk_cloudfront.errors.inconsistent_quantities.InconsistentQuantities.from_xml(
                root
            )
        case "InvalidArgument":
            raise aws_sdk_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                root
            )
        case "InvalidDefaultRootObject":
            raise aws_sdk_cloudfront.errors.invalid_default_root_object.InvalidDefaultRootObject.from_xml(
                root
            )
        case "InvalidDomainNameForOriginAccessControl":
            raise aws_sdk_cloudfront.errors.invalid_domain_name_for_origin_access_control.InvalidDomainNameForOriginAccessControl.from_xml(
                root
            )
        case "InvalidErrorCode":
            raise aws_sdk_cloudfront.errors.invalid_error_code.InvalidErrorCode.from_xml(
                root
            )
        case "InvalidForwardCookies":
            raise aws_sdk_cloudfront.errors.invalid_forward_cookies.InvalidForwardCookies.from_xml(
                root
            )
        case "InvalidFunctionAssociation":
            raise aws_sdk_cloudfront.errors.invalid_function_association.InvalidFunctionAssociation.from_xml(
                root
            )
        case "InvalidGeoRestrictionParameter":
            raise aws_sdk_cloudfront.errors.invalid_geo_restriction_parameter.InvalidGeoRestrictionParameter.from_xml(
                root
            )
        case "InvalidHeadersForS3Origin":
            raise aws_sdk_cloudfront.errors.invalid_headers_for_s3_origin.InvalidHeadersForS3Origin.from_xml(
                root
            )
        case "InvalidLambdaFunctionAssociation":
            raise aws_sdk_cloudfront.errors.invalid_lambda_function_association.InvalidLambdaFunctionAssociation.from_xml(
                root
            )
        case "InvalidLocationCode":
            raise aws_sdk_cloudfront.errors.invalid_location_code.InvalidLocationCode.from_xml(
                root
            )
        case "InvalidMinimumProtocolVersion":
            raise aws_sdk_cloudfront.errors.invalid_minimum_protocol_version.InvalidMinimumProtocolVersion.from_xml(
                root
            )
        case "InvalidOrigin":
            raise aws_sdk_cloudfront.errors.invalid_origin.InvalidOrigin.from_xml(root)
        case "InvalidOriginAccessControl":
            raise aws_sdk_cloudfront.errors.invalid_origin_access_control.InvalidOriginAccessControl.from_xml(
                root
            )
        case "InvalidOriginAccessIdentity":
            raise aws_sdk_cloudfront.errors.invalid_origin_access_identity.InvalidOriginAccessIdentity.from_xml(
                root
            )
        case "InvalidOriginKeepaliveTimeout":
            raise aws_sdk_cloudfront.errors.invalid_origin_keepalive_timeout.InvalidOriginKeepaliveTimeout.from_xml(
                root
            )
        case "InvalidOriginReadTimeout":
            raise aws_sdk_cloudfront.errors.invalid_origin_read_timeout.InvalidOriginReadTimeout.from_xml(
                root
            )
        case "InvalidProtocolSettings":
            raise aws_sdk_cloudfront.errors.invalid_protocol_settings.InvalidProtocolSettings.from_xml(
                root
            )
        case "InvalidQueryStringParameters":
            raise aws_sdk_cloudfront.errors.invalid_query_string_parameters.InvalidQueryStringParameters.from_xml(
                root
            )
        case "InvalidRelativePath":
            raise aws_sdk_cloudfront.errors.invalid_relative_path.InvalidRelativePath.from_xml(
                root
            )
        case "InvalidRequiredProtocol":
            raise aws_sdk_cloudfront.errors.invalid_required_protocol.InvalidRequiredProtocol.from_xml(
                root
            )
        case "InvalidResponseCode":
            raise aws_sdk_cloudfront.errors.invalid_response_code.InvalidResponseCode.from_xml(
                root
            )
        case "InvalidTTLOrder":
            raise aws_sdk_cloudfront.errors.invalid_ttl_order.InvalidTTLOrder.from_xml(
                root
            )
        case "InvalidViewerCertificate":
            raise aws_sdk_cloudfront.errors.invalid_viewer_certificate.InvalidViewerCertificate.from_xml(
                root
            )
        case "InvalidWebACLId":
            raise aws_sdk_cloudfront.errors.invalid_web_acl_id.InvalidWebACLId.from_xml(
                root
            )
        case "MissingBody":
            raise aws_sdk_cloudfront.errors.missing_body.MissingBody.from_xml(root)
        case "NoSuchCachePolicy":
            raise aws_sdk_cloudfront.errors.no_such_cache_policy.NoSuchCachePolicy.from_xml(
                root
            )
        case "NoSuchContinuousDeploymentPolicy":
            raise aws_sdk_cloudfront.errors.no_such_continuous_deployment_policy.NoSuchContinuousDeploymentPolicy.from_xml(
                root
            )
        case "NoSuchFieldLevelEncryptionConfig":
            raise aws_sdk_cloudfront.errors.no_such_field_level_encryption_config.NoSuchFieldLevelEncryptionConfig.from_xml(
                root
            )
        case "NoSuchOrigin":
            raise aws_sdk_cloudfront.errors.no_such_origin.NoSuchOrigin.from_xml(root)
        case "NoSuchOriginRequestPolicy":
            raise aws_sdk_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy.from_xml(
                root
            )
        case "NoSuchRealtimeLogConfig":
            raise aws_sdk_cloudfront.errors.no_such_realtime_log_config.NoSuchRealtimeLogConfig.from_xml(
                root
            )
        case "NoSuchResponseHeadersPolicy":
            raise aws_sdk_cloudfront.errors.no_such_response_headers_policy.NoSuchResponseHeadersPolicy.from_xml(
                root
            )
        case "RealtimeLogConfigOwnerMismatch":
            raise aws_sdk_cloudfront.errors.realtime_log_config_owner_mismatch.RealtimeLogConfigOwnerMismatch.from_xml(
                root
            )
        case "TooManyCacheBehaviors":
            raise aws_sdk_cloudfront.errors.too_many_cache_behaviors.TooManyCacheBehaviors.from_xml(
                root
            )
        case "TooManyCertificates":
            raise aws_sdk_cloudfront.errors.too_many_certificates.TooManyCertificates.from_xml(
                root
            )
        case "TooManyCookieNamesInWhiteList":
            raise aws_sdk_cloudfront.errors.too_many_cookie_names_in_white_list.TooManyCookieNamesInWhiteList.from_xml(
                root
            )
        case "TooManyDistributionCNAMEs":
            raise aws_sdk_cloudfront.errors.too_many_distribution_cnam_es.TooManyDistributionCNAMEs.from_xml(
                root
            )
        case "TooManyDistributions":
            raise aws_sdk_cloudfront.errors.too_many_distributions.TooManyDistributions.from_xml(
                root
            )
        case "TooManyDistributionsAssociatedToCachePolicy":
            raise aws_sdk_cloudfront.errors.too_many_distributions_associated_to_cache_policy.TooManyDistributionsAssociatedToCachePolicy.from_xml(
                root
            )
        case "TooManyDistributionsAssociatedToFieldLevelEncryptionConfig":
            raise aws_sdk_cloudfront.errors.too_many_distributions_associated_to_field_level_encryption_config.TooManyDistributionsAssociatedToFieldLevelEncryptionConfig.from_xml(
                root
            )
        case "TooManyDistributionsAssociatedToKeyGroup":
            raise aws_sdk_cloudfront.errors.too_many_distributions_associated_to_key_group.TooManyDistributionsAssociatedToKeyGroup.from_xml(
                root
            )
        case "TooManyDistributionsAssociatedToOriginAccessControl":
            raise aws_sdk_cloudfront.errors.too_many_distributions_associated_to_origin_access_control.TooManyDistributionsAssociatedToOriginAccessControl.from_xml(
                root
            )
        case "TooManyDistributionsAssociatedToOriginRequestPolicy":
            raise aws_sdk_cloudfront.errors.too_many_distributions_associated_to_origin_request_policy.TooManyDistributionsAssociatedToOriginRequestPolicy.from_xml(
                root
            )
        case "TooManyDistributionsAssociatedToResponseHeadersPolicy":
            raise aws_sdk_cloudfront.errors.too_many_distributions_associated_to_response_headers_policy.TooManyDistributionsAssociatedToResponseHeadersPolicy.from_xml(
                root
            )
        case "TooManyDistributionsWithFunctionAssociations":
            raise aws_sdk_cloudfront.errors.too_many_distributions_with_function_associations.TooManyDistributionsWithFunctionAssociations.from_xml(
                root
            )
        case "TooManyDistributionsWithLambdaAssociations":
            raise aws_sdk_cloudfront.errors.too_many_distributions_with_lambda_associations.TooManyDistributionsWithLambdaAssociations.from_xml(
                root
            )
        case "TooManyDistributionsWithSingleFunctionARN":
            raise aws_sdk_cloudfront.errors.too_many_distributions_with_single_function_arn.TooManyDistributionsWithSingleFunctionARN.from_xml(
                root
            )
        case "TooManyFunctionAssociations":
            raise aws_sdk_cloudfront.errors.too_many_function_associations.TooManyFunctionAssociations.from_xml(
                root
            )
        case "TooManyHeadersInForwardedValues":
            raise aws_sdk_cloudfront.errors.too_many_headers_in_forwarded_values.TooManyHeadersInForwardedValues.from_xml(
                root
            )
        case "TooManyKeyGroupsAssociatedToDistribution":
            raise aws_sdk_cloudfront.errors.too_many_key_groups_associated_to_distribution.TooManyKeyGroupsAssociatedToDistribution.from_xml(
                root
            )
        case "TooManyLambdaFunctionAssociations":
            raise aws_sdk_cloudfront.errors.too_many_lambda_function_associations.TooManyLambdaFunctionAssociations.from_xml(
                root
            )
        case "TooManyOriginCustomHeaders":
            raise aws_sdk_cloudfront.errors.too_many_origin_custom_headers.TooManyOriginCustomHeaders.from_xml(
                root
            )
        case "TooManyOriginGroupsPerDistribution":
            raise aws_sdk_cloudfront.errors.too_many_origin_groups_per_distribution.TooManyOriginGroupsPerDistribution.from_xml(
                root
            )
        case "TooManyOrigins":
            raise aws_sdk_cloudfront.errors.too_many_origins.TooManyOrigins.from_xml(
                root
            )
        case "TooManyQueryStringParameters":
            raise aws_sdk_cloudfront.errors.too_many_query_string_parameters.TooManyQueryStringParameters.from_xml(
                root
            )
        case "TooManyTrustedSigners":
            raise aws_sdk_cloudfront.errors.too_many_trusted_signers.TooManyTrustedSigners.from_xml(
                root
            )
        case "TrustedKeyGroupDoesNotExist":
            raise aws_sdk_cloudfront.errors.trusted_key_group_does_not_exist.TrustedKeyGroupDoesNotExist.from_xml(
                root
            )
        case "TrustedSignerDoesNotExist":
            raise aws_sdk_cloudfront.errors.trusted_signer_does_not_exist.TrustedSignerDoesNotExist.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_cloudfront.types.create_distribution_result.CreateDistributionResult:
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


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_cloudfront.types.create_distribution_result.CreateDistributionResult:
    out: aws_sdk_cloudfront.types.create_distribution_result.CreateDistributionResult = {
        "distribution": aws_sdk_cloudfront.types.distribution.deserialize_xml(
            fromstring(await response.aread())
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
        return handle_response(response), response
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
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
