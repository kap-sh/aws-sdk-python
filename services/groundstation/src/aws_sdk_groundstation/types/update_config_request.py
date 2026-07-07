"""Generated from Smithy shape ``com.amazonaws.groundstation#UpdateConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.config_capability_type
    import aws_sdk_groundstation.types.config_type_data
    import aws_sdk_groundstation.types.safe_name
    import aws_sdk_groundstation.types.uuid


class UpdateConfigRequest(TypedDict, closed=True):
    config_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>UUID of a <code>Config</code>.</p>"""
    name: "aws_sdk_groundstation.types.safe_name.SafeName"
    """<p>Name of a <code>Config</code>.</p>"""
    config_type: (
        "aws_sdk_groundstation.types.config_capability_type.ConfigCapabilityType"
    )
    """<p>Type of a <code>Config</code>.</p>"""
    config_data: "aws_sdk_groundstation.types.config_type_data.ConfigTypeData"
    """<p>Parameters of a <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_groundstation.types.config_type_data

    out["configData"] = aws_sdk_groundstation.types.config_type_data.serialize_json(
        value["config_data"]
    )
    return out


def deserialize_json(data: dict) -> UpdateConfigRequest:
    out: UpdateConfigRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateConfigRequest.name required")
    if "configData" in data:
        import aws_sdk_groundstation.types.config_type_data

        out["config_data"] = (
            aws_sdk_groundstation.types.config_type_data.deserialize_json(
                data["configData"]
            )
        )
    else:
        raise DeserializationError("UpdateConfigRequest.config_data required")
    return out
