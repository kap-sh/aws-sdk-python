"""Generated from Smithy shape ``com.amazonaws.groundstation#ConfigListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.config_arn
    import capo_groundstation.types.config_capability_type


class ConfigListItem(TypedDict, closed=True):
    config_id: NotRequired["str"]
    """<p>UUID of a <code>Config</code>.</p>"""
    config_type: NotRequired[
        "capo_groundstation.types.config_capability_type.ConfigCapabilityType"
    ]
    """<p>Type of a <code>Config</code>.</p>"""
    config_arn: NotRequired["capo_groundstation.types.config_arn.ConfigArn"]
    """<p>ARN of a <code>Config</code>.</p>"""
    name: NotRequired["str"]
    """<p>Name of a <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigListItem) -> dict:
    out: dict = {}
    if "config_id" in value:
        out["configId"] = value["config_id"]
    if "config_type" in value:
        import capo_groundstation.types.config_capability_type

        out["configType"] = (
            capo_groundstation.types.config_capability_type.serialize_json(
                value["config_type"]
            )
        )
    if "config_arn" in value:
        out["configArn"] = value["config_arn"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ConfigListItem:
    out: ConfigListItem = {}  # type: ignore[typeddict-item]
    if "configId" in data:
        out["config_id"] = data["configId"]
    if "configType" in data:
        import capo_groundstation.types.config_capability_type

        out["config_type"] = (
            capo_groundstation.types.config_capability_type.deserialize_json(
                data["configType"]
            )
        )
    if "configArn" in data:
        out["config_arn"] = data["configArn"]
    if "name" in data:
        out["name"] = data["name"]
    return out
