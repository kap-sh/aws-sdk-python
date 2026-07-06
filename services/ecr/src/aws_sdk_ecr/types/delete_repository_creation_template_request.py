"""Generated from Smithy shape ``com.amazonaws.ecr#DeleteRepositoryCreationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.prefix


class DeleteRepositoryCreationTemplateRequest(TypedDict, closed=True):
    prefix: "aws_sdk_ecr.types.prefix.Prefix"
    """<p>The repository namespace prefix associated with the repository creation template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRepositoryCreationTemplateRequest) -> dict:
    out: dict = {}
    out["prefix"] = value["prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRepositoryCreationTemplateRequest:
    out: DeleteRepositoryCreationTemplateRequest = {}  # type: ignore[typeddict-item]
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    else:
        raise DeserializationError(
            "DeleteRepositoryCreationTemplateRequest.prefix required"
        )
    return out
