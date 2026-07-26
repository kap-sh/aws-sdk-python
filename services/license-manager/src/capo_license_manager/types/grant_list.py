"""Generated from Smithy shape ``com.amazonaws.licensemanager#GrantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.grant

GrantList: TypeAlias = list["capo_license_manager.types.grant.Grant"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantList) -> list:
    import capo_license_manager.types.grant

    out: list = []
    for item in value:
        out.append(capo_license_manager.types.grant.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GrantList:
    import capo_license_manager.types.grant

    out: GrantList = []
    for item in data:
        out.append(capo_license_manager.types.grant.deserialize_aws_json_1_1(item))
    return out
