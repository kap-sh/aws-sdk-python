"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AttributeType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.attribute_name_type
    import aws_sdk_cognito_identity_provider.types.attribute_value_type


class AttributeType(TypedDict, closed=True):
    name: (
        "aws_sdk_cognito_identity_provider.types.attribute_name_type.AttributeNameType"
    )
    r"""<p>The name of the attribute, for example <code>email</code> or <code>custom:department</code>.</p> <p>In some older user pools, the regex pattern for acceptable values of this parameter is <code>[\p{L}\p{M}\p{S}\p{N}\p{P}]+</code>. Older pools will eventually be updated to use the new pattern. Affected user pools are those created before May 2024 in US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), Middle East (Bahrain), and South America (São Paulo). </p>"""
    value: NotRequired[
        "aws_sdk_cognito_identity_provider.types.attribute_value_type.AttributeValueType"
    ]
    """<p>The value of the attribute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeType) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttributeType:
    out: AttributeType = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("AttributeType.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    return out
