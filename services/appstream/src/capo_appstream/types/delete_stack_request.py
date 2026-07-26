"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteStackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.string


class DeleteStackRequest(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the stack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteStackRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteStackRequest:
    out: DeleteStackRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
