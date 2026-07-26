"""Generated from Smithy shape ``com.amazonaws.macie2#AdminStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The current status of an account as the delegated Amazon Macie administrator account for an organization in Organizations. Possible values are:</p>"""
AdminStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLING_IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdminStatus) -> str:
    return value


def deserialize_json(data: str) -> AdminStatus:
    return cast(AdminStatus, data)
