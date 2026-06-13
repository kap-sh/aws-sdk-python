"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ObjectiveSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.objective_summary

ObjectiveSummaryList: TypeAlias = list[
    "aws_sdk_controlcatalog.types.objective_summary.ObjectiveSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectiveSummaryList) -> list:
    import aws_sdk_controlcatalog.types.objective_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_controlcatalog.types.objective_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ObjectiveSummaryList:
    import aws_sdk_controlcatalog.types.objective_summary

    out: ObjectiveSummaryList = []
    for item in data:
        out.append(
            aws_sdk_controlcatalog.types.objective_summary.deserialize_json(item)
        )
    return out
