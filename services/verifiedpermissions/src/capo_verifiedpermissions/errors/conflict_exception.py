"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.resource_conflict_list


class ConflictException_(TypedDict, closed=True):
    message: "str"
    resources: (
        "capo_verifiedpermissions.types.resource_conflict_list.ResourceConflictList"
    )
    """<p>The list of resources referenced with this failed request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_verifiedpermissions.types.resource_conflict_list

    out["resources"] = (
        capo_verifiedpermissions.types.resource_conflict_list.serialize_aws_json_1_0(
            value["resources"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "resources" in data:
        import capo_verifiedpermissions.types.resource_conflict_list

        out["resources"] = (
            capo_verifiedpermissions.types.resource_conflict_list.deserialize_aws_json_1_0(
                data["resources"]
            )
        )
    else:
        raise DeserializationError("ConflictException_.resources required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.verifiedpermissions#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ConflictException":
        return cls(deserialize_aws_json_1_0(data))
