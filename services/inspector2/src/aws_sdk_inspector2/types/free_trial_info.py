"""Generated from Smithy shape ``com.amazonaws.inspector2#FreeTrialInfo``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_inspector2.types.free_trial_status
    import aws_sdk_inspector2.types.free_trial_type


class FreeTrialInfo(TypedDict):
    type: "aws_sdk_inspector2.types.free_trial_type.FreeTrialType"
    """<p>The type of scan covered by the Amazon Inspector free trail.</p>"""
    start: "datetime.datetime"
    """<p>The date and time that the Amazon Inspector free trail started for a given account.</p>"""
    end: "datetime.datetime"
    """<p>The date and time that the Amazon Inspector free trail ends for a given account.</p>"""
    status: "aws_sdk_inspector2.types.free_trial_status.FreeTrialStatus"
    """<p>The order to sort results by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialInfo) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    import aws_sdk_inspector2.types._prelude.timestamp

    out["start"] = aws_sdk_inspector2.types._prelude.timestamp.serialize_json(
        value["start"]
    )
    import aws_sdk_inspector2.types._prelude.timestamp

    out["end"] = aws_sdk_inspector2.types._prelude.timestamp.serialize_json(
        value["end"]
    )
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> FreeTrialInfo:
    out: FreeTrialInfo = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("FreeTrialInfo.type required")
    if "start" in data:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["start"] = aws_sdk_inspector2.types._prelude.timestamp.deserialize_json(
            data["start"]
        )
    else:
        raise DeserializationError("FreeTrialInfo.start required")
    if "end" in data:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["end"] = aws_sdk_inspector2.types._prelude.timestamp.deserialize_json(
            data["end"]
        )
    else:
        raise DeserializationError("FreeTrialInfo.end required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("FreeTrialInfo.status required")
    return out
