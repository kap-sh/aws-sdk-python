"""Generated from Smithy shape ``com.amazonaws.qapps#AppRequiredCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qapps.types.app_required_capability

AppRequiredCapabilities: TypeAlias = list[
    "capo_qapps.types.app_required_capability.AppRequiredCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppRequiredCapabilities) -> list:
    import capo_qapps.types.app_required_capability

    out: list = []
    for item in value:
        out.append(capo_qapps.types.app_required_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppRequiredCapabilities:
    import capo_qapps.types.app_required_capability

    out: AppRequiredCapabilities = []
    for item in data:
        out.append(capo_qapps.types.app_required_capability.deserialize_json(item))
    return out
