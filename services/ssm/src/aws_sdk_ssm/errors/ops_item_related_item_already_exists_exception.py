"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemRelatedItemAlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_id
    import aws_sdk_ssm.types.ops_item_related_item_association_resource_uri
    import aws_sdk_ssm.types.string


class OpsItemRelatedItemAlreadyExistsException_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]
    resource_uri: NotRequired[
        "aws_sdk_ssm.types.ops_item_related_item_association_resource_uri.OpsItemRelatedItemAssociationResourceUri"
    ]
    ops_item_id: NotRequired["aws_sdk_ssm.types.ops_item_id.OpsItemId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemRelatedItemAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_uri" in value:
        out["ResourceUri"] = value["resource_uri"]
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemRelatedItemAlreadyExistsException_:
    out: OpsItemRelatedItemAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceUri" in data:
        out["resource_uri"] = data["ResourceUri"]
    if "OpsItemId" in data:
        out["ops_item_id"] = data["OpsItemId"]
    return out


class OpsItemRelatedItemAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#OpsItemRelatedItemAlreadyExistsException``."""

    code: str | None = "OpsItemRelatedItemAlreadyExistsException"

    def __init__(self, data: OpsItemRelatedItemAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OpsItemRelatedItemAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "OpsItemRelatedItemAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))
