"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#LastAuditTimestamp``."""

import datetime
from typing import TypeAlias

"""<p>The time that a recovery group was last assessed for recommendations, in UTC ISO-8601 format.</p>"""
LastAuditTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastAuditTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> LastAuditTimestamp:
    return datetime.datetime.fromisoformat(data)
