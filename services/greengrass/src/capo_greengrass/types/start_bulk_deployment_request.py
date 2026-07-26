"""Generated from Smithy shape ``com.amazonaws.greengrass#StartBulkDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string
    import capo_greengrass.types.tags


class StartBulkDeploymentRequest(TypedDict, closed=True):
    amzn_client_token: NotRequired["capo_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    execution_role_arn: NotRequired["capo_greengrass.types.__string.__string"]
    """The ARN of the execution role to associate with the bulk deployment operation. This IAM role must allow the ''greengrass:CreateDeployment'' action for all group versions that are listed in the input file. This IAM role must have access to the S3 bucket containing the input file."""
    input_file_uri: NotRequired["capo_greengrass.types.__string.__string"]
    """The URI of the input file contained in the S3 bucket. The execution role must have ''getObject'' permissions on this bucket to access the input file. The input file is a JSON-serialized, line delimited file with UTF-8 encoding that provides a list of group and version IDs and the deployment type. This file must be less than 100 MB. Currently, AWS IoT Greengrass supports only ''NewDeployment'' deployment types."""
    tags: NotRequired["capo_greengrass.types.tags.Tags"]
    """Tag(s) to add to the new resource."""


# --- restJson1 ser/de ---
def serialize_json(value: StartBulkDeploymentRequest) -> dict:
    out: dict = {}
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "input_file_uri" in value:
        out["InputFileUri"] = value["input_file_uri"]
    if "tags" in value:
        import capo_greengrass.types.tags

        out["tags"] = capo_greengrass.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartBulkDeploymentRequest:
    out: StartBulkDeploymentRequest = {}  # type: ignore[typeddict-item]
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "InputFileUri" in data:
        out["input_file_uri"] = data["InputFileUri"]
    if "tags" in data:
        import capo_greengrass.types.tags

        out["tags"] = capo_greengrass.types.tags.deserialize_json(data["tags"])
    return out
