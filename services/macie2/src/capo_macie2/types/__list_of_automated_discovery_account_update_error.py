"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfAutomatedDiscoveryAccountUpdateError``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.automated_discovery_account_update_error

__listOfAutomatedDiscoveryAccountUpdateError: TypeAlias = list[
    "capo_macie2.types.automated_discovery_account_update_error.AutomatedDiscoveryAccountUpdateError"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAutomatedDiscoveryAccountUpdateError) -> list:
    import capo_macie2.types.automated_discovery_account_update_error

    out: list = []
    for item in value:
        out.append(
            capo_macie2.types.automated_discovery_account_update_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfAutomatedDiscoveryAccountUpdateError:
    import capo_macie2.types.automated_discovery_account_update_error

    out: __listOfAutomatedDiscoveryAccountUpdateError = []
    for item in data:
        out.append(
            capo_macie2.types.automated_discovery_account_update_error.deserialize_json(
                item
            )
        )
    return out
