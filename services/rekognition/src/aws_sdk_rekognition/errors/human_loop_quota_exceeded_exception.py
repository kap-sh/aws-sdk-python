"""Generated from Smithy shape ``com.amazonaws.rekognition#HumanLoopQuotaExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.string


class HumanLoopQuotaExceededException_(TypedDict):
    resource_type: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The resource type.</p>"""
    quota_code: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The quota code.</p>"""
    service_code: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The service code.</p>"""
    message: NotRequired["aws_sdk_rekognition.types.string.String"]
    code: NotRequired["aws_sdk_rekognition.types.string.String"]
    logref: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>A universally unique identifier (UUID) for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanLoopQuotaExceededException_) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    if "logref" in value:
        out["Logref"] = value["logref"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HumanLoopQuotaExceededException_:
    out: HumanLoopQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Logref" in data:
        out["logref"] = data["Logref"]
    return out


class HumanLoopQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rekognition#HumanLoopQuotaExceededException``."""

    code: str | None = "HumanLoopQuotaExceededException"

    def __init__(self, data: HumanLoopQuotaExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="HumanLoopQuotaExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "HumanLoopQuotaExceededException":
        return cls(deserialize_aws_json_1_1(data))
