"""Generated from Smithy shape ``com.amazonaws.dlm#ResourceNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dlm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dlm.types.error_code
    import aws_sdk_dlm.types.error_message
    import aws_sdk_dlm.types.policy_id_list
    import aws_sdk_dlm.types.string


class ResourceNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_dlm.types.error_message.ErrorMessage"]
    code: NotRequired["aws_sdk_dlm.types.error_code.ErrorCode"]
    resource_type: NotRequired["aws_sdk_dlm.types.string.String"]
    """<p>Value is the type of resource that was not found.</p>"""
    resource_ids: NotRequired["aws_sdk_dlm.types.policy_id_list.PolicyIdList"]
    """<p>Value is a list of resource IDs that were not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_ids" in value:
        import aws_sdk_dlm.types.policy_id_list

        out["ResourceIds"] = aws_sdk_dlm.types.policy_id_list.serialize_json(
            value["resource_ids"]
        )
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceIds" in data:
        import aws_sdk_dlm.types.policy_id_list

        out["resource_ids"] = aws_sdk_dlm.types.policy_id_list.deserialize_json(
            data["ResourceIds"]
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dlm#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(self, data: ResourceNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_json(data))
