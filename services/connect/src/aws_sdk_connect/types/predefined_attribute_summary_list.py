"""Generated from Smithy shape ``com.amazonaws.connect#PredefinedAttributeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.predefined_attribute_summary

PredefinedAttributeSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.predefined_attribute_summary.PredefinedAttributeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PredefinedAttributeSummaryList) -> list:
    import aws_sdk_connect.types.predefined_attribute_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.predefined_attribute_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PredefinedAttributeSummaryList:
    import aws_sdk_connect.types.predefined_attribute_summary

    out: PredefinedAttributeSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.predefined_attribute_summary.deserialize_json(item)
        )
    return out
