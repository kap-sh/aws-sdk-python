"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanExtension``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.availability_zone_id
    import aws_sdk_sagemaker.types.currency_code
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.training_plan_extension_duration_hours
    import aws_sdk_sagemaker.types.training_plan_extension_offering_id


class TrainingPlanExtension(TypedDict):
    training_plan_extension_offering_id: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_extension_offering_id.TrainingPlanExtensionOfferingId"
    ]
    """<p>The unique identifier of the extension offering that was used to create this extension.</p>"""
    extended_at: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp when the extension was created.</p>"""
    start_date: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The start date of the extension period.</p>"""
    end_date: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The end date of the extension period.</p>"""
    status: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The current status of the extension (e.g., Pending, Active, Scheduled, Failed, Expired).</p>"""
    payment_status: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The payment processing status of the extension.</p>"""
    availability_zone: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The Availability Zone of the extension.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_sagemaker.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The Availability Zone ID of the extension.</p>"""
    duration_hours: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_extension_duration_hours.TrainingPlanExtensionDurationHours"
    ]
    """<p>The duration of the extension in hours.</p>"""
    upfront_fee: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The upfront fee for the extension.</p>"""
    currency_code: NotRequired["aws_sdk_sagemaker.types.currency_code.CurrencyCode"]
    """<p>The currency code for the upfront fee (e.g., USD).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanExtension) -> dict:
    out: dict = {}
    if "training_plan_extension_offering_id" in value:
        out["TrainingPlanExtensionOfferingId"] = value[
            "training_plan_extension_offering_id"
        ]
    if "extended_at" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["ExtendedAt"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["extended_at"]
        )
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
    if "status" in value:
        out["Status"] = value["status"]
    if "payment_status" in value:
        out["PaymentStatus"] = value["payment_status"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    if "duration_hours" in value:
        out["DurationHours"] = value["duration_hours"]
    if "upfront_fee" in value:
        out["UpfrontFee"] = value["upfront_fee"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingPlanExtension:
    out: TrainingPlanExtension = {}  # type: ignore[typeddict-item]
    if "TrainingPlanExtensionOfferingId" in data:
        out["training_plan_extension_offering_id"] = data[
            "TrainingPlanExtensionOfferingId"
        ]
    if "ExtendedAt" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["extended_at"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["ExtendedAt"]
        )
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
    if "Status" in data:
        out["status"] = data["Status"]
    if "PaymentStatus" in data:
        out["payment_status"] = data["PaymentStatus"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "AvailabilityZoneId" in data:
        out["availability_zone_id"] = data["AvailabilityZoneId"]
    if "DurationHours" in data:
        out["duration_hours"] = data["DurationHours"]
    if "UpfrontFee" in data:
        out["upfront_fee"] = data["UpfrontFee"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    return out
