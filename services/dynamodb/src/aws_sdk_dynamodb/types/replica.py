"""Generated from Smithy shape ``com.amazonaws.dynamodb#Replica``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.region_name


class Replica(TypedDict, closed=True):
    region_name: NotRequired["aws_sdk_dynamodb.types.region_name.RegionName"]
    """<p>The Region where the replica needs to be created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Replica) -> dict:
    out: dict = {}
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Replica:
    out: Replica = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    return out
