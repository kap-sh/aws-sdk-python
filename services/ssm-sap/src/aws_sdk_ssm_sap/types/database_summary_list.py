"""Generated from Smithy shape ``com.amazonaws.ssmsap#DatabaseSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.database_summary

DatabaseSummaryList: TypeAlias = list[
    "aws_sdk_ssm_sap.types.database_summary.DatabaseSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseSummaryList) -> list:
    import aws_sdk_ssm_sap.types.database_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_sap.types.database_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatabaseSummaryList:
    import aws_sdk_ssm_sap.types.database_summary

    out: DatabaseSummaryList = []
    for item in data:
        out.append(aws_sdk_ssm_sap.types.database_summary.deserialize_json(item))
    return out
