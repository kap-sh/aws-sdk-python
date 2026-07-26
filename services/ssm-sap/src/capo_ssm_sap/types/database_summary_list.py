"""Generated from Smithy shape ``com.amazonaws.ssmsap#DatabaseSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_sap.types.database_summary

DatabaseSummaryList: TypeAlias = list[
    "capo_ssm_sap.types.database_summary.DatabaseSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseSummaryList) -> list:
    import capo_ssm_sap.types.database_summary

    out: list = []
    for item in value:
        out.append(capo_ssm_sap.types.database_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatabaseSummaryList:
    import capo_ssm_sap.types.database_summary

    out: DatabaseSummaryList = []
    for item in data:
        out.append(capo_ssm_sap.types.database_summary.deserialize_json(item))
    return out
