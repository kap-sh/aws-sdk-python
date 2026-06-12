"""Generated from Smithy shape ``com.amazonaws.inspector#CreateResourceGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.resource_group_tags


class CreateResourceGroupRequest(TypedDict):
    resource_group_tags: "aws_sdk_inspector.types.resource_group_tags.ResourceGroupTags"
    """<p>A collection of keys and an array of possible values, '[{\"key\":\"key1\",\"values\":[\"Value1\",\"Value2\"]},{\"key\":\"Key2\",\"values\":[\"Value3\"]}]'.</p> <p>For example,'[{\"key\":\"Name\",\"values\":[\"TestEC2Instance\"]}]'.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateResourceGroupRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.resource_group_tags

    out["resourceGroupTags"] = (
        aws_sdk_inspector.types.resource_group_tags.serialize_aws_json_1_1(
            value["resource_group_tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateResourceGroupRequest:
    out: CreateResourceGroupRequest = {}  # type: ignore[typeddict-item]
    if "resourceGroupTags" in data:
        import aws_sdk_inspector.types.resource_group_tags

        out["resource_group_tags"] = (
            aws_sdk_inspector.types.resource_group_tags.deserialize_aws_json_1_1(
                data["resourceGroupTags"]
            )
        )
    else:
        raise DeserializationError(
            "CreateResourceGroupRequest.resource_group_tags required"
        )
    return out
