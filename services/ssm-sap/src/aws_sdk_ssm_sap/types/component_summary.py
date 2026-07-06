"""Generated from Smithy shape ``com.amazonaws.ssmsap#ComponentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application_id
    import aws_sdk_ssm_sap.types.component_id
    import aws_sdk_ssm_sap.types.component_type
    import aws_sdk_ssm_sap.types.ssm_sap_arn
    import aws_sdk_ssm_sap.types.tag_map


class ComponentSummary(TypedDict, closed=True):
    application_id: NotRequired["aws_sdk_ssm_sap.types.application_id.ApplicationId"]
    """<p>The ID of the application.</p>"""
    component_id: NotRequired["aws_sdk_ssm_sap.types.component_id.ComponentId"]
    """<p>The ID of the component.</p>"""
    component_type: NotRequired["aws_sdk_ssm_sap.types.component_type.ComponentType"]
    """<p>The type of the component.</p>"""
    tags: NotRequired["aws_sdk_ssm_sap.types.tag_map.TagMap"]
    """<p>The tags of the component.</p>"""
    arn: NotRequired["aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn"]
    """<p>The Amazon Resource Name (ARN) of the component summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentSummary) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "component_id" in value:
        out["ComponentId"] = value["component_id"]
    if "component_type" in value:
        import aws_sdk_ssm_sap.types.component_type

        out["ComponentType"] = aws_sdk_ssm_sap.types.component_type.serialize_json(
            value["component_type"]
        )
    if "tags" in value:
        import aws_sdk_ssm_sap.types.tag_map

        out["Tags"] = aws_sdk_ssm_sap.types.tag_map.serialize_json(value["tags"])
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> ComponentSummary:
    out: ComponentSummary = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "ComponentId" in data:
        out["component_id"] = data["ComponentId"]
    if "ComponentType" in data:
        import aws_sdk_ssm_sap.types.component_type

        out["component_type"] = aws_sdk_ssm_sap.types.component_type.deserialize_json(
            data["ComponentType"]
        )
    if "Tags" in data:
        import aws_sdk_ssm_sap.types.tag_map

        out["tags"] = aws_sdk_ssm_sap.types.tag_map.deserialize_json(data["Tags"])
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
