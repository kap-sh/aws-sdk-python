"""Generated from Smithy shape ``com.amazonaws.medialive#MulticastSettingsCreateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_multicast_source_create_request


class MulticastSettingsCreateRequest(TypedDict):
    sources: NotRequired[
        "aws_sdk_medialive.types.__list_of_multicast_source_create_request.__listOfMulticastSourceCreateRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MulticastSettingsCreateRequest) -> dict:
    out: dict = {}
    if "sources" in value:
        import aws_sdk_medialive.types.__list_of_multicast_source_create_request

        out["sources"] = (
            aws_sdk_medialive.types.__list_of_multicast_source_create_request.serialize_json(
                value["sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> MulticastSettingsCreateRequest:
    out: MulticastSettingsCreateRequest = {}  # type: ignore[typeddict-item]
    if "sources" in data:
        import aws_sdk_medialive.types.__list_of_multicast_source_create_request

        out["sources"] = (
            aws_sdk_medialive.types.__list_of_multicast_source_create_request.deserialize_json(
                data["sources"]
            )
        )
    return out
