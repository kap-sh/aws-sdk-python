"""Generated from Smithy shape ``com.amazonaws.medialive#MulticastSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_multicast_source


class MulticastSettings(TypedDict, closed=True):
    sources: NotRequired[
        "aws_sdk_medialive.types.__list_of_multicast_source.__listOfMulticastSource"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MulticastSettings) -> dict:
    out: dict = {}
    if "sources" in value:
        import aws_sdk_medialive.types.__list_of_multicast_source

        out["sources"] = (
            aws_sdk_medialive.types.__list_of_multicast_source.serialize_json(
                value["sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> MulticastSettings:
    out: MulticastSettings = {}  # type: ignore[typeddict-item]
    if "sources" in data:
        import aws_sdk_medialive.types.__list_of_multicast_source

        out["sources"] = (
            aws_sdk_medialive.types.__list_of_multicast_source.deserialize_json(
                data["sources"]
            )
        )
    return out
