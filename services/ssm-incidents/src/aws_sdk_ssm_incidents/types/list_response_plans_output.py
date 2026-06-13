"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ListResponsePlansOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.next_token
    import aws_sdk_ssm_incidents.types.response_plan_summary_list


class ListResponsePlansOutput(TypedDict):
    response_plan_summaries: (
        "aws_sdk_ssm_incidents.types.response_plan_summary_list.ResponsePlanSummaryList"
    )
    """<p>Details of each response plan.</p>"""
    next_token: NotRequired["aws_sdk_ssm_incidents.types.next_token.NextToken"]
    """<p>The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResponsePlansOutput) -> dict:
    out: dict = {}
    import aws_sdk_ssm_incidents.types.response_plan_summary_list

    out["responsePlanSummaries"] = (
        aws_sdk_ssm_incidents.types.response_plan_summary_list.serialize_json(
            value["response_plan_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResponsePlansOutput:
    out: ListResponsePlansOutput = {}  # type: ignore[typeddict-item]
    if "responsePlanSummaries" in data:
        import aws_sdk_ssm_incidents.types.response_plan_summary_list

        out["response_plan_summaries"] = (
            aws_sdk_ssm_incidents.types.response_plan_summary_list.deserialize_json(
                data["responsePlanSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListResponsePlansOutput.response_plan_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
