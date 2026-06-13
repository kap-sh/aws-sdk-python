"""Generated from Smithy shape ``com.amazonaws.rtbfabric#FilterCriterion``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.value_list


class FilterCriterion(TypedDict):
    path: "str"
    """<p>The path to filter.</p>"""
    values: "aws_sdk_rtbfabric.types.value_list.ValueList"
    """<p>The value to filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriterion) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    import aws_sdk_rtbfabric.types.value_list

    out["values"] = aws_sdk_rtbfabric.types.value_list.serialize_json(value["values"])
    return out


def deserialize_json(data: dict) -> FilterCriterion:
    out: FilterCriterion = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("FilterCriterion.path required")
    if "values" in data:
        import aws_sdk_rtbfabric.types.value_list

        out["values"] = aws_sdk_rtbfabric.types.value_list.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("FilterCriterion.values required")
    return out
