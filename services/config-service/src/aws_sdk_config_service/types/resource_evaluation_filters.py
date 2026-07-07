"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceEvaluationFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.evaluation_context_identifier
    import aws_sdk_config_service.types.evaluation_mode
    import aws_sdk_config_service.types.time_window


class ResourceEvaluationFilters(TypedDict, closed=True):
    evaluation_mode: NotRequired[
        "aws_sdk_config_service.types.evaluation_mode.EvaluationMode"
    ]
    """<p>Filters all resource evaluations results based on an evaluation mode.</p> <important> <p>Currently, <code>DECTECTIVE</code> is not supported as a valid value. Ignore other documentation stating otherwise.</p> </important>"""
    time_window: NotRequired["aws_sdk_config_service.types.time_window.TimeWindow"]
    """<p>Returns a <code>TimeWindow</code> object.</p>"""
    evaluation_context_identifier: NotRequired[
        "aws_sdk_config_service.types.evaluation_context_identifier.EvaluationContextIdentifier"
    ]
    """<p>Filters evaluations for a given infrastructure deployment. For example: CFN Stack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceEvaluationFilters) -> dict:
    out: dict = {}
    if "evaluation_mode" in value:
        import aws_sdk_config_service.types.evaluation_mode

        out["EvaluationMode"] = (
            aws_sdk_config_service.types.evaluation_mode.serialize_aws_json_1_1(
                value["evaluation_mode"]
            )
        )
    if "time_window" in value:
        import aws_sdk_config_service.types.time_window

        out["TimeWindow"] = (
            aws_sdk_config_service.types.time_window.serialize_aws_json_1_1(
                value["time_window"]
            )
        )
    if "evaluation_context_identifier" in value:
        out["EvaluationContextIdentifier"] = value["evaluation_context_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceEvaluationFilters:
    out: ResourceEvaluationFilters = {}  # type: ignore[typeddict-item]
    if "EvaluationMode" in data:
        import aws_sdk_config_service.types.evaluation_mode

        out["evaluation_mode"] = (
            aws_sdk_config_service.types.evaluation_mode.deserialize_aws_json_1_1(
                data["EvaluationMode"]
            )
        )
    if "TimeWindow" in data:
        import aws_sdk_config_service.types.time_window

        out["time_window"] = (
            aws_sdk_config_service.types.time_window.deserialize_aws_json_1_1(
                data["TimeWindow"]
            )
        )
    if "EvaluationContextIdentifier" in data:
        out["evaluation_context_identifier"] = data["EvaluationContextIdentifier"]
    return out
