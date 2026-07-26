"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AccessControlAttributeValueSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso_admin.types.access_control_attribute_value_source

AccessControlAttributeValueSourceList: TypeAlias = list[
    "capo_sso_admin.types.access_control_attribute_value_source.AccessControlAttributeValueSource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessControlAttributeValueSourceList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AccessControlAttributeValueSourceList:
    return list(data)
