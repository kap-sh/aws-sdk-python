"""Generated from Smithy shape ``com.amazonaws.acmpca#MalformedCertificateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import ServiceError

if TYPE_CHECKING:
    import capo_acm_pca.types.string


class MalformedCertificateException_(TypedDict, closed=True):
    message: NotRequired["capo_acm_pca.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MalformedCertificateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MalformedCertificateException_:
    out: MalformedCertificateException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MalformedCertificateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.acmpca#MalformedCertificateException``."""

    code: str | None = "MalformedCertificateException"

    def __init__(self, data: MalformedCertificateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MalformedCertificateException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "MalformedCertificateException":
        return cls(deserialize_aws_json_1_1(data))
