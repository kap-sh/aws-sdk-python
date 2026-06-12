"""Generated from Smithy shape ``com.amazonaws.sagemaker#Explainability``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.metrics_source


class Explainability(TypedDict):
    report: NotRequired["aws_sdk_sagemaker.types.metrics_source.MetricsSource"]
    """<p>The explainability report for a model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Explainability) -> dict:
    out: dict = {}
    if "report" in value:
        import aws_sdk_sagemaker.types.metrics_source

        out["Report"] = aws_sdk_sagemaker.types.metrics_source.serialize_aws_json_1_1(
            value["report"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Explainability:
    out: Explainability = {}  # type: ignore[typeddict-item]
    if "Report" in data:
        import aws_sdk_sagemaker.types.metrics_source

        out["report"] = aws_sdk_sagemaker.types.metrics_source.deserialize_aws_json_1_1(
            data["Report"]
        )
    return out
