"""Generated from Smithy shape ``com.amazonaws.kafka#ListConfigurationRevisionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__list_of_configuration_revision
    import capo_kafka.types.__string


class ListConfigurationRevisionsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Paginated results marker.</p>"""
    revisions: NotRequired[
        "capo_kafka.types.__list_of_configuration_revision.__listOfConfigurationRevision"
    ]
    """<p>List of ConfigurationRevision objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationRevisionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "revisions" in value:
        import capo_kafka.types.__list_of_configuration_revision

        out["revisions"] = (
            capo_kafka.types.__list_of_configuration_revision.serialize_json(
                value["revisions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListConfigurationRevisionsResponse:
    out: ListConfigurationRevisionsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "revisions" in data:
        import capo_kafka.types.__list_of_configuration_revision

        out["revisions"] = (
            capo_kafka.types.__list_of_configuration_revision.deserialize_json(
                data["revisions"]
            )
        )
    return out
