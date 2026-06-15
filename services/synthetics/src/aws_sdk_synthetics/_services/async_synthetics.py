"""Generated from Smithy shape ``com.amazonaws.synthetics#Synthetics``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_synthetics._auth._signers
import aws_sdk_synthetics._auth._sigv4
from aws_sdk_synthetics._auth._identity import Credentials
from aws_sdk_synthetics._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_synthetics._auth._zapros_handler import AuthMiddleware
from aws_sdk_synthetics._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.artifact_config_input
    import aws_sdk_synthetics.types.associate_resource_request
    import aws_sdk_synthetics.types.associate_resource_response
    import aws_sdk_synthetics.types.boolean
    import aws_sdk_synthetics.types.browser_configs
    import aws_sdk_synthetics.types.browser_type
    import aws_sdk_synthetics.types.canary_arn
    import aws_sdk_synthetics.types.canary_code_input
    import aws_sdk_synthetics.types.canary_name
    import aws_sdk_synthetics.types.canary_run_config_input
    import aws_sdk_synthetics.types.canary_schedule_input
    import aws_sdk_synthetics.types.create_canary_request
    import aws_sdk_synthetics.types.create_canary_response
    import aws_sdk_synthetics.types.create_group_request
    import aws_sdk_synthetics.types.create_group_response
    import aws_sdk_synthetics.types.delete_canary_request
    import aws_sdk_synthetics.types.delete_canary_response
    import aws_sdk_synthetics.types.delete_group_request
    import aws_sdk_synthetics.types.delete_group_response
    import aws_sdk_synthetics.types.describe_canaries_last_run_name_filter
    import aws_sdk_synthetics.types.describe_canaries_last_run_request
    import aws_sdk_synthetics.types.describe_canaries_last_run_response
    import aws_sdk_synthetics.types.describe_canaries_name_filter
    import aws_sdk_synthetics.types.describe_canaries_request
    import aws_sdk_synthetics.types.describe_canaries_response
    import aws_sdk_synthetics.types.describe_runtime_versions_request
    import aws_sdk_synthetics.types.describe_runtime_versions_response
    import aws_sdk_synthetics.types.disassociate_resource_request
    import aws_sdk_synthetics.types.disassociate_resource_response
    import aws_sdk_synthetics.types.get_canary_request
    import aws_sdk_synthetics.types.get_canary_response
    import aws_sdk_synthetics.types.get_canary_runs_request
    import aws_sdk_synthetics.types.get_canary_runs_response
    import aws_sdk_synthetics.types.get_group_request
    import aws_sdk_synthetics.types.get_group_response
    import aws_sdk_synthetics.types.group_identifier
    import aws_sdk_synthetics.types.group_name
    import aws_sdk_synthetics.types.list_associated_groups_request
    import aws_sdk_synthetics.types.list_associated_groups_response
    import aws_sdk_synthetics.types.list_group_resources_request
    import aws_sdk_synthetics.types.list_group_resources_response
    import aws_sdk_synthetics.types.list_groups_request
    import aws_sdk_synthetics.types.list_groups_response
    import aws_sdk_synthetics.types.list_tags_for_resource_request
    import aws_sdk_synthetics.types.list_tags_for_resource_response
    import aws_sdk_synthetics.types.max_canary_results
    import aws_sdk_synthetics.types.max_group_results
    import aws_sdk_synthetics.types.max_size100
    import aws_sdk_synthetics.types.max_size1024
    import aws_sdk_synthetics.types.pagination_token
    import aws_sdk_synthetics.types.provisioned_resource_cleanup_setting
    import aws_sdk_synthetics.types.resource_arn
    import aws_sdk_synthetics.types.resource_list
    import aws_sdk_synthetics.types.role_arn
    import aws_sdk_synthetics.types.run_type
    import aws_sdk_synthetics.types.start_canary_dry_run_request
    import aws_sdk_synthetics.types.start_canary_dry_run_response
    import aws_sdk_synthetics.types.start_canary_request
    import aws_sdk_synthetics.types.start_canary_response
    import aws_sdk_synthetics.types.stop_canary_request
    import aws_sdk_synthetics.types.stop_canary_response
    import aws_sdk_synthetics.types.string
    import aws_sdk_synthetics.types.tag_key_list
    import aws_sdk_synthetics.types.tag_map
    import aws_sdk_synthetics.types.tag_resource_request
    import aws_sdk_synthetics.types.tag_resource_response
    import aws_sdk_synthetics.types.token
    import aws_sdk_synthetics.types.untag_resource_request
    import aws_sdk_synthetics.types.untag_resource_response
    import aws_sdk_synthetics.types.update_canary_request
    import aws_sdk_synthetics.types.update_canary_response
    import aws_sdk_synthetics.types.uuid
    import aws_sdk_synthetics.types.visual_reference_input
    import aws_sdk_synthetics.types.visual_references
    import aws_sdk_synthetics.types.vpc_config_input


class AsyncsyntheticsClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncsyntheticsClient:
    """A client for the ``synthetics`` service.

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
        self._config = AsyncsyntheticsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncsyntheticsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncsyntheticsClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
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

    async def associate_resource(
        self,
        group_identifier: "aws_sdk_synthetics.types.group_identifier.GroupIdentifier",
        resource_arn: "aws_sdk_synthetics.types.canary_arn.CanaryArn",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
    ) -> (
        "aws_sdk_synthetics.types.associate_resource_response.AssociateResourceResponse"
    ):
        """<p>Associates a canary with a group. Using groups can help you with managing and automating your canaries, and you can also view aggregated run results and statistics for all canaries in a group. </p> <p>You must run this operation in the Region where the canary exists.</p>

        Args:
            group_identifier: <p>Specifies the group. You can specify the group name, the ARN, or the group ID as the <code>GroupIdentifier</code>.</p>
            resource_arn: <p>The ARN of the canary that you want to associate with the specified group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.associate_resource_request.AssociateResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.associate_resource_response.AssociateResourceResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.associate_resource

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.associate_resource.async_associate_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.associate_resource_request.AssociateResourceRequest = {}  # type: ignore[typeddict-item]
        input_["group_identifier"] = group_identifier
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_canary(
        self,
        name: "aws_sdk_synthetics.types.canary_name.CanaryName",
        code: "aws_sdk_synthetics.types.canary_code_input.CanaryCodeInput",
        artifact_s3_location: "aws_sdk_synthetics.types.string.String",
        execution_role_arn: "aws_sdk_synthetics.types.role_arn.RoleArn",
        schedule: "aws_sdk_synthetics.types.canary_schedule_input.CanaryScheduleInput",
        runtime_version: "aws_sdk_synthetics.types.string.String",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
        run_config: Optional[
            "aws_sdk_synthetics.types.canary_run_config_input.CanaryRunConfigInput"
        ] = None,
        success_retention_period_in_days: Optional[
            "aws_sdk_synthetics.types.max_size1024.MaxSize1024"
        ] = None,
        failure_retention_period_in_days: Optional[
            "aws_sdk_synthetics.types.max_size1024.MaxSize1024"
        ] = None,
        vpc_config: Optional[
            "aws_sdk_synthetics.types.vpc_config_input.VpcConfigInput"
        ] = None,
        resources_to_replicate_tags: Optional[
            "aws_sdk_synthetics.types.resource_list.ResourceList"
        ] = None,
        provisioned_resource_cleanup: Optional[
            "aws_sdk_synthetics.types.provisioned_resource_cleanup_setting.ProvisionedResourceCleanupSetting"
        ] = None,
        browser_configs: Optional[
            "aws_sdk_synthetics.types.browser_configs.BrowserConfigs"
        ] = None,
        tags: Optional["aws_sdk_synthetics.types.tag_map.TagMap"] = None,
        artifact_config: Optional[
            "aws_sdk_synthetics.types.artifact_config_input.ArtifactConfigInput"
        ] = None,
    ) -> "aws_sdk_synthetics.types.create_canary_response.CreateCanaryResponse":
        r"""<p>Creates a canary. Canaries are scripts that monitor your endpoints and APIs from the outside-in. Canaries help you check the availability and latency of your web services and troubleshoot anomalies by investigating load time data, screenshots of the UI, logs, and metrics. You can set up a canary to run continuously or just once. </p> <p>Do not use <code>CreateCanary</code> to modify an existing canary. Use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UpdateCanary.html\">UpdateCanary</a> instead.</p> <p>To create canaries, you must have the <code>CloudWatchSyntheticsFullAccess</code> policy. If you are creating a new IAM role for the canary, you also need the <code>iam:CreateRole</code>, <code>iam:CreatePolicy</code> and <code>iam:AttachRolePolicy</code> permissions. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Roles\">Necessary Roles and Permissions</a>.</p> <p>Do not include secrets or proprietary information in your canary names. The canary name makes up part of the Amazon Resource Name (ARN) for the canary, and the ARN is included in outbound calls over the internet. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html\">Security Considerations for Synthetics Canaries</a>.</p>

        Args:
            name: <p>The name for this canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account.</p> <p>Do not include secrets or proprietary information in your canary names. The canary name makes up part of the canary ARN, and the ARN is included in outbound calls over the internet. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html\">Security Considerations for Synthetics Canaries</a>.</p>
            code: <p>A structure that includes the entry point from which the canary should start running your script. If the script is stored in an Amazon S3 bucket, the bucket name, key, and version are also included. </p>
            artifact_s3_location: <p>The location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary. Artifacts include the log file, screenshots, and HAR files. The name of the Amazon S3 bucket can't include a period (.).</p>
            execution_role_arn: <p>The ARN of the IAM role to be used to run the canary. This role must already exist, and must include <code>lambda.amazonaws.com</code> as a principal in the trust policy. The role must also have the following permissions:</p> <ul> <li> <p> <code>s3:PutObject</code> </p> </li> <li> <p> <code>s3:GetBucketLocation</code> </p> </li> <li> <p> <code>s3:ListAllMyBuckets</code> </p> </li> <li> <p> <code>cloudwatch:PutMetricData</code> </p> </li> <li> <p> <code>logs:CreateLogGroup</code> </p> </li> <li> <p> <code>logs:CreateLogStream</code> </p> </li> <li> <p> <code>logs:PutLogEvents</code> </p> </li> </ul>
            schedule: <p>A structure that contains information about how often the canary is to run and when these test runs are to stop.</p>
            run_config: <p>A structure that contains the configuration for individual canary runs, such as timeout value and environment variables.</p> <important> <p>Environment variable keys and values are encrypted at rest using Amazon Web Services owned KMS keys. However, the environment variables are not encrypted on the client side. Do not store sensitive information in them.</p> </important>
            success_retention_period_in_days: <p>The number of days to retain data about successful runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.</p> <p>This setting affects the range of information returned by <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html\">GetCanaryRuns</a>, as well as the range of information displayed in the Synthetics console. </p>
            failure_retention_period_in_days: <p>The number of days to retain data about failed runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.</p> <p>This setting affects the range of information returned by <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html\">GetCanaryRuns</a>, as well as the range of information displayed in the Synthetics console. </p>
            runtime_version: <p>Specifies the runtime version to use for the canary. For a list of valid runtime versions and more information about runtime versions, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html\"> Canary Runtime Versions</a>.</p>
            vpc_config: <p>If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html\"> Running a Canary in a VPC</a>.</p>
            resources_to_replicate_tags: <p>To have the tags that you apply to this canary also be applied to the Lambda function that the canary uses, specify this parameter with the value <code>lambda-function</code>.</p> <p>If you specify this parameter and don't specify any tags in the <code>Tags</code> parameter, the canary creation fails.</p>
            provisioned_resource_cleanup: <p>Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted. If you omit this parameter, the default of <code>AUTOMATIC</code> is used, which means that the Lambda functions and layers will be deleted when the canary is deleted.</p> <p>If the value of this parameter is <code>OFF</code>, then the value of the <code>DeleteLambda</code> parameter of the <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html\">DeleteCanary</a> operation determines whether the Lambda functions and layers will be deleted.</p>
            browser_configs: <p>CloudWatch Synthetics now supports multibrowser canaries for <code>syn-nodejs-puppeteer-11.0</code> and <code>syn-nodejs-playwright-3.0</code> runtimes. This feature allows you to run your canaries on both Firefox and Chrome browsers. To create a multibrowser canary, you need to specify the BrowserConfigs with a list of browsers you want to use.</p> <note> <p>If not specified, <code>browserConfigs</code> defaults to Chrome.</p> </note>
            tags: <p>A list of key-value pairs to associate with the canary. You can associate as many as 50 tags with a canary.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only the resources that have certain tag values.</p> <p>To have the tags that you apply to this canary also be applied to the Lambda function that the canary uses, specify this parameter with the value <code>lambda-function</code>.</p>
            artifact_config: <p>A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.create_canary_request.CreateCanaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.create_canary_response.CreateCanaryResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.create_canary

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.create_canary.async_create_canary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.create_canary_request.CreateCanaryRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["code"] = code
        input_["artifact_s3_location"] = artifact_s3_location
        input_["execution_role_arn"] = execution_role_arn
        input_["schedule"] = schedule
        if run_config is not None:
            input_["run_config"] = run_config
        if success_retention_period_in_days is not None:
            input_["success_retention_period_in_days"] = (
                success_retention_period_in_days
            )
        if failure_retention_period_in_days is not None:
            input_["failure_retention_period_in_days"] = (
                failure_retention_period_in_days
            )
        input_["runtime_version"] = runtime_version
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if resources_to_replicate_tags is not None:
            input_["resources_to_replicate_tags"] = resources_to_replicate_tags
        if provisioned_resource_cleanup is not None:
            input_["provisioned_resource_cleanup"] = provisioned_resource_cleanup
        if browser_configs is not None:
            input_["browser_configs"] = browser_configs
        if tags is not None:
            input_["tags"] = tags
        if artifact_config is not None:
            input_["artifact_config"] = artifact_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_group(
        self,
        name: "aws_sdk_synthetics.types.group_name.GroupName",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
        tags: Optional["aws_sdk_synthetics.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_synthetics.types.create_group_response.CreateGroupResponse":
        r"""<p>Creates a group which you can use to associate canaries with each other, including cross-Region canaries. Using groups can help you with managing and automating your canaries, and you can also view aggregated run results and statistics for all canaries in a group. </p> <p>Groups are global resources. When you create a group, it is replicated across Amazon Web Services Regions, and you can view it and add canaries to it from any Region. Although the group ARN format reflects the Region name where it was created, a group is not constrained to any Region. This means that you can put canaries from multiple Regions into the same group, and then use that group to view and manage all of those canaries in a single view.</p> <p>Groups are supported in all Regions except the Regions that are disabled by default. For more information about these Regions, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable\">Enabling a Region</a>.</p> <p>Each group can contain as many as 10 canaries. You can have as many as 20 groups in your account. Any single canary can be a member of up to 10 groups.</p>

        Args:
            name: <p>The name for the group. It can include any Unicode characters.</p> <p>The names for all groups in your account, across all Regions, must be unique.</p>
            tags: <p>A list of key-value pairs to associate with the group. You can associate as many as 50 tags with a group.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only the resources that have certain tag values.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.create_group_request.CreateGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.create_group_response.CreateGroupResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.create_group

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.create_group.async_create_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.create_group_request.CreateGroupRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_canary(
        self,
        name: "aws_sdk_synthetics.types.canary_name.CanaryName",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
        delete_lambda: Optional["aws_sdk_synthetics.types.boolean.boolean"] = None,
    ) -> "aws_sdk_synthetics.types.delete_canary_response.DeleteCanaryResponse":
        r"""<p>Permanently deletes the specified canary.</p> <p>If the canary's <code>ProvisionedResourceCleanup</code> field is set to <code>AUTOMATIC</code> or you specify <code>DeleteLambda</code> in this operation as <code>true</code>, CloudWatch Synthetics also deletes the Lambda functions and layers that are used by the canary.</p> <p>Other resources used and created by the canary are not automatically deleted. After you delete a canary, you should also delete the following:</p> <ul> <li> <p>The CloudWatch alarms created for this canary. These alarms have a name of <code>Synthetics-Alarm-<i>first-198-characters-of-canary-name</i>-<i>canaryId</i>-<i>alarm number</i> </code> </p> </li> <li> <p>Amazon S3 objects and buckets, such as the canary's artifact location.</p> </li> <li> <p>IAM roles created for the canary. If they were created in the console, these roles have the name <code> role/service-role/CloudWatchSyntheticsRole-<i>First-21-Characters-of-CanaryName</i> </code> </p> </li> <li> <p>CloudWatch Logs log groups created for the canary. These logs groups have the name <code>/aws/lambda/cwsyn-<i>First-21-Characters-of-CanaryName</i> </code> </p> </li> </ul> <p>Before you delete a canary, you might want to use <code>GetCanary</code> to display the information about this canary. Make note of the information returned by this operation so that you can delete these resources after you delete the canary.</p>

        Args:
            name: <p>The name of the canary that you want to delete. To find the names of your canaries, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\">DescribeCanaries</a>.</p>
            delete_lambda: <p>Specifies whether to also delete the Lambda functions and layers used by this canary. The default is <code>false</code>.</p> <p>Your setting for this parameter is used only if the canary doesn't have <code>AUTOMATIC</code> for its <code>ProvisionedResourceCleanup</code> field. If that field is set to <code>AUTOMATIC</code>, then the Lambda functions and layers will be deleted when this canary is deleted. </p> <p>Type: Boolean</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.delete_canary_request.DeleteCanaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.delete_canary_response.DeleteCanaryResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.delete_canary

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.delete_canary.async_delete_canary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.delete_canary_request.DeleteCanaryRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if delete_lambda is not None:
            input_["delete_lambda"] = delete_lambda

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_group(
        self,
        group_identifier: "aws_sdk_synthetics.types.group_identifier.GroupIdentifier",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
    ) -> "aws_sdk_synthetics.types.delete_group_response.DeleteGroupResponse":
        """<p>Deletes a group. The group doesn't need to be empty to be deleted. If there are canaries in the group, they are not deleted when you delete the group. </p> <p>Groups are a global resource that appear in all Regions, but the request to delete a group must be made from its home Region. You can find the home Region of a group within its ARN.</p>

        Args:
            group_identifier: <p>Specifies which group to delete. You can specify the group name, the ARN, or the group ID as the <code>GroupIdentifier</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.delete_group_request.DeleteGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.delete_group_response.DeleteGroupResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.delete_group

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.delete_group.async_delete_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.delete_group_request.DeleteGroupRequest = {}  # type: ignore[typeddict-item]
        input_["group_identifier"] = group_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_canaries(
        self,
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
        next_token: Optional["aws_sdk_synthetics.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_synthetics.types.max_canary_results.MaxCanaryResults"
        ] = None,
        names: Optional[
            "aws_sdk_synthetics.types.describe_canaries_name_filter.DescribeCanariesNameFilter"
        ] = None,
    ) -> "aws_sdk_synthetics.types.describe_canaries_response.DescribeCanariesResponse":
        r"""<p>This operation returns a list of the canaries in your account, along with full details about each canary.</p> <p>This operation supports resource-level authorization using an IAM policy and the <code>Names</code> parameter. If you specify the <code>Names</code> parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.</p> <p>You are required to use the <code>Names</code> parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html\"> Limiting a user to viewing specific canaries</a>.</p>

        Args:
            next_token: <p>A token that indicates that there is more data available. You can use this token in a subsequent operation to retrieve the next set of results.</p>
            max_results: <p>Specify this parameter to limit how many canaries are returned each time you use the <code>DescribeCanaries</code> operation. If you omit this parameter, the default of 20 is used.</p>
            names: <p>Use this parameter to return only canaries that match the names that you specify here. You can specify as many as five canary names.</p> <p>If you specify this parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.</p> <p>You are required to use this parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html\"> Limiting a user to viewing specific canaries</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.describe_canaries_request.DescribeCanariesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.describe_canaries_response.DescribeCanariesResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.describe_canaries

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.describe_canaries.async_describe_canaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.describe_canaries_request.DescribeCanariesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if names is not None:
            input_["names"] = names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_canaries_last_run(
        self,
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
        next_token: Optional["aws_sdk_synthetics.types.token.Token"] = None,
        max_results: Optional["aws_sdk_synthetics.types.max_size100.MaxSize100"] = None,
        names: Optional[
            "aws_sdk_synthetics.types.describe_canaries_last_run_name_filter.DescribeCanariesLastRunNameFilter"
        ] = None,
        browser_type: Optional[
            "aws_sdk_synthetics.types.browser_type.BrowserType"
        ] = None,
    ) -> "aws_sdk_synthetics.types.describe_canaries_last_run_response.DescribeCanariesLastRunResponse":
        r"""<p>Use this operation to see information from the most recent run of each canary that you have created.</p> <p>This operation supports resource-level authorization using an IAM policy and the <code>Names</code> parameter. If you specify the <code>Names</code> parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.</p> <p>You are required to use the <code>Names</code> parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html\"> Limiting a user to viewing specific canaries</a>.</p>

        Args:
            next_token: <p>A token that indicates that there is more data available. You can use this token in a subsequent <code>DescribeCanariesLastRun</code> operation to retrieve the next set of results.</p>
            max_results: <p>Specify this parameter to limit how many runs are returned each time you use the <code>DescribeLastRun</code> operation. If you omit this parameter, the default of 100 is used.</p>
            names: <p>Use this parameter to return only canaries that match the names that you specify here. You can specify as many as five canary names.</p> <p>If you specify this parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.</p> <p>You are required to use the <code>Names</code> parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html\"> Limiting a user to viewing specific canaries</a>.</p>
            browser_type: <p>The type of browser to use for the canary run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.describe_canaries_last_run_request.DescribeCanariesLastRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.describe_canaries_last_run_response.DescribeCanariesLastRunResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.describe_canaries_last_run

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.describe_canaries_last_run.async_describe_canaries_last_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.describe_canaries_last_run_request.DescribeCanariesLastRunRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if names is not None:
            input_["names"] = names
        if browser_type is not None:
            input_["browser_type"] = browser_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_runtime_versions(
        self,
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
        next_token: Optional["aws_sdk_synthetics.types.token.Token"] = None,
        max_results: Optional["aws_sdk_synthetics.types.max_size100.MaxSize100"] = None,
    ) -> "aws_sdk_synthetics.types.describe_runtime_versions_response.DescribeRuntimeVersionsResponse":
        r"""<p>Returns a list of Synthetics canary runtime versions. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html\"> Canary Runtime Versions</a>.</p>

        Args:
            next_token: <p>A token that indicates that there is more data available. You can use this token in a subsequent <code>DescribeRuntimeVersions</code> operation to retrieve the next set of results.</p>
            max_results: <p>Specify this parameter to limit how many runs are returned each time you use the <code>DescribeRuntimeVersions</code> operation. If you omit this parameter, the default of 100 is used.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.describe_runtime_versions_request.DescribeRuntimeVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.describe_runtime_versions_response.DescribeRuntimeVersionsResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.describe_runtime_versions

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.describe_runtime_versions.async_describe_runtime_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.describe_runtime_versions_request.DescribeRuntimeVersionsRequest = {}  # type: ignore[typeddict-item]
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

    async def disassociate_resource(
        self,
        group_identifier: "aws_sdk_synthetics.types.group_identifier.GroupIdentifier",
        resource_arn: "aws_sdk_synthetics.types.canary_arn.CanaryArn",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
    ) -> "aws_sdk_synthetics.types.disassociate_resource_response.DisassociateResourceResponse":
        """<p>Removes a canary from a group. You must run this operation in the Region where the canary exists.</p>

        Args:
            group_identifier: <p>Specifies the group. You can specify the group name, the ARN, or the group ID as the <code>GroupIdentifier</code>.</p>
            resource_arn: <p>The ARN of the canary that you want to remove from the specified group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.disassociate_resource_request.DisassociateResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.disassociate_resource_response.DisassociateResourceResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.disassociate_resource

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.disassociate_resource.async_disassociate_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.disassociate_resource_request.DisassociateResourceRequest = {}  # type: ignore[typeddict-item]
        input_["group_identifier"] = group_identifier
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_canary(
        self,
        name: "aws_sdk_synthetics.types.canary_name.CanaryName",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
        dry_run_id: Optional["aws_sdk_synthetics.types.uuid.UUID"] = None,
    ) -> "aws_sdk_synthetics.types.get_canary_response.GetCanaryResponse":
        r"""<p>Retrieves complete information about one canary. You must specify the name of the canary that you want. To get a list of canaries and their names, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\">DescribeCanaries</a>.</p>

        Args:
            name: <p>The name of the canary that you want details for.</p>
            dry_run_id: <p>The DryRunId associated with an existing canary’s dry run. You can use this DryRunId to retrieve information about the dry run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.get_canary_request.GetCanaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.get_canary_response.GetCanaryResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.get_canary

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.get_canary.async_get_canary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.get_canary_request.GetCanaryRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if dry_run_id is not None:
            input_["dry_run_id"] = dry_run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_canary_runs(
        self,
        name: "aws_sdk_synthetics.types.canary_name.CanaryName",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
        next_token: Optional["aws_sdk_synthetics.types.token.Token"] = None,
        max_results: Optional["aws_sdk_synthetics.types.max_size100.MaxSize100"] = None,
        dry_run_id: Optional["aws_sdk_synthetics.types.uuid.UUID"] = None,
        run_type: Optional["aws_sdk_synthetics.types.run_type.RunType"] = None,
    ) -> "aws_sdk_synthetics.types.get_canary_runs_response.GetCanaryRunsResponse":
        """<p>Retrieves a list of runs for a specified canary.</p>

        Args:
            name: <p>The name of the canary that you want to see runs for.</p>
            next_token: <p>A token that indicates that there is more data available. You can use this token in a subsequent <code>GetCanaryRuns</code> operation to retrieve the next set of results.</p> <note> <p>When auto retry is enabled for the canary, the first subsequent retry is suffixed with *1 indicating its the first retry and the next subsequent try is suffixed with *2.</p> </note>
            max_results: <p>Specify this parameter to limit how many runs are returned each time you use the <code>GetCanaryRuns</code> operation. If you omit this parameter, the default of 100 is used.</p>
            dry_run_id: <p>The DryRunId associated with an existing canary’s dry run. You can use this DryRunId to retrieve information about the dry run.</p>
            run_type: <ul> <li> <p>When you provide <code>RunType=CANARY_RUN</code> and <code>dryRunId</code>, you will get an exception </p> </li> <li> <p>When a value is not provided for <code>RunType</code>, the default value is <code>CANARY_RUN</code> </p> </li> <li> <p>When <code>CANARY_RUN</code> is provided, all canary runs excluding dry runs are returned</p> </li> <li> <p>When <code>DRY_RUN</code> is provided, all dry runs excluding canary runs are returned</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.get_canary_runs_request.GetCanaryRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.get_canary_runs_response.GetCanaryRunsResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.get_canary_runs

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.get_canary_runs.async_get_canary_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.get_canary_runs_request.GetCanaryRunsRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if dry_run_id is not None:
            input_["dry_run_id"] = dry_run_id
        if run_type is not None:
            input_["run_type"] = run_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_group(
        self,
        group_identifier: "aws_sdk_synthetics.types.group_identifier.GroupIdentifier",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
    ) -> "aws_sdk_synthetics.types.get_group_response.GetGroupResponse":
        """<p>Returns information about one group. Groups are a global resource, so you can use this operation from any Region.</p>

        Args:
            group_identifier: <p>Specifies the group to return information for. You can specify the group name, the ARN, or the group ID as the <code>GroupIdentifier</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.get_group_request.GetGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.get_group_response.GetGroupResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.get_group

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.get_group.async_get_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.get_group_request.GetGroupRequest = {}  # type: ignore[typeddict-item]
        input_["group_identifier"] = group_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_associated_groups(
        self,
        resource_arn: "aws_sdk_synthetics.types.canary_arn.CanaryArn",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_synthetics.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_synthetics.types.max_group_results.MaxGroupResults"
        ] = None,
    ) -> "aws_sdk_synthetics.types.list_associated_groups_response.ListAssociatedGroupsResponse":
        """<p>Returns a list of the groups that the specified canary is associated with. The canary that you specify must be in the current Region.</p>

        Args:
            next_token: <p>A token that indicates that there is more data available. You can use this token in a subsequent operation to retrieve the next set of results.</p>
            max_results: <p>Specify this parameter to limit how many groups are returned each time you use the <code>ListAssociatedGroups</code> operation. If you omit this parameter, the default of 20 is used.</p>
            resource_arn: <p>The ARN of the canary that you want to view groups for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.list_associated_groups_request.ListAssociatedGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.list_associated_groups_response.ListAssociatedGroupsResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.list_associated_groups

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.list_associated_groups.async_list_associated_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.list_associated_groups_request.ListAssociatedGroupsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_group_resources(
        self,
        group_identifier: "aws_sdk_synthetics.types.group_identifier.GroupIdentifier",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_synthetics.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_synthetics.types.max_group_results.MaxGroupResults"
        ] = None,
    ) -> "aws_sdk_synthetics.types.list_group_resources_response.ListGroupResourcesResponse":
        """<p>This operation returns a list of the ARNs of the canaries that are associated with the specified group.</p>

        Args:
            next_token: <p>A token that indicates that there is more data available. You can use this token in a subsequent operation to retrieve the next set of results.</p>
            max_results: <p>Specify this parameter to limit how many canary ARNs are returned each time you use the <code>ListGroupResources</code> operation. If you omit this parameter, the default of 20 is used.</p>
            group_identifier: <p>Specifies the group to return information for. You can specify the group name, the ARN, or the group ID as the <code>GroupIdentifier</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.list_group_resources_request.ListGroupResourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.list_group_resources_response.ListGroupResourcesResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.list_group_resources

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.list_group_resources.async_list_group_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.list_group_resources_request.ListGroupResourcesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["group_identifier"] = group_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_groups(
        self,
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_synthetics.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_synthetics.types.max_group_results.MaxGroupResults"
        ] = None,
    ) -> "aws_sdk_synthetics.types.list_groups_response.ListGroupsResponse":
        """<p>Returns a list of all groups in the account, displaying their names, unique IDs, and ARNs. The groups from all Regions are returned.</p>

        Args:
            next_token: <p>A token that indicates that there is more data available. You can use this token in a subsequent operation to retrieve the next set of results.</p>
            max_results: <p>Specify this parameter to limit how many groups are returned each time you use the <code>ListGroups</code> operation. If you omit this parameter, the default of 20 is used.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.list_groups_request.ListGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.list_groups_response.ListGroupsResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.list_groups

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.list_groups.async_list_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.list_groups_request.ListGroupsRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_synthetics.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
    ) -> "aws_sdk_synthetics.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Displays the tags associated with a canary or group.</p>

        Args:
            resource_arn: <p>The ARN of the canary or group that you want to view tags for.</p> <p>The ARN format of a canary is <code>arn:aws:synthetics:<i>Region</i>:<i>account-id</i>:canary:<i>canary-name</i> </code>.</p> <p>The ARN format of a group is <code>arn:aws:synthetics:<i>Region</i>:<i>account-id</i>:group:<i>group-name</i> </code> </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_canary(
        self,
        name: "aws_sdk_synthetics.types.canary_name.CanaryName",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
    ) -> "aws_sdk_synthetics.types.start_canary_response.StartCanaryResponse":
        r"""<p>Use this operation to run a canary that has already been created. The frequency of the canary runs is determined by the value of the canary's <code>Schedule</code>. To see a canary's schedule, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanary.html\">GetCanary</a>.</p>

        Args:
            name: <p>The name of the canary that you want to run. To find canary names, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\">DescribeCanaries</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.start_canary_request.StartCanaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.start_canary_response.StartCanaryResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.start_canary

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.start_canary.async_start_canary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.start_canary_request.StartCanaryRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_canary_dry_run(
        self,
        name: "aws_sdk_synthetics.types.canary_name.CanaryName",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
        code: Optional[
            "aws_sdk_synthetics.types.canary_code_input.CanaryCodeInput"
        ] = None,
        runtime_version: Optional["aws_sdk_synthetics.types.string.String"] = None,
        run_config: Optional[
            "aws_sdk_synthetics.types.canary_run_config_input.CanaryRunConfigInput"
        ] = None,
        vpc_config: Optional[
            "aws_sdk_synthetics.types.vpc_config_input.VpcConfigInput"
        ] = None,
        execution_role_arn: Optional[
            "aws_sdk_synthetics.types.role_arn.RoleArn"
        ] = None,
        success_retention_period_in_days: Optional[
            "aws_sdk_synthetics.types.max_size1024.MaxSize1024"
        ] = None,
        failure_retention_period_in_days: Optional[
            "aws_sdk_synthetics.types.max_size1024.MaxSize1024"
        ] = None,
        visual_reference: Optional[
            "aws_sdk_synthetics.types.visual_reference_input.VisualReferenceInput"
        ] = None,
        artifact_s3_location: Optional["aws_sdk_synthetics.types.string.String"] = None,
        artifact_config: Optional[
            "aws_sdk_synthetics.types.artifact_config_input.ArtifactConfigInput"
        ] = None,
        provisioned_resource_cleanup: Optional[
            "aws_sdk_synthetics.types.provisioned_resource_cleanup_setting.ProvisionedResourceCleanupSetting"
        ] = None,
        browser_configs: Optional[
            "aws_sdk_synthetics.types.browser_configs.BrowserConfigs"
        ] = None,
        visual_references: Optional[
            "aws_sdk_synthetics.types.visual_references.VisualReferences"
        ] = None,
    ) -> "aws_sdk_synthetics.types.start_canary_dry_run_response.StartCanaryDryRunResponse":
        r"""<p>Use this operation to start a dry run for a canary that has already been created</p>

        Args:
            name: <p>The name of the canary that you want to dry run. To find canary names, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\">DescribeCanaries</a>.</p>
            runtime_version: <p>Specifies the runtime version to use for the canary. For a list of valid runtime versions and for more information about runtime versions, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html\"> Canary Runtime Versions</a>.</p>
            execution_role_arn: <p>The ARN of the IAM role to be used to run the canary. This role must already exist, and must include <code>lambda.amazonaws.com</code> as a principal in the trust policy. The role must also have the following permissions:</p>
            success_retention_period_in_days: <p>The number of days to retain data about successful runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.</p> <p>This setting affects the range of information returned by <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html\">GetCanaryRuns</a>, as well as the range of information displayed in the Synthetics console. </p>
            failure_retention_period_in_days: <p>The number of days to retain data about failed runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.</p> <p>This setting affects the range of information returned by <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html\">GetCanaryRuns</a>, as well as the range of information displayed in the Synthetics console. </p>
            artifact_s3_location: <p>The location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary. Artifacts include the log file, screenshots, and HAR files. The name of the Amazon S3 bucket can't include a period (.).</p>
            provisioned_resource_cleanup: <p>Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted. If you omit this parameter, the default of <code>AUTOMATIC</code> is used, which means that the Lambda functions and layers will be deleted when the canary is deleted.</p> <p>If the value of this parameter is <code>OFF</code>, then the value of the <code>DeleteLambda</code> parameter of the <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html\">DeleteCanary</a> operation determines whether the Lambda functions and layers will be deleted.</p>
            browser_configs: <p>A structure that specifies the browser type to use for a canary run. CloudWatch Synthetics supports running canaries on both <code>CHROME</code> and <code>FIREFOX</code> browsers.</p> <note> <p>If not specified, <code>browserConfigs</code> defaults to Chrome.</p> </note>
            visual_references: <p>A list of visual reference configurations for the canary, one for each browser type that the canary is configured to run on. Visual references are used for visual monitoring comparisons.</p> <p> <code>syn-nodejs-puppeteer-11.0</code> and above, and <code>syn-nodejs-playwright-3.0</code> and above, only supports <code>visualReferences</code>. <code>visualReference</code> field is not supported.</p> <p>Versions older than <code>syn-nodejs-puppeteer-11.0</code> supports both <code>visualReference</code> and <code>visualReferences</code> for backward compatibility. It is recommended to use <code>visualReferences</code> for consistency and future compatibility.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.start_canary_dry_run_request.StartCanaryDryRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.start_canary_dry_run_response.StartCanaryDryRunResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.start_canary_dry_run

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.start_canary_dry_run.async_start_canary_dry_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.start_canary_dry_run_request.StartCanaryDryRunRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if code is not None:
            input_["code"] = code
        if runtime_version is not None:
            input_["runtime_version"] = runtime_version
        if run_config is not None:
            input_["run_config"] = run_config
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if success_retention_period_in_days is not None:
            input_["success_retention_period_in_days"] = (
                success_retention_period_in_days
            )
        if failure_retention_period_in_days is not None:
            input_["failure_retention_period_in_days"] = (
                failure_retention_period_in_days
            )
        if visual_reference is not None:
            input_["visual_reference"] = visual_reference
        if artifact_s3_location is not None:
            input_["artifact_s3_location"] = artifact_s3_location
        if artifact_config is not None:
            input_["artifact_config"] = artifact_config
        if provisioned_resource_cleanup is not None:
            input_["provisioned_resource_cleanup"] = provisioned_resource_cleanup
        if browser_configs is not None:
            input_["browser_configs"] = browser_configs
        if visual_references is not None:
            input_["visual_references"] = visual_references

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_canary(
        self,
        name: "aws_sdk_synthetics.types.canary_name.CanaryName",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
    ) -> "aws_sdk_synthetics.types.stop_canary_response.StopCanaryResponse":
        r"""<p>Stops the canary to prevent all future runs. If the canary is currently running,the run that is in progress completes on its own, publishes metrics, and uploads artifacts, but it is not recorded in Synthetics as a completed run.</p> <p>You can use <code>StartCanary</code> to start it running again with the canary’s current schedule at any point in the future. </p>

        Args:
            name: <p>The name of the canary that you want to stop. To find the names of your canaries, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\">ListCanaries</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.stop_canary_request.StopCanaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.stop_canary_response.StopCanaryResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.stop_canary

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.stop_canary.async_stop_canary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.stop_canary_request.StopCanaryRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_synthetics.types.resource_arn.ResourceArn",
        tags: "aws_sdk_synthetics.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
    ) -> "aws_sdk_synthetics.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified canary or group. </p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can use the <code>TagResource</code> action with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a canary or group.</p>

        Args:
            resource_arn: <p>The ARN of the canary or group that you're adding tags to.</p> <p>The ARN format of a canary is <code>arn:aws:synthetics:<i>Region</i>:<i>account-id</i>:canary:<i>canary-name</i> </code>.</p> <p>The ARN format of a group is <code>arn:aws:synthetics:<i>Region</i>:<i>account-id</i>:group:<i>group-name</i> </code> </p>
            tags: <p>The list of key-value pairs to associate with the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_synthetics.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_synthetics.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
    ) -> "aws_sdk_synthetics.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the canary or group that you're removing tags from.</p> <p>The ARN format of a canary is <code>arn:aws:synthetics:<i>Region</i>:<i>account-id</i>:canary:<i>canary-name</i> </code>.</p> <p>The ARN format of a group is <code>arn:aws:synthetics:<i>Region</i>:<i>account-id</i>:group:<i>group-name</i> </code> </p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_canary(
        self,
        name: "aws_sdk_synthetics.types.canary_name.CanaryName",
        *,
        config_overrides: Optional[AsyncsyntheticsClientConfig] = None,
        code: Optional[
            "aws_sdk_synthetics.types.canary_code_input.CanaryCodeInput"
        ] = None,
        execution_role_arn: Optional[
            "aws_sdk_synthetics.types.role_arn.RoleArn"
        ] = None,
        runtime_version: Optional["aws_sdk_synthetics.types.string.String"] = None,
        schedule: Optional[
            "aws_sdk_synthetics.types.canary_schedule_input.CanaryScheduleInput"
        ] = None,
        run_config: Optional[
            "aws_sdk_synthetics.types.canary_run_config_input.CanaryRunConfigInput"
        ] = None,
        success_retention_period_in_days: Optional[
            "aws_sdk_synthetics.types.max_size1024.MaxSize1024"
        ] = None,
        failure_retention_period_in_days: Optional[
            "aws_sdk_synthetics.types.max_size1024.MaxSize1024"
        ] = None,
        vpc_config: Optional[
            "aws_sdk_synthetics.types.vpc_config_input.VpcConfigInput"
        ] = None,
        visual_reference: Optional[
            "aws_sdk_synthetics.types.visual_reference_input.VisualReferenceInput"
        ] = None,
        artifact_s3_location: Optional["aws_sdk_synthetics.types.string.String"] = None,
        artifact_config: Optional[
            "aws_sdk_synthetics.types.artifact_config_input.ArtifactConfigInput"
        ] = None,
        provisioned_resource_cleanup: Optional[
            "aws_sdk_synthetics.types.provisioned_resource_cleanup_setting.ProvisionedResourceCleanupSetting"
        ] = None,
        dry_run_id: Optional["aws_sdk_synthetics.types.uuid.UUID"] = None,
        visual_references: Optional[
            "aws_sdk_synthetics.types.visual_references.VisualReferences"
        ] = None,
        browser_configs: Optional[
            "aws_sdk_synthetics.types.browser_configs.BrowserConfigs"
        ] = None,
    ) -> "aws_sdk_synthetics.types.update_canary_response.UpdateCanaryResponse":
        r"""<p>Updates the configuration of a canary that has already been created.</p> <p>For multibrowser canaries, you can add or remove browsers by updating the browserConfig list in the update call. For example:</p> <ul> <li> <p>To add Firefox to a canary that currently uses Chrome, specify browserConfigs as [CHROME, FIREFOX]</p> </li> <li> <p>To remove Firefox and keep only Chrome, specify browserConfigs as [CHROME]</p> </li> </ul> <p>You can't use this operation to update the tags of an existing canary. To change the tags of an existing canary, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_TagResource.html\">TagResource</a>.</p> <note> <p>When you use the <code>dryRunId</code> field when updating a canary, the only other field you can provide is the <code>Schedule</code>. Adding any other field will thrown an exception.</p> </note>

        Args:
            name: <p>The name of the canary that you want to update. To find the names of your canaries, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\">DescribeCanaries</a>.</p> <p>You cannot change the name of a canary that has already been created.</p>
            code: <p>A structure that includes the entry point from which the canary should start running your script. If the script is stored in an Amazon S3 bucket, the bucket name, key, and version are also included. </p>
            execution_role_arn: <p>The ARN of the IAM role to be used to run the canary. This role must already exist, and must include <code>lambda.amazonaws.com</code> as a principal in the trust policy. The role must also have the following permissions:</p> <ul> <li> <p> <code>s3:PutObject</code> </p> </li> <li> <p> <code>s3:GetBucketLocation</code> </p> </li> <li> <p> <code>s3:ListAllMyBuckets</code> </p> </li> <li> <p> <code>cloudwatch:PutMetricData</code> </p> </li> <li> <p> <code>logs:CreateLogGroup</code> </p> </li> <li> <p> <code>logs:CreateLogStream</code> </p> </li> <li> <p> <code>logs:CreateLogStream</code> </p> </li> </ul>
            runtime_version: <p>Specifies the runtime version to use for the canary. For a list of valid runtime versions and for more information about runtime versions, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html\"> Canary Runtime Versions</a>.</p>
            schedule: <p>A structure that contains information about how often the canary is to run, and when these runs are to stop.</p>
            run_config: <p>A structure that contains the timeout value that is used for each individual run of the canary.</p> <important> <p>Environment variable keys and values are encrypted at rest using Amazon Web Services owned KMS keys. However, the environment variables are not encrypted on the client side. Do not store sensitive information in them.</p> </important>
            success_retention_period_in_days: <p>The number of days to retain data about successful runs of this canary.</p> <p>This setting affects the range of information returned by <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html\">GetCanaryRuns</a>, as well as the range of information displayed in the Synthetics console. </p>
            failure_retention_period_in_days: <p>The number of days to retain data about failed runs of this canary.</p> <p>This setting affects the range of information returned by <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html\">GetCanaryRuns</a>, as well as the range of information displayed in the Synthetics console. </p>
            vpc_config: <p>If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html\"> Running a Canary in a VPC</a>.</p>
            visual_reference: <p>Defines the screenshots to use as the baseline for comparisons during visual monitoring comparisons during future runs of this canary. If you omit this parameter, no changes are made to any baseline screenshots that the canary might be using already.</p> <p>Visual monitoring is supported only on canaries running the <b>syn-puppeteer-node-3.2</b> runtime or later. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_SyntheticsLogger_VisualTesting.html\"> Visual monitoring</a> and <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Blueprints_VisualTesting.html\"> Visual monitoring blueprint</a> </p>
            artifact_s3_location: <p>The location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary. Artifacts include the log file, screenshots, and HAR files. The name of the Amazon S3 bucket can't include a period (.).</p>
            artifact_config: <p>A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.</p>
            provisioned_resource_cleanup: <p>Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted.</p> <p>If the value of this parameter is <code>OFF</code>, then the value of the <code>DeleteLambda</code> parameter of the <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html\">DeleteCanary</a> operation determines whether the Lambda functions and layers will be deleted.</p>
            dry_run_id: <p>Update the existing canary using the updated configurations from the DryRun associated with the DryRunId.</p> <note> <p>When you use the <code>dryRunId</code> field when updating a canary, the only other field you can provide is the <code>Schedule</code>. Adding any other field will thrown an exception.</p> </note>
            visual_references: <p>A list of visual reference configurations for the canary, one for each browser type that the canary is configured to run on. Visual references are used for visual monitoring comparisons.</p> <p> <code>syn-nodejs-puppeteer-11.0</code> and above, and <code>syn-nodejs-playwright-3.0</code> and above, only supports <code>visualReferences</code>. <code>visualReference</code> field is not supported.</p> <p>Versions older than <code>syn-nodejs-puppeteer-11.0</code> supports both <code>visualReference</code> and <code>visualReferences</code> for backward compatibility. It is recommended to use <code>visualReferences</code> for consistency and future compatibility.</p> <p>For multibrowser visual monitoring, you can update the baseline for all configured browsers in a single update call by specifying a list of VisualReference objects, one per browser. Each VisualReference object maps to a specific browser configuration, allowing you to manage visual baselines for multiple browsers simultaneously.</p> <p>For single configuration canaries using Chrome browser (default browser), use visualReferences for <code>syn-nodejs-puppeteer-11.0</code> and above, and <code>syn-nodejs-playwright-3.0</code> and above canaries. The browserType in the visualReference object is not mandatory.</p>
            browser_configs: <p>A structure that specifies the browser type to use for a canary run. CloudWatch Synthetics supports running canaries on both <code>CHROME</code> and <code>FIREFOX</code> browsers.</p> <note> <p>If not specified, <code>browserConfigs</code> defaults to Chrome.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_synthetics.types.update_canary_request.UpdateCanaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_synthetics.types.update_canary_response.UpdateCanaryResponse"
        ]:
            import aws_sdk_synthetics._operations.synthetics.update_canary

            (
                output,
                http_response,
            ) = await aws_sdk_synthetics._operations.synthetics.update_canary.async_update_canary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_synthetics.types.update_canary_request.UpdateCanaryRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if code is not None:
            input_["code"] = code
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if runtime_version is not None:
            input_["runtime_version"] = runtime_version
        if schedule is not None:
            input_["schedule"] = schedule
        if run_config is not None:
            input_["run_config"] = run_config
        if success_retention_period_in_days is not None:
            input_["success_retention_period_in_days"] = (
                success_retention_period_in_days
            )
        if failure_retention_period_in_days is not None:
            input_["failure_retention_period_in_days"] = (
                failure_retention_period_in_days
            )
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if visual_reference is not None:
            input_["visual_reference"] = visual_reference
        if artifact_s3_location is not None:
            input_["artifact_s3_location"] = artifact_s3_location
        if artifact_config is not None:
            input_["artifact_config"] = artifact_config
        if provisioned_resource_cleanup is not None:
            input_["provisioned_resource_cleanup"] = provisioned_resource_cleanup
        if dry_run_id is not None:
            input_["dry_run_id"] = dry_run_id
        if visual_references is not None:
            input_["visual_references"] = visual_references
        if browser_configs is not None:
            input_["browser_configs"] = browser_configs

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
