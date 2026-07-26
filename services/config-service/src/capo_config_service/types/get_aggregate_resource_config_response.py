"""Generated from Smithy shape ``com.amazonaws.configservice#GetAggregateResourceConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.configuration_item


class GetAggregateResourceConfigResponse(TypedDict, closed=True):
    configuration_item: NotRequired[
        "capo_config_service.types.configuration_item.ConfigurationItem"
    ]
    """<p>Returns a <code>ConfigurationItem</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAggregateResourceConfigResponse) -> dict:
    out: dict = {}
    if "configuration_item" in value:
        import capo_config_service.types.configuration_item

        out["ConfigurationItem"] = (
            capo_config_service.types.configuration_item.serialize_aws_json_1_1(
                value["configuration_item"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAggregateResourceConfigResponse:
    out: GetAggregateResourceConfigResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationItem" in data:
        import capo_config_service.types.configuration_item

        out["configuration_item"] = (
            capo_config_service.types.configuration_item.deserialize_aws_json_1_1(
                data["ConfigurationItem"]
            )
        )
    return out
