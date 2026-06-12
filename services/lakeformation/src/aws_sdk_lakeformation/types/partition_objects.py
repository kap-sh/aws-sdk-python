"""Generated from Smithy shape ``com.amazonaws.lakeformation#PartitionObjects``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.partition_values_list
    import aws_sdk_lakeformation.types.table_object_list


class PartitionObjects(TypedDict):
    partition_values: NotRequired[
        "aws_sdk_lakeformation.types.partition_values_list.PartitionValuesList"
    ]
    """<p>A list of partition values.</p>"""
    objects: NotRequired[
        "aws_sdk_lakeformation.types.table_object_list.TableObjectList"
    ]
    """<p>A list of table objects</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PartitionObjects) -> dict:
    out: dict = {}
    if "partition_values" in value:
        import aws_sdk_lakeformation.types.partition_values_list

        out["PartitionValues"] = (
            aws_sdk_lakeformation.types.partition_values_list.serialize_json(
                value["partition_values"]
            )
        )
    if "objects" in value:
        import aws_sdk_lakeformation.types.table_object_list

        out["Objects"] = aws_sdk_lakeformation.types.table_object_list.serialize_json(
            value["objects"]
        )
    return out


def deserialize_json(data: dict) -> PartitionObjects:
    out: PartitionObjects = {}  # type: ignore[typeddict-item]
    if "PartitionValues" in data:
        import aws_sdk_lakeformation.types.partition_values_list

        out["partition_values"] = (
            aws_sdk_lakeformation.types.partition_values_list.deserialize_json(
                data["PartitionValues"]
            )
        )
    if "Objects" in data:
        import aws_sdk_lakeformation.types.table_object_list

        out["objects"] = aws_sdk_lakeformation.types.table_object_list.deserialize_json(
            data["Objects"]
        )
    return out
