"""Generated from Smithy shape ``com.amazonaws.medialive#MediaConnectRouterGroupSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string


class MediaConnectRouterGroupSettings(TypedDict, closed=True):
    availability_zones: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """The names of the Availability Zones in which to write output to MediaConnect Router."""


# --- restJson1 ser/de ---
def serialize_json(value: MediaConnectRouterGroupSettings) -> dict:
    out: dict = {}
    if "availability_zones" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["availabilityZones"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["availability_zones"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaConnectRouterGroupSettings:
    out: MediaConnectRouterGroupSettings = {}  # type: ignore[typeddict-item]
    if "availabilityZones" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["availability_zones"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["availabilityZones"]
            )
        )
    return out
