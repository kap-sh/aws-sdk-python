"""Generated from Smithy shape ``com.amazonaws.devopsagent#InvalidParameterException``."""

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, ServiceError


class InvalidParameterException_(TypedDict, closed=True):
    message: "str"
    """<p>Detailed error message describing which parameter is invalid and why.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidParameterException_:
    out: InvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidParameterException_.message required")
    return out


class InvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devopsagent#InvalidParameterException``."""

    code: str | None = "InvalidParameterException"

    def __init__(self, data: InvalidParameterException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidParameterException":
        return cls(deserialize_json(data))
