"""Generated from Smithy shape ``com.amazonaws.kafka#ListConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of_configuration
    import aws_sdk_kafka.types.__string


class ListConfigurationsResponse(TypedDict):
    configurations: NotRequired[
        "aws_sdk_kafka.types.__list_of_configuration.__listOfConfiguration"
    ]
    """<p>An array of MSK configurations.</p>"""
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The paginated results marker. When the result of a ListConfigurations operation is truncated, the call returns NextToken in the response. To get another batch of configurations, provide this token in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationsResponse) -> dict:
    out: dict = {}
    if "configurations" in value:
        import aws_sdk_kafka.types.__list_of_configuration

        out["configurations"] = (
            aws_sdk_kafka.types.__list_of_configuration.serialize_json(
                value["configurations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfigurationsResponse:
    out: ListConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "configurations" in data:
        import aws_sdk_kafka.types.__list_of_configuration

        out["configurations"] = (
            aws_sdk_kafka.types.__list_of_configuration.deserialize_json(
                data["configurations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
