"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrafficPattern``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.phases
    import capo_sagemaker.types.stairs
    import capo_sagemaker.types.traffic_type


class TrafficPattern(TypedDict, closed=True):
    traffic_type: NotRequired["capo_sagemaker.types.traffic_type.TrafficType"]
    """<p>Defines the traffic patterns. Choose either <code>PHASES</code> or <code>STAIRS</code>.</p>"""
    phases: NotRequired["capo_sagemaker.types.phases.Phases"]
    """<p>Defines the phases traffic specification.</p>"""
    stairs: NotRequired["capo_sagemaker.types.stairs.Stairs"]
    """<p>Defines the stairs traffic pattern.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrafficPattern) -> dict:
    out: dict = {}
    if "traffic_type" in value:
        import capo_sagemaker.types.traffic_type

        out["TrafficType"] = capo_sagemaker.types.traffic_type.serialize_aws_json_1_1(
            value["traffic_type"]
        )
    if "phases" in value:
        import capo_sagemaker.types.phases

        out["Phases"] = capo_sagemaker.types.phases.serialize_aws_json_1_1(
            value["phases"]
        )
    if "stairs" in value:
        import capo_sagemaker.types.stairs

        out["Stairs"] = capo_sagemaker.types.stairs.serialize_aws_json_1_1(
            value["stairs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrafficPattern:
    out: TrafficPattern = {}  # type: ignore[typeddict-item]
    if "TrafficType" in data:
        import capo_sagemaker.types.traffic_type

        out["traffic_type"] = (
            capo_sagemaker.types.traffic_type.deserialize_aws_json_1_1(
                data["TrafficType"]
            )
        )
    if "Phases" in data:
        import capo_sagemaker.types.phases

        out["phases"] = capo_sagemaker.types.phases.deserialize_aws_json_1_1(
            data["Phases"]
        )
    if "Stairs" in data:
        import capo_sagemaker.types.stairs

        out["stairs"] = capo_sagemaker.types.stairs.deserialize_aws_json_1_1(
            data["Stairs"]
        )
    return out
