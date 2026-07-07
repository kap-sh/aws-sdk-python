"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedResultsConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.conflicting_items
    import aws_sdk_kendra.types.string


class FeaturedResultsConflictException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_kendra.types.string.String"]
    """<p>An explanation for the conflicting queries.</p>"""
    conflicting_items: NotRequired[
        "aws_sdk_kendra.types.conflicting_items.ConflictingItems"
    ]
    """<p>A list of the conflicting queries, including the query text, the name for the featured results set, and the identifier of the featured results set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedResultsConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "conflicting_items" in value:
        import aws_sdk_kendra.types.conflicting_items

        out["ConflictingItems"] = (
            aws_sdk_kendra.types.conflicting_items.serialize_aws_json_1_1(
                value["conflicting_items"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FeaturedResultsConflictException_:
    out: FeaturedResultsConflictException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ConflictingItems" in data:
        import aws_sdk_kendra.types.conflicting_items

        out["conflicting_items"] = (
            aws_sdk_kendra.types.conflicting_items.deserialize_aws_json_1_1(
                data["ConflictingItems"]
            )
        )
    return out


class FeaturedResultsConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kendra#FeaturedResultsConflictException``."""

    code: str | None = "FeaturedResultsConflictException"

    def __init__(self, data: FeaturedResultsConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FeaturedResultsConflictException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "FeaturedResultsConflictException":
        return cls(deserialize_aws_json_1_1(data))
