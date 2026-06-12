"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateDedicatedIpPoolRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.pool_name
    import aws_sdk_sesv2.types.scaling_mode
    import aws_sdk_sesv2.types.tag_list


class CreateDedicatedIpPoolRequest(TypedDict):
    pool_name: "aws_sdk_sesv2.types.pool_name.PoolName"
    """<p>The name of the dedicated IP pool.</p>"""
    tags: NotRequired["aws_sdk_sesv2.types.tag_list.TagList"]
    """<p>An object that defines the tags (keys and values) that you want to associate with the pool.</p>"""
    scaling_mode: NotRequired["aws_sdk_sesv2.types.scaling_mode.ScalingMode"]
    """<p>The type of scaling mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDedicatedIpPoolRequest) -> dict:
    out: dict = {}
    out["PoolName"] = value["pool_name"]
    if "tags" in value:
        import aws_sdk_sesv2.types.tag_list

        out["Tags"] = aws_sdk_sesv2.types.tag_list.serialize_json(value["tags"])
    if "scaling_mode" in value:
        import aws_sdk_sesv2.types.scaling_mode

        out["ScalingMode"] = aws_sdk_sesv2.types.scaling_mode.serialize_json(
            value["scaling_mode"]
        )
    return out


def deserialize_json(data: dict) -> CreateDedicatedIpPoolRequest:
    out: CreateDedicatedIpPoolRequest = {}  # type: ignore[typeddict-item]
    if "PoolName" in data:
        out["pool_name"] = data["PoolName"]
    else:
        raise DeserializationError("CreateDedicatedIpPoolRequest.pool_name required")
    if "Tags" in data:
        import aws_sdk_sesv2.types.tag_list

        out["tags"] = aws_sdk_sesv2.types.tag_list.deserialize_json(data["Tags"])
    if "ScalingMode" in data:
        import aws_sdk_sesv2.types.scaling_mode

        out["scaling_mode"] = aws_sdk_sesv2.types.scaling_mode.deserialize_json(
            data["ScalingMode"]
        )
    return out
