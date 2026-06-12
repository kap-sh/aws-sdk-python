"""Generated from Smithy shape ``com.amazonaws.configservice#EvaluationModeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.evaluation_mode


class EvaluationModeConfiguration(TypedDict):
    mode: NotRequired["aws_sdk_config_service.types.evaluation_mode.EvaluationMode"]
    """<p>The mode of an evaluation. The valid values are Detective or Proactive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationModeConfiguration) -> dict:
    out: dict = {}
    if "mode" in value:
        import aws_sdk_config_service.types.evaluation_mode

        out["Mode"] = (
            aws_sdk_config_service.types.evaluation_mode.serialize_aws_json_1_1(
                value["mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationModeConfiguration:
    out: EvaluationModeConfiguration = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        import aws_sdk_config_service.types.evaluation_mode

        out["mode"] = (
            aws_sdk_config_service.types.evaluation_mode.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    return out
