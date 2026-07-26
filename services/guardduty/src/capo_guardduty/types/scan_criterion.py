"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanCriterion``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.scan_condition
    import capo_guardduty.types.scan_criterion_key

ScanCriterion: TypeAlias = dict[
    "capo_guardduty.types.scan_criterion_key.ScanCriterionKey",
    "capo_guardduty.types.scan_condition.ScanCondition",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ScanCriterion) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_guardduty.types.scan_condition
        import capo_guardduty.types.scan_criterion_key

        out[capo_guardduty.types.scan_criterion_key.serialize_json(key)] = (
            capo_guardduty.types.scan_condition.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> ScanCriterion:
    out: ScanCriterion = {}
    for key, value in data.items():
        import capo_guardduty.types.scan_condition
        import capo_guardduty.types.scan_criterion_key

        out[capo_guardduty.types.scan_criterion_key.deserialize_json(key)] = (
            capo_guardduty.types.scan_condition.deserialize_json(value)
        )
    return out
