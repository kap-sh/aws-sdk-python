"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetCapacityExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_gamelift.errors import ServiceError

if TYPE_CHECKING:
    import capo_gamelift.types.non_empty_string


class FleetCapacityExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetCapacityExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FleetCapacityExceededException_:
    out: FleetCapacityExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class FleetCapacityExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.gamelift#FleetCapacityExceededException``."""

    code: str | None = "FleetCapacityExceededException"

    def __init__(self, data: FleetCapacityExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FleetCapacityExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "FleetCapacityExceededException":
        return cls(deserialize_aws_json_1_1(data))
