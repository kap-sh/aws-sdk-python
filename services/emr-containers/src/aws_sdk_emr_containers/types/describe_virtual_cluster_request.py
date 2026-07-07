"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DescribeVirtualClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.resource_id_string


class DescribeVirtualClusterRequest(TypedDict, closed=True):
    id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    """<p>The ID of the virtual cluster that will be described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVirtualClusterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeVirtualClusterRequest:
    out: DescribeVirtualClusterRequest = {}  # type: ignore[typeddict-item]
    return out
