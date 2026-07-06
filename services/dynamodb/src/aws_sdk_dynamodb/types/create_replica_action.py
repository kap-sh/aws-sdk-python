"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateReplicaAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.region_name


class CreateReplicaAction(TypedDict, closed=True):
    region_name: "aws_sdk_dynamodb.types.region_name.RegionName"
    """<p>The Region of the replica to be added.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateReplicaAction) -> dict:
    out: dict = {}
    out["RegionName"] = value["region_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateReplicaAction:
    out: CreateReplicaAction = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    else:
        raise DeserializationError("CreateReplicaAction.region_name required")
    return out
