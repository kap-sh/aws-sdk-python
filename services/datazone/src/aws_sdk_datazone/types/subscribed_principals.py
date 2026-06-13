"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedPrincipals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.subscribed_principal

SubscribedPrincipals: TypeAlias = list[
    "aws_sdk_datazone.types.subscribed_principal.SubscribedPrincipal"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedPrincipals) -> list:
    import aws_sdk_datazone.types.subscribed_principal

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.subscribed_principal.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubscribedPrincipals:
    import aws_sdk_datazone.types.subscribed_principal

    out: SubscribedPrincipals = []
    for item in data:
        out.append(aws_sdk_datazone.types.subscribed_principal.deserialize_json(item))
    return out
