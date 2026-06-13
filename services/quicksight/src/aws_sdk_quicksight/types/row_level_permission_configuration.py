"""Generated from Smithy shape ``com.amazonaws.quicksight#RowLevelPermissionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.row_level_permission_data_set
    import aws_sdk_quicksight.types.row_level_permission_tag_configuration


class RowLevelPermissionConfiguration(TypedDict):
    tag_configuration: NotRequired[
        "aws_sdk_quicksight.types.row_level_permission_tag_configuration.RowLevelPermissionTagConfiguration"
    ]
    row_level_permission_data_set: NotRequired[
        "aws_sdk_quicksight.types.row_level_permission_data_set.RowLevelPermissionDataSet"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RowLevelPermissionConfiguration) -> dict:
    out: dict = {}
    if "tag_configuration" in value:
        import aws_sdk_quicksight.types.row_level_permission_tag_configuration

        out["TagConfiguration"] = (
            aws_sdk_quicksight.types.row_level_permission_tag_configuration.serialize_json(
                value["tag_configuration"]
            )
        )
    if "row_level_permission_data_set" in value:
        import aws_sdk_quicksight.types.row_level_permission_data_set

        out["RowLevelPermissionDataSet"] = (
            aws_sdk_quicksight.types.row_level_permission_data_set.serialize_json(
                value["row_level_permission_data_set"]
            )
        )
    return out


def deserialize_json(data: dict) -> RowLevelPermissionConfiguration:
    out: RowLevelPermissionConfiguration = {}  # type: ignore[typeddict-item]
    if "TagConfiguration" in data:
        import aws_sdk_quicksight.types.row_level_permission_tag_configuration

        out["tag_configuration"] = (
            aws_sdk_quicksight.types.row_level_permission_tag_configuration.deserialize_json(
                data["TagConfiguration"]
            )
        )
    if "RowLevelPermissionDataSet" in data:
        import aws_sdk_quicksight.types.row_level_permission_data_set

        out["row_level_permission_data_set"] = (
            aws_sdk_quicksight.types.row_level_permission_data_set.deserialize_json(
                data["RowLevelPermissionDataSet"]
            )
        )
    return out
