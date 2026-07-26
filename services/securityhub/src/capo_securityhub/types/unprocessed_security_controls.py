"""Generated from Smithy shape ``com.amazonaws.securityhub#UnprocessedSecurityControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.unprocessed_security_control

UnprocessedSecurityControls: TypeAlias = list[
    "capo_securityhub.types.unprocessed_security_control.UnprocessedSecurityControl"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedSecurityControls) -> list:
    import capo_securityhub.types.unprocessed_security_control

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.unprocessed_security_control.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UnprocessedSecurityControls:
    import capo_securityhub.types.unprocessed_security_control

    out: UnprocessedSecurityControls = []
    for item in data:
        out.append(
            capo_securityhub.types.unprocessed_security_control.deserialize_json(item)
        )
    return out
