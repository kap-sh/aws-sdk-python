"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetApplicationComponentStrategiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.application_component_strategies


class GetApplicationComponentStrategiesResponse(TypedDict):
    application_component_strategies: NotRequired[
        "aws_sdk_migrationhubstrategy.types.application_component_strategies.ApplicationComponentStrategies"
    ]
    """<p> A list of application component strategy recommendations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationComponentStrategiesResponse) -> dict:
    out: dict = {}
    if "application_component_strategies" in value:
        import aws_sdk_migrationhubstrategy.types.application_component_strategies

        out["applicationComponentStrategies"] = (
            aws_sdk_migrationhubstrategy.types.application_component_strategies.serialize_json(
                value["application_component_strategies"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetApplicationComponentStrategiesResponse:
    out: GetApplicationComponentStrategiesResponse = {}  # type: ignore[typeddict-item]
    if "applicationComponentStrategies" in data:
        import aws_sdk_migrationhubstrategy.types.application_component_strategies

        out["application_component_strategies"] = (
            aws_sdk_migrationhubstrategy.types.application_component_strategies.deserialize_json(
                data["applicationComponentStrategies"]
            )
        )
    return out
