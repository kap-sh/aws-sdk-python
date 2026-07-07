"""Generated from Smithy shape ``com.amazonaws.mediastore#GetMetricPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container_name


class GetMetricPolicyInput(TypedDict, closed=True):
    container_name: "aws_sdk_mediastore.types.container_name.ContainerName"
    """<p>The name of the container that is associated with the metric policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMetricPolicyInput) -> dict:
    out: dict = {}
    out["ContainerName"] = value["container_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMetricPolicyInput:
    out: GetMetricPolicyInput = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    else:
        raise DeserializationError("GetMetricPolicyInput.container_name required")
    return out
