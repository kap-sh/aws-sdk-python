"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListSpacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.space_list


class ListSpacesResponse(TypedDict, closed=True):
    spaces: NotRequired["capo_sagemaker.types.space_list.SpaceList"]
    """<p>The list of spaces.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSpacesResponse) -> dict:
    out: dict = {}
    if "spaces" in value:
        import capo_sagemaker.types.space_list

        out["Spaces"] = capo_sagemaker.types.space_list.serialize_aws_json_1_1(
            value["spaces"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSpacesResponse:
    out: ListSpacesResponse = {}  # type: ignore[typeddict-item]
    if "Spaces" in data:
        import capo_sagemaker.types.space_list

        out["spaces"] = capo_sagemaker.types.space_list.deserialize_aws_json_1_1(
            data["Spaces"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
