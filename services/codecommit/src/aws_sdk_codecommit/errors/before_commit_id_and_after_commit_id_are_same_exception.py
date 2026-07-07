"""Generated from Smithy shape ``com.amazonaws.codecommit#BeforeCommitIdAndAfterCommitIdAreSameException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.message


class BeforeCommitIdAndAfterCommitIdAreSameException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BeforeCommitIdAndAfterCommitIdAreSameException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BeforeCommitIdAndAfterCommitIdAreSameException_:
    out: BeforeCommitIdAndAfterCommitIdAreSameException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class BeforeCommitIdAndAfterCommitIdAreSameException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#BeforeCommitIdAndAfterCommitIdAreSameException``."""

    code: str | None = "BeforeCommitIdAndAfterCommitIdAreSameException"

    def __init__(self, data: BeforeCommitIdAndAfterCommitIdAreSameException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BeforeCommitIdAndAfterCommitIdAreSameException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "BeforeCommitIdAndAfterCommitIdAreSameException":
        return cls(deserialize_aws_json_1_1(data))
