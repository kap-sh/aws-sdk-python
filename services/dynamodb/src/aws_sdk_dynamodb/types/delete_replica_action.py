"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteReplicaAction``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.region_name


class DeleteReplicaAction(TypedDict):
    region_name: "aws_sdk_dynamodb.types.region_name.RegionName"
    """<p>The Region of the replica to be removed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteReplicaAction) -> dict:
    out: dict = {}
    out["RegionName"] = value["region_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteReplicaAction:
    out: DeleteReplicaAction = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    else:
        raise DeserializationError("DeleteReplicaAction.region_name required")
    return out
