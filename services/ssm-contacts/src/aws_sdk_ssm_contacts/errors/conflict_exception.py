"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.dependent_entity_list
    import aws_sdk_ssm_contacts.types.string


class ConflictException_(TypedDict, closed=True):
    message: "aws_sdk_ssm_contacts.types.string.String"
    resource_id: "aws_sdk_ssm_contacts.types.string.String"
    """Identifier of the resource in use"""
    resource_type: "aws_sdk_ssm_contacts.types.string.String"
    """Type of the resource in use"""
    dependent_entities: NotRequired[
        "aws_sdk_ssm_contacts.types.dependent_entity_list.DependentEntityList"
    ]
    """List of dependent entities containing information on relation type and resourceArns linked to the resource in use"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConflictException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    if "dependent_entities" in value:
        import aws_sdk_ssm_contacts.types.dependent_entity_list

        out["DependentEntities"] = (
            aws_sdk_ssm_contacts.types.dependent_entity_list.serialize_aws_json_1_1(
                value["dependent_entities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ConflictException_.resource_id required")
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("ConflictException_.resource_type required")
    if "DependentEntities" in data:
        import aws_sdk_ssm_contacts.types.dependent_entity_list

        out["dependent_entities"] = (
            aws_sdk_ssm_contacts.types.dependent_entity_list.deserialize_aws_json_1_1(
                data["DependentEntities"]
            )
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssmcontacts#ConflictException``."""

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
    def from_aws_json_1_1(cls, data: dict) -> "ConflictException":
        return cls(deserialize_aws_json_1_1(data))
