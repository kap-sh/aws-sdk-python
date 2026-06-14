"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CognitoGroupConfigurationItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.group_entity_type


class CognitoGroupConfigurationItem(TypedDict):
    group_entity_type: NotRequired[
        "aws_sdk_verifiedpermissions.types.group_entity_type.GroupEntityType"
    ]
    """<p>The name of the schema entity type that's mapped to the user pool group. Defaults to <code>AWS::CognitoGroup</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CognitoGroupConfigurationItem) -> dict:
    out: dict = {}
    if "group_entity_type" in value:
        out["groupEntityType"] = value["group_entity_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CognitoGroupConfigurationItem:
    out: CognitoGroupConfigurationItem = {}  # type: ignore[typeddict-item]
    if "groupEntityType" in data:
        out["group_entity_type"] = data["groupEntityType"]
    return out
