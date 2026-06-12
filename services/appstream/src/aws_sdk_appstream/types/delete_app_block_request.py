"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteAppBlockRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.name


class DeleteAppBlockRequest(TypedDict):
    name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the app block.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAppBlockRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAppBlockRequest:
    out: DeleteAppBlockRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
