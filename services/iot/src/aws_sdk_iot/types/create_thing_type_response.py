"""Generated from Smithy shape ``com.amazonaws.iot#CreateThingTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.thing_type_arn
    import aws_sdk_iot.types.thing_type_id
    import aws_sdk_iot.types.thing_type_name


class CreateThingTypeResponse(TypedDict, closed=True):
    thing_type_name: NotRequired["aws_sdk_iot.types.thing_type_name.ThingTypeName"]
    """<p>The name of the thing type.</p>"""
    thing_type_arn: NotRequired["aws_sdk_iot.types.thing_type_arn.ThingTypeArn"]
    """<p>The Amazon Resource Name (ARN) of the thing type.</p>"""
    thing_type_id: NotRequired["aws_sdk_iot.types.thing_type_id.ThingTypeId"]
    """<p>The thing type ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThingTypeResponse) -> dict:
    out: dict = {}
    if "thing_type_name" in value:
        out["thingTypeName"] = value["thing_type_name"]
    if "thing_type_arn" in value:
        out["thingTypeArn"] = value["thing_type_arn"]
    if "thing_type_id" in value:
        out["thingTypeId"] = value["thing_type_id"]
    return out


def deserialize_json(data: dict) -> CreateThingTypeResponse:
    out: CreateThingTypeResponse = {}  # type: ignore[typeddict-item]
    if "thingTypeName" in data:
        out["thing_type_name"] = data["thingTypeName"]
    if "thingTypeArn" in data:
        out["thing_type_arn"] = data["thingTypeArn"]
    if "thingTypeId" in data:
        out["thing_type_id"] = data["thingTypeId"]
    return out
