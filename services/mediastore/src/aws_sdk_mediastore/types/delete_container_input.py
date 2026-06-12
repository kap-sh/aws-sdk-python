"""Generated from Smithy shape ``com.amazonaws.mediastore#DeleteContainerInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container_name


class DeleteContainerInput(TypedDict):
    container_name: "aws_sdk_mediastore.types.container_name.ContainerName"
    """<p>The name of the container to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteContainerInput) -> dict:
    out: dict = {}
    out["ContainerName"] = value["container_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteContainerInput:
    out: DeleteContainerInput = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    else:
        raise DeserializationError("DeleteContainerInput.container_name required")
    return out
