"""Generated from Smithy shape ``com.amazonaws.kms#GetKeyRotationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kms.types.boolean_type
    import aws_sdk_kms.types.date_type
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.rotation_period_in_days_type


class GetKeyRotationStatusResponse(TypedDict, closed=True):
    key_rotation_enabled: "aws_sdk_kms.types.boolean_type.BooleanType"
    """<p>A Boolean value that specifies whether key rotation is enabled.</p>"""
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>Identifies the specified symmetric encryption KMS key.</p>"""
    rotation_period_in_days: NotRequired[
        "aws_sdk_kms.types.rotation_period_in_days_type.RotationPeriodInDaysType"
    ]
    """<p>The number of days between each automatic rotation. The default value is 365 days.</p>"""
    next_rotation_date: NotRequired["aws_sdk_kms.types.date_type.DateType"]
    """<p>The next date that KMS will automatically rotate the key material.</p>"""
    on_demand_rotation_start_date: NotRequired["aws_sdk_kms.types.date_type.DateType"]
    """<p>Identifies the date and time that an in progress on-demand rotation was initiated.</p> <p>KMS uses a background process to perform rotations. As a result, there might be a slight delay between initiating on-demand key rotation and the rotation's completion. Once the on-demand rotation is complete, KMS removes this field from the response. You can use <a>ListKeyRotations</a> to view the details of the completed on-demand rotation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetKeyRotationStatusResponse) -> dict:
    out: dict = {}
    out["KeyRotationEnabled"] = value.get("key_rotation_enabled", False)
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "rotation_period_in_days" in value:
        out["RotationPeriodInDays"] = value["rotation_period_in_days"]
    if "next_rotation_date" in value:
        import aws_sdk_kms.types.date_type

        out["NextRotationDate"] = aws_sdk_kms.types.date_type.serialize_aws_json_1_1(
            value["next_rotation_date"]
        )
    if "on_demand_rotation_start_date" in value:
        import aws_sdk_kms.types.date_type

        out["OnDemandRotationStartDate"] = (
            aws_sdk_kms.types.date_type.serialize_aws_json_1_1(
                value["on_demand_rotation_start_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetKeyRotationStatusResponse:
    out: GetKeyRotationStatusResponse = {}  # type: ignore[typeddict-item]
    if "KeyRotationEnabled" in data:
        out["key_rotation_enabled"] = data["KeyRotationEnabled"]
    else:
        out["key_rotation_enabled"] = False
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "RotationPeriodInDays" in data:
        out["rotation_period_in_days"] = data["RotationPeriodInDays"]
    if "NextRotationDate" in data:
        import aws_sdk_kms.types.date_type

        out["next_rotation_date"] = (
            aws_sdk_kms.types.date_type.deserialize_aws_json_1_1(
                data["NextRotationDate"]
            )
        )
    if "OnDemandRotationStartDate" in data:
        import aws_sdk_kms.types.date_type

        out["on_demand_rotation_start_date"] = (
            aws_sdk_kms.types.date_type.deserialize_aws_json_1_1(
                data["OnDemandRotationStartDate"]
            )
        )
    return out
