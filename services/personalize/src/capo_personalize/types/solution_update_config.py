"""Generated from Smithy shape ``com.amazonaws.personalize#SolutionUpdateConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.auto_training_config
    import capo_personalize.types.events_config


class SolutionUpdateConfig(TypedDict, closed=True):
    auto_training_config: NotRequired[
        "capo_personalize.types.auto_training_config.AutoTrainingConfig"
    ]
    events_config: NotRequired["capo_personalize.types.events_config.EventsConfig"]
    """<p>Describes the configuration of an event, which includes a list of event parameters. You can specify up to 10 event parameters. Events are used in solution creation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SolutionUpdateConfig) -> dict:
    out: dict = {}
    if "auto_training_config" in value:
        import capo_personalize.types.auto_training_config

        out["autoTrainingConfig"] = (
            capo_personalize.types.auto_training_config.serialize_aws_json_1_1(
                value["auto_training_config"]
            )
        )
    if "events_config" in value:
        import capo_personalize.types.events_config

        out["eventsConfig"] = (
            capo_personalize.types.events_config.serialize_aws_json_1_1(
                value["events_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SolutionUpdateConfig:
    out: SolutionUpdateConfig = {}  # type: ignore[typeddict-item]
    if "autoTrainingConfig" in data:
        import capo_personalize.types.auto_training_config

        out["auto_training_config"] = (
            capo_personalize.types.auto_training_config.deserialize_aws_json_1_1(
                data["autoTrainingConfig"]
            )
        )
    if "eventsConfig" in data:
        import capo_personalize.types.events_config

        out["events_config"] = (
            capo_personalize.types.events_config.deserialize_aws_json_1_1(
                data["eventsConfig"]
            )
        )
    return out
