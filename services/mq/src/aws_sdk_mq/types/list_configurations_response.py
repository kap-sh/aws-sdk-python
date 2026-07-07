"""Generated from Smithy shape ``com.amazonaws.mq#ListConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__integer
    import aws_sdk_mq.types.__list_of_configuration
    import aws_sdk_mq.types.__string


class ListConfigurationsResponse(TypedDict, closed=True):
    configurations: NotRequired[
        "aws_sdk_mq.types.__list_of_configuration.__listOfConfiguration"
    ]
    """<p>The list of all revisions for the specified configuration.</p>"""
    max_results: NotRequired["aws_sdk_mq.types.__integer.__integer"]
    """<p>The maximum number of configurations that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.</p>"""
    next_token: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationsResponse) -> dict:
    out: dict = {}
    if "configurations" in value:
        import aws_sdk_mq.types.__list_of_configuration

        out["configurations"] = aws_sdk_mq.types.__list_of_configuration.serialize_json(
            value["configurations"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfigurationsResponse:
    out: ListConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "configurations" in data:
        import aws_sdk_mq.types.__list_of_configuration

        out["configurations"] = (
            aws_sdk_mq.types.__list_of_configuration.deserialize_json(
                data["configurations"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
