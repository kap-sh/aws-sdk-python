"""Generated from Smithy shape ``com.amazonaws.glue#UnfilteredPartition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.boolean
    import aws_sdk_glue.types.name_string_list
    import aws_sdk_glue.types.partition


class UnfilteredPartition(TypedDict, closed=True):
    partition: NotRequired["aws_sdk_glue.types.partition.Partition"]
    """<p>The partition object.</p>"""
    authorized_columns: NotRequired[
        "aws_sdk_glue.types.name_string_list.NameStringList"
    ]
    """<p>The list of columns the user has permissions to access.</p>"""
    is_registered_with_lake_formation: "aws_sdk_glue.types.boolean.Boolean"
    """<p>A Boolean value indicating that the partition location is registered with Lake Formation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnfilteredPartition) -> dict:
    out: dict = {}
    if "partition" in value:
        import aws_sdk_glue.types.partition

        out["Partition"] = aws_sdk_glue.types.partition.serialize_aws_json_1_1(
            value["partition"]
        )
    if "authorized_columns" in value:
        import aws_sdk_glue.types.name_string_list

        out["AuthorizedColumns"] = (
            aws_sdk_glue.types.name_string_list.serialize_aws_json_1_1(
                value["authorized_columns"]
            )
        )
    out["IsRegisteredWithLakeFormation"] = value.get(
        "is_registered_with_lake_formation", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnfilteredPartition:
    out: UnfilteredPartition = {}  # type: ignore[typeddict-item]
    if "Partition" in data:
        import aws_sdk_glue.types.partition

        out["partition"] = aws_sdk_glue.types.partition.deserialize_aws_json_1_1(
            data["Partition"]
        )
    if "AuthorizedColumns" in data:
        import aws_sdk_glue.types.name_string_list

        out["authorized_columns"] = (
            aws_sdk_glue.types.name_string_list.deserialize_aws_json_1_1(
                data["AuthorizedColumns"]
            )
        )
    if "IsRegisteredWithLakeFormation" in data:
        out["is_registered_with_lake_formation"] = data["IsRegisteredWithLakeFormation"]
    else:
        out["is_registered_with_lake_formation"] = False
    return out
