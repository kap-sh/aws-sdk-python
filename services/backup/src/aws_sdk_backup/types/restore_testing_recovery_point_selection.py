"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingRecoveryPointSelection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.integer
    import aws_sdk_backup.types.restore_testing_recovery_point_selection_algorithm
    import aws_sdk_backup.types.restore_testing_recovery_point_type_list
    import aws_sdk_backup.types.string_list


class RestoreTestingRecoveryPointSelection(TypedDict):
    algorithm: NotRequired[
        "aws_sdk_backup.types.restore_testing_recovery_point_selection_algorithm.RestoreTestingRecoveryPointSelectionAlgorithm"
    ]
    r"""<p>Acceptable values include \"LATEST_WITHIN_WINDOW\" or \"RANDOM_WITHIN_WINDOW\"</p>"""
    exclude_vaults: NotRequired["aws_sdk_backup.types.string_list.stringList"]
    """<p>Accepted values include specific ARNs or list of selectors. Defaults to empty list if not listed.</p>"""
    include_vaults: NotRequired["aws_sdk_backup.types.string_list.stringList"]
    r"""<p>Accepted values include wildcard [\"*\"] or by specific ARNs or ARN wilcard replacement [\"arn:aws:backup:us-west-2:123456789012:backup-vault:asdf\", ...] [\"arn:aws:backup:*:*:backup-vault:asdf-*\", ...]</p>"""
    recovery_point_types: NotRequired[
        "aws_sdk_backup.types.restore_testing_recovery_point_type_list.RestoreTestingRecoveryPointTypeList"
    ]
    """<p>These are the types of recovery points.</p> <p>Include <code>SNAPSHOT</code> to restore only snapshot recovery points; include <code>CONTINUOUS</code> to restore continuous recovery points (point in time restore / PITR); use both to restore either a snapshot or a continuous recovery point. The recovery point will be determined by the value for <code>Algorithm</code>.</p>"""
    selection_window_days: "aws_sdk_backup.types.integer.integer"
    """<p>Accepted values are integers from 1 to 365.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingRecoveryPointSelection) -> dict:
    out: dict = {}
    if "algorithm" in value:
        import aws_sdk_backup.types.restore_testing_recovery_point_selection_algorithm

        out["Algorithm"] = (
            aws_sdk_backup.types.restore_testing_recovery_point_selection_algorithm.serialize_json(
                value["algorithm"]
            )
        )
    if "exclude_vaults" in value:
        import aws_sdk_backup.types.string_list

        out["ExcludeVaults"] = aws_sdk_backup.types.string_list.serialize_json(
            value["exclude_vaults"]
        )
    if "include_vaults" in value:
        import aws_sdk_backup.types.string_list

        out["IncludeVaults"] = aws_sdk_backup.types.string_list.serialize_json(
            value["include_vaults"]
        )
    if "recovery_point_types" in value:
        import aws_sdk_backup.types.restore_testing_recovery_point_type_list

        out["RecoveryPointTypes"] = (
            aws_sdk_backup.types.restore_testing_recovery_point_type_list.serialize_json(
                value["recovery_point_types"]
            )
        )
    out["SelectionWindowDays"] = value.get("selection_window_days", 0)
    return out


def deserialize_json(data: dict) -> RestoreTestingRecoveryPointSelection:
    out: RestoreTestingRecoveryPointSelection = {}  # type: ignore[typeddict-item]
    if "Algorithm" in data:
        import aws_sdk_backup.types.restore_testing_recovery_point_selection_algorithm

        out["algorithm"] = (
            aws_sdk_backup.types.restore_testing_recovery_point_selection_algorithm.deserialize_json(
                data["Algorithm"]
            )
        )
    if "ExcludeVaults" in data:
        import aws_sdk_backup.types.string_list

        out["exclude_vaults"] = aws_sdk_backup.types.string_list.deserialize_json(
            data["ExcludeVaults"]
        )
    if "IncludeVaults" in data:
        import aws_sdk_backup.types.string_list

        out["include_vaults"] = aws_sdk_backup.types.string_list.deserialize_json(
            data["IncludeVaults"]
        )
    if "RecoveryPointTypes" in data:
        import aws_sdk_backup.types.restore_testing_recovery_point_type_list

        out["recovery_point_types"] = (
            aws_sdk_backup.types.restore_testing_recovery_point_type_list.deserialize_json(
                data["RecoveryPointTypes"]
            )
        )
    if "SelectionWindowDays" in data:
        out["selection_window_days"] = data["SelectionWindowDays"]
    else:
        out["selection_window_days"] = 0
    return out
