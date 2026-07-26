"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfAutomatedDiscoveryAccount``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.automated_discovery_account

__listOfAutomatedDiscoveryAccount: TypeAlias = list[
    "capo_macie2.types.automated_discovery_account.AutomatedDiscoveryAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAutomatedDiscoveryAccount) -> list:
    import capo_macie2.types.automated_discovery_account

    out: list = []
    for item in value:
        out.append(capo_macie2.types.automated_discovery_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAutomatedDiscoveryAccount:
    import capo_macie2.types.automated_discovery_account

    out: __listOfAutomatedDiscoveryAccount = []
    for item in data:
        out.append(capo_macie2.types.automated_discovery_account.deserialize_json(item))
    return out
