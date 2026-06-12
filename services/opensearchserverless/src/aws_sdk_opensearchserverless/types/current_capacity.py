"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CurrentCapacity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.capacity_details


class CurrentCapacity(TypedDict):
    search: NotRequired[
        "aws_sdk_opensearchserverless.types.capacity_details.CapacityDetails"
    ]
    """<p>The search capacity for the collection group.</p>"""
    indexing: NotRequired[
        "aws_sdk_opensearchserverless.types.capacity_details.CapacityDetails"
    ]
    """<p>The indexing capacity for the collection group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CurrentCapacity) -> dict:
    out: dict = {}
    if "search" in value:
        import aws_sdk_opensearchserverless.types.capacity_details

        out["search"] = (
            aws_sdk_opensearchserverless.types.capacity_details.serialize_aws_json_1_0(
                value["search"]
            )
        )
    if "indexing" in value:
        import aws_sdk_opensearchserverless.types.capacity_details

        out["indexing"] = (
            aws_sdk_opensearchserverless.types.capacity_details.serialize_aws_json_1_0(
                value["indexing"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CurrentCapacity:
    out: CurrentCapacity = {}  # type: ignore[typeddict-item]
    if "search" in data:
        import aws_sdk_opensearchserverless.types.capacity_details

        out["search"] = (
            aws_sdk_opensearchserverless.types.capacity_details.deserialize_aws_json_1_0(
                data["search"]
            )
        )
    if "indexing" in data:
        import aws_sdk_opensearchserverless.types.capacity_details

        out["indexing"] = (
            aws_sdk_opensearchserverless.types.capacity_details.deserialize_aws_json_1_0(
                data["indexing"]
            )
        )
    return out
