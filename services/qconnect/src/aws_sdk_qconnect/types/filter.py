"""Generated from Smithy shape ``com.amazonaws.qconnect#Filter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.filter_field
    import aws_sdk_qconnect.types.filter_operator
    import aws_sdk_qconnect.types.non_empty_string


class Filter(TypedDict):
    field: "aws_sdk_qconnect.types.filter_field.FilterField"
    """<p>The field on which to filter.</p>"""
    operator: "aws_sdk_qconnect.types.filter_operator.FilterOperator"
    """<p>The operator to use for comparing the field’s value with the provided value.</p>"""
    value: "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The desired field value on which to filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["field"] = value["field"]
    out["operator"] = value["operator"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "field" in data:
        out["field"] = data["field"]
    else:
        raise DeserializationError("Filter.field required")
    if "operator" in data:
        out["operator"] = data["operator"]
    else:
        raise DeserializationError("Filter.operator required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Filter.value required")
    return out
