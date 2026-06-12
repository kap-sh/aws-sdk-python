"""Generated from Smithy shape ``com.amazonaws.codedeploy#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.arn
    import aws_sdk_codedeploy.types.tag_list


class TagResourceInput(TypedDict):
    resource_arn: "aws_sdk_codedeploy.types.arn.Arn"
    """<p> The ARN of a resource, such as a CodeDeploy application or deployment group. </p>"""
    tags: "aws_sdk_codedeploy.types.tag_list.TagList"
    """<p> A list of tags that <code>TagResource</code> associates with a resource. The resource is identified by the <code>ResourceArn</code> input parameter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_codedeploy.types.tag_list

    out["Tags"] = aws_sdk_codedeploy.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if "Tags" in data:
        import aws_sdk_codedeploy.types.tag_list

        out["tags"] = aws_sdk_codedeploy.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
