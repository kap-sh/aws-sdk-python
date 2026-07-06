"""Generated from Smithy shape ``com.amazonaws.iot#CreateThingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.thing_arn
    import aws_sdk_iot.types.thing_id
    import aws_sdk_iot.types.thing_name


class CreateThingResponse(TypedDict, closed=True):
    thing_name: NotRequired["aws_sdk_iot.types.thing_name.ThingName"]
    """<p>The name of the new thing.</p>"""
    thing_arn: NotRequired["aws_sdk_iot.types.thing_arn.ThingArn"]
    """<p>The ARN of the new thing.</p>"""
    thing_id: NotRequired["aws_sdk_iot.types.thing_id.ThingId"]
    """<p>The thing ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThingResponse) -> dict:
    out: dict = {}
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "thing_arn" in value:
        out["thingArn"] = value["thing_arn"]
    if "thing_id" in value:
        out["thingId"] = value["thing_id"]
    return out


def deserialize_json(data: dict) -> CreateThingResponse:
    out: CreateThingResponse = {}  # type: ignore[typeddict-item]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "thingArn" in data:
        out["thing_arn"] = data["thingArn"]
    if "thingId" in data:
        out["thing_id"] = data["thingId"]
    return out
