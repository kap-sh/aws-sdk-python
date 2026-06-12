"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ListApplicationDependenciesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__string
    import aws_sdk_serverlessapplicationrepository.types.max_items


class ListApplicationDependenciesRequest(TypedDict):
    application_id: "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    max_items: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.max_items.MaxItems"
    ]
    """<p>The total number of items to return.</p>"""
    next_token: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A token to specify where to start paginating.</p>"""
    semantic_version: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The semantic version of the application to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationDependenciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationDependenciesRequest:
    out: ListApplicationDependenciesRequest = {}  # type: ignore[typeddict-item]
    return out
