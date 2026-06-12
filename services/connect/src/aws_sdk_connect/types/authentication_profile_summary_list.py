"""Generated from Smithy shape ``com.amazonaws.connect#AuthenticationProfileSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.authentication_profile_summary

AuthenticationProfileSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.authentication_profile_summary.AuthenticationProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationProfileSummaryList) -> list:
    import aws_sdk_connect.types.authentication_profile_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.authentication_profile_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AuthenticationProfileSummaryList:
    import aws_sdk_connect.types.authentication_profile_summary

    out: AuthenticationProfileSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.authentication_profile_summary.deserialize_json(item)
        )
    return out
