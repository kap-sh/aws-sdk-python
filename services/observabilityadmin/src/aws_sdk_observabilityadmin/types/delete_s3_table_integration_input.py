"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DeleteS3TableIntegrationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.resource_arn


class DeleteS3TableIntegrationInput(TypedDict):
    arn: "aws_sdk_observabilityadmin.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the S3 Table integration to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteS3TableIntegrationInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteS3TableIntegrationInput:
    out: DeleteS3TableIntegrationInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DeleteS3TableIntegrationInput.arn required")
    return out
