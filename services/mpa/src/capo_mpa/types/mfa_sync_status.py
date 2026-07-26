"""Generated from Smithy shape ``com.amazonaws.mpa#MfaSyncStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Indicates if the approver's MFA device is in-sync with the Identity Source</p> <ul> <li> <p> <code>IN_SYNC</code>: The approver's MFA device is in-sync with the Identity Source</p> </li> <li> <p> <code>OUT_OF_SYNC</code>: The approver's MFA device is out-of-sync with the Identity Source</p> </li> </ul>"""
MfaSyncStatus: TypeAlias = Literal[
    "IN_SYNC",
    "OUT_OF_SYNC",
]


# --- restJson1 ser/de ---
def serialize_json(value: MfaSyncStatus) -> str:
    return value


def deserialize_json(data: str) -> MfaSyncStatus:
    return cast(MfaSyncStatus, data)
