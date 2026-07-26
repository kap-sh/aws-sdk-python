"""Generated from Smithy shape ``com.amazonaws.ssmsap#ApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.application_discovery_status
    import capo_ssm_sap.types.application_id
    import capo_ssm_sap.types.application_type
    import capo_ssm_sap.types.ssm_sap_arn
    import capo_ssm_sap.types.tag_map


class ApplicationSummary(TypedDict, closed=True):
    id: NotRequired["capo_ssm_sap.types.application_id.ApplicationId"]
    """<p>The ID of the application.</p>"""
    discovery_status: NotRequired[
        "capo_ssm_sap.types.application_discovery_status.ApplicationDiscoveryStatus"
    ]
    """<p>The status of the latest discovery.</p>"""
    type: NotRequired["capo_ssm_sap.types.application_type.ApplicationType"]
    """<p>The type of the application.</p>"""
    arn: NotRequired["capo_ssm_sap.types.ssm_sap_arn.SsmSapArn"]
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    tags: NotRequired["capo_ssm_sap.types.tag_map.TagMap"]
    """<p>The tags on the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "discovery_status" in value:
        import capo_ssm_sap.types.application_discovery_status

        out["DiscoveryStatus"] = (
            capo_ssm_sap.types.application_discovery_status.serialize_json(
                value["discovery_status"]
            )
        )
    if "type" in value:
        import capo_ssm_sap.types.application_type

        out["Type"] = capo_ssm_sap.types.application_type.serialize_json(value["type"])
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "tags" in value:
        import capo_ssm_sap.types.tag_map

        out["Tags"] = capo_ssm_sap.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "DiscoveryStatus" in data:
        import capo_ssm_sap.types.application_discovery_status

        out["discovery_status"] = (
            capo_ssm_sap.types.application_discovery_status.deserialize_json(
                data["DiscoveryStatus"]
            )
        )
    if "Type" in data:
        import capo_ssm_sap.types.application_type

        out["type"] = capo_ssm_sap.types.application_type.deserialize_json(data["Type"])
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Tags" in data:
        import capo_ssm_sap.types.tag_map

        out["tags"] = capo_ssm_sap.types.tag_map.deserialize_json(data["Tags"])
    return out
