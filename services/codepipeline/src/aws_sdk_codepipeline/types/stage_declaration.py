"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageDeclaration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.before_entry_conditions
    import aws_sdk_codepipeline.types.failure_conditions
    import aws_sdk_codepipeline.types.stage_action_declaration_list
    import aws_sdk_codepipeline.types.stage_blocker_declaration_list
    import aws_sdk_codepipeline.types.stage_name
    import aws_sdk_codepipeline.types.success_conditions


class StageDeclaration(TypedDict):
    name: "aws_sdk_codepipeline.types.stage_name.StageName"
    """<p>The name of the stage.</p>"""
    blockers: NotRequired[
        "aws_sdk_codepipeline.types.stage_blocker_declaration_list.StageBlockerDeclarationList"
    ]
    """<p>Reserved for future use.</p>"""
    actions: "aws_sdk_codepipeline.types.stage_action_declaration_list.StageActionDeclarationList"
    """<p>The actions included in a stage.</p>"""
    on_failure: NotRequired[
        "aws_sdk_codepipeline.types.failure_conditions.FailureConditions"
    ]
    """<p>The method to use when a stage has not completed successfully. For example, configuring this field for rollback will roll back a failed stage automatically to the last successful pipeline execution in the stage.</p>"""
    on_success: NotRequired[
        "aws_sdk_codepipeline.types.success_conditions.SuccessConditions"
    ]
    """<p>The method to use when a stage has succeeded. For example, configuring this field for conditions will allow the stage to succeed when the conditions are met.</p>"""
    before_entry: NotRequired[
        "aws_sdk_codepipeline.types.before_entry_conditions.BeforeEntryConditions"
    ]
    """<p>The method to use when a stage allows entry. For example, configuring this field for conditions will allow entry to the stage when the conditions are met.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageDeclaration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "blockers" in value:
        import aws_sdk_codepipeline.types.stage_blocker_declaration_list

        out["blockers"] = (
            aws_sdk_codepipeline.types.stage_blocker_declaration_list.serialize_aws_json_1_1(
                value["blockers"]
            )
        )
    import aws_sdk_codepipeline.types.stage_action_declaration_list

    out["actions"] = (
        aws_sdk_codepipeline.types.stage_action_declaration_list.serialize_aws_json_1_1(
            value["actions"]
        )
    )
    if "on_failure" in value:
        import aws_sdk_codepipeline.types.failure_conditions

        out["onFailure"] = (
            aws_sdk_codepipeline.types.failure_conditions.serialize_aws_json_1_1(
                value["on_failure"]
            )
        )
    if "on_success" in value:
        import aws_sdk_codepipeline.types.success_conditions

        out["onSuccess"] = (
            aws_sdk_codepipeline.types.success_conditions.serialize_aws_json_1_1(
                value["on_success"]
            )
        )
    if "before_entry" in value:
        import aws_sdk_codepipeline.types.before_entry_conditions

        out["beforeEntry"] = (
            aws_sdk_codepipeline.types.before_entry_conditions.serialize_aws_json_1_1(
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
        import aws_sdk_codepipeline.types.stage_blocker_declaration_list

        out["blockers"] = (
            aws_sdk_codepipeline.types.stage_blocker_declaration_list.deserialize_aws_json_1_1(
                data["blockers"]
            )
        )
    if "actions" in data:
        import aws_sdk_codepipeline.types.stage_action_declaration_list

        out["actions"] = (
            aws_sdk_codepipeline.types.stage_action_declaration_list.deserialize_aws_json_1_1(
                data["actions"]
            )
        )
    else:
        raise DeserializationError("StageDeclaration.actions required")
    if "onFailure" in data:
        import aws_sdk_codepipeline.types.failure_conditions

        out["on_failure"] = (
            aws_sdk_codepipeline.types.failure_conditions.deserialize_aws_json_1_1(
                data["onFailure"]
            )
        )
    if "onSuccess" in data:
        import aws_sdk_codepipeline.types.success_conditions

        out["on_success"] = (
            aws_sdk_codepipeline.types.success_conditions.deserialize_aws_json_1_1(
                data["onSuccess"]
            )
        )
    if "beforeEntry" in data:
        import aws_sdk_codepipeline.types.before_entry_conditions

        out["before_entry"] = (
            aws_sdk_codepipeline.types.before_entry_conditions.deserialize_aws_json_1_1(
                data["beforeEntry"]
            )
        )
    return out
