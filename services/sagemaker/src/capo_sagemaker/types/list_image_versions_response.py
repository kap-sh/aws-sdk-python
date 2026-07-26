"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListImageVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.image_versions
    import capo_sagemaker.types.next_token


class ListImageVersionsResponse(TypedDict, closed=True):
    image_versions: NotRequired["capo_sagemaker.types.image_versions.ImageVersions"]
    """<p>A list of versions and their properties.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of versions, if there are any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListImageVersionsResponse) -> dict:
    out: dict = {}
    if "image_versions" in value:
        import capo_sagemaker.types.image_versions

        out["ImageVersions"] = (
            capo_sagemaker.types.image_versions.serialize_aws_json_1_1(
                value["image_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListImageVersionsResponse:
    out: ListImageVersionsResponse = {}  # type: ignore[typeddict-item]
    if "ImageVersions" in data:
        import capo_sagemaker.types.image_versions

        out["image_versions"] = (
            capo_sagemaker.types.image_versions.deserialize_aws_json_1_1(
                data["ImageVersions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
