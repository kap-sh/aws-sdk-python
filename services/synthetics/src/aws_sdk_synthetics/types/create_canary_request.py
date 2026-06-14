"""Generated from Smithy shape ``com.amazonaws.synthetics#CreateCanaryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_synthetics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.artifact_config_input
    import aws_sdk_synthetics.types.browser_configs
    import aws_sdk_synthetics.types.canary_code_input
    import aws_sdk_synthetics.types.canary_name
    import aws_sdk_synthetics.types.canary_run_config_input
    import aws_sdk_synthetics.types.canary_schedule_input
    import aws_sdk_synthetics.types.max_size1024
    import aws_sdk_synthetics.types.provisioned_resource_cleanup_setting
    import aws_sdk_synthetics.types.resource_list
    import aws_sdk_synthetics.types.role_arn
    import aws_sdk_synthetics.types.string
    import aws_sdk_synthetics.types.tag_map
    import aws_sdk_synthetics.types.vpc_config_input


class CreateCanaryRequest(TypedDict):
    name: "aws_sdk_synthetics.types.canary_name.CanaryName"
    r"""<p>The name for this canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account.</p> <p>Do not include secrets or proprietary information in your canary names. The canary name makes up part of the canary ARN, and the ARN is included in outbound calls over the internet. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html\">Security Considerations for Synthetics Canaries</a>.</p>"""
    code: "aws_sdk_synthetics.types.canary_code_input.CanaryCodeInput"
    """<p>A structure that includes the entry point from which the canary should start running your script. If the script is stored in an Amazon S3 bucket, the bucket name, key, and version are also included. </p>"""
    artifact_s3_location: "aws_sdk_synthetics.types.string.String"
    """<p>The location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary. Artifacts include the log file, screenshots, and HAR files. The name of the Amazon S3 bucket can't include a period (.).</p>"""
    execution_role_arn: "aws_sdk_synthetics.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role to be used to run the canary. This role must already exist, and must include <code>lambda.amazonaws.com</code> as a principal in the trust policy. The role must also have the following permissions:</p> <ul> <li> <p> <code>s3:PutObject</code> </p> </li> <li> <p> <code>s3:GetBucketLocation</code> </p> </li> <li> <p> <code>s3:ListAllMyBuckets</code> </p> </li> <li> <p> <code>cloudwatch:PutMetricData</code> </p> </li> <li> <p> <code>logs:CreateLogGroup</code> </p> </li> <li> <p> <code>logs:CreateLogStream</code> </p> </li> <li> <p> <code>logs:PutLogEvents</code> </p> </li> </ul>"""
    schedule: "aws_sdk_synthetics.types.canary_schedule_input.CanaryScheduleInput"
    """<p>A structure that contains information about how often the canary is to run and when these test runs are to stop.</p>"""
    run_config: NotRequired[
        "aws_sdk_synthetics.types.canary_run_config_input.CanaryRunConfigInput"
    ]
    """<p>A structure that contains the configuration for individual canary runs, such as timeout value and environment variables.</p> <important> <p>Environment variable keys and values are encrypted at rest using Amazon Web Services owned KMS keys. However, the environment variables are not encrypted on the client side. Do not store sensitive information in them.</p> </important>"""
    success_retention_period_in_days: NotRequired[
        "aws_sdk_synthetics.types.max_size1024.MaxSize1024"
    ]
    r"""<p>The number of days to retain data about successful runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.</p> <p>This setting affects the range of information returned by <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html\">GetCanaryRuns</a>, as well as the range of information displayed in the Synthetics console. </p>"""
    failure_retention_period_in_days: NotRequired[
        "aws_sdk_synthetics.types.max_size1024.MaxSize1024"
    ]
    r"""<p>The number of days to retain data about failed runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.</p> <p>This setting affects the range of information returned by <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html\">GetCanaryRuns</a>, as well as the range of information displayed in the Synthetics console. </p>"""
    runtime_version: "aws_sdk_synthetics.types.string.String"
    r"""<p>Specifies the runtime version to use for the canary. For a list of valid runtime versions and more information about runtime versions, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html\"> Canary Runtime Versions</a>.</p>"""
    vpc_config: NotRequired["aws_sdk_synthetics.types.vpc_config_input.VpcConfigInput"]
    r"""<p>If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html\"> Running a Canary in a VPC</a>.</p>"""
    resources_to_replicate_tags: NotRequired[
        "aws_sdk_synthetics.types.resource_list.ResourceList"
    ]
    """<p>To have the tags that you apply to this canary also be applied to the Lambda function that the canary uses, specify this parameter with the value <code>lambda-function</code>.</p> <p>If you specify this parameter and don't specify any tags in the <code>Tags</code> parameter, the canary creation fails.</p>"""
    provisioned_resource_cleanup: NotRequired[
        "aws_sdk_synthetics.types.provisioned_resource_cleanup_setting.ProvisionedResourceCleanupSetting"
    ]
    r"""<p>Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted. If you omit this parameter, the default of <code>AUTOMATIC</code> is used, which means that the Lambda functions and layers will be deleted when the canary is deleted.</p> <p>If the value of this parameter is <code>OFF</code>, then the value of the <code>DeleteLambda</code> parameter of the <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html\">DeleteCanary</a> operation determines whether the Lambda functions and layers will be deleted.</p>"""
    browser_configs: NotRequired[
        "aws_sdk_synthetics.types.browser_configs.BrowserConfigs"
    ]
    """<p>CloudWatch Synthetics now supports multibrowser canaries for <code>syn-nodejs-puppeteer-11.0</code> and <code>syn-nodejs-playwright-3.0</code> runtimes. This feature allows you to run your canaries on both Firefox and Chrome browsers. To create a multibrowser canary, you need to specify the BrowserConfigs with a list of browsers you want to use.</p> <note> <p>If not specified, <code>browserConfigs</code> defaults to Chrome.</p> </note>"""
    tags: NotRequired["aws_sdk_synthetics.types.tag_map.TagMap"]
    """<p>A list of key-value pairs to associate with the canary. You can associate as many as 50 tags with a canary.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only the resources that have certain tag values.</p> <p>To have the tags that you apply to this canary also be applied to the Lambda function that the canary uses, specify this parameter with the value <code>lambda-function</code>.</p>"""
    artifact_config: NotRequired[
        "aws_sdk_synthetics.types.artifact_config_input.ArtifactConfigInput"
    ]
    """<p>A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCanaryRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_synthetics.types.canary_code_input

    out["Code"] = aws_sdk_synthetics.types.canary_code_input.serialize_json(
        value["code"]
    )
    out["ArtifactS3Location"] = value["artifact_s3_location"]
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    import aws_sdk_synthetics.types.canary_schedule_input

    out["Schedule"] = aws_sdk_synthetics.types.canary_schedule_input.serialize_json(
        value["schedule"]
    )
    if "run_config" in value:
        import aws_sdk_synthetics.types.canary_run_config_input

        out["RunConfig"] = (
            aws_sdk_synthetics.types.canary_run_config_input.serialize_json(
                value["run_config"]
            )
        )
    if "success_retention_period_in_days" in value:
        out["SuccessRetentionPeriodInDays"] = value["success_retention_period_in_days"]
    if "failure_retention_period_in_days" in value:
        out["FailureRetentionPeriodInDays"] = value["failure_retention_period_in_days"]
    out["RuntimeVersion"] = value["runtime_version"]
    if "vpc_config" in value:
        import aws_sdk_synthetics.types.vpc_config_input

        out["VpcConfig"] = aws_sdk_synthetics.types.vpc_config_input.serialize_json(
            value["vpc_config"]
        )
    if "resources_to_replicate_tags" in value:
        import aws_sdk_synthetics.types.resource_list

        out["ResourcesToReplicateTags"] = (
            aws_sdk_synthetics.types.resource_list.serialize_json(
                value["resources_to_replicate_tags"]
            )
        )
    if "provisioned_resource_cleanup" in value:
        import aws_sdk_synthetics.types.provisioned_resource_cleanup_setting

        out["ProvisionedResourceCleanup"] = (
            aws_sdk_synthetics.types.provisioned_resource_cleanup_setting.serialize_json(
                value["provisioned_resource_cleanup"]
            )
        )
    if "browser_configs" in value:
        import aws_sdk_synthetics.types.browser_configs

        out["BrowserConfigs"] = aws_sdk_synthetics.types.browser_configs.serialize_json(
            value["browser_configs"]
        )
    if "tags" in value:
        import aws_sdk_synthetics.types.tag_map

        out["Tags"] = aws_sdk_synthetics.types.tag_map.serialize_json(value["tags"])
    if "artifact_config" in value:
        import aws_sdk_synthetics.types.artifact_config_input

        out["ArtifactConfig"] = (
            aws_sdk_synthetics.types.artifact_config_input.serialize_json(
                value["artifact_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateCanaryRequest:
    out: CreateCanaryRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateCanaryRequest.name required")
    if "Code" in data:
        import aws_sdk_synthetics.types.canary_code_input

        out["code"] = aws_sdk_synthetics.types.canary_code_input.deserialize_json(
            data["Code"]
        )
    else:
        raise DeserializationError("CreateCanaryRequest.code required")
    if "ArtifactS3Location" in data:
        out["artifact_s3_location"] = data["ArtifactS3Location"]
    else:
        raise DeserializationError("CreateCanaryRequest.artifact_s3_location required")
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        raise DeserializationError("CreateCanaryRequest.execution_role_arn required")
    if "Schedule" in data:
        import aws_sdk_synthetics.types.canary_schedule_input

        out["schedule"] = (
            aws_sdk_synthetics.types.canary_schedule_input.deserialize_json(
                data["Schedule"]
            )
        )
    else:
        raise DeserializationError("CreateCanaryRequest.schedule required")
    if "RunConfig" in data:
        import aws_sdk_synthetics.types.canary_run_config_input

        out["run_config"] = (
            aws_sdk_synthetics.types.canary_run_config_input.deserialize_json(
                data["RunConfig"]
            )
        )
    if "SuccessRetentionPeriodInDays" in data:
        out["success_retention_period_in_days"] = data["SuccessRetentionPeriodInDays"]
    if "FailureRetentionPeriodInDays" in data:
        out["failure_retention_period_in_days"] = data["FailureRetentionPeriodInDays"]
    if "RuntimeVersion" in data:
        out["runtime_version"] = data["RuntimeVersion"]
    else:
        raise DeserializationError("CreateCanaryRequest.runtime_version required")
    if "VpcConfig" in data:
        import aws_sdk_synthetics.types.vpc_config_input

        out["vpc_config"] = aws_sdk_synthetics.types.vpc_config_input.deserialize_json(
            data["VpcConfig"]
        )
    if "ResourcesToReplicateTags" in data:
        import aws_sdk_synthetics.types.resource_list

        out["resources_to_replicate_tags"] = (
            aws_sdk_synthetics.types.resource_list.deserialize_json(
                data["ResourcesToReplicateTags"]
            )
        )
    if "ProvisionedResourceCleanup" in data:
        import aws_sdk_synthetics.types.provisioned_resource_cleanup_setting

        out["provisioned_resource_cleanup"] = (
            aws_sdk_synthetics.types.provisioned_resource_cleanup_setting.deserialize_json(
                data["ProvisionedResourceCleanup"]
            )
        )
    if "BrowserConfigs" in data:
        import aws_sdk_synthetics.types.browser_configs

        out["browser_configs"] = (
            aws_sdk_synthetics.types.browser_configs.deserialize_json(
                data["BrowserConfigs"]
            )
        )
    if "Tags" in data:
        import aws_sdk_synthetics.types.tag_map

        out["tags"] = aws_sdk_synthetics.types.tag_map.deserialize_json(data["Tags"])
    if "ArtifactConfig" in data:
        import aws_sdk_synthetics.types.artifact_config_input

        out["artifact_config"] = (
            aws_sdk_synthetics.types.artifact_config_input.deserialize_json(
                data["ArtifactConfig"]
            )
        )
    return out
