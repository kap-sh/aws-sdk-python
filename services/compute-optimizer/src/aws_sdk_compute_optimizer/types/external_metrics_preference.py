"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExternalMetricsPreference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.external_metrics_source


class ExternalMetricsPreference(TypedDict):
    source: NotRequired[
        "aws_sdk_compute_optimizer.types.external_metrics_source.ExternalMetricsSource"
    ]
    """<p> Contains the source options for external metrics preferences. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExternalMetricsPreference) -> dict:
    out: dict = {}
    if "source" in value:
        import aws_sdk_compute_optimizer.types.external_metrics_source

        out["source"] = (
            aws_sdk_compute_optimizer.types.external_metrics_source.serialize_aws_json_1_0(
                value["source"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExternalMetricsPreference:
    out: ExternalMetricsPreference = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import aws_sdk_compute_optimizer.types.external_metrics_source

        out["source"] = (
            aws_sdk_compute_optimizer.types.external_metrics_source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    return out
