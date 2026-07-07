"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bcm_data_exports.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.generic_string


class ThrottlingException_(TypedDict, closed=True):
    message: "aws_sdk_bcm_data_exports.types.generic_string.GenericString"
    quota_code: NotRequired[
        "aws_sdk_bcm_data_exports.types.generic_string.GenericString"
    ]
    """<p>The quota code that exceeded the throttling limit.</p>"""
    service_code: NotRequired[
        "aws_sdk_bcm_data_exports.types.generic_string.GenericString"
    ]
    """<p>The service code that exceeded the throttling limit. It will always be “AWSBillingAndCostManagementDataExports”.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bcmdataexports#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_1(data))
