"""Generated from Smithy shape ``com.amazonaws.fsx#IncompatibleRegionForMultiAZ``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_message


class IncompatibleRegionForMultiAZ_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncompatibleRegionForMultiAZ_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IncompatibleRegionForMultiAZ_:
    out: IncompatibleRegionForMultiAZ_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class IncompatibleRegionForMultiAZ(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#IncompatibleRegionForMultiAZ``."""

    code: str | None = "IncompatibleRegionForMultiAZ"

    def __init__(self, data: IncompatibleRegionForMultiAZ_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncompatibleRegionForMultiAZ",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IncompatibleRegionForMultiAZ":
        return cls(deserialize_aws_json_1_1(data))
