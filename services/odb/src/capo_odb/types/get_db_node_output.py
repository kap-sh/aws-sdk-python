"""Generated from Smithy shape ``com.amazonaws.odb#GetDbNodeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.db_node


class GetDbNodeOutput(TypedDict, closed=True):
    db_node: NotRequired["capo_odb.types.db_node.DbNode"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbNodeOutput) -> dict:
    out: dict = {}
    if "db_node" in value:
        import capo_odb.types.db_node

        out["dbNode"] = capo_odb.types.db_node.serialize_aws_json_1_0(value["db_node"])
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbNodeOutput:
    out: GetDbNodeOutput = {}  # type: ignore[typeddict-item]
    if "dbNode" in data:
        import capo_odb.types.db_node

        out["db_node"] = capo_odb.types.db_node.deserialize_aws_json_1_0(data["dbNode"])
    return out
