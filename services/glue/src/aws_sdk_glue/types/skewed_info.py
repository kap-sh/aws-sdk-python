"""Generated from Smithy shape ``com.amazonaws.glue#SkewedInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_value_string_list
    import aws_sdk_glue.types.location_map
    import aws_sdk_glue.types.name_string_list


class SkewedInfo(TypedDict):
    skewed_column_names: NotRequired[
        "aws_sdk_glue.types.name_string_list.NameStringList"
    ]
    """<p>A list of names of columns that contain skewed values.</p>"""
    skewed_column_values: NotRequired[
        "aws_sdk_glue.types.column_value_string_list.ColumnValueStringList"
    ]
    """<p>A list of values that appear so frequently as to be considered skewed.</p>"""
    skewed_column_value_location_maps: NotRequired[
        "aws_sdk_glue.types.location_map.LocationMap"
    ]
    """<p>A mapping of skewed values to the columns that contain them.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SkewedInfo) -> dict:
    out: dict = {}
    if "skewed_column_names" in value:
        import aws_sdk_glue.types.name_string_list

        out["SkewedColumnNames"] = (
            aws_sdk_glue.types.name_string_list.serialize_aws_json_1_1(
                value["skewed_column_names"]
            )
        )
    if "skewed_column_values" in value:
        import aws_sdk_glue.types.column_value_string_list

        out["SkewedColumnValues"] = (
            aws_sdk_glue.types.column_value_string_list.serialize_aws_json_1_1(
                value["skewed_column_values"]
            )
        )
    if "skewed_column_value_location_maps" in value:
        import aws_sdk_glue.types.location_map

        out["SkewedColumnValueLocationMaps"] = (
            aws_sdk_glue.types.location_map.serialize_aws_json_1_1(
                value["skewed_column_value_location_maps"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SkewedInfo:
    out: SkewedInfo = {}  # type: ignore[typeddict-item]
    if "SkewedColumnNames" in data:
        import aws_sdk_glue.types.name_string_list

        out["skewed_column_names"] = (
            aws_sdk_glue.types.name_string_list.deserialize_aws_json_1_1(
                data["SkewedColumnNames"]
            )
        )
    if "SkewedColumnValues" in data:
        import aws_sdk_glue.types.column_value_string_list

        out["skewed_column_values"] = (
            aws_sdk_glue.types.column_value_string_list.deserialize_aws_json_1_1(
                data["SkewedColumnValues"]
            )
        )
    if "SkewedColumnValueLocationMaps" in data:
        import aws_sdk_glue.types.location_map

        out["skewed_column_value_location_maps"] = (
            aws_sdk_glue.types.location_map.deserialize_aws_json_1_1(
                data["SkewedColumnValueLocationMaps"]
            )
        )
    return out
