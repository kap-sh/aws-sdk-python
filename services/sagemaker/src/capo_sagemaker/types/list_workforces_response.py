"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListWorkforcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.workforces


class ListWorkforcesResponse(TypedDict, closed=True):
    workforces: NotRequired["capo_sagemaker.types.workforces.Workforces"]
    """<p>A list containing information about your workforce.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token to resume pagination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkforcesResponse) -> dict:
    out: dict = {}
    if "workforces" in value:
        import capo_sagemaker.types.workforces

        out["Workforces"] = capo_sagemaker.types.workforces.serialize_aws_json_1_1(
            value["workforces"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkforcesResponse:
    out: ListWorkforcesResponse = {}  # type: ignore[typeddict-item]
    if "Workforces" in data:
        import capo_sagemaker.types.workforces

        out["workforces"] = capo_sagemaker.types.workforces.deserialize_aws_json_1_1(
            data["Workforces"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
