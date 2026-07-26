"""Generated from Smithy shape ``com.amazonaws.codecommit#GetRepositoryTriggersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.repository_triggers_configuration_id
    import capo_codecommit.types.repository_triggers_list


class GetRepositoryTriggersOutput(TypedDict, closed=True):
    configuration_id: NotRequired[
        "capo_codecommit.types.repository_triggers_configuration_id.RepositoryTriggersConfigurationId"
    ]
    """<p>The system-generated unique ID for the trigger.</p>"""
    triggers: NotRequired[
        "capo_codecommit.types.repository_triggers_list.RepositoryTriggersList"
    ]
    """<p>The JSON block of configuration information for each trigger.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRepositoryTriggersOutput) -> dict:
    out: dict = {}
    if "configuration_id" in value:
        out["configurationId"] = value["configuration_id"]
    if "triggers" in value:
        import capo_codecommit.types.repository_triggers_list

        out["triggers"] = (
            capo_codecommit.types.repository_triggers_list.serialize_aws_json_1_1(
                value["triggers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRepositoryTriggersOutput:
    out: GetRepositoryTriggersOutput = {}  # type: ignore[typeddict-item]
    if "configurationId" in data:
        out["configuration_id"] = data["configurationId"]
    if "triggers" in data:
        import capo_codecommit.types.repository_triggers_list

        out["triggers"] = (
            capo_codecommit.types.repository_triggers_list.deserialize_aws_json_1_1(
                data["triggers"]
            )
        )
    return out
