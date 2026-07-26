"""Generated from Smithy shape ``com.amazonaws.securityagent#ApplicationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.application_summary

ApplicationSummaryList: TypeAlias = list[
    "capo_securityagent.types.application_summary.ApplicationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummaryList) -> list:
    import capo_securityagent.types.application_summary

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.application_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationSummaryList:
    import capo_securityagent.types.application_summary

    out: ApplicationSummaryList = []
    for item in data:
        out.append(capo_securityagent.types.application_summary.deserialize_json(item))
    return out
