"""Generated from Smithy shape ``com.amazonaws.workdocs#EntityNotExistsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.entity_id_list
    import aws_sdk_workdocs.types.error_message_type


class EntityNotExistsException_(TypedDict):
    message: NotRequired["aws_sdk_workdocs.types.error_message_type.ErrorMessageType"]
    entity_ids: NotRequired["aws_sdk_workdocs.types.entity_id_list.EntityIdList"]
    """<p>The IDs of the non-existent resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntityNotExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "entity_ids" in value:
        import aws_sdk_workdocs.types.entity_id_list

        out["EntityIds"] = aws_sdk_workdocs.types.entity_id_list.serialize_json(
            value["entity_ids"]
        )
    return out


def deserialize_json(data: dict) -> EntityNotExistsException_:
    out: EntityNotExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "EntityIds" in data:
        import aws_sdk_workdocs.types.entity_id_list

        out["entity_ids"] = aws_sdk_workdocs.types.entity_id_list.deserialize_json(
            data["EntityIds"]
        )
    return out


class EntityNotExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#EntityNotExistsException``."""

    code: str | None = "EntityNotExistsException"

    def __init__(self, data: EntityNotExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EntityNotExistsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "EntityNotExistsException":
        return cls(deserialize_json(data))
