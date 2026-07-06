"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListApplicationComponentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.application_component_details
    import aws_sdk_migrationhubstrategy.types.next_token


class ListApplicationComponentsResponse(TypedDict, closed=True):
    application_component_infos: NotRequired[
        "aws_sdk_migrationhubstrategy.types.application_component_details.ApplicationComponentDetails"
    ]
    """<p> The list of application components with detailed information about each component. </p>"""
    next_token: NotRequired["aws_sdk_migrationhubstrategy.types.next_token.NextToken"]
    """<p> The token you use to retrieve the next set of results, or null if there are no more results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationComponentsResponse) -> dict:
    out: dict = {}
    if "application_component_infos" in value:
        import aws_sdk_migrationhubstrategy.types.application_component_details

        out["applicationComponentInfos"] = (
            aws_sdk_migrationhubstrategy.types.application_component_details.serialize_json(
                value["application_component_infos"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationComponentsResponse:
    out: ListApplicationComponentsResponse = {}  # type: ignore[typeddict-item]
    if "applicationComponentInfos" in data:
        import aws_sdk_migrationhubstrategy.types.application_component_details

        out["application_component_infos"] = (
            aws_sdk_migrationhubstrategy.types.application_component_details.deserialize_json(
                data["applicationComponentInfos"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
