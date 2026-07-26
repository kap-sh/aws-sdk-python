"""Generated from Smithy shape ``com.amazonaws.organizations#Parents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.parent

Parents: TypeAlias = list["capo_organizations.types.parent.Parent"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Parents) -> list:
    import capo_organizations.types.parent

    out: list = []
    for item in value:
        out.append(capo_organizations.types.parent.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Parents:
    import capo_organizations.types.parent

    out: Parents = []
    for item in data:
        out.append(capo_organizations.types.parent.deserialize_aws_json_1_1(item))
    return out
