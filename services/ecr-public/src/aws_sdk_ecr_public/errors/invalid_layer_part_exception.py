"""Generated from Smithy shape ``com.amazonaws.ecrpublic#InvalidLayerPartException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr_public.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.exception_message
    import aws_sdk_ecr_public.types.part_size
    import aws_sdk_ecr_public.types.registry_id
    import aws_sdk_ecr_public.types.repository_name
    import aws_sdk_ecr_public.types.upload_id


class InvalidLayerPartException_(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr_public.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID that's associated with the layer part.</p>"""
    repository_name: NotRequired[
        "aws_sdk_ecr_public.types.repository_name.RepositoryName"
    ]
    """<p>The name of the repository.</p>"""
    upload_id: NotRequired["aws_sdk_ecr_public.types.upload_id.UploadId"]
    """<p>The upload ID that's associated with the layer part.</p>"""
    last_valid_byte_received: NotRequired["aws_sdk_ecr_public.types.part_size.PartSize"]
    """<p>The position of the last byte of the layer part.</p>"""
    message: NotRequired["aws_sdk_ecr_public.types.exception_message.ExceptionMessage"]


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
    """Modeled error for Smithy shape ``com.amazonaws.ecrpublic#InvalidLayerPartException``."""

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
