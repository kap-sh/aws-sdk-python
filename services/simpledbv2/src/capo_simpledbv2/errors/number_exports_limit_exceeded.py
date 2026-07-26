"""Generated from Smithy shape ``com.amazonaws.simpledbv2#NumberExportsLimitExceeded``."""

from typing_extensions import TypedDict

from capo_simpledbv2.errors import DeserializationError, ServiceError


class NumberExportsLimitExceeded_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: NumberExportsLimitExceeded_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NumberExportsLimitExceeded_:
    out: NumberExportsLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("NumberExportsLimitExceeded_.message required")
    return out


class NumberExportsLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.simpledbv2#NumberExportsLimitExceeded``."""

    code: str | None = "NumberExportsLimitExceeded"

    def __init__(self, data: NumberExportsLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NumberExportsLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NumberExportsLimitExceeded":
        return cls(deserialize_json(data))
