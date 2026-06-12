"""Generated from Smithy shape ``com.amazonaws.codedeploy#AddTagsToOnPremisesInstancesInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.instance_name_list
    import aws_sdk_codedeploy.types.tag_list


class AddTagsToOnPremisesInstancesInput(TypedDict):
    tags: "aws_sdk_codedeploy.types.tag_list.TagList"
    """<p>The tag key-value pairs to add to the on-premises instances.</p> <p>Keys and values are both required. Keys cannot be null or empty strings. Value-only tags are not allowed.</p>"""
    instance_names: "aws_sdk_codedeploy.types.instance_name_list.InstanceNameList"
    """<p>The names of the on-premises instances to which to add tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsToOnPremisesInstancesInput) -> dict:
    out: dict = {}
    import aws_sdk_codedeploy.types.tag_list

    out["tags"] = aws_sdk_codedeploy.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    import aws_sdk_codedeploy.types.instance_name_list

    out["instanceNames"] = (
        aws_sdk_codedeploy.types.instance_name_list.serialize_aws_json_1_1(
            value["instance_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsToOnPremisesInstancesInput:
    out: AddTagsToOnPremisesInstancesInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_codedeploy.types.tag_list

        out["tags"] = aws_sdk_codedeploy.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        raise DeserializationError("AddTagsToOnPremisesInstancesInput.tags required")
    if "instanceNames" in data:
        import aws_sdk_codedeploy.types.instance_name_list

        out["instance_names"] = (
            aws_sdk_codedeploy.types.instance_name_list.deserialize_aws_json_1_1(
                data["instanceNames"]
            )
        )
    else:
        raise DeserializationError(
            "AddTagsToOnPremisesInstancesInput.instance_names required"
        )
    return out
