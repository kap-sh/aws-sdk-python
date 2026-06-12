"""Generated from Smithy shape ``com.amazonaws.ecr#InvalidLayerPartException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.exception_message
    import aws_sdk_ecr.types.part_size
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name
    import aws_sdk_ecr.types.upload_id


class InvalidLayerPartException_(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the exception.</p>"""
    repository_name: NotRequired["aws_sdk_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the exception.</p>"""
    upload_id: NotRequired["aws_sdk_ecr.types.upload_id.UploadId"]
    """<p>The upload ID associated with the exception.</p>"""
    last_valid_byte_received: NotRequired["aws_sdk_ecr.types.part_size.PartSize"]
    """<p>The last valid byte received from the layer part upload that is associated with the exception.</p>"""
    message: NotRequired["aws_sdk_ecr.types.exception_message.ExceptionMessage"]
    """<p>The error message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidLayerPartException_) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "upload_id" in value:
        out["uploadId"] = value["upload_id"]
    if "last_valid_byte_received" in value:
        out["lastValidByteReceived"] = value["last_valid_byte_received"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidLayerPartException_:
    out: InvalidLayerPartException_ = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "uploadId" in data:
        out["upload_id"] = data["uploadId"]
    if "lastValidByteReceived" in data:
        out["last_valid_byte_received"] = data["lastValidByteReceived"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidLayerPartException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#InvalidLayerPartException``."""

    code: str | None = "InvalidLayerPartException"

    def __init__(self, data: InvalidLayerPartException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidLayerPartException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidLayerPartException":
        return cls(deserialize_aws_json_1_1(data))
