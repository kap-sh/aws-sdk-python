"""Generated from Smithy shape ``com.amazonaws.codecommit#PullRequestMergedStateChangedEventMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.merge_metadata
    import capo_codecommit.types.reference_name
    import capo_codecommit.types.repository_name


class PullRequestMergedStateChangedEventMetadata(TypedDict, closed=True):
    repository_name: NotRequired["capo_codecommit.types.repository_name.RepositoryName"]
    """<p>The name of the repository where the pull request was created.</p>"""
    destination_reference: NotRequired[
        "capo_codecommit.types.reference_name.ReferenceName"
    ]
    """<p>The name of the branch that the pull request is merged into.</p>"""
    merge_metadata: NotRequired["capo_codecommit.types.merge_metadata.MergeMetadata"]
    """<p>Information about the merge state change event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestMergedStateChangedEventMetadata) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "destination_reference" in value:
        out["destinationReference"] = value["destination_reference"]
    if "merge_metadata" in value:
        import capo_codecommit.types.merge_metadata

        out["mergeMetadata"] = (
            capo_codecommit.types.merge_metadata.serialize_aws_json_1_1(
                value["merge_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PullRequestMergedStateChangedEventMetadata:
    out: PullRequestMergedStateChangedEventMetadata = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "destinationReference" in data:
        out["destination_reference"] = data["destinationReference"]
    if "mergeMetadata" in data:
        import capo_codecommit.types.merge_metadata

        out["merge_metadata"] = (
            capo_codecommit.types.merge_metadata.deserialize_aws_json_1_1(
                data["mergeMetadata"]
            )
        )
    return out
