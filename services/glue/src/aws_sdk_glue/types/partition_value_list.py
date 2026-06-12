"""Generated from Smithy shape ``com.amazonaws.glue#PartitionValueList``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.value_string_list


class PartitionValueList(TypedDict):
    values: "aws_sdk_glue.types.value_string_list.ValueStringList"
    """<p>The list of values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionValueList) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.value_string_list

    out["Values"] = aws_sdk_glue.types.value_string_list.serialize_aws_json_1_1(
        value["values"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PartitionValueList:
    out: PartitionValueList = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import aws_sdk_glue.types.value_string_list

        out["values"] = aws_sdk_glue.types.value_string_list.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        raise DeserializationError("PartitionValueList.values required")
    return out
