"""Generated from Smithy shape ``com.amazonaws.mpa#UpdateAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

"""<p>Actions that can be taken when updating an approval team</p> <ul> <li> <p> <code>SYNCHRONIZE_MFA_DEVICES</code>: Synchronize MFA devices for all approvers on the team</p> </li> </ul>"""
UpdateAction: TypeAlias = Literal["SYNCHRONIZE_MFA_DEVICES",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SYNCHRONIZE_MFA_DEVICES",))


def serialize_json(value: UpdateAction) -> str:
    return value


def deserialize_json(data: str) -> UpdateAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateAction value: {data!r}")
    return cast(UpdateAction, data)
