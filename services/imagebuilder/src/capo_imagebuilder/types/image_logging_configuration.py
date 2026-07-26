"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageLoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.log_group_name


class ImageLoggingConfiguration(TypedDict, closed=True):
    log_group_name: NotRequired["capo_imagebuilder.types.log_group_name.LogGroupName"]
    """<p>The log group name that Image Builder uses for image creation. If not specified, the log group name defaults to <code>/aws/imagebuilder/image-name</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageLoggingConfiguration) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    return out


def deserialize_json(data: dict) -> ImageLoggingConfiguration:
    out: ImageLoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    return out
