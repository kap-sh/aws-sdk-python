"""Generated from Smithy shape ``com.amazonaws.kms#GetKeyRotationStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.boolean_type
    import aws_sdk_kms.types.date_type
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.rotation_period_in_days_type


class GetKeyRotationStatusResponse(TypedDict):
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
