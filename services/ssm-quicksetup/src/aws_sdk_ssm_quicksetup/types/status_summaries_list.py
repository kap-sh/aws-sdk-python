"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#StatusSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.status_summary

StatusSummariesList: TypeAlias = list[
    "aws_sdk_ssm_quicksetup.types.status_summary.StatusSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: StatusSummariesList) -> list:
    import aws_sdk_ssm_quicksetup.types.status_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_quicksetup.types.status_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> StatusSummariesList:
    import aws_sdk_ssm_quicksetup.types.status_summary

    out: StatusSummariesList = []
    for item in data:
        out.append(aws_sdk_ssm_quicksetup.types.status_summary.deserialize_json(item))
    return out
