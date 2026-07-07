"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactFlowVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.contact_flow_description
    import aws_sdk_connect.types.flow_content_sha256
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.resource_version
    import aws_sdk_connect.types.timestamp


class CreateContactFlowVersionRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.contact_flow_description.ContactFlowDescription"
    ]
    """<p>The description of the flow version.</p>"""
    contact_flow_id: "aws_sdk_connect.types.arn.ARN"
    """<p>The identifier of the flow.</p>"""
    flow_content_sha256: NotRequired[
        "aws_sdk_connect.types.flow_content_sha256.FlowContentSha256"
    ]
    """<p>Indicates the checksum value of the flow content.</p>"""
    contact_flow_version: NotRequired[
        "aws_sdk_connect.types.resource_version.ResourceVersion"
    ]
    """<p>The identifier of the flow version.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactFlowVersionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "flow_content_sha256" in value:
        out["FlowContentSha256"] = value["flow_content_sha256"]
    if "contact_flow_version" in value:
        out["ContactFlowVersion"] = value["contact_flow_version"]
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> CreateContactFlowVersionRequest:
    out: CreateContactFlowVersionRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "FlowContentSha256" in data:
        out["flow_content_sha256"] = data["FlowContentSha256"]
    if "ContactFlowVersion" in data:
        out["contact_flow_version"] = data["ContactFlowVersion"]
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
