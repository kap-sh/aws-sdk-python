"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CognitoGroupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.group_entity_type


class CognitoGroupConfiguration(TypedDict, closed=True):
    group_entity_type: (
        "aws_sdk_verifiedpermissions.types.group_entity_type.GroupEntityType"
    )
    """<p>The name of the schema entity type that's mapped to the user pool group. Defaults to <code>AWS::CognitoGroup</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CognitoGroupConfiguration) -> dict:
    out: dict = {}
    out["groupEntityType"] = value["group_entity_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CognitoGroupConfiguration:
    out: CognitoGroupConfiguration = {}  # type: ignore[typeddict-item]
    if "groupEntityType" in data:
        out["group_entity_type"] = data["groupEntityType"]
    else:
        raise DeserializationError(
            "CognitoGroupConfiguration.group_entity_type required"
        )
    return out
