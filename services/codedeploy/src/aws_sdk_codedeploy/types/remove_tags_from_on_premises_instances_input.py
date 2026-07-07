"""Generated from Smithy shape ``com.amazonaws.codedeploy#RemoveTagsFromOnPremisesInstancesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.instance_name_list
    import aws_sdk_codedeploy.types.tag_list


class RemoveTagsFromOnPremisesInstancesInput(TypedDict, closed=True):
    tags: "aws_sdk_codedeploy.types.tag_list.TagList"
    """<p>The tag key-value pairs to remove from the on-premises instances.</p>"""
    instance_names: "aws_sdk_codedeploy.types.instance_name_list.InstanceNameList"
    """<p>The names of the on-premises instances from which to remove tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsFromOnPremisesInstancesInput) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsFromOnPremisesInstancesInput:
    out: RemoveTagsFromOnPremisesInstancesInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_codedeploy.types.tag_list

        out["tags"] = aws_sdk_codedeploy.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        raise DeserializationError(
            "RemoveTagsFromOnPremisesInstancesInput.tags required"
        )
    if "instanceNames" in data:
        import aws_sdk_codedeploy.types.instance_name_list

        out["instance_names"] = (
            aws_sdk_codedeploy.types.instance_name_list.deserialize_aws_json_1_1(
                data["instanceNames"]
            )
        )
    else:
        raise DeserializationError(
            "RemoveTagsFromOnPremisesInstancesInput.instance_names required"
        )
    return out
