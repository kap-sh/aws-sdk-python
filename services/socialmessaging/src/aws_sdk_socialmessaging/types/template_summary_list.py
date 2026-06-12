"""Generated from Smithy shape ``com.amazonaws.socialmessaging#TemplateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.template_summary

TemplateSummaryList: TypeAlias = list[
    "aws_sdk_socialmessaging.types.template_summary.TemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSummaryList) -> list:
    import aws_sdk_socialmessaging.types.template_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_socialmessaging.types.template_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TemplateSummaryList:
    import aws_sdk_socialmessaging.types.template_summary

    out: TemplateSummaryList = []
    for item in data:
        out.append(
            aws_sdk_socialmessaging.types.template_summary.deserialize_json(item)
        )
    return out
