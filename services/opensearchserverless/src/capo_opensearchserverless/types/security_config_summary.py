"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#SecurityConfigSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.config_description
    import capo_opensearchserverless.types.policy_version
    import capo_opensearchserverless.types.security_config_id
    import capo_opensearchserverless.types.security_config_type


class SecurityConfigSummary(TypedDict, closed=True):
    id: NotRequired[
        "capo_opensearchserverless.types.security_config_id.SecurityConfigId"
    ]
    """<p>The unique identifier of the security configuration.</p>"""
    type: NotRequired[
        "capo_opensearchserverless.types.security_config_type.SecurityConfigType"
    ]
    """<p>The type of security configuration.</p>"""
    config_version: NotRequired[
        "capo_opensearchserverless.types.policy_version.PolicyVersion"
    ]
    """<p>The version of the security configuration.</p>"""
    description: NotRequired[
        "capo_opensearchserverless.types.config_description.ConfigDescription"
    ]
    """<p>The description of the security configuration.</p>"""
    created_date: NotRequired["int"]
    """<p>The Epoch time when the security configuration was created.</p>"""
    last_modified_date: NotRequired["int"]
    """<p>The timestamp of when the configuration was last modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecurityConfigSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        out["type"] = value["type"]
    if "config_version" in value:
        out["configVersion"] = value["config_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_date" in value:
        out["createdDate"] = value["created_date"]
    if "last_modified_date" in value:
        out["lastModifiedDate"] = value["last_modified_date"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SecurityConfigSummary:
    out: SecurityConfigSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "type" in data:
        out["type"] = data["type"]
    if "configVersion" in data:
        out["config_version"] = data["configVersion"]
    if "description" in data:
        out["description"] = data["description"]
    if "createdDate" in data:
        out["created_date"] = data["createdDate"]
    if "lastModifiedDate" in data:
        out["last_modified_date"] = data["lastModifiedDate"]
    return out
