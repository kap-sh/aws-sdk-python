"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListApplicationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.filter_list
    import aws_sdk_ssm_sap.types.max_results
    import aws_sdk_ssm_sap.types.next_token


class ListApplicationsInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_ssm_sap.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_ssm_sap.types.max_results.MaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>"""
    filters: NotRequired["aws_sdk_ssm_sap.types.filter_list.FilterList"]
    """<p>The filter of name, value, and operator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import aws_sdk_ssm_sap.types.filter_list

        out["Filters"] = aws_sdk_ssm_sap.types.filter_list.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> ListApplicationsInput:
    out: ListApplicationsInput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Filters" in data:
        import aws_sdk_ssm_sap.types.filter_list

        out["filters"] = aws_sdk_ssm_sap.types.filter_list.deserialize_json(
            data["Filters"]
        )
    return out
