"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListArtifactsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_artifacts_by
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.source_uri
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.timestamp


class ListArtifactsRequest(TypedDict):
    source_uri: NotRequired["aws_sdk_sagemaker.types.source_uri.SourceUri"]
    """<p>A filter that returns only artifacts with the specified source URI.</p>"""
    artifact_type: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>A filter that returns only artifacts of the specified type.</p>"""
    created_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only artifacts created on or after the specified time.</p>"""
    created_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only artifacts created on or before the specified time.</p>"""
    sort_by: NotRequired["aws_sdk_sagemaker.types.sort_artifacts_by.SortArtifactsBy"]
    """<p>The property used to sort results. The default value is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order. The default value is <code>Descending</code>.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous call to <code>ListArtifacts</code> didn't return the full set of artifacts, the call returns a token for getting the next set of artifacts.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of artifacts to return in the response. The default value is 10.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListArtifactsRequest) -> dict:
    out: dict = {}
    if "source_uri" in value:
        out["SourceUri"] = value["source_uri"]
    if "artifact_type" in value:
        out["ArtifactType"] = value["artifact_type"]
    if "created_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedAfter"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedBefore"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.sort_artifacts_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.sort_artifacts_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListArtifactsRequest:
    out: ListArtifactsRequest = {}  # type: ignore[typeddict-item]
    if "SourceUri" in data:
        out["source_uri"] = data["SourceUri"]
    if "ArtifactType" in data:
        out["artifact_type"] = data["ArtifactType"]
    if "CreatedAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedAfter"]
            )
        )
    if "CreatedBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedBefore"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.sort_artifacts_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.sort_artifacts_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
