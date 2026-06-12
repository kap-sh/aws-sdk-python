"""Generated from Smithy shape ``com.amazonaws.medialive#ListVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_channel_engine_version_response


class ListVersionsResponse(TypedDict):
    versions: NotRequired[
        "aws_sdk_medialive.types.__list_of_channel_engine_version_response.__listOfChannelEngineVersionResponse"
    ]
    """List of engine versions that are available for this AWS account."""


# --- restJson1 ser/de ---
def serialize_json(value: ListVersionsResponse) -> dict:
    out: dict = {}
    if "versions" in value:
        import aws_sdk_medialive.types.__list_of_channel_engine_version_response

        out["versions"] = (
            aws_sdk_medialive.types.__list_of_channel_engine_version_response.serialize_json(
                value["versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListVersionsResponse:
    out: ListVersionsResponse = {}  # type: ignore[typeddict-item]
    if "versions" in data:
        import aws_sdk_medialive.types.__list_of_channel_engine_version_response

        out["versions"] = (
            aws_sdk_medialive.types.__list_of_channel_engine_version_response.deserialize_json(
                data["versions"]
            )
        )
    return out
