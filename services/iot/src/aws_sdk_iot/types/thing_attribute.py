"""Generated from Smithy shape ``com.amazonaws.iot#ThingAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.attributes
    import aws_sdk_iot.types.thing_arn
    import aws_sdk_iot.types.thing_name
    import aws_sdk_iot.types.thing_type_name
    import aws_sdk_iot.types.version


class ThingAttribute(TypedDict):
    thing_name: NotRequired["aws_sdk_iot.types.thing_name.ThingName"]
    """<p>The name of the thing.</p>"""
    thing_type_name: NotRequired["aws_sdk_iot.types.thing_type_name.ThingTypeName"]
    """<p>The name of the thing type, if the thing has been associated with a type.</p>"""
    thing_arn: NotRequired["aws_sdk_iot.types.thing_arn.ThingArn"]
    """<p>The thing ARN.</p>"""
    attributes: NotRequired["aws_sdk_iot.types.attributes.Attributes"]
    """<p>A list of thing attributes which are name-value pairs.</p>"""
    version: "aws_sdk_iot.types.version.Version"
    """<p>The version of the thing record in the registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThingAttribute) -> dict:
    out: dict = {}
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "thing_type_name" in value:
        out["thingTypeName"] = value["thing_type_name"]
    if "thing_arn" in value:
        out["thingArn"] = value["thing_arn"]
    if "attributes" in value:
        import aws_sdk_iot.types.attributes

        out["attributes"] = aws_sdk_iot.types.attributes.serialize_json(
            value["attributes"]
        )
    out["version"] = value.get("version", 0)
    return out


def deserialize_json(data: dict) -> ThingAttribute:
    out: ThingAttribute = {}  # type: ignore[typeddict-item]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "thingTypeName" in data:
        out["thing_type_name"] = data["thingTypeName"]
    if "thingArn" in data:
        out["thing_arn"] = data["thingArn"]
    if "attributes" in data:
        import aws_sdk_iot.types.attributes

        out["attributes"] = aws_sdk_iot.types.attributes.deserialize_json(
            data["attributes"]
        )
    if "version" in data:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    return out
