"""Generated from Smithy shape ``com.amazonaws.kms#GetKeyLastUsageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kms.types.date_type
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.key_last_usage_data


class GetKeyLastUsageResponse(TypedDict, closed=True):
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The globally unique identifier for the KMS key.</p>"""
    key_last_usage: NotRequired[
        "aws_sdk_kms.types.key_last_usage_data.KeyLastUsageData"
    ]
    """<p>Contains usage information about the last time the KMS key was used for a successful cryptographic operation. If the key has not been used since tracking began, this response element is empty.</p>"""
    tracking_start_date: NotRequired["aws_sdk_kms.types.date_type.DateType"]
    """<p>The date from which KMS began recording cryptographic activity for this key, or the date the KMS key was created, whichever is later.</p>"""
    key_creation_date: NotRequired["aws_sdk_kms.types.date_type.DateType"]
    """<p>The date and time when the KMS key was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetKeyLastUsageResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "key_last_usage" in value:
        import aws_sdk_kms.types.key_last_usage_data

        out["KeyLastUsage"] = (
            aws_sdk_kms.types.key_last_usage_data.serialize_aws_json_1_1(
                value["key_last_usage"]
            )
        )
    if "tracking_start_date" in value:
        import aws_sdk_kms.types.date_type

        out["TrackingStartDate"] = aws_sdk_kms.types.date_type.serialize_aws_json_1_1(
            value["tracking_start_date"]
        )
    if "key_creation_date" in value:
        import aws_sdk_kms.types.date_type

        out["KeyCreationDate"] = aws_sdk_kms.types.date_type.serialize_aws_json_1_1(
            value["key_creation_date"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetKeyLastUsageResponse:
    out: GetKeyLastUsageResponse = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "KeyLastUsage" in data:
        import aws_sdk_kms.types.key_last_usage_data

        out["key_last_usage"] = (
            aws_sdk_kms.types.key_last_usage_data.deserialize_aws_json_1_1(
                data["KeyLastUsage"]
            )
        )
    if "TrackingStartDate" in data:
        import aws_sdk_kms.types.date_type

        out["tracking_start_date"] = (
            aws_sdk_kms.types.date_type.deserialize_aws_json_1_1(
                data["TrackingStartDate"]
            )
        )
    if "KeyCreationDate" in data:
        import aws_sdk_kms.types.date_type

        out["key_creation_date"] = aws_sdk_kms.types.date_type.deserialize_aws_json_1_1(
            data["KeyCreationDate"]
        )
    return out
