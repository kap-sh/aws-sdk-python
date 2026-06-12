"""Generated from Smithy shape ``com.amazonaws.rdsdata#StructValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.array_value_list


class StructValue(TypedDict):
    attributes: NotRequired["aws_sdk_rds_data.types.array_value_list.ArrayValueList"]
    """<p>The attributes returned in the record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StructValue) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_rds_data.types.array_value_list

        out["attributes"] = aws_sdk_rds_data.types.array_value_list.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> StructValue:
    out: StructValue = {}  # type: ignore[typeddict-item]
    if "attributes" in data:
        import aws_sdk_rds_data.types.array_value_list

        out["attributes"] = aws_sdk_rds_data.types.array_value_list.deserialize_json(
            data["attributes"]
        )
    return out
