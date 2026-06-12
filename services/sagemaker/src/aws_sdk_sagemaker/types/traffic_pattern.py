"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrafficPattern``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.phases
    import aws_sdk_sagemaker.types.stairs
    import aws_sdk_sagemaker.types.traffic_type


class TrafficPattern(TypedDict):
    traffic_type: NotRequired["aws_sdk_sagemaker.types.traffic_type.TrafficType"]
    """<p>Defines the traffic patterns. Choose either <code>PHASES</code> or <code>STAIRS</code>.</p>"""
    phases: NotRequired["aws_sdk_sagemaker.types.phases.Phases"]
    """<p>Defines the phases traffic specification.</p>"""
    stairs: NotRequired["aws_sdk_sagemaker.types.stairs.Stairs"]
    """<p>Defines the stairs traffic pattern.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrafficPattern) -> dict:
    out: dict = {}
    if "traffic_type" in value:
        import aws_sdk_sagemaker.types.traffic_type

        out["TrafficType"] = (
            aws_sdk_sagemaker.types.traffic_type.serialize_aws_json_1_1(
                value["traffic_type"]
            )
        )
    if "phases" in value:
        import aws_sdk_sagemaker.types.phases

        out["Phases"] = aws_sdk_sagemaker.types.phases.serialize_aws_json_1_1(
            value["phases"]
        )
    if "stairs" in value:
        import aws_sdk_sagemaker.types.stairs

        out["Stairs"] = aws_sdk_sagemaker.types.stairs.serialize_aws_json_1_1(
            value["stairs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrafficPattern:
    out: TrafficPattern = {}  # type: ignore[typeddict-item]
    if "TrafficType" in data:
        import aws_sdk_sagemaker.types.traffic_type

        out["traffic_type"] = (
            aws_sdk_sagemaker.types.traffic_type.deserialize_aws_json_1_1(
                data["TrafficType"]
            )
        )
    if "Phases" in data:
        import aws_sdk_sagemaker.types.phases

        out["phases"] = aws_sdk_sagemaker.types.phases.deserialize_aws_json_1_1(
            data["Phases"]
        )
    if "Stairs" in data:
        import aws_sdk_sagemaker.types.stairs

        out["stairs"] = aws_sdk_sagemaker.types.stairs.deserialize_aws_json_1_1(
            data["Stairs"]
        )
    return out
