"""Generated from Smithy shape ``com.amazonaws.mediastore#DescribeContainerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container_name


class DescribeContainerInput(TypedDict, closed=True):
    container_name: NotRequired["aws_sdk_mediastore.types.container_name.ContainerName"]
    """<p>The name of the container to query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContainerInput) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["ContainerName"] = value["container_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContainerInput:
    out: DescribeContainerInput = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    return out
