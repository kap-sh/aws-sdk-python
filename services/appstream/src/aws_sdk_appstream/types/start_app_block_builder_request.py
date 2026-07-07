"""Generated from Smithy shape ``com.amazonaws.appstream#StartAppBlockBuilderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.name


class StartAppBlockBuilderRequest(TypedDict, closed=True):
    name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the app block builder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartAppBlockBuilderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartAppBlockBuilderRequest:
    out: StartAppBlockBuilderRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
