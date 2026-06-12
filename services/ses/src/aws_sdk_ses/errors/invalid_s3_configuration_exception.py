"""Generated from Smithy shape ``com.amazonaws.ses#InvalidS3ConfigurationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ses.types.error_message
    import aws_sdk_ses.types.s3_bucket_name


class InvalidS3ConfigurationException_(TypedDict):
    bucket: NotRequired["aws_sdk_ses.types.s3_bucket_name.S3BucketName"]
    """<p>Indicated that the S3 Bucket was not found.</p>"""
    message: NotRequired["aws_sdk_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidS3ConfigurationException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "bucket" in value:
        pairs.append((f"{prefix}.Bucket", str(value["bucket"])))
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidS3ConfigurationException_:
    out: InvalidS3ConfigurationException_ = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidS3ConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#InvalidS3ConfigurationException``."""

    code: str | None = "InvalidS3ConfigurationException"

    def __init__(self, data: InvalidS3ConfigurationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidS3ConfigurationException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidS3ConfigurationException":
        return cls(deserialize_query(el))
