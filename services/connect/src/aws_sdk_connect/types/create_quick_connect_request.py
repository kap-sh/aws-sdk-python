"""Generated from Smithy shape ``com.amazonaws.connect#CreateQuickConnectRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.quick_connect_config
    import aws_sdk_connect.types.quick_connect_description
    import aws_sdk_connect.types.quick_connect_name
    import aws_sdk_connect.types.tag_map


class CreateQuickConnectRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "aws_sdk_connect.types.quick_connect_name.QuickConnectName"
    """<p>A unique name of the quick connect.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.quick_connect_description.QuickConnectDescription"
    ]
    """<p>The description of the quick connect.</p>"""
    quick_connect_config: (
        "aws_sdk_connect.types.quick_connect_config.QuickConnectConfig"
    )
    """<p>Configuration settings for the quick connect.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQuickConnectRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_connect.types.quick_connect_config

    out["QuickConnectConfig"] = (
        aws_sdk_connect.types.quick_connect_config.serialize_json(
            value["quick_connect_config"]
        )
    )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateQuickConnectRequest:
    out: CreateQuickConnectRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateQuickConnectRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "QuickConnectConfig" in data:
        import aws_sdk_connect.types.quick_connect_config

        out["quick_connect_config"] = (
            aws_sdk_connect.types.quick_connect_config.deserialize_json(
                data["QuickConnectConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateQuickConnectRequest.quick_connect_config required"
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
