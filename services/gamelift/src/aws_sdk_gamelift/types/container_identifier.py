"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.non_empty_string
    import aws_sdk_gamelift.types.non_zero_and128_max_ascii_string


class ContainerIdentifier(TypedDict, closed=True):
    container_name: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and128_max_ascii_string.NonZeroAnd128MaxAsciiString"
    ]
    """<p>The identifier for a container that's running in a compute. </p>"""
    container_runtime_id: NotRequired[
        "aws_sdk_gamelift.types.non_empty_string.NonEmptyString"
    ]
    """<p>The runtime ID for the container that's running in a compute. This value is unique within the compute. It is returned as a <code>ContainerAttribute</code> value in a <code>Compute</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerIdentifier) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["ContainerName"] = value["container_name"]
    if "container_runtime_id" in value:
        out["ContainerRuntimeId"] = value["container_runtime_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerIdentifier:
    out: ContainerIdentifier = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    if "ContainerRuntimeId" in data:
        out["container_runtime_id"] = data["ContainerRuntimeId"]
    return out
