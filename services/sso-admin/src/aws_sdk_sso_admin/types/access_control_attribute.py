"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AccessControlAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.access_control_attribute_key
    import aws_sdk_sso_admin.types.access_control_attribute_value


class AccessControlAttribute(TypedDict, closed=True):
    key: (
        "aws_sdk_sso_admin.types.access_control_attribute_key.AccessControlAttributeKey"
    )
    """<p>The name of the attribute associated with your identities in your identity source. This is used to map a specified attribute in your identity source with an attribute in IAM Identity Center.</p>"""
    value: "aws_sdk_sso_admin.types.access_control_attribute_value.AccessControlAttributeValue"
    """<p>The value used for mapping a specified attribute to an identity source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessControlAttribute) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import aws_sdk_sso_admin.types.access_control_attribute_value

    out["Value"] = (
        aws_sdk_sso_admin.types.access_control_attribute_value.serialize_aws_json_1_1(
            value["value"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessControlAttribute:
    out: AccessControlAttribute = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("AccessControlAttribute.key required")
    if "Value" in data:
        import aws_sdk_sso_admin.types.access_control_attribute_value

        out["value"] = (
            aws_sdk_sso_admin.types.access_control_attribute_value.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    else:
        raise DeserializationError("AccessControlAttribute.value required")
    return out
