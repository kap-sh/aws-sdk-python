"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidFilterOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidFilterOption_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The specified filter option isn't valid. Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidFilterOption_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidFilterOption_:
    out: InvalidFilterOption_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidFilterOption(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidFilterOption``."""

    code: str | None = "InvalidFilterOption"

    def __init__(self, data: InvalidFilterOption_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidFilterOption",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidFilterOption":
        return cls(deserialize_aws_json_1_1(data))
