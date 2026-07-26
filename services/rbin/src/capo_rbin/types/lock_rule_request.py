"""Generated from Smithy shape ``com.amazonaws.rbin#LockRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rbin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rbin.types.lock_configuration
    import capo_rbin.types.rule_identifier


class LockRuleRequest(TypedDict, closed=True):
    identifier: "capo_rbin.types.rule_identifier.RuleIdentifier"
    """<p>The unique ID of the retention rule.</p>"""
    lock_configuration: "capo_rbin.types.lock_configuration.LockConfiguration"
    """<p>Information about the retention rule lock configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LockRuleRequest) -> dict:
    out: dict = {}
    import capo_rbin.types.lock_configuration

    out["LockConfiguration"] = capo_rbin.types.lock_configuration.serialize_json(
        value["lock_configuration"]
    )
    return out


def deserialize_json(data: dict) -> LockRuleRequest:
    out: LockRuleRequest = {}  # type: ignore[typeddict-item]
    if "LockConfiguration" in data:
        import capo_rbin.types.lock_configuration

        out["lock_configuration"] = capo_rbin.types.lock_configuration.deserialize_json(
            data["LockConfiguration"]
        )
    else:
        raise DeserializationError("LockRuleRequest.lock_configuration required")
    return out
