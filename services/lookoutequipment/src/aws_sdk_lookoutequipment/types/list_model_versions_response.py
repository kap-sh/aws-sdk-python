"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListModelVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.model_version_summaries
    import aws_sdk_lookoutequipment.types.next_token


class ListModelVersionsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p>If the total number of results exceeds the limit that the response can display, the response returns an opaque pagination token indicating where to continue the listing of machine learning model versions. Use this token in the <code>NextToken</code> field in the request to list the next page of results.</p>"""
    model_version_summaries: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version_summaries.ModelVersionSummaries"
    ]
    """<p>Provides information on the specified model version, including the created time, model and dataset ARNs, and status.</p> <note> <p>If you don't supply the <code>ModelName</code> request parameter, or if you supply the name of a model that doesn't exist, <code>ListModelVersions</code> returns an empty array in <code>ModelVersionSummaries</code>. </p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListModelVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "model_version_summaries" in value:
        import aws_sdk_lookoutequipment.types.model_version_summaries

        out["ModelVersionSummaries"] = (
            aws_sdk_lookoutequipment.types.model_version_summaries.serialize_aws_json_1_0(
                value["model_version_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListModelVersionsResponse:
    out: ListModelVersionsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ModelVersionSummaries" in data:
        import aws_sdk_lookoutequipment.types.model_version_summaries

        out["model_version_summaries"] = (
            aws_sdk_lookoutequipment.types.model_version_summaries.deserialize_aws_json_1_0(
                data["ModelVersionSummaries"]
            )
        )
    return out
