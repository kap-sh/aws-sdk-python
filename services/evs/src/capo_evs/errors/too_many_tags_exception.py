"""Generated from Smithy shape ``com.amazonaws.evs#TooManyTagsException``."""

from typing_extensions import TypedDict

from capo_evs.errors import DeserializationError, ServiceError


class TooManyTagsException_(TypedDict, closed=True):
    message: "str"
    """<p>Describes the error encountered.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TooManyTagsException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TooManyTagsException_:
    out: TooManyTagsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("TooManyTagsException_.message required")
    return out


class TooManyTagsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.evs#TooManyTagsException``."""

    code: str | None = "TooManyTagsException"

    def __init__(self, data: TooManyTagsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyTagsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "TooManyTagsException":
        return cls(deserialize_aws_json_1_0(data))
