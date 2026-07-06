"""Generated from Smithy shape ``com.amazonaws.personalize#CreateEventTrackerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.tags


class CreateEventTrackerRequest(TypedDict, closed=True):
    name: "aws_sdk_personalize.types.name.Name"
    """<p>The name for the event tracker.</p>"""
    dataset_group_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset group that receives the event data.</p>"""
    tags: NotRequired["aws_sdk_personalize.types.tags.Tags"]
    r"""<p>A list of <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html\">tags</a> to apply to the event tracker.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEventTrackerRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["datasetGroupArn"] = value["dataset_group_arn"]
    if "tags" in value:
        import aws_sdk_personalize.types.tags

        out["tags"] = aws_sdk_personalize.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEventTrackerRequest:
    out: CreateEventTrackerRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEventTrackerRequest.name required")
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    else:
        raise DeserializationError(
            "CreateEventTrackerRequest.dataset_group_arn required"
        )
    if "tags" in data:
        import aws_sdk_personalize.types.tags

        out["tags"] = aws_sdk_personalize.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
