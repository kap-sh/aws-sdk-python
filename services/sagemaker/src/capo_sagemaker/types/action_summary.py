"""Generated from Smithy shape ``com.amazonaws.sagemaker#ActionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.action_arn
    import capo_sagemaker.types.action_source
    import capo_sagemaker.types.action_status
    import capo_sagemaker.types.experiment_entity_name
    import capo_sagemaker.types.string64
    import capo_sagemaker.types.timestamp


class ActionSummary(TypedDict, closed=True):
    action_arn: NotRequired["capo_sagemaker.types.action_arn.ActionArn"]
    """<p>The Amazon Resource Name (ARN) of the action.</p>"""
    action_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the action.</p>"""
    source: NotRequired["capo_sagemaker.types.action_source.ActionSource"]
    """<p>The source of the action.</p>"""
    action_type: NotRequired["capo_sagemaker.types.string64.String64"]
    """<p>The type of the action.</p>"""
    status: NotRequired["capo_sagemaker.types.action_status.ActionStatus"]
    """<p>The status of the action.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the action was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the action was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionSummary) -> dict:
    out: dict = {}
    if "action_arn" in value:
        out["ActionArn"] = value["action_arn"]
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
    if "source" in value:
        import capo_sagemaker.types.action_source

        out["Source"] = capo_sagemaker.types.action_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "action_type" in value:
        out["ActionType"] = value["action_type"]
    if "status" in value:
        import capo_sagemaker.types.action_status

        out["Status"] = capo_sagemaker.types.action_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionSummary:
    out: ActionSummary = {}  # type: ignore[typeddict-item]
    if "ActionArn" in data:
        out["action_arn"] = data["ActionArn"]
    if "ActionName" in data:
        out["action_name"] = data["ActionName"]
    if "Source" in data:
        import capo_sagemaker.types.action_source

        out["source"] = capo_sagemaker.types.action_source.deserialize_aws_json_1_1(
            data["Source"]
        )
    if "ActionType" in data:
        out["action_type"] = data["ActionType"]
    if "Status" in data:
        import capo_sagemaker.types.action_status

        out["status"] = capo_sagemaker.types.action_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
