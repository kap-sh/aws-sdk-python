"""Generated from Smithy shape ``com.amazonaws.appstream#EntitlementAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.entitlement_attribute

EntitlementAttributeList: TypeAlias = list[
    "aws_sdk_appstream.types.entitlement_attribute.EntitlementAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementAttributeList) -> list:
    import aws_sdk_appstream.types.entitlement_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appstream.types.entitlement_attribute.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntitlementAttributeList:
    import aws_sdk_appstream.types.entitlement_attribute

    out: EntitlementAttributeList = []
    for item in data:
        out.append(
            aws_sdk_appstream.types.entitlement_attribute.deserialize_aws_json_1_1(item)
        )
    return out
