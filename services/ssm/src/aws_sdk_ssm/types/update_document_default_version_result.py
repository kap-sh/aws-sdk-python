"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateDocumentDefaultVersionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_default_version_description


class UpdateDocumentDefaultVersionResult(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_ssm.types.document_default_version_description.DocumentDefaultVersionDescription"
    ]
    """<p>The description of a custom document that you want to set as the default version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDocumentDefaultVersionResult) -> dict:
    out: dict = {}
    if "description" in value:
        import aws_sdk_ssm.types.document_default_version_description

        out["Description"] = (
            aws_sdk_ssm.types.document_default_version_description.serialize_aws_json_1_1(
                value["description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDocumentDefaultVersionResult:
    out: UpdateDocumentDefaultVersionResult = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        import aws_sdk_ssm.types.document_default_version_description

        out["description"] = (
            aws_sdk_ssm.types.document_default_version_description.deserialize_aws_json_1_1(
                data["Description"]
            )
        )
    return out
