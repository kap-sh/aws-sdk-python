"""Generated from Smithy shape ``com.amazonaws.sagemaker#Experiment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_arn
    import aws_sdk_sagemaker.types.experiment_description
    import aws_sdk_sagemaker.types.experiment_entity_name
    import aws_sdk_sagemaker.types.experiment_source
    import aws_sdk_sagemaker.types.tag_list
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.user_context


class Experiment(TypedDict, closed=True):
    experiment_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment.</p>"""
    experiment_arn: NotRequired["aws_sdk_sagemaker.types.experiment_arn.ExperimentArn"]
    """<p>The Amazon Resource Name (ARN) of the experiment.</p>"""
    display_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment as displayed. If <code>DisplayName</code> isn't specified, <code>ExperimentName</code> is displayed.</p>"""
    source: NotRequired["aws_sdk_sagemaker.types.experiment_source.ExperimentSource"]
    description: NotRequired[
        "aws_sdk_sagemaker.types.experiment_description.ExperimentDescription"
    ]
    """<p>The description of the experiment.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the experiment was created.</p>"""
    created_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    """<p>Who created the experiment.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the experiment was last modified.</p>"""
    last_modified_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    r"""<p>The list of tags that are associated with the experiment. You can use <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html\">Search</a> API to search on the tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Experiment) -> dict:
    out: dict = {}
    if "experiment_name" in value:
        out["ExperimentName"] = value["experiment_name"]
    if "experiment_arn" in value:
        out["ExperimentArn"] = value["experiment_arn"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "source" in value:
        import aws_sdk_sagemaker.types.experiment_source

        out["Source"] = (
            aws_sdk_sagemaker.types.experiment_source.serialize_aws_json_1_1(
                value["source"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["CreatedBy"] = aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_modified_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Experiment:
    out: Experiment = {}  # type: ignore[typeddict-item]
    if "ExperimentName" in data:
        out["experiment_name"] = data["ExperimentName"]
    if "ExperimentArn" in data:
        out["experiment_arn"] = data["ExperimentArn"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Source" in data:
        import aws_sdk_sagemaker.types.experiment_source

        out["source"] = (
            aws_sdk_sagemaker.types.experiment_source.deserialize_aws_json_1_1(
                data["Source"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "CreatedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["created_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["CreatedBy"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastModifiedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["last_modified_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
