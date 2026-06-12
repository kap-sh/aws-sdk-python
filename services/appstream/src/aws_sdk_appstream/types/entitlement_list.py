"""Generated from Smithy shape ``com.amazonaws.appstream#EntitlementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.entitlement

EntitlementList: TypeAlias = list["aws_sdk_appstream.types.entitlement.Entitlement"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementList) -> list:
    import aws_sdk_appstream.types.entitlement

    out: list = []
    for item in value:
        out.append(aws_sdk_appstream.types.entitlement.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EntitlementList:
    import aws_sdk_appstream.types.entitlement

    out: EntitlementList = []
    for item in data:
        out.append(aws_sdk_appstream.types.entitlement.deserialize_aws_json_1_1(item))
    return out
