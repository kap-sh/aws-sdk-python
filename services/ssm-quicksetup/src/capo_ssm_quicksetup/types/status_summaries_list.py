"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#StatusSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.status_summary

StatusSummariesList: TypeAlias = list[
    "capo_ssm_quicksetup.types.status_summary.StatusSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: StatusSummariesList) -> list:
    import capo_ssm_quicksetup.types.status_summary

    out: list = []
    for item in value:
        out.append(capo_ssm_quicksetup.types.status_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> StatusSummariesList:
    import capo_ssm_quicksetup.types.status_summary

    out: StatusSummariesList = []
    for item in data:
        out.append(capo_ssm_quicksetup.types.status_summary.deserialize_json(item))
    return out
