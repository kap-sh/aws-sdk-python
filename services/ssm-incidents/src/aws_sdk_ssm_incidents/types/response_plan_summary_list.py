"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ResponsePlanSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.response_plan_summary

ResponsePlanSummaryList: TypeAlias = list[
    "aws_sdk_ssm_incidents.types.response_plan_summary.ResponsePlanSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponsePlanSummaryList) -> list:
    import aws_sdk_ssm_incidents.types.response_plan_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_incidents.types.response_plan_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResponsePlanSummaryList:
    import aws_sdk_ssm_incidents.types.response_plan_summary

    out: ResponsePlanSummaryList = []
    for item in data:
        out.append(
            aws_sdk_ssm_incidents.types.response_plan_summary.deserialize_json(item)
        )
    return out
