"""Generated from Smithy shape ``com.amazonaws.greengrassv2#AssociatedClientDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.io_t_thing_name
    import aws_sdk_greengrassv2.types.timestamp


class AssociatedClientDevice(TypedDict, closed=True):
    thing_name: NotRequired["aws_sdk_greengrassv2.types.io_t_thing_name.IoTThingName"]
    """<p>The name of the IoT thing that represents the associated client device.</p>"""
    association_timestamp: NotRequired["aws_sdk_greengrassv2.types.timestamp.Timestamp"]
    """<p>The time that the client device was associated, expressed in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedClientDevice) -> dict:
    out: dict = {}
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "association_timestamp" in value:
        import aws_sdk_greengrassv2.types.timestamp

        out["associationTimestamp"] = (
            aws_sdk_greengrassv2.types.timestamp.serialize_json(
                value["association_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociatedClientDevice:
    out: AssociatedClientDevice = {}  # type: ignore[typeddict-item]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "associationTimestamp" in data:
        import aws_sdk_greengrassv2.types.timestamp

        out["association_timestamp"] = (
            aws_sdk_greengrassv2.types.timestamp.deserialize_json(
                data["associationTimestamp"]
            )
        )
    return out
