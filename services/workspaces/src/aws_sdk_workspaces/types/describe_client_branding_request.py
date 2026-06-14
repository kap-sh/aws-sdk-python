"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeClientBrandingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.directory_id


class DescribeClientBrandingRequest(TypedDict):
    resource_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p>The directory identifier of the WorkSpace for which you want to view client branding information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClientBrandingRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClientBrandingRequest:
    out: DescribeClientBrandingRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("DescribeClientBrandingRequest.resource_id required")
    return out
