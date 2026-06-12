"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListTapePoolsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.marker
    import aws_sdk_storage_gateway.types.pool_infos


class ListTapePoolsOutput(TypedDict):
    pool_infos: NotRequired["aws_sdk_storage_gateway.types.pool_infos.PoolInfos"]
    """<p>An array of <code>PoolInfo</code> objects, where each object describes a single custom tape pool. If there are no custom tape pools, the <code>PoolInfos</code> is an empty array. </p>"""
    marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>A string that indicates the position at which to begin the returned list of tape pools. Use the marker in your next request to continue pagination of tape pools. If there are no more tape pools to list, this element does not appear in the response body. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTapePoolsOutput) -> dict:
    out: dict = {}
    if "pool_infos" in value:
        import aws_sdk_storage_gateway.types.pool_infos

        out["PoolInfos"] = (
            aws_sdk_storage_gateway.types.pool_infos.serialize_aws_json_1_1(
                value["pool_infos"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTapePoolsOutput:
    out: ListTapePoolsOutput = {}  # type: ignore[typeddict-item]
    if "PoolInfos" in data:
        import aws_sdk_storage_gateway.types.pool_infos

        out["pool_infos"] = (
            aws_sdk_storage_gateway.types.pool_infos.deserialize_aws_json_1_1(
                data["PoolInfos"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
