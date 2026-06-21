"""Generated from Smithy shape ``com.amazonaws.mpa#UpdateAction``."""

from typing import Literal, TypeAlias, cast

"""<p>Actions that can be taken when updating an approval team</p> <ul> <li> <p> <code>SYNCHRONIZE_MFA_DEVICES</code>: Synchronize MFA devices for all approvers on the team</p> </li> </ul>"""
UpdateAction: TypeAlias = Literal["SYNCHRONIZE_MFA_DEVICES",]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAction) -> str:
    return value


def deserialize_json(data: str) -> UpdateAction:
    return cast(UpdateAction, data)
