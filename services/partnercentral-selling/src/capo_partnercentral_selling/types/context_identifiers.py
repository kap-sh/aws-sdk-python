"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ContextIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.context_identifier

ContextIdentifiers: TypeAlias = list[
    "capo_partnercentral_selling.types.context_identifier.ContextIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContextIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ContextIdentifiers:
    return list(data)
