"""Generated from Smithy shape ``com.amazonaws.ssm#GetOpsMetadataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.metadata_map
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.ops_metadata_resource_id


class GetOpsMetadataResult(TypedDict, closed=True):
    resource_id: NotRequired[
        "aws_sdk_ssm.types.ops_metadata_resource_id.OpsMetadataResourceId"
    ]
    """<p>The resource ID of the Application Manager application.</p>"""
    metadata: NotRequired["aws_sdk_ssm.types.metadata_map.MetadataMap"]
    """<p>OpsMetadata for an Application Manager application.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOpsMetadataResult) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "metadata" in value:
        import aws_sdk_ssm.types.metadata_map

        out["Metadata"] = aws_sdk_ssm.types.metadata_map.serialize_aws_json_1_1(
            value["metadata"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOpsMetadataResult:
    out: GetOpsMetadataResult = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "Metadata" in data:
        import aws_sdk_ssm.types.metadata_map

        out["metadata"] = aws_sdk_ssm.types.metadata_map.deserialize_aws_json_1_1(
            data["Metadata"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
