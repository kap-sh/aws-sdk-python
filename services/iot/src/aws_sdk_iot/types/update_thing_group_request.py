"""Generated from Smithy shape ``com.amazonaws.iot#UpdateThingGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.optional_version
    import aws_sdk_iot.types.thing_group_name
    import aws_sdk_iot.types.thing_group_properties


class UpdateThingGroupRequest(TypedDict):
    thing_group_name: "aws_sdk_iot.types.thing_group_name.ThingGroupName"
    """<p>The thing group to update.</p>"""
    thing_group_properties: (
        "aws_sdk_iot.types.thing_group_properties.ThingGroupProperties"
    )
    """<p>The thing group properties.</p>"""
    expected_version: NotRequired["aws_sdk_iot.types.optional_version.OptionalVersion"]
    """<p>The expected version of the thing group. If this does not match the version of the thing group being updated, the update will fail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThingGroupRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.thing_group_properties

    out["thingGroupProperties"] = (
        aws_sdk_iot.types.thing_group_properties.serialize_json(
            value["thing_group_properties"]
        )
    )
    if "expected_version" in value:
        out["expectedVersion"] = value["expected_version"]
    return out


def deserialize_json(data: dict) -> UpdateThingGroupRequest:
    out: UpdateThingGroupRequest = {}  # type: ignore[typeddict-item]
    if "thingGroupProperties" in data:
        import aws_sdk_iot.types.thing_group_properties

        out["thing_group_properties"] = (
            aws_sdk_iot.types.thing_group_properties.deserialize_json(
                data["thingGroupProperties"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateThingGroupRequest.thing_group_properties required"
        )
    if "expectedVersion" in data:
        out["expected_version"] = data["expectedVersion"]
    return out
