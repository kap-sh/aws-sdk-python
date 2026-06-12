"""Generated from Smithy shape ``com.amazonaws.mturk#ListQualificationTypesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mturk.types.integer
    import aws_sdk_mturk.types.pagination_token
    import aws_sdk_mturk.types.qualification_type_list


class ListQualificationTypesResponse(TypedDict):
    num_results: NotRequired["aws_sdk_mturk.types.integer.Integer"]
    """<p> The number of Qualification types on this page in the filtered results list, equivalent to the number of types this operation returns. </p>"""
    next_token: NotRequired["aws_sdk_mturk.types.pagination_token.PaginationToken"]
    qualification_types: NotRequired[
        "aws_sdk_mturk.types.qualification_type_list.QualificationTypeList"
    ]
    """<p> The list of QualificationType elements returned by the query. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListQualificationTypesResponse) -> dict:
    out: dict = {}
    if "num_results" in value:
        out["NumResults"] = value["num_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "qualification_types" in value:
        import aws_sdk_mturk.types.qualification_type_list

        out["QualificationTypes"] = (
            aws_sdk_mturk.types.qualification_type_list.serialize_aws_json_1_1(
                value["qualification_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListQualificationTypesResponse:
    out: ListQualificationTypesResponse = {}  # type: ignore[typeddict-item]
    if "NumResults" in data:
        out["num_results"] = data["NumResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "QualificationTypes" in data:
        import aws_sdk_mturk.types.qualification_type_list

        out["qualification_types"] = (
            aws_sdk_mturk.types.qualification_type_list.deserialize_aws_json_1_1(
                data["QualificationTypes"]
            )
        )
    return out
