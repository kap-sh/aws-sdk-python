"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#Fqns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.fully_qualified_name

Fqns: TypeAlias = list[
    "capo_iotfleetwise.types.fully_qualified_name.FullyQualifiedName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Fqns) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Fqns:
    return list(data)
