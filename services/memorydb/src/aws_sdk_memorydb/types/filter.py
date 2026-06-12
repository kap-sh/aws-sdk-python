"""Generated from Smithy shape ``com.amazonaws.memorydb#Filter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.filter_name
    import aws_sdk_memorydb.types.filter_value_list


class Filter(TypedDict):
    name: "aws_sdk_memorydb.types.filter_name.FilterName"
    """<p>The property being filtered. For example, UserName.</p>"""
    values: "aws_sdk_memorydb.types.filter_value_list.FilterValueList"
    """<p>The property values to filter on. For example, \"user-123\".</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_memorydb.types.filter_value_list

    out["Values"] = aws_sdk_memorydb.types.filter_value_list.serialize_aws_json_1_1(
        value["values"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Filter.name required")
    if "Values" in data:
        import aws_sdk_memorydb.types.filter_value_list

        out["values"] = (
            aws_sdk_memorydb.types.filter_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("Filter.values required")
    return out
