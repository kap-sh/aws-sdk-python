"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateCustomMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workdocs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.custom_metadata_map
    import aws_sdk_workdocs.types.document_version_id_type
    import aws_sdk_workdocs.types.resource_id_type


class CreateCustomMetadataRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    resource_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the resource.</p>"""
    version_id: NotRequired[
        "aws_sdk_workdocs.types.document_version_id_type.DocumentVersionIdType"
    ]
    """<p>The ID of the version, if the custom metadata is being added to a document version.</p>"""
    custom_metadata: "aws_sdk_workdocs.types.custom_metadata_map.CustomMetadataMap"
    """<p>Custom metadata in the form of name-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomMetadataRequest) -> dict:
    out: dict = {}
    import aws_sdk_workdocs.types.custom_metadata_map

    out["CustomMetadata"] = aws_sdk_workdocs.types.custom_metadata_map.serialize_json(
        value["custom_metadata"]
    )
    return out


def deserialize_json(data: dict) -> CreateCustomMetadataRequest:
    out: CreateCustomMetadataRequest = {}  # type: ignore[typeddict-item]
    if "CustomMetadata" in data:
        import aws_sdk_workdocs.types.custom_metadata_map

        out["custom_metadata"] = (
            aws_sdk_workdocs.types.custom_metadata_map.deserialize_json(
                data["CustomMetadata"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCustomMetadataRequest.custom_metadata required"
        )
    return out
