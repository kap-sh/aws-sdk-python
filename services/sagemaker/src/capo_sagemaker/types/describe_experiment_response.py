"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeExperimentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_arn
    import capo_sagemaker.types.experiment_description
    import capo_sagemaker.types.experiment_entity_name
    import capo_sagemaker.types.experiment_source
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context


class DescribeExperimentResponse(TypedDict, closed=True):
    experiment_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment.</p>"""
    experiment_arn: NotRequired["capo_sagemaker.types.experiment_arn.ExperimentArn"]
    """<p>The Amazon Resource Name (ARN) of the experiment.</p>"""
    display_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment as displayed. If <code>DisplayName</code> isn't specified, <code>ExperimentName</code> is displayed.</p>"""
    source: NotRequired["capo_sagemaker.types.experiment_source.ExperimentSource"]
    """<p>The Amazon Resource Name (ARN) of the source and, optionally, the type.</p>"""
    description: NotRequired[
        "capo_sagemaker.types.experiment_description.ExperimentDescription"
    ]
    """<p>The description of the experiment.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the experiment was created.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    """<p>Who created the experiment.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the experiment was last modified.</p>"""
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    """<p>Who last modified the experiment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExperimentResponse) -> dict:
    out: dict = {}
    if "experiment_name" in value:
        out["ExperimentName"] = value["experiment_name"]
    if "experiment_arn" in value:
        out["ExperimentArn"] = value["experiment_arn"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "source" in value:
        import capo_sagemaker.types.experiment_source

        out["Source"] = capo_sagemaker.types.experiment_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "last_modified_by" in value:
        import capo_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            capo_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExperimentResponse:
    out: DescribeExperimentResponse = {}  # type: ignore[typeddict-item]
    if "ExperimentName" in data:
        out["experiment_name"] = data["ExperimentName"]
    if "ExperimentArn" in data:
        out["experiment_arn"] = data["ExperimentArn"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Source" in data:
        import capo_sagemaker.types.experiment_source

        out["source"] = capo_sagemaker.types.experiment_source.deserialize_aws_json_1_1(
            data["Source"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "CreatedBy" in data:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastModifiedBy" in data:
        import capo_sagemaker.types.user_context

        out["last_modified_by"] = (
            capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    return out
