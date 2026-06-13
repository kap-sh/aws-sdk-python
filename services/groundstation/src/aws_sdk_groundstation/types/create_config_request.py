"""Generated from Smithy shape ``com.amazonaws.groundstation#CreateConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.config_type_data
    import aws_sdk_groundstation.types.safe_name
    import aws_sdk_groundstation.types.tags_map


class CreateConfigRequest(TypedDict):
    name: "aws_sdk_groundstation.types.safe_name.SafeName"
    """<p>Name of a <code>Config</code>.</p>"""
    config_data: "aws_sdk_groundstation.types.config_type_data.ConfigTypeData"
    """<p>Parameters of a <code>Config</code>.</p>"""
    tags: NotRequired["aws_sdk_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to a <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_groundstation.types.config_type_data

    out["configData"] = aws_sdk_groundstation.types.config_type_data.serialize_json(
        value["config_data"]
    )
    if "tags" in value:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConfigRequest:
    out: CreateConfigRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateConfigRequest.name required")
    if "configData" in data:
        import aws_sdk_groundstation.types.config_type_data

        out["config_data"] = (
            aws_sdk_groundstation.types.config_type_data.deserialize_json(
                data["configData"]
            )
        )
    else:
        raise DeserializationError("CreateConfigRequest.config_data required")
    if "tags" in data:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
