"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AccessControlAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso_admin.types.access_control_attribute

AccessControlAttributeList: TypeAlias = list[
    "capo_sso_admin.types.access_control_attribute.AccessControlAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessControlAttributeList) -> list:
    import capo_sso_admin.types.access_control_attribute

    out: list = []
    for item in value:
        out.append(
            capo_sso_admin.types.access_control_attribute.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccessControlAttributeList:
    import capo_sso_admin.types.access_control_attribute

    out: AccessControlAttributeList = []
    for item in data:
        out.append(
            capo_sso_admin.types.access_control_attribute.deserialize_aws_json_1_1(item)
        )
    return out
