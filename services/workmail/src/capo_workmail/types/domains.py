"""Generated from Smithy shape ``com.amazonaws.workmail#Domains``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.domain

Domains: TypeAlias = list["capo_workmail.types.domain.Domain"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Domains) -> list:
    import capo_workmail.types.domain

    out: list = []
    for item in value:
        out.append(capo_workmail.types.domain.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Domains:
    import capo_workmail.types.domain

    out: Domains = []
    for item in data:
        out.append(capo_workmail.types.domain.deserialize_aws_json_1_1(item))
    return out
