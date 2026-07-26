"""Generated from Smithy shape ``com.amazonaws.rum#MetricDestinationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rum.types.destination_arn
    import capo_rum.types.iam_role_arn
    import capo_rum.types.metric_destination


class MetricDestinationSummary(TypedDict, closed=True):
    destination: NotRequired["capo_rum.types.metric_destination.MetricDestination"]
    """<p>Specifies whether the destination is <code>CloudWatch</code> or <code>Evidently</code>.</p>"""
    destination_arn: NotRequired["capo_rum.types.destination_arn.DestinationArn"]
    """<p>If the destination is <code>Evidently</code>, this specifies the ARN of the Evidently experiment that receives the metrics.</p>"""
    iam_role_arn: NotRequired["capo_rum.types.iam_role_arn.IamRoleArn"]
    """<p>This field appears only when the destination is <code>Evidently</code>. It specifies the ARN of the IAM role that is used to write to the Evidently experiment that receives the metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDestinationSummary) -> dict:
    out: dict = {}
    if "destination" in value:
        out["Destination"] = value["destination"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    return out


def deserialize_json(data: dict) -> MetricDestinationSummary:
    out: MetricDestinationSummary = {}  # type: ignore[typeddict-item]
    if "Destination" in data:
        out["destination"] = data["Destination"]
    if "DestinationArn" in data:
        out["destination_arn"] = data["DestinationArn"]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    return out
