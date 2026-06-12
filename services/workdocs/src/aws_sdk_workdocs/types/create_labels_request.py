"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateLabelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workdocs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.resource_id_type
    import aws_sdk_workdocs.types.shared_labels


class CreateLabelsRequest(TypedDict):
    resource_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the resource.</p>"""
    labels: "aws_sdk_workdocs.types.shared_labels.SharedLabels"
    """<p>List of labels to add to the resource.</p>"""
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLabelsRequest) -> dict:
    out: dict = {}
    import aws_sdk_workdocs.types.shared_labels

    out["Labels"] = aws_sdk_workdocs.types.shared_labels.serialize_json(value["labels"])
    return out


def deserialize_json(data: dict) -> CreateLabelsRequest:
    out: CreateLabelsRequest = {}  # type: ignore[typeddict-item]
    if "Labels" in data:
        import aws_sdk_workdocs.types.shared_labels

        out["labels"] = aws_sdk_workdocs.types.shared_labels.deserialize_json(
            data["Labels"]
        )
    else:
        raise DeserializationError("CreateLabelsRequest.labels required")
    return out
