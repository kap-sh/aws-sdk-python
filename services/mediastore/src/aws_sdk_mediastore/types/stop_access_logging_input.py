"""Generated from Smithy shape ``com.amazonaws.mediastore#StopAccessLoggingInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container_name


class StopAccessLoggingInput(TypedDict):
    container_name: "aws_sdk_mediastore.types.container_name.ContainerName"
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
