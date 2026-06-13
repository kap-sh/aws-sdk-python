"""Generated from Smithy shape ``com.amazonaws.s3files#ExpirationDataRule``."""

from typing import TypedDict

from aws_sdk_s3files.errors import DeserializationError


class ExpirationDataRule(TypedDict):
    days_after_last_access: "int"
    """<p>The number of days after last access before cached data expires from the file system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExpirationDataRule) -> dict:
    out: dict = {}
    out["daysAfterLastAccess"] = value["days_after_last_access"]
    return out


def deserialize_json(data: dict) -> ExpirationDataRule:
    out: ExpirationDataRule = {}  # type: ignore[typeddict-item]
    if "daysAfterLastAccess" in data:
        out["days_after_last_access"] = data["daysAfterLastAccess"]
    else:
        raise DeserializationError("ExpirationDataRule.days_after_last_access required")
    return out
