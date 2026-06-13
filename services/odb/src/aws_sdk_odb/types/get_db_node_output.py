"""Generated from Smithy shape ``com.amazonaws.odb#GetDbNodeOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_odb.types.db_node


class GetDbNodeOutput(TypedDict):
    db_node: NotRequired["aws_sdk_odb.types.db_node.DbNode"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbNodeOutput) -> dict:
    out: dict = {}
    if "db_node" in value:
        import aws_sdk_odb.types.db_node

        out["dbNode"] = aws_sdk_odb.types.db_node.serialize_aws_json_1_0(
            value["db_node"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbNodeOutput:
    out: GetDbNodeOutput = {}  # type: ignore[typeddict-item]
    if "dbNode" in data:
        import aws_sdk_odb.types.db_node

        out["db_node"] = aws_sdk_odb.types.db_node.deserialize_aws_json_1_0(
            data["dbNode"]
        )
    return out
