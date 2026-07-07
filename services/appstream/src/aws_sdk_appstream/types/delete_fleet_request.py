"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.string


class DeleteFleetRequest(TypedDict, closed=True):
    name: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The name of the fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFleetRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFleetRequest:
    out: DeleteFleetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
