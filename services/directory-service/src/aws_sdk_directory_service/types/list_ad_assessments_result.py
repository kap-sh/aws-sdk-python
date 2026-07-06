"""Generated from Smithy shape ``com.amazonaws.directoryservice#ListADAssessmentsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.assessments
    import aws_sdk_directory_service.types.next_token


class ListADAssessmentsResult(TypedDict, closed=True):
    assessments: NotRequired["aws_sdk_directory_service.types.assessments.Assessments"]
    """<p>A list of assessment summaries containing basic information about each directory assessment.</p>"""
    next_token: NotRequired["aws_sdk_directory_service.types.next_token.NextToken"]
    """<p>If not null, more results are available. Pass this value for the <code>NextToken</code> parameter in a subsequent request to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListADAssessmentsResult) -> dict:
    out: dict = {}
    if "assessments" in value:
        import aws_sdk_directory_service.types.assessments

        out["Assessments"] = (
            aws_sdk_directory_service.types.assessments.serialize_aws_json_1_1(
                value["assessments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListADAssessmentsResult:
    out: ListADAssessmentsResult = {}  # type: ignore[typeddict-item]
    if "Assessments" in data:
        import aws_sdk_directory_service.types.assessments

        out["assessments"] = (
            aws_sdk_directory_service.types.assessments.deserialize_aws_json_1_1(
                data["Assessments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
