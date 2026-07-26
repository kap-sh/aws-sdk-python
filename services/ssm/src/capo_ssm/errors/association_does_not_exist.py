"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationDoesNotExist``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class AssociationDoesNotExist_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationDoesNotExist_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationDoesNotExist_:
    out: AssociationDoesNotExist_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AssociationDoesNotExist(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#AssociationDoesNotExist``."""

    code: str | None = "AssociationDoesNotExist"

    def __init__(self, data: AssociationDoesNotExist_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AssociationDoesNotExist",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AssociationDoesNotExist":
        return cls(deserialize_aws_json_1_1(data))
