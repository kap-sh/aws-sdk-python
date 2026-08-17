"""Generated from Smithy shape ``com.amazonaws.ecr#GetLifecyclePolicyPreviewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.lifecycle_policy_preview_result_list
    import capo_ecr.types.lifecycle_policy_preview_status
    import capo_ecr.types.lifecycle_policy_preview_summary
    import capo_ecr.types.lifecycle_policy_text
    import capo_ecr.types.next_token
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class GetLifecyclePolicyPreviewResponse(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_name: NotRequired["capo_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the request.</p>"""
    lifecycle_policy_text: NotRequired[
        "capo_ecr.types.lifecycle_policy_text.LifecyclePolicyText"
    ]
    """<p>The JSON lifecycle policy text.</p>"""
    status: NotRequired[
        "capo_ecr.types.lifecycle_policy_preview_status.LifecyclePolicyPreviewStatus"
    ]
    """<p>The status of the lifecycle policy preview request.</p>"""
    next_token: NotRequired["capo_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>GetLifecyclePolicyPreview</code> request. When the results of a <code>GetLifecyclePolicyPreview</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    preview_results: NotRequired[
        "capo_ecr.types.lifecycle_policy_preview_result_list.LifecyclePolicyPreviewResultList"
    ]
    """<p>The results of the lifecycle policy preview request.</p>"""
    summary: NotRequired[
        "capo_ecr.types.lifecycle_policy_preview_summary.LifecyclePolicyPreviewSummary"
    ]
    """<p>The list of images that is returned as a result of the action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLifecyclePolicyPreviewResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "lifecycle_policy_text" in value:
        out["lifecyclePolicyText"] = value["lifecycle_policy_text"]
    if "status" in value:
        import capo_ecr.types.lifecycle_policy_preview_status

        out["status"] = (
            capo_ecr.types.lifecycle_policy_preview_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "preview_results" in value:
        import capo_ecr.types.lifecycle_policy_preview_result_list

        out["previewResults"] = (
            capo_ecr.types.lifecycle_policy_preview_result_list.serialize_aws_json_1_1(
                value["preview_results"]
            )
        )
    if "summary" in value:
        import capo_ecr.types.lifecycle_policy_preview_summary

        out["summary"] = (
            capo_ecr.types.lifecycle_policy_preview_summary.serialize_aws_json_1_1(
                value["summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLifecyclePolicyPreviewResponse:
    out: GetLifecyclePolicyPreviewResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    if data.get("lifecyclePolicyText") is not None:
        out["lifecycle_policy_text"] = data["lifecyclePolicyText"]
    if data.get("status") is not None:
        import capo_ecr.types.lifecycle_policy_preview_status

        out["status"] = (
            capo_ecr.types.lifecycle_policy_preview_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("previewResults") is not None:
        import capo_ecr.types.lifecycle_policy_preview_result_list

        out["preview_results"] = (
            capo_ecr.types.lifecycle_policy_preview_result_list.deserialize_aws_json_1_1(
                data["previewResults"]
            )
        )
    if data.get("summary") is not None:
        import capo_ecr.types.lifecycle_policy_preview_summary

        out["summary"] = (
            capo_ecr.types.lifecycle_policy_preview_summary.deserialize_aws_json_1_1(
                data["summary"]
            )
        )
    return out
