"""Generated from Smithy shape ``com.amazonaws.mq#ListConfigurationRevisionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mq.types.__integer
    import aws_sdk_mq.types.__list_of_configuration_revision
    import aws_sdk_mq.types.__string


class ListConfigurationRevisionsResponse(TypedDict):
    configuration_id: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The unique ID that Amazon MQ generates for the configuration.</p>"""
    max_results: NotRequired["aws_sdk_mq.types.__integer.__integer"]
    """<p>The maximum number of configuration revisions that can be returned per page (20 by default). This value must be an integer from 5 to 100.</p>"""
    next_token: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>"""
    revisions: NotRequired[
        "aws_sdk_mq.types.__list_of_configuration_revision.__listOfConfigurationRevision"
    ]
    """<p>The list of all revisions for the specified configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationRevisionsResponse) -> dict:
    out: dict = {}
    if "configuration_id" in value:
        out["configurationId"] = value["configuration_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "revisions" in value:
        import aws_sdk_mq.types.__list_of_configuration_revision

        out["revisions"] = (
            aws_sdk_mq.types.__list_of_configuration_revision.serialize_json(
                value["revisions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListConfigurationRevisionsResponse:
    out: ListConfigurationRevisionsResponse = {}  # type: ignore[typeddict-item]
    if "configurationId" in data:
        out["configuration_id"] = data["configurationId"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "revisions" in data:
        import aws_sdk_mq.types.__list_of_configuration_revision

        out["revisions"] = (
            aws_sdk_mq.types.__list_of_configuration_revision.deserialize_json(
                data["revisions"]
            )
        )
    return out
