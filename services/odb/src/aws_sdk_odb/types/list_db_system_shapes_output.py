"""Generated from Smithy shape ``com.amazonaws.odb#ListDbSystemShapesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.db_system_shape_list


class ListDbSystemShapesOutput(TypedDict):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    db_system_shapes: "aws_sdk_odb.types.db_system_shape_list.DbSystemShapeList"
    """<p>The list of shapes and their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDbSystemShapesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_odb.types.db_system_shape_list

    out["dbSystemShapes"] = (
        aws_sdk_odb.types.db_system_shape_list.serialize_aws_json_1_0(
            value["db_system_shapes"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDbSystemShapesOutput:
    out: ListDbSystemShapesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "dbSystemShapes" in data:
        import aws_sdk_odb.types.db_system_shape_list

        out["db_system_shapes"] = (
            aws_sdk_odb.types.db_system_shape_list.deserialize_aws_json_1_0(
                data["dbSystemShapes"]
            )
        )
    else:
        raise DeserializationError("ListDbSystemShapesOutput.db_system_shapes required")
    return out
