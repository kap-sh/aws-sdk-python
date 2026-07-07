"""Generated from Smithy shape ``com.amazonaws.appstream#CopyImageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.name


class CopyImageResponse(TypedDict, closed=True):
    destination_image_name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the destination image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyImageResponse) -> dict:
    out: dict = {}
    if "destination_image_name" in value:
        out["DestinationImageName"] = value["destination_image_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyImageResponse:
    out: CopyImageResponse = {}  # type: ignore[typeddict-item]
    if "DestinationImageName" in data:
        out["destination_image_name"] = data["DestinationImageName"]
    return out
