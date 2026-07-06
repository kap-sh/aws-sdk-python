"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecutionPreview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.integer
    import aws_sdk_ssm.types.region_list
    import aws_sdk_ssm.types.step_preview_map
    import aws_sdk_ssm.types.target_preview_list


class AutomationExecutionPreview(TypedDict, closed=True):
    step_previews: NotRequired["aws_sdk_ssm.types.step_preview_map.StepPreviewMap"]
    """<p>Information about the type of impact a runbook step would have on a resource.</p> <ul> <li> <p> <code>Mutating</code>: The runbook step would make changes to the targets through actions that create, modify, or delete resources.</p> </li> <li> <p> <code>Non_Mutating</code>: The runbook step would retrieve data about resources but not make changes to them. This category generally includes <code>Describe*</code>, <code>List*</code>, <code>Get*</code>, and similar read-only API actions.</p> </li> <li> <p> <code>Undetermined</code>: An undetermined step invokes executions performed by another orchestration service like Lambda, Step Functions, or Amazon Web Services Systems Manager Run Command. An undetermined step might also call a third-party API. Systems Manager Automation doesn't know the outcome of the orchestration processes or third-party API executions, so the results of the steps are undetermined.</p> </li> </ul>"""
    regions: NotRequired["aws_sdk_ssm.types.region_list.RegionList"]
    """<p>Information about the Amazon Web Services Regions targeted by the execution preview.</p>"""
    target_previews: NotRequired[
        "aws_sdk_ssm.types.target_preview_list.TargetPreviewList"
    ]
    """<p>Information that provides a preview of what the impact of running the specified Automation runbook would be.</p>"""
    total_accounts: "aws_sdk_ssm.types.integer.Integer"
    """<p>Information about the Amazon Web Services accounts that were included in the execution preview.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationExecutionPreview) -> dict:
    out: dict = {}
    if "step_previews" in value:
        import aws_sdk_ssm.types.step_preview_map

        out["StepPreviews"] = aws_sdk_ssm.types.step_preview_map.serialize_aws_json_1_1(
            value["step_previews"]
        )
    if "regions" in value:
        import aws_sdk_ssm.types.region_list

        out["Regions"] = aws_sdk_ssm.types.region_list.serialize_aws_json_1_1(
            value["regions"]
        )
    if "target_previews" in value:
        import aws_sdk_ssm.types.target_preview_list

        out["TargetPreviews"] = (
            aws_sdk_ssm.types.target_preview_list.serialize_aws_json_1_1(
                value["target_previews"]
            )
        )
    out["TotalAccounts"] = value.get("total_accounts", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> AutomationExecutionPreview:
    out: AutomationExecutionPreview = {}  # type: ignore[typeddict-item]
    if "StepPreviews" in data:
        import aws_sdk_ssm.types.step_preview_map

        out["step_previews"] = (
            aws_sdk_ssm.types.step_preview_map.deserialize_aws_json_1_1(
                data["StepPreviews"]
            )
        )
    if "Regions" in data:
        import aws_sdk_ssm.types.region_list

        out["regions"] = aws_sdk_ssm.types.region_list.deserialize_aws_json_1_1(
            data["Regions"]
        )
    if "TargetPreviews" in data:
        import aws_sdk_ssm.types.target_preview_list

        out["target_previews"] = (
            aws_sdk_ssm.types.target_preview_list.deserialize_aws_json_1_1(
                data["TargetPreviews"]
            )
        )
    if "TotalAccounts" in data:
        out["total_accounts"] = data["TotalAccounts"]
    else:
        out["total_accounts"] = 0
    return out
