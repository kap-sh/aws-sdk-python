"""Generated from Smithy shape ``com.amazonaws.personalize#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The resource's Amazon Resource Name (ARN).</p>"""
    tags: "aws_sdk_personalize.types.tags.Tags"
    r"""<p>Tags to apply to the resource. For more information see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html\">Tagging Amazon Personalize resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_personalize.types.tags

    out["tags"] = aws_sdk_personalize.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "tags" in data:
        import aws_sdk_personalize.types.tags

        out["tags"] = aws_sdk_personalize.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
