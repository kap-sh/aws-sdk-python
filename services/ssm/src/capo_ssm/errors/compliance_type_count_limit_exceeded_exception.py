"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceTypeCountLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class ComplianceTypeCountLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceTypeCountLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceTypeCountLimitExceededException_:
    out: ComplianceTypeCountLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ComplianceTypeCountLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ComplianceTypeCountLimitExceededException``."""

    code: str | None = "ComplianceTypeCountLimitExceededException"

    def __init__(
        self,
        data: ComplianceTypeCountLimitExceededException_,
        message: str | None = None,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ComplianceTypeCountLimitExceededException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "ComplianceTypeCountLimitExceededException":
        return cls(deserialize_aws_json_1_1(data), message)
