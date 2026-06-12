"""Generated from Smithy shape ``com.amazonaws.synthetics#UpdateCanaryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.artifact_config_input
    import aws_sdk_synthetics.types.browser_configs
    import aws_sdk_synthetics.types.canary_code_input
    import aws_sdk_synthetics.types.canary_name
    import aws_sdk_synthetics.types.canary_run_config_input
    import aws_sdk_synthetics.types.canary_schedule_input
    import aws_sdk_synthetics.types.max_size1024
    import aws_sdk_synthetics.types.provisioned_resource_cleanup_setting
    import aws_sdk_synthetics.types.role_arn
    import aws_sdk_synthetics.types.string
    import aws_sdk_synthetics.types.uuid
    import aws_sdk_synthetics.types.visual_reference_input
    import aws_sdk_synthetics.types.visual_references
    import aws_sdk_synthetics.types.vpc_config_input


class UpdateCanaryRequest(TypedDict):
    name: "aws_sdk_synthetics.types.canary_name.CanaryName"
    """<p>The name of the canary that you want to update. To find the names of your canaries, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\">DescribeCanaries</a>.</p> <p>You cannot change the name of a canary that has already been created.</p>"""
    code: NotRequired["aws_sdk_synthetics.types.canary_code_input.CanaryCodeInput"]
    """<p>A structure that includes the entry point from which the canary should start running your script. If the script is stored in an Amazon S3 bucket, the bucket name, key, and version are also included. </p>"""
    execution_role_arn: NotRequired["aws_sdk_synthetics.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role to be used to run the canary. This role must already exist, and must include <code>lambda.amazonaws.com</code> as a principal in the trust policy. The role must also have the following permissions:</p> <ul> <li> <p> <code>s3:PutObject</code> </p> </li> <li> <p> <code>s3:GetBucketLocation</code> </p> </li> <li> <p> <code>s3:ListAllMyBuckets</code> </p> </li> <li> <p> <code>cloudwatch:PutMetricData</code> </p> </li> <li> <p> <code>logs:CreateLogGroup</code> </p> </li> <li> <p> <code>logs:CreateLogStream</code> </p> </li> <li> <p> <code>logs:CreateLogStream</code> </p> </li> </ul>"""
    runtime_version: NotRequired["aws_sdk_synthetics.types.string.String"]
    """<p>Specifies the runtime version to use for the canary. For a list of valid runtime versions and for more information about runtime versions, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html\"> Canary Runtime Versions</a>.</p>"""
    schedule: NotRequired[
        "aws_sdk_synthetics.types.canary_schedule_input.CanaryScheduleInput"
    ]
    """<p>A structure that contains information about how often the canary is to run, and when these runs are to stop.</p>"""
    run_config: NotRequired[
        "aws_sdk_synthetics.types.canary_run_config_input.CanaryRunConfigInput"
    ]
    """<p>A structure that contains the timeout value that is used for each individual run of the canary.</p> <important> <p>Environment variable keys and values are encrypted at rest using Amazon Web Services owned KMS keys. However, the environment variables are not encrypted on the client side. Do not store sensitive information in them.</p> </important>"""
    success_retention_period_in_days: NotRequired[
        "aws_sdk_synthetics.types.max_size1024.MaxSize1024"
    ]
    """<p>The number of days to retain data about successful runs of this canary.</p> <p>This setting affects the range of information returned by <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html\">GetCanaryRuns</a>, as well as the range of information displayed in the Synthetics console. </p>"""
    failure_retention_period_in_days: NotRequired[
        "aws_sdk_synthetics.types.max_size1024.MaxSize1024"
    ]
    """<p>The number of days to retain data about failed runs of this canary.</p> <p>This setting affects the range of information returned by <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html\">GetCanaryRuns</a>, as well as the range of information displayed in the Synthetics console. </p>"""
    vpc_config: NotRequired["aws_sdk_synthetics.types.vpc_config_input.VpcConfigInput"]
    """<p>If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html\"> Running a Canary in a VPC</a>.</p>"""
    visual_reference: NotRequired[
        "aws_sdk_synthetics.types.visual_reference_input.VisualReferenceInput"
    ]
    """<p>Defines the screenshots to use as the baseline for comparisons during visual monitoring comparisons during future runs of this canary. If you omit this parameter, no changes are made to any baseline screenshots that the canary might be using already.</p> <p>Visual monitoring is supported only on canaries running the <b>syn-puppeteer-node-3.2</b> runtime or later. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_SyntheticsLogger_VisualTesting.html\"> Visual monitoring</a> and <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Blueprints_VisualTesting.html\"> Visual monitoring blueprint</a> </p>"""
    artifact_s3_location: NotRequired["aws_sdk_synthetics.types.string.String"]
    """<p>The location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary. Artifacts include the log file, screenshots, and HAR files. The name of the Amazon S3 bucket can't include a period (.).</p>"""
    artifact_config: NotRequired[
        "aws_sdk_synthetics.types.artifact_config_input.ArtifactConfigInput"
    ]
    """<p>A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.</p>"""
    provisioned_resource_cleanup: NotRequired[
        "aws_sdk_synthetics.types.provisioned_resource_cleanup_setting.ProvisionedResourceCleanupSetting"
    ]
    """<p>Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted.</p> <p>If the value of this parameter is <code>OFF</code>, then the value of the <code>DeleteLambda</code> parameter of the <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html\">DeleteCanary</a> operation determines whether the Lambda functions and layers will be deleted.</p>"""
    dry_run_id: NotRequired["aws_sdk_synthetics.types.uuid.UUID"]
    """<p>Update the existing canary using the updated configurations from the DryRun associated with the DryRunId.</p> <note> <p>When you use the <code>dryRunId</code> field when updating a canary, the only other field you can provide is the <code>Schedule</code>. Adding any other field will thrown an exception.</p> </note>"""
    visual_references: NotRequired[
        "aws_sdk_synthetics.types.visual_references.VisualReferences"
    ]
    """<p>A list of visual reference configurations for the canary, one for each browser type that the canary is configured to run on. Visual references are used for visual monitoring comparisons.</p> <p> <code>syn-nodejs-puppeteer-11.0</code> and above, and <code>syn-nodejs-playwright-3.0</code> and above, only supports <code>visualReferences</code>. <code>visualReference</code> field is not supported.</p> <p>Versions older than <code>syn-nodejs-puppeteer-11.0</code> supports both <code>visualReference</code> and <code>visualReferences</code> for backward compatibility. It is recommended to use <code>visualReferences</code> for consistency and future compatibility.</p> <p>For multibrowser visual monitoring, you can update the baseline for all configured browsers in a single update call by specifying a list of VisualReference objects, one per browser. Each VisualReference object maps to a specific browser configuration, allowing you to manage visual baselines for multiple browsers simultaneously.</p> <p>For single configuration canaries using Chrome browser (default browser), use visualReferences for <code>syn-nodejs-puppeteer-11.0</code> and above, and <code>syn-nodejs-playwright-3.0</code> and above canaries. The browserType in the visualReference object is not mandatory.</p>"""
    browser_configs: NotRequired[
        "aws_sdk_synthetics.types.browser_configs.BrowserConfigs"
    ]
    """<p>A structure that specifies the browser type to use for a canary run. CloudWatch Synthetics supports running canaries on both <code>CHROME</code> and <code>FIREFOX</code> browsers.</p> <note> <p>If not specified, <code>browserConfigs</code> defaults to Chrome.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCanaryRequest) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_synthetics.types.canary_code_input

        out["Code"] = aws_sdk_synthetics.types.canary_code_input.serialize_json(
            value["code"]
        )
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "runtime_version" in value:
        out["RuntimeVersion"] = value["runtime_version"]
    if "schedule" in value:
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
    if "vpc_config" in value:
        import aws_sdk_synthetics.types.vpc_config_input

        out["VpcConfig"] = aws_sdk_synthetics.types.vpc_config_input.serialize_json(
            value["vpc_config"]
        )
    if "visual_reference" in value:
        import aws_sdk_synthetics.types.visual_reference_input

        out["VisualReference"] = (
            aws_sdk_synthetics.types.visual_reference_input.serialize_json(
                value["visual_reference"]
            )
        )
    if "artifact_s3_location" in value:
        out["ArtifactS3Location"] = value["artifact_s3_location"]
    if "artifact_config" in value:
        import aws_sdk_synthetics.types.artifact_config_input

        out["ArtifactConfig"] = (
            aws_sdk_synthetics.types.artifact_config_input.serialize_json(
                value["artifact_config"]
            )
        )
    if "provisioned_resource_cleanup" in value:
        import aws_sdk_synthetics.types.provisioned_resource_cleanup_setting

        out["ProvisionedResourceCleanup"] = (
            aws_sdk_synthetics.types.provisioned_resource_cleanup_setting.serialize_json(
                value["provisioned_resource_cleanup"]
            )
        )
    if "dry_run_id" in value:
        out["DryRunId"] = value["dry_run_id"]
    if "visual_references" in value:
        import aws_sdk_synthetics.types.visual_references

        out["VisualReferences"] = (
            aws_sdk_synthetics.types.visual_references.serialize_json(
                value["visual_references"]
            )
        )
    if "browser_configs" in value:
        import aws_sdk_synthetics.types.browser_configs

        out["BrowserConfigs"] = aws_sdk_synthetics.types.browser_configs.serialize_json(
            value["browser_configs"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCanaryRequest:
    out: UpdateCanaryRequest = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_synthetics.types.canary_code_input

        out["code"] = aws_sdk_synthetics.types.canary_code_input.deserialize_json(
            data["Code"]
        )
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "RuntimeVersion" in data:
        out["runtime_version"] = data["RuntimeVersion"]
    if "Schedule" in data:
        import aws_sdk_synthetics.types.canary_schedule_input

        out["schedule"] = (
            aws_sdk_synthetics.types.canary_schedule_input.deserialize_json(
                data["Schedule"]
            )
        )
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
    if "VpcConfig" in data:
        import aws_sdk_synthetics.types.vpc_config_input

        out["vpc_config"] = aws_sdk_synthetics.types.vpc_config_input.deserialize_json(
            data["VpcConfig"]
        )
    if "VisualReference" in data:
        import aws_sdk_synthetics.types.visual_reference_input

        out["visual_reference"] = (
            aws_sdk_synthetics.types.visual_reference_input.deserialize_json(
                data["VisualReference"]
            )
        )
    if "ArtifactS3Location" in data:
        out["artifact_s3_location"] = data["ArtifactS3Location"]
    if "ArtifactConfig" in data:
        import aws_sdk_synthetics.types.artifact_config_input

        out["artifact_config"] = (
            aws_sdk_synthetics.types.artifact_config_input.deserialize_json(
                data["ArtifactConfig"]
            )
        )
    if "ProvisionedResourceCleanup" in data:
        import aws_sdk_synthetics.types.provisioned_resource_cleanup_setting

        out["provisioned_resource_cleanup"] = (
            aws_sdk_synthetics.types.provisioned_resource_cleanup_setting.deserialize_json(
                data["ProvisionedResourceCleanup"]
            )
        )
    if "DryRunId" in data:
        out["dry_run_id"] = data["DryRunId"]
    if "VisualReferences" in data:
        import aws_sdk_synthetics.types.visual_references

        out["visual_references"] = (
            aws_sdk_synthetics.types.visual_references.deserialize_json(
                data["VisualReferences"]
            )
        )
    if "BrowserConfigs" in data:
        import aws_sdk_synthetics.types.browser_configs

        out["browser_configs"] = (
            aws_sdk_synthetics.types.browser_configs.deserialize_json(
                data["BrowserConfigs"]
            )
        )
    return out
