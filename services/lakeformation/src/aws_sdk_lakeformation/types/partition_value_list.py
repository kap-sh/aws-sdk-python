"""Generated from Smithy shape ``com.amazonaws.lakeformation#PartitionValueList``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.value_string_list


class PartitionValueList(TypedDict):
    values: "aws_sdk_lakeformation.types.value_string_list.ValueStringList"
    """<p>The list of partition values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PartitionValueList) -> dict:
    out: dict = {}
    import aws_sdk_lakeformation.types.value_string_list

    out["Values"] = aws_sdk_lakeformation.types.value_string_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> PartitionValueList:
    out: PartitionValueList = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import aws_sdk_lakeformation.types.value_string_list

        out["values"] = aws_sdk_lakeformation.types.value_string_list.deserialize_json(
            data["Values"]
        )
    else:
        raise DeserializationError("PartitionValueList.values required")
    return out
