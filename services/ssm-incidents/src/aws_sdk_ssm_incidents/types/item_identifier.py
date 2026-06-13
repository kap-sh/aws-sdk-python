"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ItemIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.item_type
    import aws_sdk_ssm_incidents.types.item_value


class ItemIdentifier(TypedDict):
    value: "aws_sdk_ssm_incidents.types.item_value.ItemValue"
    """<p>Details about the related item.</p>"""
    type: "aws_sdk_ssm_incidents.types.item_type.ItemType"
    """<p>The type of related item. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ItemIdentifier) -> dict:
    out: dict = {}
    import aws_sdk_ssm_incidents.types.item_value

    out["value"] = aws_sdk_ssm_incidents.types.item_value.serialize_json(value["value"])
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ItemIdentifier:
    out: ItemIdentifier = {}  # type: ignore[typeddict-item]
    if "value" in data:
        import aws_sdk_ssm_incidents.types.item_value

        out["value"] = aws_sdk_ssm_incidents.types.item_value.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("ItemIdentifier.value required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("ItemIdentifier.type required")
    return out
