"""Generated from Smithy shape ``com.amazonaws.medialive#MulticastSettingsUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_multicast_source_update_request


class MulticastSettingsUpdateRequest(TypedDict, closed=True):
    sources: NotRequired[
        "aws_sdk_medialive.types.__list_of_multicast_source_update_request.__listOfMulticastSourceUpdateRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MulticastSettingsUpdateRequest) -> dict:
    out: dict = {}
    if "sources" in value:
        import aws_sdk_medialive.types.__list_of_multicast_source_update_request

        out["sources"] = (
            aws_sdk_medialive.types.__list_of_multicast_source_update_request.serialize_json(
                value["sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> MulticastSettingsUpdateRequest:
    out: MulticastSettingsUpdateRequest = {}  # type: ignore[typeddict-item]
    if "sources" in data:
        import aws_sdk_medialive.types.__list_of_multicast_source_update_request

        out["sources"] = (
            aws_sdk_medialive.types.__list_of_multicast_source_update_request.deserialize_json(
                data["sources"]
            )
        )
    return out
