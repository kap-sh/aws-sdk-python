"""Generated from Smithy shape ``com.amazonaws.dax#SubnetGroupInUseFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dax.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dax.types.exception_message


class SubnetGroupInUseFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_dax.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetGroupInUseFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubnetGroupInUseFault_:
    out: SubnetGroupInUseFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SubnetGroupInUseFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dax#SubnetGroupInUseFault``."""

    code: str | None = "SubnetGroupInUseFault"

    def __init__(self, data: SubnetGroupInUseFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SubnetGroupInUseFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "SubnetGroupInUseFault":
        return cls(deserialize_aws_json_1_1(data))
