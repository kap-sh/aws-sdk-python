"""Generated from Smithy shape ``com.amazonaws.ssm#GetOpsMetadataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.metadata_map
    import capo_ssm.types.next_token
    import capo_ssm.types.ops_metadata_resource_id


class GetOpsMetadataResult(TypedDict, closed=True):
    resource_id: NotRequired[
        "capo_ssm.types.ops_metadata_resource_id.OpsMetadataResourceId"
    ]
    """<p>The resource ID of the Application Manager application.</p>"""
    metadata: NotRequired["capo_ssm.types.metadata_map.MetadataMap"]
    """<p>OpsMetadata for an Application Manager application.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOpsMetadataResult) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "metadata" in value:
        import capo_ssm.types.metadata_map

        out["Metadata"] = capo_ssm.types.metadata_map.serialize_aws_json_1_1(
            value["metadata"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOpsMetadataResult:
    out: GetOpsMetadataResult = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("Metadata") is not None:
        import capo_ssm.types.metadata_map

        out["metadata"] = capo_ssm.types.metadata_map.deserialize_aws_json_1_1(
            data["Metadata"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
