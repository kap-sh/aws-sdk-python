"""Generated from Smithy shape ``com.amazonaws.ssmsap#ApplicationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application_discovery_status
    import aws_sdk_ssm_sap.types.application_id
    import aws_sdk_ssm_sap.types.application_type
    import aws_sdk_ssm_sap.types.ssm_sap_arn
    import aws_sdk_ssm_sap.types.tag_map


class ApplicationSummary(TypedDict):
    id: NotRequired["aws_sdk_ssm_sap.types.application_id.ApplicationId"]
    """<p>The ID of the application.</p>"""
    discovery_status: NotRequired[
        "aws_sdk_ssm_sap.types.application_discovery_status.ApplicationDiscoveryStatus"
    ]
    """<p>The status of the latest discovery.</p>"""
    type: NotRequired["aws_sdk_ssm_sap.types.application_type.ApplicationType"]
    """<p>The type of the application.</p>"""
    arn: NotRequired["aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn"]
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    tags: NotRequired["aws_sdk_ssm_sap.types.tag_map.TagMap"]
    """<p>The tags on the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "discovery_status" in value:
        import aws_sdk_ssm_sap.types.application_discovery_status

        out["DiscoveryStatus"] = (
            aws_sdk_ssm_sap.types.application_discovery_status.serialize_json(
                value["discovery_status"]
            )
        )
    if "type" in value:
        import aws_sdk_ssm_sap.types.application_type

        out["Type"] = aws_sdk_ssm_sap.types.application_type.serialize_json(
            value["type"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "tags" in value:
        import aws_sdk_ssm_sap.types.tag_map

        out["Tags"] = aws_sdk_ssm_sap.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "DiscoveryStatus" in data:
        import aws_sdk_ssm_sap.types.application_discovery_status

        out["discovery_status"] = (
            aws_sdk_ssm_sap.types.application_discovery_status.deserialize_json(
                data["DiscoveryStatus"]
            )
        )
    if "Type" in data:
        import aws_sdk_ssm_sap.types.application_type

        out["type"] = aws_sdk_ssm_sap.types.application_type.deserialize_json(
            data["Type"]
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Tags" in data:
        import aws_sdk_ssm_sap.types.tag_map

        out["tags"] = aws_sdk_ssm_sap.types.tag_map.deserialize_json(data["Tags"])
    return out
