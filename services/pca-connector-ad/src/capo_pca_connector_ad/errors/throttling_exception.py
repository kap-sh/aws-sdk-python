"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ThrottlingException``."""

from typing_extensions import NotRequired, TypedDict

from capo_pca_connector_ad.errors import DeserializationError, ServiceError


class ThrottlingException_(TypedDict, closed=True):
    message: "str"
    service_code: NotRequired["str"]
    """<p>Identifies the originating service.</p>"""
    quota_code: NotRequired["str"]
    """<p>The code associated with the quota.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pcaconnectorad#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=True,
            is_retryable=True,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))
