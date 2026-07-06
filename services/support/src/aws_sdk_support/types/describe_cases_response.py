"""Generated from Smithy shape ``com.amazonaws.support#DescribeCasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_support.types.case_list
    import aws_sdk_support.types.next_token


class DescribeCasesResponse(TypedDict, closed=True):
    cases: NotRequired["aws_sdk_support.types.case_list.CaseList"]
    """<p>The details for the cases that match the request.</p>"""
    next_token: NotRequired["aws_sdk_support.types.next_token.NextToken"]
    """<p>A resumption point for pagination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCasesResponse) -> dict:
    out: dict = {}
    if "cases" in value:
        import aws_sdk_support.types.case_list

        out["cases"] = aws_sdk_support.types.case_list.serialize_aws_json_1_1(
            value["cases"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCasesResponse:
    out: DescribeCasesResponse = {}  # type: ignore[typeddict-item]
    if "cases" in data:
        import aws_sdk_support.types.case_list

        out["cases"] = aws_sdk_support.types.case_list.deserialize_aws_json_1_1(
            data["cases"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
