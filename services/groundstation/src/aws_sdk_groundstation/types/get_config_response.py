"""Generated from Smithy shape ``com.amazonaws.groundstation#GetConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.config_arn
    import aws_sdk_groundstation.types.config_capability_type
    import aws_sdk_groundstation.types.config_type_data
    import aws_sdk_groundstation.types.tags_map


class GetConfigResponse(TypedDict, closed=True):
    config_id: "str"
    """<p>UUID of a <code>Config</code>.</p>"""
    config_arn: "aws_sdk_groundstation.types.config_arn.ConfigArn"
    """<p>ARN of a <code>Config</code> </p>"""
    name: "str"
    """<p>Name of a <code>Config</code>.</p>"""
    config_type: NotRequired[
        "aws_sdk_groundstation.types.config_capability_type.ConfigCapabilityType"
    ]
    """<p>Type of a <code>Config</code>.</p>"""
    config_data: "aws_sdk_groundstation.types.config_type_data.ConfigTypeData"
    """<p>Data elements in a <code>Config</code>.</p>"""
    tags: NotRequired["aws_sdk_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to a <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigResponse) -> dict:
    out: dict = {}
    out["configId"] = value["config_id"]
    out["configArn"] = value["config_arn"]
    out["name"] = value["name"]
    if "config_type" in value:
        import aws_sdk_groundstation.types.config_capability_type

        out["configType"] = (
            aws_sdk_groundstation.types.config_capability_type.serialize_json(
                value["config_type"]
            )
        )
    import aws_sdk_groundstation.types.config_type_data

    out["configData"] = aws_sdk_groundstation.types.config_type_data.serialize_json(
        value["config_data"]
    )
    if "tags" in value:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetConfigResponse:
    out: GetConfigResponse = {}  # type: ignore[typeddict-item]
    if "configId" in data:
        out["config_id"] = data["configId"]
    else:
        raise DeserializationError("GetConfigResponse.config_id required")
    if "configArn" in data:
        out["config_arn"] = data["configArn"]
    else:
        raise DeserializationError("GetConfigResponse.config_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetConfigResponse.name required")
    if "configType" in data:
        import aws_sdk_groundstation.types.config_capability_type

        out["config_type"] = (
            aws_sdk_groundstation.types.config_capability_type.deserialize_json(
                data["configType"]
            )
        )
    if "configData" in data:
        import aws_sdk_groundstation.types.config_type_data

        out["config_data"] = (
            aws_sdk_groundstation.types.config_type_data.deserialize_json(
                data["configData"]
            )
        )
    else:
        raise DeserializationError("GetConfigResponse.config_data required")
    if "tags" in data:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
