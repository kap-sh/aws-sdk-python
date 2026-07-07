"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateTrialRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_entity_name
    import aws_sdk_sagemaker.types.metadata_properties
    import aws_sdk_sagemaker.types.tag_list


class CreateTrialRequest(TypedDict, closed=True):
    trial_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial. The name must be unique in your Amazon Web Services account and is not case-sensitive.</p>"""
    display_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial as displayed. The name doesn't need to be unique. If <code>DisplayName</code> isn't specified, <code>TrialName</code> is displayed.</p>"""
    experiment_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment to associate the trial with.</p>"""
    metadata_properties: NotRequired[
        "aws_sdk_sagemaker.types.metadata_properties.MetadataProperties"
    ]
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    r"""<p>A list of tags to associate with the trial. You can use <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html\">Search</a> API to search on the tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrialRequest) -> dict:
    out: dict = {}
    if "trial_name" in value:
        out["TrialName"] = value["trial_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "experiment_name" in value:
        out["ExperimentName"] = value["experiment_name"]
    if "metadata_properties" in value:
        import aws_sdk_sagemaker.types.metadata_properties

        out["MetadataProperties"] = (
            aws_sdk_sagemaker.types.metadata_properties.serialize_aws_json_1_1(
                value["metadata_properties"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrialRequest:
    out: CreateTrialRequest = {}  # type: ignore[typeddict-item]
    if "TrialName" in data:
        out["trial_name"] = data["TrialName"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "ExperimentName" in data:
        out["experiment_name"] = data["ExperimentName"]
    if "MetadataProperties" in data:
        import aws_sdk_sagemaker.types.metadata_properties

        out["metadata_properties"] = (
            aws_sdk_sagemaker.types.metadata_properties.deserialize_aws_json_1_1(
                data["MetadataProperties"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
