"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.resource_type


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"
    resource_id: NotRequired["str"]
    """<p>The unique ID of the resource referenced in the failed request.</p>"""
    resource_type: "capo_verifiedpermissions.types.resource_type.ResourceType"
    """<p>The resource type of the resource referenced in the failed request.</p>"""
    service_code: NotRequired["str"]
    """<p>The code for the Amazon Web Services service that owns the quota.</p>"""
    quota_code: NotRequired["str"]
    """<p>The quota code recognized by the Amazon Web Services Service Quotas service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    import capo_verifiedpermissions.types.resource_type

    out["resourceType"] = (
        capo_verifiedpermissions.types.resource_type.serialize_aws_json_1_0(
            value["resource_type"]
        )
    )
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceType" in data:
        import capo_verifiedpermissions.types.resource_type

        out["resource_type"] = (
            capo_verifiedpermissions.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.resource_type required"
        )
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    if "quotaCode" in data:
        out["quota_code"] = data["quotaCode"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.verifiedpermissions#ServiceQuotaExceededException``."""

    code: str | None = "ServiceQuotaExceededException"

    def __init__(self, data: ServiceQuotaExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceQuotaExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ServiceQuotaExceededException":
        return cls(deserialize_aws_json_1_0(data))
