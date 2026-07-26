"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListSubCheckResultsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.next_token
    import capo_ssm_sap.types.sub_check_result_list


class ListSubCheckResultsOutput(TypedDict, closed=True):
    sub_check_results: NotRequired[
        "capo_ssm_sap.types.sub_check_result_list.SubCheckResultList"
    ]
    """<p>The sub-check results of a configuration check operation.</p>"""
    next_token: NotRequired["capo_ssm_sap.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubCheckResultsOutput) -> dict:
    out: dict = {}
    if "sub_check_results" in value:
        import capo_ssm_sap.types.sub_check_result_list

        out["SubCheckResults"] = (
            capo_ssm_sap.types.sub_check_result_list.serialize_json(
                value["sub_check_results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubCheckResultsOutput:
    out: ListSubCheckResultsOutput = {}  # type: ignore[typeddict-item]
    if "SubCheckResults" in data:
        import capo_ssm_sap.types.sub_check_result_list

        out["sub_check_results"] = (
            capo_ssm_sap.types.sub_check_result_list.deserialize_json(
                data["SubCheckResults"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
