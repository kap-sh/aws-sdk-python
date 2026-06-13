"""Generated from Smithy shape ``com.amazonaws.emr#CreatePersistentAppUIOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean
    import aws_sdk_emr.types.xml_string_max_len256


class CreatePersistentAppUIOutput(TypedDict):
    persistent_app_ui_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The persistent application user interface identifier.</p>"""
    runtime_role_enabled_cluster: NotRequired["aws_sdk_emr.types.boolean.Boolean"]
    """<p>Represents if the EMR on EC2 cluster that the persisent application user interface is created for is a runtime role enabled cluster or not.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePersistentAppUIOutput) -> dict:
    out: dict = {}
    if "persistent_app_ui_id" in value:
        out["PersistentAppUIId"] = value["persistent_app_ui_id"]
    if "runtime_role_enabled_cluster" in value:
        out["RuntimeRoleEnabledCluster"] = value["runtime_role_enabled_cluster"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePersistentAppUIOutput:
    out: CreatePersistentAppUIOutput = {}  # type: ignore[typeddict-item]
    if "PersistentAppUIId" in data:
        out["persistent_app_ui_id"] = data["PersistentAppUIId"]
    if "RuntimeRoleEnabledCluster" in data:
        out["runtime_role_enabled_cluster"] = data["RuntimeRoleEnabledCluster"]
    return out
