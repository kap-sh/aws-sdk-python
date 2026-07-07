"""Generated from Smithy shape ``com.amazonaws.transfer#TagStepDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transfer.types.s3_tags
    import aws_sdk_transfer.types.source_file_location
    import aws_sdk_transfer.types.workflow_step_name


class TagStepDetails(TypedDict, closed=True):
    name: NotRequired["aws_sdk_transfer.types.workflow_step_name.WorkflowStepName"]
    """<p>The name of the step, used as an identifier.</p>"""
    tags: NotRequired["aws_sdk_transfer.types.s3_tags.S3Tags"]
    """<p>Array that contains from 1 to 10 key/value pairs.</p>"""
    source_file_location: NotRequired[
        "aws_sdk_transfer.types.source_file_location.SourceFileLocation"
    ]
    """<p>Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.</p> <ul> <li> <p>To use the previous file as the input, enter <code>${previous.file}</code>. In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.</p> </li> <li> <p>To use the originally uploaded file location as input for this step, enter <code>${original.file}</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagStepDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "tags" in value:
        import aws_sdk_transfer.types.s3_tags

        out["Tags"] = aws_sdk_transfer.types.s3_tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "source_file_location" in value:
        out["SourceFileLocation"] = value["source_file_location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TagStepDetails:
    out: TagStepDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Tags" in data:
        import aws_sdk_transfer.types.s3_tags

        out["tags"] = aws_sdk_transfer.types.s3_tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "SourceFileLocation" in data:
        out["source_file_location"] = data["SourceFileLocation"]
    return out
