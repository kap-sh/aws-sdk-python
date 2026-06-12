"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListSpacesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.space_list


class ListSpacesResponse(TypedDict):
    spaces: NotRequired["aws_sdk_sagemaker.types.space_list.SpaceList"]
    """<p>The list of spaces.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSpacesResponse) -> dict:
    out: dict = {}
    if "spaces" in value:
        import aws_sdk_sagemaker.types.space_list

        out["Spaces"] = aws_sdk_sagemaker.types.space_list.serialize_aws_json_1_1(
            value["spaces"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSpacesResponse:
    out: ListSpacesResponse = {}  # type: ignore[typeddict-item]
    if "Spaces" in data:
        import aws_sdk_sagemaker.types.space_list

        out["spaces"] = aws_sdk_sagemaker.types.space_list.deserialize_aws_json_1_1(
            data["Spaces"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
