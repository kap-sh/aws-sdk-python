"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemCollectionSizeLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class ItemCollectionSizeLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]
    """<p>The total size of an item collection has exceeded the maximum limit of 10 gigabytes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ItemCollectionSizeLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ItemCollectionSizeLimitExceededException_:
    out: ItemCollectionSizeLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ItemCollectionSizeLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ItemCollectionSizeLimitExceededException``."""

    code: str | None = "ItemCollectionSizeLimitExceededException"

    def __init__(self, data: ItemCollectionSizeLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ItemCollectionSizeLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict
    ) -> "ItemCollectionSizeLimitExceededException":
        return cls(deserialize_aws_json_1_0(data))
