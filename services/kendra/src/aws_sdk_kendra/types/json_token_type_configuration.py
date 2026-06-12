"""Generated from Smithy shape ``com.amazonaws.kendra#JsonTokenTypeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.string


class JsonTokenTypeConfiguration(TypedDict):
    user_name_attribute_field: "aws_sdk_kendra.types.string.String"
    """<p>The user name attribute field.</p>"""
    group_attribute_field: "aws_sdk_kendra.types.string.String"
    """<p>The group attribute field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JsonTokenTypeConfiguration) -> dict:
    out: dict = {}
    out["UserNameAttributeField"] = value["user_name_attribute_field"]
    out["GroupAttributeField"] = value["group_attribute_field"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JsonTokenTypeConfiguration:
    out: JsonTokenTypeConfiguration = {}  # type: ignore[typeddict-item]
    if "UserNameAttributeField" in data:
        out["user_name_attribute_field"] = data["UserNameAttributeField"]
    else:
        raise DeserializationError(
            "JsonTokenTypeConfiguration.user_name_attribute_field required"
        )
    if "GroupAttributeField" in data:
        out["group_attribute_field"] = data["GroupAttributeField"]
    else:
        raise DeserializationError(
            "JsonTokenTypeConfiguration.group_attribute_field required"
        )
    return out
