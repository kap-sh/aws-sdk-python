"""Generated from Smithy shape ``com.amazonaws.mturk#ListWorkersWithQualificationTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mturk.types.integer
    import aws_sdk_mturk.types.pagination_token
    import aws_sdk_mturk.types.qualification_list


class ListWorkersWithQualificationTypeResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_mturk.types.pagination_token.PaginationToken"]
    num_results: NotRequired["aws_sdk_mturk.types.integer.Integer"]
    """<p> The number of Qualifications on this page in the filtered results list, equivalent to the number of Qualifications being returned by this call.</p>"""
    qualifications: NotRequired[
        "aws_sdk_mturk.types.qualification_list.QualificationList"
    ]
    """<p> The list of Qualification elements returned by this call. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkersWithQualificationTypeResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "num_results" in value:
        out["NumResults"] = value["num_results"]
    if "qualifications" in value:
        import aws_sdk_mturk.types.qualification_list

        out["Qualifications"] = (
            aws_sdk_mturk.types.qualification_list.serialize_aws_json_1_1(
                value["qualifications"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkersWithQualificationTypeResponse:
    out: ListWorkersWithQualificationTypeResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "NumResults" in data:
        out["num_results"] = data["NumResults"]
    if "Qualifications" in data:
        import aws_sdk_mturk.types.qualification_list

        out["qualifications"] = (
            aws_sdk_mturk.types.qualification_list.deserialize_aws_json_1_1(
                data["Qualifications"]
            )
        )
    return out
