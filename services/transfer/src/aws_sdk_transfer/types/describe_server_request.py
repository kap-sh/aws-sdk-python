"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeServerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.server_id


class DescribeServerRequest(TypedDict, closed=True):
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServerRequest) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServerRequest:
    out: DescribeServerRequest = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("DescribeServerRequest.server_id required")
    return out
