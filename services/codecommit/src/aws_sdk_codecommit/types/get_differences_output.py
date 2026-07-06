"""Generated from Smithy shape ``com.amazonaws.codecommit#GetDifferencesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.difference_list
    import aws_sdk_codecommit.types.next_token


class GetDifferencesOutput(TypedDict, closed=True):
    differences: NotRequired["aws_sdk_codecommit.types.difference_list.DifferenceList"]
    """<p>A data type object that contains information about the differences, including whether the difference is added, modified, or deleted (A, D, M).</p>"""
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDifferencesOutput) -> dict:
    out: dict = {}
    if "differences" in value:
        import aws_sdk_codecommit.types.difference_list

        out["differences"] = (
            aws_sdk_codecommit.types.difference_list.serialize_aws_json_1_1(
                value["differences"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDifferencesOutput:
    out: GetDifferencesOutput = {}  # type: ignore[typeddict-item]
    if "differences" in data:
        import aws_sdk_codecommit.types.difference_list

        out["differences"] = (
            aws_sdk_codecommit.types.difference_list.deserialize_aws_json_1_1(
                data["differences"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
