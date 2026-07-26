"""Generated from Smithy shape ``com.amazonaws.rbin#LockConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rbin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rbin.types.unlock_delay


class LockConfiguration(TypedDict, closed=True):
    unlock_delay: "capo_rbin.types.unlock_delay.UnlockDelay"
    """<p>Information about the retention rule unlock delay.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LockConfiguration) -> dict:
    out: dict = {}
    import capo_rbin.types.unlock_delay

    out["UnlockDelay"] = capo_rbin.types.unlock_delay.serialize_json(
        value["unlock_delay"]
    )
    return out


def deserialize_json(data: dict) -> LockConfiguration:
    out: LockConfiguration = {}  # type: ignore[typeddict-item]
    if "UnlockDelay" in data:
        import capo_rbin.types.unlock_delay

        out["unlock_delay"] = capo_rbin.types.unlock_delay.deserialize_json(
            data["UnlockDelay"]
        )
    else:
        raise DeserializationError("LockConfiguration.unlock_delay required")
    return out
