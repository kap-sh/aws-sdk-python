"""Generated from Smithy shape ``com.amazonaws.glue#GetUnfilteredPartitionMetadataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.boolean
    import aws_sdk_glue.types.name_string_list
    import aws_sdk_glue.types.partition


class GetUnfilteredPartitionMetadataResponse(TypedDict):
    partition: NotRequired["aws_sdk_glue.types.partition.Partition"]
    """<p>A Partition object containing the partition metadata.</p>"""
    authorized_columns: NotRequired[
        "aws_sdk_glue.types.name_string_list.NameStringList"
    ]
    """<p>A list of column names that the user has been granted access to.</p>"""
    is_registered_with_lake_formation: "aws_sdk_glue.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether the partition location is registered with Lake Formation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUnfilteredPartitionMetadataResponse) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> GetUnfilteredPartitionMetadataResponse:
    out: GetUnfilteredPartitionMetadataResponse = {}  # type: ignore[typeddict-item]
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
