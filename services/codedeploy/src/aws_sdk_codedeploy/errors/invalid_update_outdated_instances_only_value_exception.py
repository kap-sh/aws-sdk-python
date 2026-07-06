"""Generated from Smithy shape ``com.amazonaws.codedeploy#InvalidUpdateOutdatedInstancesOnlyValueException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.message


class InvalidUpdateOutdatedInstancesOnlyValueException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: InvalidUpdateOutdatedInstancesOnlyValueException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> InvalidUpdateOutdatedInstancesOnlyValueException_:
    out: InvalidUpdateOutdatedInstancesOnlyValueException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidUpdateOutdatedInstancesOnlyValueException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#InvalidUpdateOutdatedInstancesOnlyValueException``."""

    code: str | None = "InvalidUpdateOutdatedInstancesOnlyValueException"

    def __init__(self, data: InvalidUpdateOutdatedInstancesOnlyValueException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidUpdateOutdatedInstancesOnlyValueException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "InvalidUpdateOutdatedInstancesOnlyValueException":
        return cls(deserialize_aws_json_1_1(data))
