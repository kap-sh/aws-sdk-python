"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#SearchException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudsearch_domain.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.string


class SearchException_(TypedDict):
    message: NotRequired["aws_sdk_cloudsearch_domain.types.string.String"]
    """<p>A description of the error returned by the search service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SearchException_:
    out: SearchException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SearchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudsearchdomain#SearchException``."""

    code: str | None = "SearchException"

    def __init__(self, data: SearchException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SearchException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "SearchException":
        return cls(deserialize_json(data))
