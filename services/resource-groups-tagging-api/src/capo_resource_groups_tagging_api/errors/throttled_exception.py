"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ThrottledException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resource_groups_tagging_api.errors import ServiceError

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.exception_message


class ThrottledException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_resource_groups_tagging_api.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThrottledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThrottledException_:
    out: ThrottledException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ThrottledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ThrottledException``."""

    code: str | None = "ThrottledException"

    def __init__(self, data: ThrottledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottledException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ThrottledException":
        return cls(deserialize_aws_json_1_1(data))
