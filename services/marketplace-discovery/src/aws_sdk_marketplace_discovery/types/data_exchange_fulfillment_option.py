"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DataExchangeFulfillmentOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.data_artifact_list
    import aws_sdk_marketplace_discovery.types.fulfillment_option_type


class DataExchangeFulfillmentOption(TypedDict, closed=True):
    fulfillment_option_id: "str"
    """<p>The unique identifier of the fulfillment option.</p>"""
    fulfillment_option_type: "aws_sdk_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    """<p>The category of the fulfillment option.</p>"""
    fulfillment_option_display_name: "str"
    """<p>A human-readable name for the fulfillment option type.</p>"""
    data_artifacts: NotRequired[
        "aws_sdk_marketplace_discovery.types.data_artifact_list.DataArtifactList"
    ]
    """<p>The data artifacts included in this Data Exchange fulfillment option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataExchangeFulfillmentOption) -> dict:
    out: dict = {}
    out["fulfillmentOptionId"] = value["fulfillment_option_id"]
    import aws_sdk_marketplace_discovery.types.fulfillment_option_type

    out["fulfillmentOptionType"] = (
        aws_sdk_marketplace_discovery.types.fulfillment_option_type.serialize_json(
            value["fulfillment_option_type"]
        )
    )
    out["fulfillmentOptionDisplayName"] = value["fulfillment_option_display_name"]
    if "data_artifacts" in value:
        import aws_sdk_marketplace_discovery.types.data_artifact_list

        out["dataArtifacts"] = (
            aws_sdk_marketplace_discovery.types.data_artifact_list.serialize_json(
                value["data_artifacts"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataExchangeFulfillmentOption:
    out: DataExchangeFulfillmentOption = {}  # type: ignore[typeddict-item]
    if "fulfillmentOptionId" in data:
        out["fulfillment_option_id"] = data["fulfillmentOptionId"]
    else:
        raise DeserializationError(
            "DataExchangeFulfillmentOption.fulfillment_option_id required"
        )
    if "fulfillmentOptionType" in data:
        import aws_sdk_marketplace_discovery.types.fulfillment_option_type

        out["fulfillment_option_type"] = (
            aws_sdk_marketplace_discovery.types.fulfillment_option_type.deserialize_json(
                data["fulfillmentOptionType"]
            )
        )
    else:
        raise DeserializationError(
            "DataExchangeFulfillmentOption.fulfillment_option_type required"
        )
    if "fulfillmentOptionDisplayName" in data:
        out["fulfillment_option_display_name"] = data["fulfillmentOptionDisplayName"]
    else:
        raise DeserializationError(
            "DataExchangeFulfillmentOption.fulfillment_option_display_name required"
        )
    if "dataArtifacts" in data:
        import aws_sdk_marketplace_discovery.types.data_artifact_list

        out["data_artifacts"] = (
            aws_sdk_marketplace_discovery.types.data_artifact_list.deserialize_json(
                data["dataArtifacts"]
            )
        )
    return out
