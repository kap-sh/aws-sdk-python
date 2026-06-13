"""Generated from Smithy shape ``com.amazonaws.s3tables#NamespaceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.namespace_summary

NamespaceSummaryList: TypeAlias = list[
    "aws_sdk_s3tables.types.namespace_summary.NamespaceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NamespaceSummaryList) -> list:
    import aws_sdk_s3tables.types.namespace_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_s3tables.types.namespace_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> NamespaceSummaryList:
    import aws_sdk_s3tables.types.namespace_summary

    out: NamespaceSummaryList = []
    for item in data:
        out.append(aws_sdk_s3tables.types.namespace_summary.deserialize_json(item))
    return out
