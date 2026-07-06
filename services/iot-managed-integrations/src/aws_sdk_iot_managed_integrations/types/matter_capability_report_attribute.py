"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReportAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.action_name
    import aws_sdk_iot_managed_integrations.types.matter_attribute_id
    import aws_sdk_iot_managed_integrations.types.matter_capability_report_attribute_value


class MatterCapabilityReportAttribute(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.matter_attribute_id.MatterAttributeId"
    ]
    """<p>The id of the Matter attribute.</p>"""
    name: NotRequired["aws_sdk_iot_managed_integrations.types.action_name.ActionName"]
    """<p>Name for the Amazon Web Services Matter capability report attribute.</p>"""
    value: NotRequired[
        "aws_sdk_iot_managed_integrations.types.matter_capability_report_attribute_value.MatterCapabilityReportAttributeValue"
    ]
    """<p>Value for the Amazon Web Services Matter capability report attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReportAttribute) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> MatterCapabilityReportAttribute:
    out: MatterCapabilityReportAttribute = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    return out
