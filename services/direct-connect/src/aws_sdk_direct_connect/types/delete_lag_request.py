"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteLagRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.lag_id


class DeleteLagRequest(TypedDict):
    lag_id: "aws_sdk_direct_connect.types.lag_id.LagId"
    """<p>The ID of the LAG.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLagRequest) -> dict:
    out: dict = {}
    out["lagId"] = value["lag_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLagRequest:
    out: DeleteLagRequest = {}  # type: ignore[typeddict-item]
    if "lagId" in data:
        out["lag_id"] = data["lagId"]
    else:
        raise DeserializationError("DeleteLagRequest.lag_id required")
    return out
