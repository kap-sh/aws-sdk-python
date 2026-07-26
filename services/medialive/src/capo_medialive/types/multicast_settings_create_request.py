"""Generated from Smithy shape ``com.amazonaws.medialive#MulticastSettingsCreateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_multicast_source_create_request


class MulticastSettingsCreateRequest(TypedDict, closed=True):
    sources: NotRequired[
        "capo_medialive.types.__list_of_multicast_source_create_request.__listOfMulticastSourceCreateRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MulticastSettingsCreateRequest) -> dict:
    out: dict = {}
    if "sources" in value:
        import capo_medialive.types.__list_of_multicast_source_create_request

        out["sources"] = (
            capo_medialive.types.__list_of_multicast_source_create_request.serialize_json(
                value["sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> MulticastSettingsCreateRequest:
    out: MulticastSettingsCreateRequest = {}  # type: ignore[typeddict-item]
    if "sources" in data:
        import capo_medialive.types.__list_of_multicast_source_create_request

        out["sources"] = (
            capo_medialive.types.__list_of_multicast_source_create_request.deserialize_json(
                data["sources"]
            )
        )
    return out
