"""Generated from Smithy shape ``com.amazonaws.devopsagent#MonitorAccountType``."""

from typing import Literal, TypeAlias, cast

"""<p>AWS association type for monitoring account.</p>"""
MonitorAccountType: TypeAlias = Literal["monitor",]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorAccountType) -> str:
    return value


def deserialize_json(data: str) -> MonitorAccountType:
    return cast(MonitorAccountType, data)
