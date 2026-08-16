"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class OpsItemNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemNotFoundException_:
    out: OpsItemNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class OpsItemNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#OpsItemNotFoundException``."""

    code: str | None = "OpsItemNotFoundException"

    def __init__(self, data: OpsItemNotFoundException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OpsItemNotFoundException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "OpsItemNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message)
