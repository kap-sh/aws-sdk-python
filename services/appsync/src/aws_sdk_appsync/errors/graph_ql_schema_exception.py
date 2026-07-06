"""Generated from Smithy shape ``com.amazonaws.appsync#GraphQLSchemaException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appsync.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.error_message


class GraphQLSchemaException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_appsync.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: GraphQLSchemaException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> GraphQLSchemaException_:
    out: GraphQLSchemaException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class GraphQLSchemaException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appsync#GraphQLSchemaException``."""

    code: str | None = "GraphQLSchemaException"

    def __init__(self, data: GraphQLSchemaException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GraphQLSchemaException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "GraphQLSchemaException":
        return cls(deserialize_json(data))
