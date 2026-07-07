"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanExtensionOffering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.currency_code
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.training_plan_extension_duration_hours
    import aws_sdk_sagemaker.types.training_plan_extension_offering_id


class TrainingPlanExtensionOffering(TypedDict, closed=True):
    training_plan_extension_offering_id: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_extension_offering_id.TrainingPlanExtensionOfferingId"
    ]
    """<p>The unique identifier for this extension offering.</p>"""
    availability_zone: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The Availability Zone for this extension offering.</p>"""
    start_date: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The start date of this extension offering.</p>"""
    end_date: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The end date of this extension offering.</p>"""
    duration_hours: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_extension_duration_hours.TrainingPlanExtensionDurationHours"
    ]
    """<p>The duration of this extension offering in hours.</p>"""
    upfront_fee: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The upfront fee for this extension offering.</p>"""
    currency_code: NotRequired["aws_sdk_sagemaker.types.currency_code.CurrencyCode"]
    """<p>The currency code for the upfront fee (e.g., USD).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanExtensionOffering) -> dict:
    out: dict = {}
    if "training_plan_extension_offering_id" in value:
        out["TrainingPlanExtensionOfferingId"] = value[
            "training_plan_extension_offering_id"
        ]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "start_date" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["StartDate"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_date"]
        )
    if "end_date" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["EndDate"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_date"]
        )
    if "duration_hours" in value:
        out["DurationHours"] = value["duration_hours"]
    if "upfront_fee" in value:
        out["UpfrontFee"] = value["upfront_fee"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingPlanExtensionOffering:
    out: TrainingPlanExtensionOffering = {}  # type: ignore[typeddict-item]
    if "TrainingPlanExtensionOfferingId" in data:
        out["training_plan_extension_offering_id"] = data[
            "TrainingPlanExtensionOfferingId"
        ]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "StartDate" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["start_date"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartDate"]
        )
    if "EndDate" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["end_date"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndDate"]
        )
    if "DurationHours" in data:
        out["duration_hours"] = data["DurationHours"]
    if "UpfrontFee" in data:
        out["upfront_fee"] = data["UpfrontFee"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    return out
