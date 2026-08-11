"""Generated from Smithy shape ``com.amazonaws.ecs#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecs.types.resource_ids
    import capo_ecs.types.string


class ConflictException_(TypedDict, closed=True):
    resource_ids: NotRequired["capo_ecs.types.resource_ids.ResourceIds"]
    """<p>The existing task ARNs which are already associated with the <code>clientToken</code>.</p>"""
    message: NotRequired["capo_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConflictException_) -> dict:
    out: dict = {}
    if "resource_ids" in value:
        import capo_ecs.types.resource_ids

        out["resourceIds"] = capo_ecs.types.resource_ids.serialize_aws_json_1_1(
            value["resource_ids"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "resourceIds" in data:
        import capo_ecs.types.resource_ids

        out["resource_ids"] = capo_ecs.types.resource_ids.deserialize_aws_json_1_1(
            data["resourceIds"]
        )
    if "message" in data:
        out["message"] = data["message"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "ConflictException":
        return cls(deserialize_aws_json_1_1(data), message)
