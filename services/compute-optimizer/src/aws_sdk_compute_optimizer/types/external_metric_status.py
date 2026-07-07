"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExternalMetricStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.external_metric_status_code
    import aws_sdk_compute_optimizer.types.external_metric_status_reason


class ExternalMetricStatus(TypedDict, closed=True):
    status_code: NotRequired[
        "aws_sdk_compute_optimizer.types.external_metric_status_code.ExternalMetricStatusCode"
    ]
    """<p> The status code for Compute Optimizer's integration with an external metrics provider. </p>"""
    status_reason: NotRequired[
        "aws_sdk_compute_optimizer.types.external_metric_status_reason.ExternalMetricStatusReason"
    ]
    """<p> The reason for Compute Optimizer's integration status with your external metric provider. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExternalMetricStatus) -> dict:
    out: dict = {}
    if "status_code" in value:
        import aws_sdk_compute_optimizer.types.external_metric_status_code

        out["statusCode"] = (
            aws_sdk_compute_optimizer.types.external_metric_status_code.serialize_aws_json_1_0(
                value["status_code"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExternalMetricStatus:
    out: ExternalMetricStatus = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        import aws_sdk_compute_optimizer.types.external_metric_status_code

        out["status_code"] = (
            aws_sdk_compute_optimizer.types.external_metric_status_code.deserialize_aws_json_1_0(
                data["statusCode"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
