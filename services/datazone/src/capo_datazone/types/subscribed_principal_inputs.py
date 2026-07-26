"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedPrincipalInputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.subscribed_principal_input

SubscribedPrincipalInputs: TypeAlias = list[
    "capo_datazone.types.subscribed_principal_input.SubscribedPrincipalInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedPrincipalInputs) -> list:
    import capo_datazone.types.subscribed_principal_input

    out: list = []
    for item in value:
        out.append(capo_datazone.types.subscribed_principal_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubscribedPrincipalInputs:
    import capo_datazone.types.subscribed_principal_input

    out: SubscribedPrincipalInputs = []
    for item in data:
        out.append(
            capo_datazone.types.subscribed_principal_input.deserialize_json(item)
        )
    return out
