"""Generated from Smithy shape ``com.amazonaws.dax#SubnetGroupNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dax.errors import ServiceError

if TYPE_CHECKING:
    import capo_dax.types.exception_message


class SubnetGroupNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["capo_dax.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetGroupNotFoundFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubnetGroupNotFoundFault_:
    out: SubnetGroupNotFoundFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SubnetGroupNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dax#SubnetGroupNotFoundFault``."""

    code: str | None = "SubnetGroupNotFoundFault"

    def __init__(self, data: SubnetGroupNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SubnetGroupNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "SubnetGroupNotFoundFault":
        return cls(deserialize_aws_json_1_1(data))
