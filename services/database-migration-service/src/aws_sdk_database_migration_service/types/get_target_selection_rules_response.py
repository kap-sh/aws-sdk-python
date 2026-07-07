"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#GetTargetSelectionRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class GetTargetSelectionRulesResponse(TypedDict, closed=True):
    target_selection_rules: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The JSON string representing the counterpart selection rules in the target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTargetSelectionRulesResponse) -> dict:
    out: dict = {}
    if "target_selection_rules" in value:
        out["TargetSelectionRules"] = value["target_selection_rules"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTargetSelectionRulesResponse:
    out: GetTargetSelectionRulesResponse = {}  # type: ignore[typeddict-item]
    if "TargetSelectionRules" in data:
        out["target_selection_rules"] = data["TargetSelectionRules"]
    return out
