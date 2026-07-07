"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectBuildBatchConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.batch_report_mode_type
    import aws_sdk_codebuild.types.batch_restrictions
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.wrapper_boolean
    import aws_sdk_codebuild.types.wrapper_int


class ProjectBuildBatchConfig(TypedDict, closed=True):
    service_role: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the service role ARN for the batch build project.</p>"""
    combine_artifacts: NotRequired[
        "aws_sdk_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p>Specifies if the build artifacts for the batch build should be combined into a single artifact location.</p>"""
    restrictions: NotRequired[
        "aws_sdk_codebuild.types.batch_restrictions.BatchRestrictions"
    ]
    """<p>A <code>BatchRestrictions</code> object that specifies the restrictions for the batch build.</p>"""
    timeout_in_mins: NotRequired["aws_sdk_codebuild.types.wrapper_int.WrapperInt"]
    """<p>Specifies the maximum amount of time, in minutes, that the batch build must be completed in.</p>"""
    batch_report_mode: NotRequired[
        "aws_sdk_codebuild.types.batch_report_mode_type.BatchReportModeType"
    ]
    """<p>Specifies how build status reports are sent to the source provider for the batch build. This property is only used when the source provider for your project is Bitbucket, GitHub, or GitHub Enterprise, and your project is configured to report build statuses to the source provider.</p> <dl> <dt>REPORT_AGGREGATED_BATCH</dt> <dd> <p>(Default) Aggregate all of the build statuses into a single status report.</p> </dd> <dt>REPORT_INDIVIDUAL_BUILDS</dt> <dd> <p>Send a separate status report for each individual build.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectBuildBatchConfig) -> dict:
    out: dict = {}
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "combine_artifacts" in value:
        out["combineArtifacts"] = value["combine_artifacts"]
    if "restrictions" in value:
        import aws_sdk_codebuild.types.batch_restrictions

        out["restrictions"] = (
            aws_sdk_codebuild.types.batch_restrictions.serialize_aws_json_1_1(
                value["restrictions"]
            )
        )
    if "timeout_in_mins" in value:
        out["timeoutInMins"] = value["timeout_in_mins"]
    if "batch_report_mode" in value:
        import aws_sdk_codebuild.types.batch_report_mode_type

        out["batchReportMode"] = (
            aws_sdk_codebuild.types.batch_report_mode_type.serialize_aws_json_1_1(
                value["batch_report_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectBuildBatchConfig:
    out: ProjectBuildBatchConfig = {}  # type: ignore[typeddict-item]
    if "serviceRole" in data:
        out["service_role"] = data["serviceRole"]
    if "combineArtifacts" in data:
        out["combine_artifacts"] = data["combineArtifacts"]
    if "restrictions" in data:
        import aws_sdk_codebuild.types.batch_restrictions

        out["restrictions"] = (
            aws_sdk_codebuild.types.batch_restrictions.deserialize_aws_json_1_1(
                data["restrictions"]
            )
        )
    if "timeoutInMins" in data:
        out["timeout_in_mins"] = data["timeoutInMins"]
    if "batchReportMode" in data:
        import aws_sdk_codebuild.types.batch_report_mode_type

        out["batch_report_mode"] = (
            aws_sdk_codebuild.types.batch_report_mode_type.deserialize_aws_json_1_1(
                data["batchReportMode"]
            )
        )
    return out
