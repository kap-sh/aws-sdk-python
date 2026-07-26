"""Generated from Smithy shape ``com.amazonaws.ssoadmin#Grants``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso_admin.types.grant_item

Grants: TypeAlias = list["capo_sso_admin.types.grant_item.GrantItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Grants) -> list:
    import capo_sso_admin.types.grant_item

    out: list = []
    for item in value:
        out.append(capo_sso_admin.types.grant_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Grants:
    import capo_sso_admin.types.grant_item

    out: Grants = []
    for item in data:
        out.append(capo_sso_admin.types.grant_item.deserialize_aws_json_1_1(item))
    return out
