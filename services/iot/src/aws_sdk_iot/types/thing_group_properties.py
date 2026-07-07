"""Generated from Smithy shape ``com.amazonaws.iot#ThingGroupProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.attribute_payload
    import aws_sdk_iot.types.thing_group_description


class ThingGroupProperties(TypedDict, closed=True):
    thing_group_description: NotRequired[
        "aws_sdk_iot.types.thing_group_description.ThingGroupDescription"
    ]
    """<p>The thing group description.</p>"""
    attribute_payload: NotRequired[
        "aws_sdk_iot.types.attribute_payload.AttributePayload"
    ]
    """<p>The thing group attributes in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThingGroupProperties) -> dict:
    out: dict = {}
    if "thing_group_description" in value:
        out["thingGroupDescription"] = value["thing_group_description"]
    if "attribute_payload" in value:
        import aws_sdk_iot.types.attribute_payload

        out["attributePayload"] = aws_sdk_iot.types.attribute_payload.serialize_json(
            value["attribute_payload"]
        )
    return out


def deserialize_json(data: dict) -> ThingGroupProperties:
    out: ThingGroupProperties = {}  # type: ignore[typeddict-item]
    if "thingGroupDescription" in data:
        out["thing_group_description"] = data["thingGroupDescription"]
    if "attributePayload" in data:
        import aws_sdk_iot.types.attribute_payload

        out["attribute_payload"] = aws_sdk_iot.types.attribute_payload.deserialize_json(
            data["attributePayload"]
        )
    return out
