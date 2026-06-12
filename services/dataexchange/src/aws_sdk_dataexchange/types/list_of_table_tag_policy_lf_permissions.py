"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfTableTagPolicyLFPermissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.table_tag_policy_lf_permission

ListOfTableTagPolicyLFPermissions: TypeAlias = list[
    "aws_sdk_dataexchange.types.table_tag_policy_lf_permission.TableTagPolicyLFPermission"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfTableTagPolicyLFPermissions) -> list:
    return list(value)


def deserialize_json(data: list) -> ListOfTableTagPolicyLFPermissions:
    return list(data)
