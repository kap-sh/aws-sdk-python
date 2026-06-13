"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListSubCheckResultsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.next_token
    import aws_sdk_ssm_sap.types.sub_check_result_list


class ListSubCheckResultsOutput(TypedDict):
    sub_check_results: NotRequired[
        "aws_sdk_ssm_sap.types.sub_check_result_list.SubCheckResultList"
    ]
    """<p>The sub-check results of a configuration check operation.</p>"""
    next_token: NotRequired["aws_sdk_ssm_sap.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubCheckResultsOutput) -> dict:
    out: dict = {}
    if "sub_check_results" in value:
        import aws_sdk_ssm_sap.types.sub_check_result_list

        out["SubCheckResults"] = (
            aws_sdk_ssm_sap.types.sub_check_result_list.serialize_json(
                value["sub_check_results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubCheckResultsOutput:
    out: ListSubCheckResultsOutput = {}  # type: ignore[typeddict-item]
    if "SubCheckResults" in data:
        import aws_sdk_ssm_sap.types.sub_check_result_list

        out["sub_check_results"] = (
            aws_sdk_ssm_sap.types.sub_check_result_list.deserialize_json(
                data["SubCheckResults"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
