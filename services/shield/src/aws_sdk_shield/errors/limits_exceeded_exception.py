"""Generated from Smithy shape ``com.amazonaws.shield#LimitsExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_shield.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_shield.types.error_message
    import aws_sdk_shield.types.limit_number
    import aws_sdk_shield.types.limit_type


class LimitsExceededException_(TypedDict):
    message: NotRequired["aws_sdk_shield.types.error_message.errorMessage"]
    type: NotRequired["aws_sdk_shield.types.limit_type.LimitType"]
    """<p>The type of limit that would be exceeded.</p>"""
    limit: "aws_sdk_shield.types.limit_number.LimitNumber"
    """<p>The threshold that would be exceeded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LimitsExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "type" in value:
        out["Type"] = value["type"]
    out["Limit"] = value.get("limit", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> LimitsExceededException_:
    out: LimitsExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    return out


class LimitsExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.shield#LimitsExceededException``."""

    code: str | None = "LimitsExceededException"

    def __init__(self, data: LimitsExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitsExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "LimitsExceededException":
        return cls(deserialize_aws_json_1_1(data))
