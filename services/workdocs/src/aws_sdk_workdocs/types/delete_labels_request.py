"""Generated from Smithy shape ``com.amazonaws.workdocs#DeleteLabelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.boolean_type
    import aws_sdk_workdocs.types.resource_id_type
    import aws_sdk_workdocs.types.shared_labels


class DeleteLabelsRequest(TypedDict, closed=True):
    resource_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the resource.</p>"""
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    labels: NotRequired["aws_sdk_workdocs.types.shared_labels.SharedLabels"]
    """<p>List of labels to delete from the resource.</p>"""
    delete_all: "aws_sdk_workdocs.types.boolean_type.BooleanType"
    """<p>Flag to request removal of all labels from the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLabelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteLabelsRequest:
    out: DeleteLabelsRequest = {}  # type: ignore[typeddict-item]
    return out
