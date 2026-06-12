"""Generated from Smithy shape ``com.amazonaws.wafregional#WAFEntityMigrationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_waf_regional.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.error_message
    import aws_sdk_waf_regional.types.error_reason
    import aws_sdk_waf_regional.types.migration_error_type


class WAFEntityMigrationException_(TypedDict):
    message: NotRequired["aws_sdk_waf_regional.types.error_message.errorMessage"]
    migration_error_type: NotRequired[
        "aws_sdk_waf_regional.types.migration_error_type.MigrationErrorType"
    ]
    migration_error_reason: NotRequired[
        "aws_sdk_waf_regional.types.error_reason.ErrorReason"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFEntityMigrationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "migration_error_type" in value:
        import aws_sdk_waf_regional.types.migration_error_type

        out["MigrationErrorType"] = (
            aws_sdk_waf_regional.types.migration_error_type.serialize_aws_json_1_1(
                value["migration_error_type"]
            )
        )
    if "migration_error_reason" in value:
        out["MigrationErrorReason"] = value["migration_error_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFEntityMigrationException_:
    out: WAFEntityMigrationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "MigrationErrorType" in data:
        import aws_sdk_waf_regional.types.migration_error_type

        out["migration_error_type"] = (
            aws_sdk_waf_regional.types.migration_error_type.deserialize_aws_json_1_1(
                data["MigrationErrorType"]
            )
        )
    if "MigrationErrorReason" in data:
        out["migration_error_reason"] = data["MigrationErrorReason"]
    return out


class WAFEntityMigrationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafregional#WAFEntityMigrationException``."""

    code: str | None = "WAFEntityMigrationException"

    def __init__(self, data: WAFEntityMigrationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFEntityMigrationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFEntityMigrationException":
        return cls(deserialize_aws_json_1_1(data))
