"""Generated from Smithy shape ``com.amazonaws.organizations#Children``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.child

Children: TypeAlias = list["capo_organizations.types.child.Child"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Children) -> list:
    import capo_organizations.types.child

    out: list = []
    for item in value:
        out.append(capo_organizations.types.child.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Children:
    import capo_organizations.types.child

    out: Children = []
    for item in data:
        out.append(capo_organizations.types.child.deserialize_aws_json_1_1(item))
    return out
