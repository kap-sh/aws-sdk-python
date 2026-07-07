"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetTableObjectsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.partitioned_table_objects_list
    import aws_sdk_lakeformation.types.token_string


class GetTableObjectsResponse(TypedDict, closed=True):
    objects: NotRequired[
        "aws_sdk_lakeformation.types.partitioned_table_objects_list.PartitionedTableObjectsList"
    ]
    """<p>A list of objects organized by partition keys.</p>"""
    next_token: NotRequired["aws_sdk_lakeformation.types.token_string.TokenString"]
    """<p>A continuation token indicating whether additional data is available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableObjectsResponse) -> dict:
    out: dict = {}
    if "objects" in value:
        import aws_sdk_lakeformation.types.partitioned_table_objects_list

        out["Objects"] = (
            aws_sdk_lakeformation.types.partitioned_table_objects_list.serialize_json(
                value["objects"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetTableObjectsResponse:
    out: GetTableObjectsResponse = {}  # type: ignore[typeddict-item]
    if "Objects" in data:
        import aws_sdk_lakeformation.types.partitioned_table_objects_list

        out["objects"] = (
            aws_sdk_lakeformation.types.partitioned_table_objects_list.deserialize_json(
                data["Objects"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
