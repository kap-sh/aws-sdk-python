"""Generated from Smithy shape ``com.amazonaws.kafka#ListConfigurationRevisionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of_configuration_revision
    import aws_sdk_kafka.types.__string


class ListConfigurationRevisionsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>Paginated results marker.</p>"""
    revisions: NotRequired[
        "aws_sdk_kafka.types.__list_of_configuration_revision.__listOfConfigurationRevision"
    ]
    """<p>List of ConfigurationRevision objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationRevisionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "revisions" in value:
        import aws_sdk_kafka.types.__list_of_configuration_revision

        out["revisions"] = (
            aws_sdk_kafka.types.__list_of_configuration_revision.serialize_json(
                value["revisions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListConfigurationRevisionsResponse:
    out: ListConfigurationRevisionsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "revisions" in data:
        import aws_sdk_kafka.types.__list_of_configuration_revision

        out["revisions"] = (
            aws_sdk_kafka.types.__list_of_configuration_revision.deserialize_json(
                data["revisions"]
            )
        )
    return out
