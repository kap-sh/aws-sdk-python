"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfAutomatedDiscoveryAccountUpdate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.automated_discovery_account_update

__listOfAutomatedDiscoveryAccountUpdate: TypeAlias = list[
    "aws_sdk_macie2.types.automated_discovery_account_update.AutomatedDiscoveryAccountUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAutomatedDiscoveryAccountUpdate) -> list:
    import aws_sdk_macie2.types.automated_discovery_account_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_macie2.types.automated_discovery_account_update.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfAutomatedDiscoveryAccountUpdate:
    import aws_sdk_macie2.types.automated_discovery_account_update

    out: __listOfAutomatedDiscoveryAccountUpdate = []
    for item in data:
        out.append(
            aws_sdk_macie2.types.automated_discovery_account_update.deserialize_json(
                item
            )
        )
    return out
