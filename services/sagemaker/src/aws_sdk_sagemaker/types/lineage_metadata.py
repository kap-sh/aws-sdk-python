"""Generated from Smithy shape ``com.amazonaws.sagemaker#LineageMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.association_info_list
    import aws_sdk_sagemaker.types.map_string2048


class LineageMetadata(TypedDict):
    action_arns: NotRequired["aws_sdk_sagemaker.types.map_string2048.MapString2048"]
    """<p> The Amazon Resource Name (ARN) of the lineage action. </p>"""
    artifact_arns: NotRequired["aws_sdk_sagemaker.types.map_string2048.MapString2048"]
    """<p> The Amazon Resource Name (ARN) of the lineage artifact. </p>"""
    context_arns: NotRequired["aws_sdk_sagemaker.types.map_string2048.MapString2048"]
    """<p> The Amazon Resource Name (ARN) of the lineage context. </p>"""
    associations: NotRequired[
        "aws_sdk_sagemaker.types.association_info_list.AssociationInfoList"
    ]
    """<p> The lineage associations. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LineageMetadata) -> dict:
    out: dict = {}
    if "action_arns" in value:
        import aws_sdk_sagemaker.types.map_string2048

        out["ActionArns"] = (
            aws_sdk_sagemaker.types.map_string2048.serialize_aws_json_1_1(
                value["action_arns"]
            )
        )
    if "artifact_arns" in value:
        import aws_sdk_sagemaker.types.map_string2048

        out["ArtifactArns"] = (
            aws_sdk_sagemaker.types.map_string2048.serialize_aws_json_1_1(
                value["artifact_arns"]
            )
        )
    if "context_arns" in value:
        import aws_sdk_sagemaker.types.map_string2048

        out["ContextArns"] = (
            aws_sdk_sagemaker.types.map_string2048.serialize_aws_json_1_1(
                value["context_arns"]
            )
        )
    if "associations" in value:
        import aws_sdk_sagemaker.types.association_info_list

        out["Associations"] = (
            aws_sdk_sagemaker.types.association_info_list.serialize_aws_json_1_1(
                value["associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LineageMetadata:
    out: LineageMetadata = {}  # type: ignore[typeddict-item]
    if "ActionArns" in data:
        import aws_sdk_sagemaker.types.map_string2048

        out["action_arns"] = (
            aws_sdk_sagemaker.types.map_string2048.deserialize_aws_json_1_1(
                data["ActionArns"]
            )
        )
    if "ArtifactArns" in data:
        import aws_sdk_sagemaker.types.map_string2048

        out["artifact_arns"] = (
            aws_sdk_sagemaker.types.map_string2048.deserialize_aws_json_1_1(
                data["ArtifactArns"]
            )
        )
    if "ContextArns" in data:
        import aws_sdk_sagemaker.types.map_string2048

        out["context_arns"] = (
            aws_sdk_sagemaker.types.map_string2048.deserialize_aws_json_1_1(
                data["ContextArns"]
            )
        )
    if "Associations" in data:
        import aws_sdk_sagemaker.types.association_info_list

        out["associations"] = (
            aws_sdk_sagemaker.types.association_info_list.deserialize_aws_json_1_1(
                data["Associations"]
            )
        )
    return out
