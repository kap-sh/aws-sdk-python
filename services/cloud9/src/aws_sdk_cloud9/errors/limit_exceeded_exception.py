"""Generated from Smithy shape ``com.amazonaws.cloud9#LimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloud9.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.integer
    import aws_sdk_cloud9.types.string


class LimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_cloud9.types.string.String"]
    class_name: NotRequired["aws_sdk_cloud9.types.string.String"]
    code: "aws_sdk_cloud9.types.integer.Integer"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "class_name" in value:
        out["className"] = value["class_name"]
    out["code"] = value.get("code", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "className" in data:
        out["class_name"] = data["className"]
    if "code" in data:
        out["code"] = data["code"]
    else:
        out["code"] = 0
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloud9#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(self, data: LimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "LimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
