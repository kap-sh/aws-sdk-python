"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ListApplicationDependenciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__string
    import capo_serverlessapplicationrepository.types.max_items


class ListApplicationDependenciesRequest(TypedDict, closed=True):
    application_id: "capo_serverlessapplicationrepository.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    max_items: NotRequired[
        "capo_serverlessapplicationrepository.types.max_items.MaxItems"
    ]
    """<p>The total number of items to return.</p>"""
    next_token: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A token to specify where to start paginating.</p>"""
    semantic_version: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The semantic version of the application to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationDependenciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationDependenciesRequest:
    out: ListApplicationDependenciesRequest = {}  # type: ignore[typeddict-item]
    return out
