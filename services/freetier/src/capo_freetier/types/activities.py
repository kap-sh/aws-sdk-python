"""Generated from Smithy shape ``com.amazonaws.freetier#Activities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_freetier.types.activity_summary

Activities: TypeAlias = list["capo_freetier.types.activity_summary.ActivitySummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Activities) -> list:
    import capo_freetier.types.activity_summary

    out: list = []
    for item in value:
        out.append(capo_freetier.types.activity_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Activities:
    import capo_freetier.types.activity_summary

    out: Activities = []
    for item in data:
        out.append(capo_freetier.types.activity_summary.deserialize_aws_json_1_0(item))
    return out
