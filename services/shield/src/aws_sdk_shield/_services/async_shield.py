"""Generated from Smithy shape ``com.amazonaws.shield#AWSShield_20160616``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_shield._auth._signers
import aws_sdk_shield._auth._sigv4
from aws_sdk_shield._auth._identity import Credentials
from aws_sdk_shield._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_shield._auth._zapros_handler import AuthMiddleware
from aws_sdk_shield._pagination import resolve_path as _resolve_path
from aws_sdk_shield._services._aws_config import aaws_config
from aws_sdk_shield._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_shield.types.associate_drt_log_bucket_request
    import aws_sdk_shield.types.associate_drt_log_bucket_response
    import aws_sdk_shield.types.associate_drt_role_request
    import aws_sdk_shield.types.associate_drt_role_response
    import aws_sdk_shield.types.associate_health_check_request
    import aws_sdk_shield.types.associate_health_check_response
    import aws_sdk_shield.types.associate_proactive_engagement_details_request
    import aws_sdk_shield.types.associate_proactive_engagement_details_response
    import aws_sdk_shield.types.attack_id
    import aws_sdk_shield.types.attack_summary
    import aws_sdk_shield.types.auto_renew
    import aws_sdk_shield.types.create_protection_group_request
    import aws_sdk_shield.types.create_protection_group_response
    import aws_sdk_shield.types.create_protection_request
    import aws_sdk_shield.types.create_protection_response
    import aws_sdk_shield.types.create_subscription_request
    import aws_sdk_shield.types.create_subscription_response
    import aws_sdk_shield.types.delete_protection_group_request
    import aws_sdk_shield.types.delete_protection_group_response
    import aws_sdk_shield.types.delete_protection_request
    import aws_sdk_shield.types.delete_protection_response
    import aws_sdk_shield.types.delete_subscription_request
    import aws_sdk_shield.types.delete_subscription_response
    import aws_sdk_shield.types.describe_attack_request
    import aws_sdk_shield.types.describe_attack_response
    import aws_sdk_shield.types.describe_attack_statistics_request
    import aws_sdk_shield.types.describe_attack_statistics_response
    import aws_sdk_shield.types.describe_drt_access_request
    import aws_sdk_shield.types.describe_drt_access_response
    import aws_sdk_shield.types.describe_emergency_contact_settings_request
    import aws_sdk_shield.types.describe_emergency_contact_settings_response
    import aws_sdk_shield.types.describe_protection_group_request
    import aws_sdk_shield.types.describe_protection_group_response
    import aws_sdk_shield.types.describe_protection_request
    import aws_sdk_shield.types.describe_protection_response
    import aws_sdk_shield.types.describe_subscription_request
    import aws_sdk_shield.types.describe_subscription_response
    import aws_sdk_shield.types.disable_application_layer_automatic_response_request
    import aws_sdk_shield.types.disable_application_layer_automatic_response_response
    import aws_sdk_shield.types.disable_proactive_engagement_request
    import aws_sdk_shield.types.disable_proactive_engagement_response
    import aws_sdk_shield.types.disassociate_drt_log_bucket_request
    import aws_sdk_shield.types.disassociate_drt_log_bucket_response
    import aws_sdk_shield.types.disassociate_drt_role_request
    import aws_sdk_shield.types.disassociate_drt_role_response
    import aws_sdk_shield.types.disassociate_health_check_request
    import aws_sdk_shield.types.disassociate_health_check_response
    import aws_sdk_shield.types.emergency_contact_list
    import aws_sdk_shield.types.enable_application_layer_automatic_response_request
    import aws_sdk_shield.types.enable_application_layer_automatic_response_response
    import aws_sdk_shield.types.enable_proactive_engagement_request
    import aws_sdk_shield.types.enable_proactive_engagement_response
    import aws_sdk_shield.types.get_subscription_state_request
    import aws_sdk_shield.types.get_subscription_state_response
    import aws_sdk_shield.types.health_check_arn
    import aws_sdk_shield.types.inclusion_protection_filters
    import aws_sdk_shield.types.inclusion_protection_group_filters
    import aws_sdk_shield.types.list_attacks_request
    import aws_sdk_shield.types.list_attacks_response
    import aws_sdk_shield.types.list_protection_groups_request
    import aws_sdk_shield.types.list_protection_groups_response
    import aws_sdk_shield.types.list_protections_request
    import aws_sdk_shield.types.list_protections_response
    import aws_sdk_shield.types.list_resources_in_protection_group_request
    import aws_sdk_shield.types.list_resources_in_protection_group_response
    import aws_sdk_shield.types.list_tags_for_resource_request
    import aws_sdk_shield.types.list_tags_for_resource_response
    import aws_sdk_shield.types.log_bucket
    import aws_sdk_shield.types.max_results
    import aws_sdk_shield.types.protected_resource_type
    import aws_sdk_shield.types.protection
    import aws_sdk_shield.types.protection_group_aggregation
    import aws_sdk_shield.types.protection_group_id
    import aws_sdk_shield.types.protection_group_members
    import aws_sdk_shield.types.protection_group_pattern
    import aws_sdk_shield.types.protection_id
    import aws_sdk_shield.types.protection_name
    import aws_sdk_shield.types.resource_arn
    import aws_sdk_shield.types.resource_arn_filter_list
    import aws_sdk_shield.types.response_action
    import aws_sdk_shield.types.role_arn
    import aws_sdk_shield.types.tag_key_list
    import aws_sdk_shield.types.tag_list
    import aws_sdk_shield.types.tag_resource_request
    import aws_sdk_shield.types.tag_resource_response
    import aws_sdk_shield.types.time_range
    import aws_sdk_shield.types.token
    import aws_sdk_shield.types.untag_resource_request
    import aws_sdk_shield.types.untag_resource_response
    import aws_sdk_shield.types.update_application_layer_automatic_response_request
    import aws_sdk_shield.types.update_application_layer_automatic_response_response
    import aws_sdk_shield.types.update_emergency_contact_settings_request
    import aws_sdk_shield.types.update_emergency_contact_settings_response
    import aws_sdk_shield.types.update_protection_group_request
    import aws_sdk_shield.types.update_protection_group_response
    import aws_sdk_shield.types.update_subscription_request
    import aws_sdk_shield.types.update_subscription_response


class AsyncShieldClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class AsyncShieldClient:
    """A client for the ``Shield`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = AsyncShieldClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncShieldClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncShieldClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def associate_drt_log_bucket(
        self,
        log_bucket: "aws_sdk_shield.types.log_bucket.LogBucket",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.associate_drt_log_bucket_response.AssociateDRTLogBucketResponse":
        r"""<p>Authorizes the Shield Response Team (SRT) to access the specified Amazon S3 bucket containing log data such as Application Load Balancer access logs, CloudFront logs, or logs from third party sources. You can associate up to 10 Amazon S3 buckets with your subscription.</p> <p>To use the services of the SRT and make an <code>AssociateDRTLogBucket</code> request, you must be subscribed to the <a href=\"http://aws.amazon.com/premiumsupport/business-support/\">Business Support plan</a> or the <a href=\"http://aws.amazon.com/premiumsupport/enterprise-support/\">Enterprise Support plan</a>.</p>

        Args:
            log_bucket: <p>The Amazon S3 bucket that contains the logs that you want to share.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.associate_drt_log_bucket_request.AssociateDRTLogBucketRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.associate_drt_log_bucket_response.AssociateDRTLogBucketResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.associate_drt_log_bucket

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.associate_drt_log_bucket.async_associate_drt_log_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.associate_drt_log_bucket_request.AssociateDRTLogBucketRequest = {}  # type: ignore[typeddict-item]
        input_["log_bucket"] = log_bucket

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_drt_role(
        self,
        role_arn: "aws_sdk_shield.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.associate_drt_role_response.AssociateDRTRoleResponse":
        r"""<p>Authorizes the Shield Response Team (SRT) using the specified role, to access your Amazon Web Services account to assist with DDoS attack mitigation during potential attacks. This enables the SRT to inspect your WAF configuration and create or update WAF rules and web ACLs.</p> <p>You can associate only one <code>RoleArn</code> with your subscription. If you submit an <code>AssociateDRTRole</code> request for an account that already has an associated role, the new <code>RoleArn</code> will replace the existing <code>RoleArn</code>. </p> <p>Prior to making the <code>AssociateDRTRole</code> request, you must attach the <code>AWSShieldDRTAccessPolicy</code> managed policy to the role that you'll specify in the request. You can access this policy in the IAM console at <a href=\"https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSShieldDRTAccessPolicy\">AWSShieldDRTAccessPolicy</a>. For more information see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html\">Adding and removing IAM identity permissions</a>. The role must also trust the service principal <code>drt.shield.amazonaws.com</code>. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html\">IAM JSON policy elements: Principal</a>.</p> <p>The SRT will have access only to your WAF and Shield resources. By submitting this request, you authorize the SRT to inspect your WAF and Shield configuration and create and update WAF rules and web ACLs on your behalf. The SRT takes these actions only if explicitly authorized by you.</p> <p>You must have the <code>iam:PassRole</code> permission to make an <code>AssociateDRTRole</code> request. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html\">Granting a user permissions to pass a role to an Amazon Web Services service</a>. </p> <p>To use the services of the SRT and make an <code>AssociateDRTRole</code> request, you must be subscribed to the <a href=\"http://aws.amazon.com/premiumsupport/business-support/\">Business Support plan</a> or the <a href=\"http://aws.amazon.com/premiumsupport/enterprise-support/\">Enterprise Support plan</a>.</p>

        Args:
            role_arn: <p>The Amazon Resource Name (ARN) of the role the SRT will use to access your Amazon Web Services account.</p> <p>Prior to making the <code>AssociateDRTRole</code> request, you must attach the <a href=\"https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSShieldDRTAccessPolicy\">AWSShieldDRTAccessPolicy</a> managed policy to this role. For more information see <a href=\" https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html\">Attaching and Detaching IAM Policies</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.associate_drt_role_request.AssociateDRTRoleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.associate_drt_role_response.AssociateDRTRoleResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.associate_drt_role

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.associate_drt_role.async_associate_drt_role(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.associate_drt_role_request.AssociateDRTRoleRequest = {}  # type: ignore[typeddict-item]
        input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_health_check(
        self,
        protection_id: "aws_sdk_shield.types.protection_id.ProtectionId",
        health_check_arn: "aws_sdk_shield.types.health_check_arn.HealthCheckArn",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.associate_health_check_response.AssociateHealthCheckResponse":
        r"""<p>Adds health-based detection to the Shield Advanced protection for a resource. Shield Advanced health-based detection uses the health of your Amazon Web Services resource to improve responsiveness and accuracy in attack detection and response. </p> <p>You define the health check in Route 53 and then associate it with your Shield Advanced protection. For more information, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html#ddos-advanced-health-check-option\">Shield Advanced Health-Based Detection</a> in the <i>WAF Developer Guide</i>. </p>

        Args:
            protection_id: <p>The unique identifier (ID) for the <a>Protection</a> object to add the health check association to. </p>
            health_check_arn: <p>The Amazon Resource Name (ARN) of the health check to associate with the protection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.associate_health_check_request.AssociateHealthCheckRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.associate_health_check_response.AssociateHealthCheckResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.associate_health_check

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.associate_health_check.async_associate_health_check(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.associate_health_check_request.AssociateHealthCheckRequest = {}  # type: ignore[typeddict-item]
        input_["protection_id"] = protection_id
        input_["health_check_arn"] = health_check_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_proactive_engagement_details(
        self,
        emergency_contact_list: "aws_sdk_shield.types.emergency_contact_list.EmergencyContactList",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.associate_proactive_engagement_details_response.AssociateProactiveEngagementDetailsResponse":
        """<p>Initializes proactive engagement and sets the list of contacts for the Shield Response Team (SRT) to use. You must provide at least one phone number in the emergency contact list. </p> <p>After you have initialized proactive engagement using this call, to disable or enable proactive engagement, use the calls <code>DisableProactiveEngagement</code> and <code>EnableProactiveEngagement</code>. </p> <note> <p>This call defines the list of email addresses and phone numbers that the SRT can use to contact you for escalations to the SRT and to initiate proactive customer support.</p> <p>The contacts that you provide in the request replace any contacts that were already defined. If you already have contacts defined and want to use them, retrieve the list using <code>DescribeEmergencyContactSettings</code> and then provide it to this call. </p> </note>

        Args:
            emergency_contact_list: <p>A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you for escalations to the SRT and to initiate proactive customer support. </p> <p>To enable proactive engagement, the contact list must include at least one phone number.</p> <note> <p>The contacts that you provide here replace any contacts that were already defined. If you already have contacts defined and want to use them, retrieve the list using <code>DescribeEmergencyContactSettings</code> and then provide it here. </p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.associate_proactive_engagement_details_request.AssociateProactiveEngagementDetailsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.associate_proactive_engagement_details_response.AssociateProactiveEngagementDetailsResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.associate_proactive_engagement_details

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.associate_proactive_engagement_details.async_associate_proactive_engagement_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.associate_proactive_engagement_details_request.AssociateProactiveEngagementDetailsRequest = {}  # type: ignore[typeddict-item]
        input_["emergency_contact_list"] = emergency_contact_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_protection(
        self,
        name: "aws_sdk_shield.types.protection_name.ProtectionName",
        resource_arn: "aws_sdk_shield.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
        tags: Optional["aws_sdk_shield.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_shield.types.create_protection_response.CreateProtectionResponse":
        r"""<p>Enables Shield Advanced for a specific Amazon Web Services resource. The resource can be an Amazon CloudFront distribution, Amazon Route 53 hosted zone, Global Accelerator standard accelerator, Elastic IP Address, Application Load Balancer, or a Classic Load Balancer. You can protect Amazon EC2 instances and Network Load Balancers by association with protected Amazon EC2 Elastic IP addresses.</p> <p>You can add protection to only a single resource with each <code>CreateProtection</code> request. You can add protection to multiple resources at once through the Shield Advanced console at <a href=\"https://console.aws.amazon.com/wafv2/shieldv2#/\">https://console.aws.amazon.com/wafv2/shieldv2#/</a>. For more information see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html\">Getting Started with Shield Advanced</a> and <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html\">Adding Shield Advanced protection to Amazon Web Services resources</a>.</p>

        Args:
            name: <p>Friendly name for the <code>Protection</code> you are creating.</p>
            resource_arn: <p>The ARN (Amazon Resource Name) of the resource to be protected.</p> <p>The ARN should be in one of the following formats:</p> <ul> <li> <p>For an Application Load Balancer: <code>arn:aws:elasticloadbalancing:<i>region</i>:<i>account-id</i>:loadbalancer/app/<i>load-balancer-name</i>/<i>load-balancer-id</i> </code> </p> </li> <li> <p>For an Elastic Load Balancer (Classic Load Balancer): <code>arn:aws:elasticloadbalancing:<i>region</i>:<i>account-id</i>:loadbalancer/<i>load-balancer-name</i> </code> </p> </li> <li> <p>For an Amazon CloudFront distribution: <code>arn:aws:cloudfront::<i>account-id</i>:distribution/<i>distribution-id</i> </code> </p> </li> <li> <p>For an Global Accelerator standard accelerator: <code>arn:aws:globalaccelerator::<i>account-id</i>:accelerator/<i>accelerator-id</i> </code> </p> </li> <li> <p>For Amazon Route 53: <code>arn:aws:route53:::hostedzone/<i>hosted-zone-id</i> </code> </p> </li> <li> <p>For an Elastic IP address: <code>arn:aws:ec2:<i>region</i>:<i>account-id</i>:eip-allocation/<i>allocation-id</i> </code> </p> </li> </ul>
            tags: <p>One or more tag key-value pairs for the <a>Protection</a> object that is created.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.create_protection_request.CreateProtectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.create_protection_response.CreateProtectionResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.create_protection

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.create_protection.async_create_protection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.create_protection_request.CreateProtectionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["resource_arn"] = resource_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_protection_group(
        self,
        protection_group_id: "aws_sdk_shield.types.protection_group_id.ProtectionGroupId",
        aggregation: "aws_sdk_shield.types.protection_group_aggregation.ProtectionGroupAggregation",
        pattern: "aws_sdk_shield.types.protection_group_pattern.ProtectionGroupPattern",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
        resource_type: Optional[
            "aws_sdk_shield.types.protected_resource_type.ProtectedResourceType"
        ] = None,
        members: Optional[
            "aws_sdk_shield.types.protection_group_members.ProtectionGroupMembers"
        ] = None,
        tags: Optional["aws_sdk_shield.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_shield.types.create_protection_group_response.CreateProtectionGroupResponse":
        """<p>Creates a grouping of protected resources so they can be handled as a collective. This resource grouping improves the accuracy of detection and reduces false positives. </p>

        Args:
            protection_group_id: <p>The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it. </p>
            aggregation: <p>Defines how Shield combines resource data for the group in order to detect, mitigate, and report events.</p> <ul> <li> <p>Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.</p> </li> <li> <p>Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.</p> </li> <li> <p>Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront and origin resources for CloudFront distributions.</p> </li> </ul>
            pattern: <p>The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource Amazon Resource Names (ARNs), or include all resources of a specified resource type. </p>
            resource_type: <p>The resource type to include in the protection group. All protected resources of this type are included in the protection group. Newly protected resources of this type are automatically added to the group. You must set this when you set <code>Pattern</code> to <code>BY_RESOURCE_TYPE</code> and you must not set it for any other <code>Pattern</code> setting. </p>
            members: <p>The Amazon Resource Names (ARNs) of the resources to include in the protection group. You must set this when you set <code>Pattern</code> to <code>ARBITRARY</code> and you must not set it for any other <code>Pattern</code> setting. </p>
            tags: <p>One or more tag key-value pairs for the protection group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.create_protection_group_request.CreateProtectionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.create_protection_group_response.CreateProtectionGroupResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.create_protection_group

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.create_protection_group.async_create_protection_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.create_protection_group_request.CreateProtectionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["protection_group_id"] = protection_group_id
        input_["aggregation"] = aggregation
        input_["pattern"] = pattern
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if members is not None:
            input_["members"] = members
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_subscription(
        self, *, config_overrides: Optional[AsyncShieldClientConfig] = None
    ) -> "aws_sdk_shield.types.create_subscription_response.CreateSubscriptionResponse":
        """<p>Activates Shield Advanced for an account.</p> <note> <p>For accounts that are members of an Organizations organization, Shield Advanced subscriptions are billed against the organization's payer account, regardless of whether the payer account itself is subscribed. </p> </note> <p>When you initially create a subscription, your subscription is set to be automatically renewed at the end of the existing subscription period. You can change this by submitting an <code>UpdateSubscription</code> request. </p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.create_subscription_request.CreateSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.create_subscription_response.CreateSubscriptionResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.create_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.create_subscription.async_create_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.create_subscription_request.CreateSubscriptionRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_protection(
        self,
        protection_id: "aws_sdk_shield.types.protection_id.ProtectionId",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.delete_protection_response.DeleteProtectionResponse":
        """<p>Deletes an Shield Advanced <a>Protection</a>.</p>

        Args:
            protection_id: <p>The unique identifier (ID) for the <a>Protection</a> object to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.delete_protection_request.DeleteProtectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.delete_protection_response.DeleteProtectionResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.delete_protection

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.delete_protection.async_delete_protection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.delete_protection_request.DeleteProtectionRequest = {}  # type: ignore[typeddict-item]
        input_["protection_id"] = protection_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_protection_group(
        self,
        protection_group_id: "aws_sdk_shield.types.protection_group_id.ProtectionGroupId",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.delete_protection_group_response.DeleteProtectionGroupResponse":
        """<p>Removes the specified protection group.</p>

        Args:
            protection_group_id: <p>The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.delete_protection_group_request.DeleteProtectionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.delete_protection_group_response.DeleteProtectionGroupResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.delete_protection_group

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.delete_protection_group.async_delete_protection_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.delete_protection_group_request.DeleteProtectionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["protection_group_id"] = protection_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_subscription(
        self, *, config_overrides: Optional[AsyncShieldClientConfig] = None
    ) -> "aws_sdk_shield.types.delete_subscription_response.DeleteSubscriptionResponse":
        """<p>Removes Shield Advanced from an account. Shield Advanced requires a 1-year subscription commitment. You cannot delete a subscription prior to the completion of that commitment. </p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.delete_subscription_request.DeleteSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.delete_subscription_response.DeleteSubscriptionResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.delete_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.delete_subscription.async_delete_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.delete_subscription_request.DeleteSubscriptionRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_attack(
        self,
        attack_id: "aws_sdk_shield.types.attack_id.AttackId",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.describe_attack_response.DescribeAttackResponse":
        """<p>Describes the details of a DDoS attack. </p>

        Args:
            attack_id: <p>The unique identifier (ID) for the attack.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.describe_attack_request.DescribeAttackRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.describe_attack_response.DescribeAttackResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.describe_attack

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.describe_attack.async_describe_attack(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.describe_attack_request.DescribeAttackRequest = {}  # type: ignore[typeddict-item]
        input_["attack_id"] = attack_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_attack_statistics(
        self, *, config_overrides: Optional[AsyncShieldClientConfig] = None
    ) -> "aws_sdk_shield.types.describe_attack_statistics_response.DescribeAttackStatisticsResponse":
        """<p>Provides information about the number and type of attacks Shield has detected in the last year for all resources that belong to your account, regardless of whether you've defined Shield protections for them. This operation is available to Shield customers as well as to Shield Advanced customers.</p> <p>The operation returns data for the time range of midnight UTC, one year ago, to midnight UTC, today. For example, if the current time is <code>2020-10-26 15:39:32 PDT</code>, equal to <code>2020-10-26 22:39:32 UTC</code>, then the time range for the attack data returned is from <code>2019-10-26 00:00:00 UTC</code> to <code>2020-10-26 00:00:00 UTC</code>. </p> <p>The time range indicates the period covered by the attack statistics data items.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.describe_attack_statistics_request.DescribeAttackStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.describe_attack_statistics_response.DescribeAttackStatisticsResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.describe_attack_statistics

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.describe_attack_statistics.async_describe_attack_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.describe_attack_statistics_request.DescribeAttackStatisticsRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_drt_access(
        self, *, config_overrides: Optional[AsyncShieldClientConfig] = None
    ) -> "aws_sdk_shield.types.describe_drt_access_response.DescribeDRTAccessResponse":
        """<p>Returns the current role and list of Amazon S3 log buckets used by the Shield Response Team (SRT) to access your Amazon Web Services account while assisting with attack mitigation.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.describe_drt_access_request.DescribeDRTAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.describe_drt_access_response.DescribeDRTAccessResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.describe_drt_access

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.describe_drt_access.async_describe_drt_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.describe_drt_access_request.DescribeDRTAccessRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_emergency_contact_settings(
        self, *, config_overrides: Optional[AsyncShieldClientConfig] = None
    ) -> "aws_sdk_shield.types.describe_emergency_contact_settings_response.DescribeEmergencyContactSettingsResponse":
        """<p>A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you if you have proactive engagement enabled, for escalations to the SRT and to initiate proactive customer support.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.describe_emergency_contact_settings_request.DescribeEmergencyContactSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.describe_emergency_contact_settings_response.DescribeEmergencyContactSettingsResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.describe_emergency_contact_settings

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.describe_emergency_contact_settings.async_describe_emergency_contact_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.describe_emergency_contact_settings_request.DescribeEmergencyContactSettingsRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_protection(
        self,
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
        protection_id: Optional[
            "aws_sdk_shield.types.protection_id.ProtectionId"
        ] = None,
        resource_arn: Optional["aws_sdk_shield.types.resource_arn.ResourceArn"] = None,
    ) -> "aws_sdk_shield.types.describe_protection_response.DescribeProtectionResponse":
        """<p>Lists the details of a <a>Protection</a> object.</p>

        Args:
            protection_id: <p>The unique identifier (ID) for the <a>Protection</a> object to describe. You must provide either the <code>ResourceArn</code> of the protected resource or the <code>ProtectionID</code> of the protection, but not both.</p>
            resource_arn: <p>The ARN (Amazon Resource Name) of the protected Amazon Web Services resource. You must provide either the <code>ResourceArn</code> of the protected resource or the <code>ProtectionID</code> of the protection, but not both.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.describe_protection_request.DescribeProtectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.describe_protection_response.DescribeProtectionResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.describe_protection

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.describe_protection.async_describe_protection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.describe_protection_request.DescribeProtectionRequest = {}  # type: ignore[typeddict-item]
        if protection_id is not None:
            input_["protection_id"] = protection_id
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_protection_group(
        self,
        protection_group_id: "aws_sdk_shield.types.protection_group_id.ProtectionGroupId",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.describe_protection_group_response.DescribeProtectionGroupResponse":
        """<p>Returns the specification for the specified protection group.</p>

        Args:
            protection_group_id: <p>The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.describe_protection_group_request.DescribeProtectionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.describe_protection_group_response.DescribeProtectionGroupResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.describe_protection_group

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.describe_protection_group.async_describe_protection_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.describe_protection_group_request.DescribeProtectionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["protection_group_id"] = protection_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_subscription(
        self, *, config_overrides: Optional[AsyncShieldClientConfig] = None
    ) -> "aws_sdk_shield.types.describe_subscription_response.DescribeSubscriptionResponse":
        """<p>Provides details about the Shield Advanced subscription for an account.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.describe_subscription_request.DescribeSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.describe_subscription_response.DescribeSubscriptionResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.describe_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.describe_subscription.async_describe_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.describe_subscription_request.DescribeSubscriptionRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disable_application_layer_automatic_response(
        self,
        resource_arn: "aws_sdk_shield.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.disable_application_layer_automatic_response_response.DisableApplicationLayerAutomaticResponseResponse":
        """<p>Disable the Shield Advanced automatic application layer DDoS mitigation feature for the protected resource. This stops Shield Advanced from creating, verifying, and applying WAF rules for attacks that it detects for the resource. </p>

        Args:
            resource_arn: <p>The ARN (Amazon Resource Name) of the protected resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.disable_application_layer_automatic_response_request.DisableApplicationLayerAutomaticResponseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.disable_application_layer_automatic_response_response.DisableApplicationLayerAutomaticResponseResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.disable_application_layer_automatic_response

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.disable_application_layer_automatic_response.async_disable_application_layer_automatic_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.disable_application_layer_automatic_response_request.DisableApplicationLayerAutomaticResponseRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disable_proactive_engagement(
        self, *, config_overrides: Optional[AsyncShieldClientConfig] = None
    ) -> "aws_sdk_shield.types.disable_proactive_engagement_response.DisableProactiveEngagementResponse":
        """<p>Removes authorization from the Shield Response Team (SRT) to notify contacts about escalations to the SRT and to initiate proactive customer support.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.disable_proactive_engagement_request.DisableProactiveEngagementRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.disable_proactive_engagement_response.DisableProactiveEngagementResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.disable_proactive_engagement

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.disable_proactive_engagement.async_disable_proactive_engagement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.disable_proactive_engagement_request.DisableProactiveEngagementRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_drt_log_bucket(
        self,
        log_bucket: "aws_sdk_shield.types.log_bucket.LogBucket",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.disassociate_drt_log_bucket_response.DisassociateDRTLogBucketResponse":
        """<p>Removes the Shield Response Team's (SRT) access to the specified Amazon S3 bucket containing the logs that you shared previously.</p>

        Args:
            log_bucket: <p>The Amazon S3 bucket that contains the logs that you want to share.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.disassociate_drt_log_bucket_request.DisassociateDRTLogBucketRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.disassociate_drt_log_bucket_response.DisassociateDRTLogBucketResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.disassociate_drt_log_bucket

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.disassociate_drt_log_bucket.async_disassociate_drt_log_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.disassociate_drt_log_bucket_request.DisassociateDRTLogBucketRequest = {}  # type: ignore[typeddict-item]
        input_["log_bucket"] = log_bucket

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_drt_role(
        self, *, config_overrides: Optional[AsyncShieldClientConfig] = None
    ) -> "aws_sdk_shield.types.disassociate_drt_role_response.DisassociateDRTRoleResponse":
        """<p>Removes the Shield Response Team's (SRT) access to your Amazon Web Services account.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.disassociate_drt_role_request.DisassociateDRTRoleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.disassociate_drt_role_response.DisassociateDRTRoleResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.disassociate_drt_role

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.disassociate_drt_role.async_disassociate_drt_role(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.disassociate_drt_role_request.DisassociateDRTRoleRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_health_check(
        self,
        protection_id: "aws_sdk_shield.types.protection_id.ProtectionId",
        health_check_arn: "aws_sdk_shield.types.health_check_arn.HealthCheckArn",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.disassociate_health_check_response.DisassociateHealthCheckResponse":
        r"""<p>Removes health-based detection from the Shield Advanced protection for a resource. Shield Advanced health-based detection uses the health of your Amazon Web Services resource to improve responsiveness and accuracy in attack detection and response. </p> <p>You define the health check in Route 53 and then associate or disassociate it with your Shield Advanced protection. For more information, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html#ddos-advanced-health-check-option\">Shield Advanced Health-Based Detection</a> in the <i>WAF Developer Guide</i>. </p>

        Args:
            protection_id: <p>The unique identifier (ID) for the <a>Protection</a> object to remove the health check association from. </p>
            health_check_arn: <p>The Amazon Resource Name (ARN) of the health check that is associated with the protection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.disassociate_health_check_request.DisassociateHealthCheckRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.disassociate_health_check_response.DisassociateHealthCheckResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.disassociate_health_check

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.disassociate_health_check.async_disassociate_health_check(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.disassociate_health_check_request.DisassociateHealthCheckRequest = {}  # type: ignore[typeddict-item]
        input_["protection_id"] = protection_id
        input_["health_check_arn"] = health_check_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def enable_application_layer_automatic_response(
        self,
        resource_arn: "aws_sdk_shield.types.resource_arn.ResourceArn",
        action: "aws_sdk_shield.types.response_action.ResponseAction",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.enable_application_layer_automatic_response_response.EnableApplicationLayerAutomaticResponseResponse":
        r"""<p>Enable the Shield Advanced automatic application layer DDoS mitigation for the protected resource. </p> <note> <p>This feature is available for Amazon CloudFront distributions and Application Load Balancers only.</p> </note> <p>This causes Shield Advanced to create, verify, and apply WAF rules for DDoS attacks that it detects for the resource. Shield Advanced applies the rules in a Shield rule group inside the web ACL that you've associated with the resource. For information about how automatic mitigation works and the requirements for using it, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-automatic-app-layer-response.html\">Shield Advanced automatic application layer DDoS mitigation</a>.</p> <note> <p>Don't use this action to make changes to automatic mitigation settings when it's already enabled for a resource. Instead, use <a>UpdateApplicationLayerAutomaticResponse</a>.</p> </note> <p>To use this feature, you must associate a web ACL with the protected resource. The web ACL must be created using the latest version of WAF (v2). You can associate the web ACL through the Shield Advanced console at <a href=\"https://console.aws.amazon.com/wafv2/shieldv2#/\">https://console.aws.amazon.com/wafv2/shieldv2#/</a>. For more information, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html\">Getting Started with Shield Advanced</a>. You can also associate the web ACL to the resource through the WAF console or the WAF API, but you must manage Shield Advanced automatic mitigation through Shield Advanced. For information about WAF, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/\">WAF Developer Guide</a>.</p>

        Args:
            resource_arn: <p>The ARN (Amazon Resource Name) of the protected resource.</p>
            action: <p>Specifies the action setting that Shield Advanced should use in the WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.enable_application_layer_automatic_response_request.EnableApplicationLayerAutomaticResponseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.enable_application_layer_automatic_response_response.EnableApplicationLayerAutomaticResponseResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.enable_application_layer_automatic_response

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.enable_application_layer_automatic_response.async_enable_application_layer_automatic_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.enable_application_layer_automatic_response_request.EnableApplicationLayerAutomaticResponseRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["action"] = action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def enable_proactive_engagement(
        self, *, config_overrides: Optional[AsyncShieldClientConfig] = None
    ) -> "aws_sdk_shield.types.enable_proactive_engagement_response.EnableProactiveEngagementResponse":
        """<p>Authorizes the Shield Response Team (SRT) to use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.enable_proactive_engagement_request.EnableProactiveEngagementRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.enable_proactive_engagement_response.EnableProactiveEngagementResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.enable_proactive_engagement

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.enable_proactive_engagement.async_enable_proactive_engagement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.enable_proactive_engagement_request.EnableProactiveEngagementRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_subscription_state(
        self, *, config_overrides: Optional[AsyncShieldClientConfig] = None
    ) -> "aws_sdk_shield.types.get_subscription_state_response.GetSubscriptionStateResponse":
        """<p>Returns the <code>SubscriptionState</code>, either <code>Active</code> or <code>Inactive</code>.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.get_subscription_state_request.GetSubscriptionStateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.get_subscription_state_response.GetSubscriptionStateResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.get_subscription_state

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.get_subscription_state.async_get_subscription_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.get_subscription_state_request.GetSubscriptionStateRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_attacks(
        self,
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
        resource_arns: Optional[
            "aws_sdk_shield.types.resource_arn_filter_list.ResourceArnFilterList"
        ] = None,
        start_time: Optional["aws_sdk_shield.types.time_range.TimeRange"] = None,
        end_time: Optional["aws_sdk_shield.types.time_range.TimeRange"] = None,
        next_token: Optional["aws_sdk_shield.types.token.Token"] = None,
        max_results: Optional["aws_sdk_shield.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_shield.types.list_attacks_response.ListAttacksResponse":
        r"""<p>Returns all ongoing DDoS attacks or all DDoS attacks during a specified time period.</p>

        Args:
            resource_arns: <p>The ARNs (Amazon Resource Names) of the resources that were attacked. If you leave this blank, all applicable resources for this account will be included.</p>
            start_time: <p>The start of the time period for the attacks. This is a <code>timestamp</code> type. The request syntax listing for this call indicates a <code>number</code> type, but you can provide the time in any valid <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp\">timestamp format</a> setting. </p>
            end_time: <p>The end of the time period for the attacks. This is a <code>timestamp</code> type. The request syntax listing for this call indicates a <code>number</code> type, but you can provide the time in any valid <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp\">timestamp format</a> setting. </p>
            next_token: <p>When you request a list of objects from Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a <code>NextToken</code> value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request. </p> <p>You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the <code>MaxResults</code> setting. Shield Advanced will not return more than <code>MaxResults</code> objects, but may return fewer, even if more objects are still available.</p> <p>Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a <code>NextToken</code> value.</p> <p>On your first call to a list operation, leave this setting empty.</p>
            max_results: <p>The greatest number of objects that you want Shield Advanced to return to the list request. Shield Advanced might return fewer objects than you indicate in this setting, even if more objects are available. If there are more objects remaining, Shield Advanced will always also return a <code>NextToken</code> value in the response.</p> <p>The default setting is 20.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.list_attacks_request.ListAttacksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.list_attacks_response.ListAttacksResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.list_attacks

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.list_attacks.async_list_attacks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.list_attacks_request.ListAttacksRequest = {}  # type: ignore[typeddict-item]
        if resource_arns is not None:
            input_["resource_arns"] = resource_arns
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_attacks(
        self,
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
        resource_arns: Optional[
            "aws_sdk_shield.types.resource_arn_filter_list.ResourceArnFilterList"
        ] = None,
        start_time: Optional["aws_sdk_shield.types.time_range.TimeRange"] = None,
        end_time: Optional["aws_sdk_shield.types.time_range.TimeRange"] = None,
        next_token: Optional["aws_sdk_shield.types.token.Token"] = None,
        max_results: Optional["aws_sdk_shield.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_shield.types.attack_summary.AttackSummary]":
        _token = next_token
        while True:
            _response = await self.list_attacks(
                config_overrides=config_overrides,
                resource_arns=resource_arns,
                start_time=start_time,
                end_time=end_time,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("attack_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_protection_groups(
        self,
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
        next_token: Optional["aws_sdk_shield.types.token.Token"] = None,
        max_results: Optional["aws_sdk_shield.types.max_results.MaxResults"] = None,
        inclusion_filters: Optional[
            "aws_sdk_shield.types.inclusion_protection_group_filters.InclusionProtectionGroupFilters"
        ] = None,
    ) -> "aws_sdk_shield.types.list_protection_groups_response.ListProtectionGroupsResponse":
        """<p>Retrieves <a>ProtectionGroup</a> objects for the account. You can retrieve all protection groups or you can provide filtering criteria and retrieve just the subset of protection groups that match the criteria. </p>

        Args:
            next_token: <p>When you request a list of objects from Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a <code>NextToken</code> value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request. </p> <p>You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the <code>MaxResults</code> setting. Shield Advanced will not return more than <code>MaxResults</code> objects, but may return fewer, even if more objects are still available.</p> <p>Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a <code>NextToken</code> value.</p> <p>On your first call to a list operation, leave this setting empty.</p>
            max_results: <p>The greatest number of objects that you want Shield Advanced to return to the list request. Shield Advanced might return fewer objects than you indicate in this setting, even if more objects are available. If there are more objects remaining, Shield Advanced will always also return a <code>NextToken</code> value in the response.</p> <p>The default setting is 20.</p>
            inclusion_filters: <p>Narrows the set of protection groups that the call retrieves. You can retrieve a single protection group by its name and you can retrieve all protection groups that are configured with specific pattern or aggregation settings. You can provide up to one criteria per filter type. Shield Advanced returns the protection groups that exactly match all of the search criteria that you provide.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.list_protection_groups_request.ListProtectionGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.list_protection_groups_response.ListProtectionGroupsResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.list_protection_groups

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.list_protection_groups.async_list_protection_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.list_protection_groups_request.ListProtectionGroupsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if inclusion_filters is not None:
            input_["inclusion_filters"] = inclusion_filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_protections(
        self,
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
        next_token: Optional["aws_sdk_shield.types.token.Token"] = None,
        max_results: Optional["aws_sdk_shield.types.max_results.MaxResults"] = None,
        inclusion_filters: Optional[
            "aws_sdk_shield.types.inclusion_protection_filters.InclusionProtectionFilters"
        ] = None,
    ) -> "aws_sdk_shield.types.list_protections_response.ListProtectionsResponse":
        """<p>Retrieves <a>Protection</a> objects for the account. You can retrieve all protections or you can provide filtering criteria and retrieve just the subset of protections that match the criteria. </p>

        Args:
            next_token: <p>When you request a list of objects from Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a <code>NextToken</code> value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request. </p> <p>You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the <code>MaxResults</code> setting. Shield Advanced will not return more than <code>MaxResults</code> objects, but may return fewer, even if more objects are still available.</p> <p>Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a <code>NextToken</code> value.</p> <p>On your first call to a list operation, leave this setting empty.</p>
            max_results: <p>The greatest number of objects that you want Shield Advanced to return to the list request. Shield Advanced might return fewer objects than you indicate in this setting, even if more objects are available. If there are more objects remaining, Shield Advanced will always also return a <code>NextToken</code> value in the response.</p> <p>The default setting is 20.</p>
            inclusion_filters: <p>Narrows the set of protections that the call retrieves. You can retrieve a single protection by providing its name or the ARN (Amazon Resource Name) of its protected resource. You can also retrieve all protections for a specific resource type. You can provide up to one criteria per filter type. Shield Advanced returns protections that exactly match all of the filter criteria that you provide.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.list_protections_request.ListProtectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.list_protections_response.ListProtectionsResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.list_protections

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.list_protections.async_list_protections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.list_protections_request.ListProtectionsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if inclusion_filters is not None:
            input_["inclusion_filters"] = inclusion_filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_protections(
        self,
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
        next_token: Optional["aws_sdk_shield.types.token.Token"] = None,
        max_results: Optional["aws_sdk_shield.types.max_results.MaxResults"] = None,
        inclusion_filters: Optional[
            "aws_sdk_shield.types.inclusion_protection_filters.InclusionProtectionFilters"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_shield.types.protection.Protection]":
        _token = next_token
        while True:
            _response = await self.list_protections(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                inclusion_filters=inclusion_filters,
            )
            _page = _resolve_path(_response, ("protections",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resources_in_protection_group(
        self,
        protection_group_id: "aws_sdk_shield.types.protection_group_id.ProtectionGroupId",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
        next_token: Optional["aws_sdk_shield.types.token.Token"] = None,
        max_results: Optional["aws_sdk_shield.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_shield.types.list_resources_in_protection_group_response.ListResourcesInProtectionGroupResponse":
        """<p>Retrieves the resources that are included in the protection group. </p>

        Args:
            protection_group_id: <p>The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it. </p>
            next_token: <p>When you request a list of objects from Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a <code>NextToken</code> value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request. </p> <p>You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the <code>MaxResults</code> setting. Shield Advanced will not return more than <code>MaxResults</code> objects, but may return fewer, even if more objects are still available.</p> <p>Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a <code>NextToken</code> value.</p> <p>On your first call to a list operation, leave this setting empty.</p>
            max_results: <p>The greatest number of objects that you want Shield Advanced to return to the list request. Shield Advanced might return fewer objects than you indicate in this setting, even if more objects are available. If there are more objects remaining, Shield Advanced will always also return a <code>NextToken</code> value in the response.</p> <p>The default setting is 20.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.list_resources_in_protection_group_request.ListResourcesInProtectionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.list_resources_in_protection_group_response.ListResourcesInProtectionGroupResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.list_resources_in_protection_group

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.list_resources_in_protection_group.async_list_resources_in_protection_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.list_resources_in_protection_group_request.ListResourcesInProtectionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["protection_group_id"] = protection_group_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_shield.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Gets information about Amazon Web Services tags for a specified Amazon Resource Name (ARN) in Shield.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to get tags for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_shield.types.resource_arn.ResourceArn",
        tags: "aws_sdk_shield.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for a resource in Shield.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to add or update tags for.</p>
            tags: <p>The tags that you want to modify or add to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_shield.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_shield.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource in Shield.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from.</p>
            tag_keys: <p>The tag key for each tag that you want to remove from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_application_layer_automatic_response(
        self,
        resource_arn: "aws_sdk_shield.types.resource_arn.ResourceArn",
        action: "aws_sdk_shield.types.response_action.ResponseAction",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
    ) -> "aws_sdk_shield.types.update_application_layer_automatic_response_response.UpdateApplicationLayerAutomaticResponseResponse":
        """<p>Updates an existing Shield Advanced automatic application layer DDoS mitigation configuration for the specified resource.</p>

        Args:
            resource_arn: <p>The ARN (Amazon Resource Name) of the resource.</p>
            action: <p>Specifies the action setting that Shield Advanced should use in the WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.update_application_layer_automatic_response_request.UpdateApplicationLayerAutomaticResponseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.update_application_layer_automatic_response_response.UpdateApplicationLayerAutomaticResponseResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.update_application_layer_automatic_response

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.update_application_layer_automatic_response.async_update_application_layer_automatic_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.update_application_layer_automatic_response_request.UpdateApplicationLayerAutomaticResponseRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["action"] = action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_emergency_contact_settings(
        self,
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
        emergency_contact_list: Optional[
            "aws_sdk_shield.types.emergency_contact_list.EmergencyContactList"
        ] = None,
    ) -> "aws_sdk_shield.types.update_emergency_contact_settings_response.UpdateEmergencyContactSettingsResponse":
        """<p>Updates the details of the list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you if you have proactive engagement enabled, for escalations to the SRT and to initiate proactive customer support.</p>

        Args:
            emergency_contact_list: <p>A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you if you have proactive engagement enabled, for escalations to the SRT and to initiate proactive customer support.</p> <p>If you have proactive engagement enabled, the contact list must include at least one phone number.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.update_emergency_contact_settings_request.UpdateEmergencyContactSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.update_emergency_contact_settings_response.UpdateEmergencyContactSettingsResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.update_emergency_contact_settings

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.update_emergency_contact_settings.async_update_emergency_contact_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.update_emergency_contact_settings_request.UpdateEmergencyContactSettingsRequest = {}  # type: ignore[typeddict-item]
        if emergency_contact_list is not None:
            input_["emergency_contact_list"] = emergency_contact_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_protection_group(
        self,
        protection_group_id: "aws_sdk_shield.types.protection_group_id.ProtectionGroupId",
        aggregation: "aws_sdk_shield.types.protection_group_aggregation.ProtectionGroupAggregation",
        pattern: "aws_sdk_shield.types.protection_group_pattern.ProtectionGroupPattern",
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
        resource_type: Optional[
            "aws_sdk_shield.types.protected_resource_type.ProtectedResourceType"
        ] = None,
        members: Optional[
            "aws_sdk_shield.types.protection_group_members.ProtectionGroupMembers"
        ] = None,
    ) -> "aws_sdk_shield.types.update_protection_group_response.UpdateProtectionGroupResponse":
        """<p>Updates an existing protection group. A protection group is a grouping of protected resources so they can be handled as a collective. This resource grouping improves the accuracy of detection and reduces false positives. </p>

        Args:
            protection_group_id: <p>The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it. </p>
            aggregation: <p>Defines how Shield combines resource data for the group in order to detect, mitigate, and report events.</p> <ul> <li> <p>Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.</p> </li> <li> <p>Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.</p> </li> <li> <p>Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront distributions and origin resources for CloudFront distributions.</p> </li> </ul>
            pattern: <p>The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource Amazon Resource Names (ARNs), or include all resources of a specified resource type.</p>
            resource_type: <p>The resource type to include in the protection group. All protected resources of this type are included in the protection group. You must set this when you set <code>Pattern</code> to <code>BY_RESOURCE_TYPE</code> and you must not set it for any other <code>Pattern</code> setting. </p>
            members: <p>The Amazon Resource Names (ARNs) of the resources to include in the protection group. You must set this when you set <code>Pattern</code> to <code>ARBITRARY</code> and you must not set it for any other <code>Pattern</code> setting. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.update_protection_group_request.UpdateProtectionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.update_protection_group_response.UpdateProtectionGroupResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.update_protection_group

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.update_protection_group.async_update_protection_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.update_protection_group_request.UpdateProtectionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["protection_group_id"] = protection_group_id
        input_["aggregation"] = aggregation
        input_["pattern"] = pattern
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if members is not None:
            input_["members"] = members

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_subscription(
        self,
        *,
        config_overrides: Optional[AsyncShieldClientConfig] = None,
        auto_renew: Optional["aws_sdk_shield.types.auto_renew.AutoRenew"] = None,
    ) -> "aws_sdk_shield.types.update_subscription_response.UpdateSubscriptionResponse":
        """<p>Updates the details of an existing subscription. Only enter values for parameters you want to change. Empty parameters are not updated.</p> <note> <p>For accounts that are members of an Organizations organization, Shield Advanced subscriptions are billed against the organization's payer account, regardless of whether the payer account itself is subscribed. </p> </note>

        Args:
            auto_renew: <p>When you initally create a subscription, <code>AutoRenew</code> is set to <code>ENABLED</code>. If <code>ENABLED</code>, the subscription will be automatically renewed at the end of the existing subscription period. You can change this by submitting an <code>UpdateSubscription</code> request. If the <code>UpdateSubscription</code> request does not included a value for <code>AutoRenew</code>, the existing value for <code>AutoRenew</code> remains unchanged.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_shield.types.update_subscription_request.UpdateSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_shield.types.update_subscription_response.UpdateSubscriptionResponse"
        ]:
            import aws_sdk_shield._operations.aws_shield_20160616.update_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_shield._operations.aws_shield_20160616.update_subscription.async_update_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_shield.types.update_subscription_request.UpdateSubscriptionRequest = {}  # type: ignore[typeddict-item]
        if auto_renew is not None:
            input_["auto_renew"] = auto_renew

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
