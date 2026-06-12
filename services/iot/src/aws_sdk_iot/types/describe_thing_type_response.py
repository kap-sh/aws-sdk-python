"""Generated from Smithy shape ``com.amazonaws.iot#DescribeThingTypeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.thing_type_arn
    import aws_sdk_iot.types.thing_type_id
    import aws_sdk_iot.types.thing_type_metadata
    import aws_sdk_iot.types.thing_type_name
    import aws_sdk_iot.types.thing_type_properties


class DescribeThingTypeResponse(TypedDict):
    thing_type_name: NotRequired["aws_sdk_iot.types.thing_type_name.ThingTypeName"]
    """<p>The name of the thing type.</p>"""
    thing_type_id: NotRequired["aws_sdk_iot.types.thing_type_id.ThingTypeId"]
    """<p>The thing type ID.</p>"""
    thing_type_arn: NotRequired["aws_sdk_iot.types.thing_type_arn.ThingTypeArn"]
    """<p>The thing type ARN.</p>"""
    thing_type_properties: NotRequired[
        "aws_sdk_iot.types.thing_type_properties.ThingTypeProperties"
    ]
    """<p>The ThingTypeProperties contains information about the thing type including description, a list of searchable thing attribute names, and MQTT5 configuration.</p>"""
    thing_type_metadata: NotRequired[
        "aws_sdk_iot.types.thing_type_metadata.ThingTypeMetadata"
    ]
    """<p>The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when it was deprecated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThingTypeResponse) -> dict:
    out: dict = {}
    if "thing_type_name" in value:
        out["thingTypeName"] = value["thing_type_name"]
    if "thing_type_id" in value:
        out["thingTypeId"] = value["thing_type_id"]
    if "thing_type_arn" in value:
        out["thingTypeArn"] = value["thing_type_arn"]
    if "thing_type_properties" in value:
        import aws_sdk_iot.types.thing_type_properties

        out["thingTypeProperties"] = (
            aws_sdk_iot.types.thing_type_properties.serialize_json(
                value["thing_type_properties"]
            )
        )
    if "thing_type_metadata" in value:
        import aws_sdk_iot.types.thing_type_metadata

        out["thingTypeMetadata"] = aws_sdk_iot.types.thing_type_metadata.serialize_json(
            value["thing_type_metadata"]
        )
    return out


def deserialize_json(data: dict) -> DescribeThingTypeResponse:
    out: DescribeThingTypeResponse = {}  # type: ignore[typeddict-item]
    if "thingTypeName" in data:
        out["thing_type_name"] = data["thingTypeName"]
    if "thingTypeId" in data:
        out["thing_type_id"] = data["thingTypeId"]
    if "thingTypeArn" in data:
        out["thing_type_arn"] = data["thingTypeArn"]
    if "thingTypeProperties" in data:
        import aws_sdk_iot.types.thing_type_properties

        out["thing_type_properties"] = (
            aws_sdk_iot.types.thing_type_properties.deserialize_json(
                data["thingTypeProperties"]
            )
        )
    if "thingTypeMetadata" in data:
        import aws_sdk_iot.types.thing_type_metadata

        out["thing_type_metadata"] = (
            aws_sdk_iot.types.thing_type_metadata.deserialize_json(
                data["thingTypeMetadata"]
            )
        )
    return out
