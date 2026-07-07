"""Generated from Smithy shape ``com.amazonaws.iot#UpdateThingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.attribute_payload
    import aws_sdk_iot.types.optional_version
    import aws_sdk_iot.types.remove_thing_type
    import aws_sdk_iot.types.thing_name
    import aws_sdk_iot.types.thing_type_name


class UpdateThingRequest(TypedDict, closed=True):
    thing_name: "aws_sdk_iot.types.thing_name.ThingName"
    """<p>The name of the thing to update.</p> <p>You can't change a thing's name. To change a thing's name, you must create a new thing, give it the new name, and then delete the old thing.</p>"""
    thing_type_name: NotRequired["aws_sdk_iot.types.thing_type_name.ThingTypeName"]
    """<p>The name of the thing type.</p>"""
    attribute_payload: NotRequired[
        "aws_sdk_iot.types.attribute_payload.AttributePayload"
    ]
    r"""<p>A list of thing attributes, a JSON string containing name-value pairs. For example:</p> <p> <code>{\\"attributes\\":{\\"name1\\":\\"value2\\"}}</code> </p> <p>This data is used to add new attributes or update existing attributes.</p>"""
    expected_version: NotRequired["aws_sdk_iot.types.optional_version.OptionalVersion"]
    """<p>The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the <code>UpdateThing</code> request is rejected with a <code>VersionConflictException</code>.</p>"""
    remove_thing_type: "aws_sdk_iot.types.remove_thing_type.RemoveThingType"
    """<p>Remove a thing type association. If <b>true</b>, the association is removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThingRequest) -> dict:
    out: dict = {}
    if "thing_type_name" in value:
        out["thingTypeName"] = value["thing_type_name"]
    if "attribute_payload" in value:
        import aws_sdk_iot.types.attribute_payload

        out["attributePayload"] = aws_sdk_iot.types.attribute_payload.serialize_json(
            value["attribute_payload"]
        )
    if "expected_version" in value:
        out["expectedVersion"] = value["expected_version"]
    out["removeThingType"] = value.get("remove_thing_type", False)
    return out


def deserialize_json(data: dict) -> UpdateThingRequest:
    out: UpdateThingRequest = {}  # type: ignore[typeddict-item]
    if "thingTypeName" in data:
        out["thing_type_name"] = data["thingTypeName"]
    if "attributePayload" in data:
        import aws_sdk_iot.types.attribute_payload

        out["attribute_payload"] = aws_sdk_iot.types.attribute_payload.deserialize_json(
            data["attributePayload"]
        )
    if "expectedVersion" in data:
        out["expected_version"] = data["expectedVersion"]
    if "removeThingType" in data:
        out["remove_thing_type"] = data["removeThingType"]
    else:
        out["remove_thing_type"] = False
    return out
