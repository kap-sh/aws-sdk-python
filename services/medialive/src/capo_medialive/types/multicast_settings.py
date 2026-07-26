"""Generated from Smithy shape ``com.amazonaws.medialive#MulticastSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_multicast_source


class MulticastSettings(TypedDict, closed=True):
    sources: NotRequired[
        "capo_medialive.types.__list_of_multicast_source.__listOfMulticastSource"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MulticastSettings) -> dict:
    out: dict = {}
    if "sources" in value:
        import capo_medialive.types.__list_of_multicast_source

        out["sources"] = capo_medialive.types.__list_of_multicast_source.serialize_json(
            value["sources"]
        )
    return out


def deserialize_json(data: dict) -> MulticastSettings:
    out: MulticastSettings = {}  # type: ignore[typeddict-item]
    if "sources" in data:
        import capo_medialive.types.__list_of_multicast_source

        out["sources"] = (
            capo_medialive.types.__list_of_multicast_source.deserialize_json(
                data["sources"]
            )
        )
    return out
