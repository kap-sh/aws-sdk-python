"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageDeclaration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.before_entry_conditions
    import capo_codepipeline.types.failure_conditions
    import capo_codepipeline.types.stage_action_declaration_list
    import capo_codepipeline.types.stage_blocker_declaration_list
    import capo_codepipeline.types.stage_name
    import capo_codepipeline.types.success_conditions


class StageDeclaration(TypedDict, closed=True):
    name: "capo_codepipeline.types.stage_name.StageName"
    """<p>The name of the stage.</p>"""
    blockers: NotRequired[
        "capo_codepipeline.types.stage_blocker_declaration_list.StageBlockerDeclarationList"
    ]
    """<p>Reserved for future use.</p>"""
    actions: "capo_codepipeline.types.stage_action_declaration_list.StageActionDeclarationList"
    """<p>The actions included in a stage.</p>"""
    on_failure: NotRequired[
        "capo_codepipeline.types.failure_conditions.FailureConditions"
    ]
    """<p>The method to use when a stage has not completed successfully. For example, configuring this field for rollback will roll back a failed stage automatically to the last successful pipeline execution in the stage.</p>"""
    on_success: NotRequired[
        "capo_codepipeline.types.success_conditions.SuccessConditions"
    ]
    """<p>The method to use when a stage has succeeded. For example, configuring this field for conditions will allow the stage to succeed when the conditions are met.</p>"""
    before_entry: NotRequired[
        "capo_codepipeline.types.before_entry_conditions.BeforeEntryConditions"
    ]
    """<p>The method to use when a stage allows entry. For example, configuring this field for conditions will allow entry to the stage when the conditions are met.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageDeclaration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "blockers" in value:
        import capo_codepipeline.types.stage_blocker_declaration_list

        out["blockers"] = (
            capo_codepipeline.types.stage_blocker_declaration_list.serialize_aws_json_1_1(
                value["blockers"]
            )
        )
    import capo_codepipeline.types.stage_action_declaration_list

    out["actions"] = (
        capo_codepipeline.types.stage_action_declaration_list.serialize_aws_json_1_1(
            value["actions"]
        )
    )
    if "on_failure" in value:
        import capo_codepipeline.types.failure_conditions

        out["onFailure"] = (
            capo_codepipeline.types.failure_conditions.serialize_aws_json_1_1(
                value["on_failure"]
            )
        )
    if "on_success" in value:
        import capo_codepipeline.types.success_conditions

        out["onSuccess"] = (
            capo_codepipeline.types.success_conditions.serialize_aws_json_1_1(
                value["on_success"]
            )
        )
    if "before_entry" in value:
        import capo_codepipeline.types.before_entry_conditions

        out["beforeEntry"] = (
            capo_codepipeline.types.before_entry_conditions.serialize_aws_json_1_1(
                value["before_entry"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StageDeclaration:
    out: StageDeclaration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StageDeclaration.name required")
    if "blockers" in data:
        import capo_codepipeline.types.stage_blocker_declaration_list

        out["blockers"] = (
            capo_codepipeline.types.stage_blocker_declaration_list.deserialize_aws_json_1_1(
                data["blockers"]
            )
        )
    if "actions" in data:
        import capo_codepipeline.types.stage_action_declaration_list

        out["actions"] = (
            capo_codepipeline.types.stage_action_declaration_list.deserialize_aws_json_1_1(
                data["actions"]
            )
        )
    else:
        raise DeserializationError("StageDeclaration.actions required")
    if "onFailure" in data:
        import capo_codepipeline.types.failure_conditions

        out["on_failure"] = (
            capo_codepipeline.types.failure_conditions.deserialize_aws_json_1_1(
                data["onFailure"]
            )
        )
    if "onSuccess" in data:
        import capo_codepipeline.types.success_conditions

        out["on_success"] = (
            capo_codepipeline.types.success_conditions.deserialize_aws_json_1_1(
                data["onSuccess"]
            )
        )
    if "beforeEntry" in data:
        import capo_codepipeline.types.before_entry_conditions

        out["before_entry"] = (
            capo_codepipeline.types.before_entry_conditions.deserialize_aws_json_1_1(
                data["beforeEntry"]
            )
        )
    return out
