"""Generated from Smithy shape ``com.amazonaws.appflow#PardotConnectorProfileProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.boolean
    import aws_sdk_appflow.types.business_unit_id
    import aws_sdk_appflow.types.instance_url


class PardotConnectorProfileProperties(TypedDict, closed=True):
    instance_url: NotRequired["aws_sdk_appflow.types.instance_url.InstanceUrl"]
    """<p>The location of the Salesforce Pardot resource.</p>"""
    is_sandbox_environment: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Indicates whether the connector profile applies to a sandbox or production environment.</p>"""
    business_unit_id: NotRequired[
        "aws_sdk_appflow.types.business_unit_id.BusinessUnitId"
    ]
    """<p>The business unit id of Salesforce Pardot instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PardotConnectorProfileProperties) -> dict:
    out: dict = {}
    if "instance_url" in value:
        out["instanceUrl"] = value["instance_url"]
    out["isSandboxEnvironment"] = value.get("is_sandbox_environment", False)
    if "business_unit_id" in value:
        out["businessUnitId"] = value["business_unit_id"]
    return out


def deserialize_json(data: dict) -> PardotConnectorProfileProperties:
    out: PardotConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if "instanceUrl" in data:
        out["instance_url"] = data["instanceUrl"]
    if "isSandboxEnvironment" in data:
        out["is_sandbox_environment"] = data["isSandboxEnvironment"]
    else:
        out["is_sandbox_environment"] = False
    if "businessUnitId" in data:
        out["business_unit_id"] = data["businessUnitId"]
    return out
