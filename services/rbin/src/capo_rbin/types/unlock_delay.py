"""Generated from Smithy shape ``com.amazonaws.rbin#UnlockDelay``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rbin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rbin.types.unlock_delay_unit
    import capo_rbin.types.unlock_delay_value


class UnlockDelay(TypedDict, closed=True):
    unlock_delay_value: "capo_rbin.types.unlock_delay_value.UnlockDelayValue"
    """<p>The unlock delay period, measured in the unit specified for <b> UnlockDelayUnit</b>.</p>"""
    unlock_delay_unit: "capo_rbin.types.unlock_delay_unit.UnlockDelayUnit"
    """<p>The unit of time in which to measure the unlock delay. Currently, the unlock delay can be measured only in days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnlockDelay) -> dict:
    out: dict = {}
    out["UnlockDelayValue"] = value["unlock_delay_value"]
    import capo_rbin.types.unlock_delay_unit

    out["UnlockDelayUnit"] = capo_rbin.types.unlock_delay_unit.serialize_json(
        value["unlock_delay_unit"]
    )
    return out


def deserialize_json(data: dict) -> UnlockDelay:
    out: UnlockDelay = {}  # type: ignore[typeddict-item]
    if "UnlockDelayValue" in data:
        out["unlock_delay_value"] = data["UnlockDelayValue"]
    else:
        raise DeserializationError("UnlockDelay.unlock_delay_value required")
    if "UnlockDelayUnit" in data:
        import capo_rbin.types.unlock_delay_unit

        out["unlock_delay_unit"] = capo_rbin.types.unlock_delay_unit.deserialize_json(
            data["UnlockDelayUnit"]
        )
    else:
        raise DeserializationError("UnlockDelay.unlock_delay_unit required")
    return out
