"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateParameterGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.tag_list


class CreateParameterGroupRequest(TypedDict, closed=True):
    parameter_group_name: "aws_sdk_memorydb.types.string.String"
    """<p>The name of the parameter group.</p>"""
    family: "aws_sdk_memorydb.types.string.String"
    """<p>The name of the parameter group family that the parameter group can be used with.</p>"""
    description: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>An optional description of the parameter group.</p>"""
    tags: NotRequired["aws_sdk_memorydb.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateParameterGroupRequest) -> dict:
    out: dict = {}
    out["ParameterGroupName"] = value["parameter_group_name"]
    out["Family"] = value["family"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_memorydb.types.tag_list

        out["Tags"] = aws_sdk_memorydb.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateParameterGroupRequest:
    out: CreateParameterGroupRequest = {}  # type: ignore[typeddict-item]
    if "ParameterGroupName" in data:
        out["parameter_group_name"] = data["ParameterGroupName"]
    else:
        raise DeserializationError(
            "CreateParameterGroupRequest.parameter_group_name required"
        )
    if "Family" in data:
        out["family"] = data["Family"]
    else:
        raise DeserializationError("CreateParameterGroupRequest.family required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_memorydb.types.tag_list

        out["tags"] = aws_sdk_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
