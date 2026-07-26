"""Generated from Smithy shape ``com.amazonaws.mediastore#StopAccessLoggingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediastore.types.container_name


class StopAccessLoggingInput(TypedDict, closed=True):
    container_name: "capo_mediastore.types.container_name.ContainerName"
    """<p>The name of the container that you want to stop access logging on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopAccessLoggingInput) -> dict:
    out: dict = {}
    out["ContainerName"] = value["container_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopAccessLoggingInput:
    out: StopAccessLoggingInput = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    else:
        raise DeserializationError("StopAccessLoggingInput.container_name required")
    return out
