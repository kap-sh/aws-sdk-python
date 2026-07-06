"""Generated from Smithy shape ``com.amazonaws.fms#EntryViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.entries_with_conflicts
    import aws_sdk_fms.types.entry_description
    import aws_sdk_fms.types.entry_violation_reasons
    import aws_sdk_fms.types.length_bounded_string


class EntryViolation(TypedDict, closed=True):
    expected_entry: NotRequired["aws_sdk_fms.types.entry_description.EntryDescription"]
    """<p>The Firewall Manager-managed network ACL entry that is involved in the entry violation. </p>"""
    expected_evaluation_order: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The evaluation location within the ordered list of entries where the <code>ExpectedEntry</code> should be, according to the network ACL policy specifications. </p>"""
    actual_evaluation_order: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The evaluation location within the ordered list of entries where the <code>ExpectedEntry</code> is currently located. </p>"""
    entry_at_expected_evaluation_order: NotRequired[
        "aws_sdk_fms.types.entry_description.EntryDescription"
    ]
    """<p>The entry that's currently in the <code>ExpectedEvaluationOrder</code> location, in place of the expected entry. </p>"""
    entries_with_conflicts: NotRequired[
        "aws_sdk_fms.types.entries_with_conflicts.EntriesWithConflicts"
    ]
    """<p>The list of entries that are in conflict with <code>ExpectedEntry</code>. </p>"""
    entry_violation_reasons: NotRequired[
        "aws_sdk_fms.types.entry_violation_reasons.EntryViolationReasons"
    ]
    """<p>Descriptions of the violations that Firewall Manager found for these entries. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntryViolation) -> dict:
    out: dict = {}
    if "expected_entry" in value:
        import aws_sdk_fms.types.entry_description

        out["ExpectedEntry"] = (
            aws_sdk_fms.types.entry_description.serialize_aws_json_1_1(
                value["expected_entry"]
            )
        )
    if "expected_evaluation_order" in value:
        out["ExpectedEvaluationOrder"] = value["expected_evaluation_order"]
    if "actual_evaluation_order" in value:
        out["ActualEvaluationOrder"] = value["actual_evaluation_order"]
    if "entry_at_expected_evaluation_order" in value:
        import aws_sdk_fms.types.entry_description

        out["EntryAtExpectedEvaluationOrder"] = (
            aws_sdk_fms.types.entry_description.serialize_aws_json_1_1(
                value["entry_at_expected_evaluation_order"]
            )
        )
    if "entries_with_conflicts" in value:
        import aws_sdk_fms.types.entries_with_conflicts

        out["EntriesWithConflicts"] = (
            aws_sdk_fms.types.entries_with_conflicts.serialize_aws_json_1_1(
                value["entries_with_conflicts"]
            )
        )
    if "entry_violation_reasons" in value:
        import aws_sdk_fms.types.entry_violation_reasons

        out["EntryViolationReasons"] = (
            aws_sdk_fms.types.entry_violation_reasons.serialize_aws_json_1_1(
                value["entry_violation_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntryViolation:
    out: EntryViolation = {}  # type: ignore[typeddict-item]
    if "ExpectedEntry" in data:
        import aws_sdk_fms.types.entry_description

        out["expected_entry"] = (
            aws_sdk_fms.types.entry_description.deserialize_aws_json_1_1(
                data["ExpectedEntry"]
            )
        )
    if "ExpectedEvaluationOrder" in data:
        out["expected_evaluation_order"] = data["ExpectedEvaluationOrder"]
    if "ActualEvaluationOrder" in data:
        out["actual_evaluation_order"] = data["ActualEvaluationOrder"]
    if "EntryAtExpectedEvaluationOrder" in data:
        import aws_sdk_fms.types.entry_description

        out["entry_at_expected_evaluation_order"] = (
            aws_sdk_fms.types.entry_description.deserialize_aws_json_1_1(
                data["EntryAtExpectedEvaluationOrder"]
            )
        )
    if "EntriesWithConflicts" in data:
        import aws_sdk_fms.types.entries_with_conflicts

        out["entries_with_conflicts"] = (
            aws_sdk_fms.types.entries_with_conflicts.deserialize_aws_json_1_1(
                data["EntriesWithConflicts"]
            )
        )
    if "EntryViolationReasons" in data:
        import aws_sdk_fms.types.entry_violation_reasons

        out["entry_violation_reasons"] = (
            aws_sdk_fms.types.entry_violation_reasons.deserialize_aws_json_1_1(
                data["EntryViolationReasons"]
            )
        )
    return out
