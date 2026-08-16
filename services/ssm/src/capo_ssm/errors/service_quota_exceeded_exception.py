"""Generated from Smithy shape ``com.amazonaws.ssm#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_ssm.types.string.String"
    resource_id: NotRequired["capo_ssm.types.string.String"]
    """<p>The unique ID of the resource referenced in the failed request.</p>"""
    resource_type: NotRequired["capo_ssm.types.string.String"]
    """<p>The resource type of the resource referenced in the failed request.</p>"""
    quota_code: "capo_ssm.types.string.String"
    """<p>The quota code recognized by the Amazon Web Services Service Quotas service.</p>"""
    service_code: "capo_ssm.types.string.String"
    """<p>The code for the Amazon Web Services service that owns the quota.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    out["QuotaCode"] = value["quota_code"]
    out["ServiceCode"] = value["service_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.quota_code required")
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.service_code required"
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ServiceQuotaExceededException``."""

    code: str | None = "ServiceQuotaExceededException"

    def __init__(
        self, data: ServiceQuotaExceededException_, message: str | None = None
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceQuotaExceededException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "ServiceQuotaExceededException":
        return cls(deserialize_aws_json_1_1(data), message)
