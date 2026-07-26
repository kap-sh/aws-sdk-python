"""Generated from Smithy shape ``com.amazonaws.iot#Mqtt5Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.propagating_attribute_list


class Mqtt5Configuration(TypedDict, closed=True):
    propagating_attributes: NotRequired[
        "capo_iot.types.propagating_attribute_list.PropagatingAttributeList"
    ]
    """<p>An object that represents the propagating thing attributes and the connection attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Mqtt5Configuration) -> dict:
    out: dict = {}
    if "propagating_attributes" in value:
        import capo_iot.types.propagating_attribute_list

        out["propagatingAttributes"] = (
            capo_iot.types.propagating_attribute_list.serialize_json(
                value["propagating_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> Mqtt5Configuration:
    out: Mqtt5Configuration = {}  # type: ignore[typeddict-item]
    if "propagatingAttributes" in data:
        import capo_iot.types.propagating_attribute_list

        out["propagating_attributes"] = (
            capo_iot.types.propagating_attribute_list.deserialize_json(
                data["propagatingAttributes"]
            )
        )
    return out
