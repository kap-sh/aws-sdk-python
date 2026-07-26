"""Generated from Smithy shape ``com.amazonaws.synthetics#Canary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.artifact_config_output
    import capo_synthetics.types.browser_configs
    import capo_synthetics.types.canary_code_output
    import capo_synthetics.types.canary_name
    import capo_synthetics.types.canary_run_config_output
    import capo_synthetics.types.canary_schedule_output
    import capo_synthetics.types.canary_status
    import capo_synthetics.types.canary_timeline
    import capo_synthetics.types.dry_run_config_output
    import capo_synthetics.types.engine_configs
    import capo_synthetics.types.function_arn
    import capo_synthetics.types.max_size1024
    import capo_synthetics.types.provisioned_resource_cleanup_setting
    import capo_synthetics.types.role_arn
    import capo_synthetics.types.string
    import capo_synthetics.types.tag_map
    import capo_synthetics.types.uuid
    import capo_synthetics.types.visual_reference_output
    import capo_synthetics.types.visual_references_output
    import capo_synthetics.types.vpc_config_output


class Canary(TypedDict, closed=True):
    id: NotRequired["capo_synthetics.types.uuid.UUID"]
    """<p>The unique ID of this canary.</p>"""
    name: NotRequired["capo_synthetics.types.canary_name.CanaryName"]
    """<p>The name of the canary.</p>"""
    code: NotRequired["capo_synthetics.types.canary_code_output.CanaryCodeOutput"]
    execution_role_arn: NotRequired["capo_synthetics.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role used to run the canary. This role must include <code>lambda.amazonaws.com</code> as a principal in the trust policy.</p>"""
    schedule: NotRequired[
        "capo_synthetics.types.canary_schedule_output.CanaryScheduleOutput"
    ]
    """<p>A structure that contains information about how often the canary is to run, and when these runs are to stop.</p>"""
    run_config: NotRequired[
        "capo_synthetics.types.canary_run_config_output.CanaryRunConfigOutput"
    ]
    success_retention_period_in_days: NotRequired[
        "capo_synthetics.types.max_size1024.MaxSize1024"
    ]
    r"""<p>The number of days to retain data about successful runs of this canary.</p> <p>This setting affects the range of information returned by <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html\">GetCanaryRuns</a>, as well as the range of information displayed in the Synthetics console. </p>"""
    failure_retention_period_in_days: NotRequired[
        "capo_synthetics.types.max_size1024.MaxSize1024"
    ]
    r"""<p>The number of days to retain data about failed runs of this canary.</p> <p>This setting affects the range of information returned by <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html\">GetCanaryRuns</a>, as well as the range of information displayed in the Synthetics console. </p>"""
    status: NotRequired["capo_synthetics.types.canary_status.CanaryStatus"]
    """<p>A structure that contains information about the canary's status.</p>"""
    timeline: NotRequired["capo_synthetics.types.canary_timeline.CanaryTimeline"]
    """<p>A structure that contains information about when the canary was created, modified, and most recently run.</p>"""
    artifact_s3_location: NotRequired["capo_synthetics.types.string.String"]
    """<p>The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary. Artifacts include the log file, screenshots, and HAR files.</p>"""
    engine_arn: NotRequired["capo_synthetics.types.function_arn.FunctionArn"]
    r"""<p>The ARN of the Lambda function that is used as your canary's engine. For more information about Lambda ARN format, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html\">Resources and Conditions for Lambda Actions</a>.</p>"""
    runtime_version: NotRequired["capo_synthetics.types.string.String"]
    r"""<p>Specifies the runtime version to use for the canary. For more information about runtime versions, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html\"> Canary Runtime Versions</a>.</p>"""
    vpc_config: NotRequired["capo_synthetics.types.vpc_config_output.VpcConfigOutput"]
    visual_reference: NotRequired[
        "capo_synthetics.types.visual_reference_output.VisualReferenceOutput"
    ]
    """<p>If this canary performs visual monitoring by comparing screenshots, this structure contains the ID of the canary run to use as the baseline for screenshots, and the coordinates of any parts of the screen to ignore during the visual monitoring comparison.</p>"""
    provisioned_resource_cleanup: NotRequired[
        "capo_synthetics.types.provisioned_resource_cleanup_setting.ProvisionedResourceCleanupSetting"
    ]
    r"""<p>Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted. If it is <code>AUTOMATIC</code>, the Lambda functions and layers will be deleted when the canary is deleted.</p> <p>If the value of this parameter is <code>OFF</code>, then the value of the <code>DeleteLambda</code> parameter of the <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html\">DeleteCanary</a> operation determines whether the Lambda functions and layers will be deleted.</p>"""
    browser_configs: NotRequired["capo_synthetics.types.browser_configs.BrowserConfigs"]
    """<p>A structure that specifies the browser type to use for a canary run. CloudWatch Synthetics supports running canaries on both <code>CHROME</code> and <code>FIREFOX</code> browsers.</p> <note> <p>If not specified, <code>browserConfigs</code> defaults to Chrome.</p> </note>"""
    engine_configs: NotRequired["capo_synthetics.types.engine_configs.EngineConfigs"]
    """<p>A list of engine configurations for the canary, one for each browser type that the canary is configured to run on.</p> <p>All runtime versions <code>syn-nodejs-puppeteer-11.0</code> and above, and <code>syn-nodejs-playwright-3.0</code> and above, use <code>engineConfigs</code> only. You can no longer use <code>engineArn</code> in these versions.</p> <p>Runtime versions older than <code>syn-nodejs-puppeteer-11.0</code> and <code>syn-nodejs-playwright-3.0</code> continue to support <code>engineArn</code> to ensure backward compatibility.</p>"""
    visual_references: NotRequired[
        "capo_synthetics.types.visual_references_output.VisualReferencesOutput"
    ]
    """<p>A list of visual reference configurations for the canary, one for each browser type that the canary is configured to run on. Visual references are used for visual monitoring comparisons.</p> <p> <code>syn-nodejs-puppeteer-11.0</code> and above, and <code>syn-nodejs-playwright-3.0</code> and above, only supports <code>visualReferences</code>. <code>visualReference</code> field is not supported.</p> <p>Versions older than <code>syn-nodejs-puppeteer-11.0</code> supports both <code>visualReference</code> and <code>visualReferences</code> for backward compatibility. It is recommended to use <code>visualReferences</code> for consistency and future compatibility.</p>"""
    tags: NotRequired["capo_synthetics.types.tag_map.TagMap"]
    """<p>The list of key-value pairs that are associated with the canary.</p>"""
    artifact_config: NotRequired[
        "capo_synthetics.types.artifact_config_output.ArtifactConfigOutput"
    ]
    """<p>A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.</p>"""
    dry_run_config: NotRequired[
        "capo_synthetics.types.dry_run_config_output.DryRunConfigOutput"
    ]
    """<p>Returns the dry run configurations for a canary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Canary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "code" in value:
        import capo_synthetics.types.canary_code_output

        out["Code"] = capo_synthetics.types.canary_code_output.serialize_json(
            value["code"]
        )
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "schedule" in value:
        import capo_synthetics.types.canary_schedule_output

        out["Schedule"] = capo_synthetics.types.canary_schedule_output.serialize_json(
            value["schedule"]
        )
    if "run_config" in value:
        import capo_synthetics.types.canary_run_config_output

        out["RunConfig"] = (
            capo_synthetics.types.canary_run_config_output.serialize_json(
                value["run_config"]
            )
        )
    if "success_retention_period_in_days" in value:
        out["SuccessRetentionPeriodInDays"] = value["success_retention_period_in_days"]
    if "failure_retention_period_in_days" in value:
        out["FailureRetentionPeriodInDays"] = value["failure_retention_period_in_days"]
    if "status" in value:
        import capo_synthetics.types.canary_status

        out["Status"] = capo_synthetics.types.canary_status.serialize_json(
            value["status"]
        )
    if "timeline" in value:
        import capo_synthetics.types.canary_timeline

        out["Timeline"] = capo_synthetics.types.canary_timeline.serialize_json(
            value["timeline"]
        )
    if "artifact_s3_location" in value:
        out["ArtifactS3Location"] = value["artifact_s3_location"]
    if "engine_arn" in value:
        out["EngineArn"] = value["engine_arn"]
    if "runtime_version" in value:
        out["RuntimeVersion"] = value["runtime_version"]
    if "vpc_config" in value:
        import capo_synthetics.types.vpc_config_output

        out["VpcConfig"] = capo_synthetics.types.vpc_config_output.serialize_json(
            value["vpc_config"]
        )
    if "visual_reference" in value:
        import capo_synthetics.types.visual_reference_output

        out["VisualReference"] = (
            capo_synthetics.types.visual_reference_output.serialize_json(
                value["visual_reference"]
            )
        )
    if "provisioned_resource_cleanup" in value:
        import capo_synthetics.types.provisioned_resource_cleanup_setting

        out["ProvisionedResourceCleanup"] = (
            capo_synthetics.types.provisioned_resource_cleanup_setting.serialize_json(
                value["provisioned_resource_cleanup"]
            )
        )
    if "browser_configs" in value:
        import capo_synthetics.types.browser_configs

        out["BrowserConfigs"] = capo_synthetics.types.browser_configs.serialize_json(
            value["browser_configs"]
        )
    if "engine_configs" in value:
        import capo_synthetics.types.engine_configs

        out["EngineConfigs"] = capo_synthetics.types.engine_configs.serialize_json(
            value["engine_configs"]
        )
    if "visual_references" in value:
        import capo_synthetics.types.visual_references_output

        out["VisualReferences"] = (
            capo_synthetics.types.visual_references_output.serialize_json(
                value["visual_references"]
            )
        )
    if "tags" in value:
        import capo_synthetics.types.tag_map

        out["Tags"] = capo_synthetics.types.tag_map.serialize_json(value["tags"])
    if "artifact_config" in value:
        import capo_synthetics.types.artifact_config_output

        out["ArtifactConfig"] = (
            capo_synthetics.types.artifact_config_output.serialize_json(
                value["artifact_config"]
            )
        )
    if "dry_run_config" in value:
        import capo_synthetics.types.dry_run_config_output

        out["DryRunConfig"] = (
            capo_synthetics.types.dry_run_config_output.serialize_json(
                value["dry_run_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> Canary:
    out: Canary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Code" in data:
        import capo_synthetics.types.canary_code_output

        out["code"] = capo_synthetics.types.canary_code_output.deserialize_json(
            data["Code"]
        )
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "Schedule" in data:
        import capo_synthetics.types.canary_schedule_output

        out["schedule"] = capo_synthetics.types.canary_schedule_output.deserialize_json(
            data["Schedule"]
        )
    if "RunConfig" in data:
        import capo_synthetics.types.canary_run_config_output

        out["run_config"] = (
            capo_synthetics.types.canary_run_config_output.deserialize_json(
                data["RunConfig"]
            )
        )
    if "SuccessRetentionPeriodInDays" in data:
        out["success_retention_period_in_days"] = data["SuccessRetentionPeriodInDays"]
    if "FailureRetentionPeriodInDays" in data:
        out["failure_retention_period_in_days"] = data["FailureRetentionPeriodInDays"]
    if "Status" in data:
        import capo_synthetics.types.canary_status

        out["status"] = capo_synthetics.types.canary_status.deserialize_json(
            data["Status"]
        )
    if "Timeline" in data:
        import capo_synthetics.types.canary_timeline

        out["timeline"] = capo_synthetics.types.canary_timeline.deserialize_json(
            data["Timeline"]
        )
    if "ArtifactS3Location" in data:
        out["artifact_s3_location"] = data["ArtifactS3Location"]
    if "EngineArn" in data:
        out["engine_arn"] = data["EngineArn"]
    if "RuntimeVersion" in data:
        out["runtime_version"] = data["RuntimeVersion"]
    if "VpcConfig" in data:
        import capo_synthetics.types.vpc_config_output

        out["vpc_config"] = capo_synthetics.types.vpc_config_output.deserialize_json(
            data["VpcConfig"]
        )
    if "VisualReference" in data:
        import capo_synthetics.types.visual_reference_output

        out["visual_reference"] = (
            capo_synthetics.types.visual_reference_output.deserialize_json(
                data["VisualReference"]
            )
        )
    if "ProvisionedResourceCleanup" in data:
        import capo_synthetics.types.provisioned_resource_cleanup_setting

        out["provisioned_resource_cleanup"] = (
            capo_synthetics.types.provisioned_resource_cleanup_setting.deserialize_json(
                data["ProvisionedResourceCleanup"]
            )
        )
    if "BrowserConfigs" in data:
        import capo_synthetics.types.browser_configs

        out["browser_configs"] = capo_synthetics.types.browser_configs.deserialize_json(
            data["BrowserConfigs"]
        )
    if "EngineConfigs" in data:
        import capo_synthetics.types.engine_configs

        out["engine_configs"] = capo_synthetics.types.engine_configs.deserialize_json(
            data["EngineConfigs"]
        )
    if "VisualReferences" in data:
        import capo_synthetics.types.visual_references_output

        out["visual_references"] = (
            capo_synthetics.types.visual_references_output.deserialize_json(
                data["VisualReferences"]
            )
        )
    if "Tags" in data:
        import capo_synthetics.types.tag_map

        out["tags"] = capo_synthetics.types.tag_map.deserialize_json(data["Tags"])
    if "ArtifactConfig" in data:
        import capo_synthetics.types.artifact_config_output

        out["artifact_config"] = (
            capo_synthetics.types.artifact_config_output.deserialize_json(
                data["ArtifactConfig"]
            )
        )
    if "DryRunConfig" in data:
        import capo_synthetics.types.dry_run_config_output

        out["dry_run_config"] = (
            capo_synthetics.types.dry_run_config_output.deserialize_json(
                data["DryRunConfig"]
            )
        )
    return out
