"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.variant_status
    import aws_sdk_sagemaker.types.variant_status_message


class ProductionVariantStatus(TypedDict, closed=True):
    status: NotRequired["aws_sdk_sagemaker.types.variant_status.VariantStatus"]
    """<p>The endpoint variant status which describes the current deployment stage status or operational status.</p> <ul> <li> <p> <code>Creating</code>: Creating inference resources for the production variant.</p> </li> <li> <p> <code>Deleting</code>: Terminating inference resources for the production variant.</p> </li> <li> <p> <code>Updating</code>: Updating capacity for the production variant.</p> </li> <li> <p> <code>ActivatingTraffic</code>: Turning on traffic for the production variant.</p> </li> <li> <p> <code>Baking</code>: Waiting period to monitor the CloudWatch alarms in the automatic rollback configuration.</p> </li> </ul>"""
    status_message: NotRequired[
        "aws_sdk_sagemaker.types.variant_status_message.VariantStatusMessage"
    ]
    """<p>A message that describes the status of the production variant.</p>"""
    start_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The start time of the current status change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductionVariantStatus) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sagemaker.types.variant_status

        out["Status"] = aws_sdk_sagemaker.types.variant_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "start_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["StartTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductionVariantStatus:
    out: ProductionVariantStatus = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sagemaker.types.variant_status

        out["status"] = aws_sdk_sagemaker.types.variant_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "StartTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["start_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    return out
