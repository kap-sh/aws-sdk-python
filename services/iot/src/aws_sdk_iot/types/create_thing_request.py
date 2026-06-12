"""Generated from Smithy shape ``com.amazonaws.iot#CreateThingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.attribute_payload
    import aws_sdk_iot.types.billing_group_name
    import aws_sdk_iot.types.thing_name
    import aws_sdk_iot.types.thing_type_name


class CreateThingRequest(TypedDict):
    thing_name: "aws_sdk_iot.types.thing_name.ThingName"
    """<p>The name of the thing to create.</p> <p>You can't change a thing's name after you create it. To change a thing's name, you must create a new thing, give it the new name, and then delete the old thing.</p>"""
    thing_type_name: NotRequired["aws_sdk_iot.types.thing_type_name.ThingTypeName"]
    """<p>The name of the thing type associated with the new thing.</p>"""
    attribute_payload: NotRequired[
        "aws_sdk_iot.types.attribute_payload.AttributePayload"
    ]
    """<p>The attribute payload, which consists of up to three name/value pairs in a JSON document. For example:</p> <p> <code>{\\"attributes\\":{\\"string1\\":\\"string2\\"}}</code> </p>"""
    billing_group_name: NotRequired[
        "aws_sdk_iot.types.billing_group_name.BillingGroupName"
    ]
    """<p>The name of the billing group the thing will be added to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThingRequest) -> dict:
    out: dict = {}
    if "thing_type_name" in value:
        out["thingTypeName"] = value["thing_type_name"]
    if "attribute_payload" in value:
        import aws_sdk_iot.types.attribute_payload

        out["attributePayload"] = aws_sdk_iot.types.attribute_payload.serialize_json(
            value["attribute_payload"]
        )
    if "billing_group_name" in value:
        out["billingGroupName"] = value["billing_group_name"]
    return out


def deserialize_json(data: dict) -> CreateThingRequest:
    out: CreateThingRequest = {}  # type: ignore[typeddict-item]
    if "thingTypeName" in data:
        out["thing_type_name"] = data["thingTypeName"]
    if "attributePayload" in data:
        import aws_sdk_iot.types.attribute_payload

        out["attribute_payload"] = aws_sdk_iot.types.attribute_payload.deserialize_json(
            data["attributePayload"]
        )
    if "billingGroupName" in data:
        out["billing_group_name"] = data["billingGroupName"]
    return out
