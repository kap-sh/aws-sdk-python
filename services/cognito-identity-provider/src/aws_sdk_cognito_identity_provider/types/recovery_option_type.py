"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RecoveryOptionType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.priority_type
    import aws_sdk_cognito_identity_provider.types.recovery_option_name_type


class RecoveryOptionType(TypedDict, closed=True):
    priority: "aws_sdk_cognito_identity_provider.types.priority_type.PriorityType"
    """<p>Your priority preference for using the specified attribute in account recovery. The highest priority is <code>1</code>.</p>"""
    name: "aws_sdk_cognito_identity_provider.types.recovery_option_name_type.RecoveryOptionNameType"
    """<p>The recovery method that this object sets a recovery option for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecoveryOptionType) -> dict:
    out: dict = {}
    out["Priority"] = value["priority"]
    import aws_sdk_cognito_identity_provider.types.recovery_option_name_type

    out["Name"] = (
        aws_sdk_cognito_identity_provider.types.recovery_option_name_type.serialize_aws_json_1_1(
            value["name"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecoveryOptionType:
    out: RecoveryOptionType = {}  # type: ignore[typeddict-item]
    if "Priority" in data:
        out["priority"] = data["Priority"]
    else:
        raise DeserializationError("RecoveryOptionType.priority required")
    if "Name" in data:
        import aws_sdk_cognito_identity_provider.types.recovery_option_name_type

        out["name"] = (
            aws_sdk_cognito_identity_provider.types.recovery_option_name_type.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("RecoveryOptionType.name required")
    return out
