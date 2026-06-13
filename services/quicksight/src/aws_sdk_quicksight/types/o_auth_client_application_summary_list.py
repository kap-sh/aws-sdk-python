"""Generated from Smithy shape ``com.amazonaws.quicksight#OAuthClientApplicationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.o_auth_client_application_summary

OAuthClientApplicationSummaryList: TypeAlias = list[
    "aws_sdk_quicksight.types.o_auth_client_application_summary.OAuthClientApplicationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: OAuthClientApplicationSummaryList) -> list:
    import aws_sdk_quicksight.types.o_auth_client_application_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.o_auth_client_application_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OAuthClientApplicationSummaryList:
    import aws_sdk_quicksight.types.o_auth_client_application_summary

    out: OAuthClientApplicationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.o_auth_client_application_summary.deserialize_json(
                item
            )
        )
    return out
