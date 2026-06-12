"""Generated from Smithy shape ``com.amazonaws.connect#SecurityProfileSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.security_profile_summary

SecurityProfileSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.security_profile_summary.SecurityProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfileSummaryList) -> list:
    import aws_sdk_connect.types.security_profile_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.security_profile_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SecurityProfileSummaryList:
    import aws_sdk_connect.types.security_profile_summary

    out: SecurityProfileSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.security_profile_summary.deserialize_json(item)
        )
    return out
