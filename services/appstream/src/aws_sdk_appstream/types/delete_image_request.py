"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.name


class DeleteImageRequest(TypedDict, closed=True):
    name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteImageRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteImageRequest:
    out: DeleteImageRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
