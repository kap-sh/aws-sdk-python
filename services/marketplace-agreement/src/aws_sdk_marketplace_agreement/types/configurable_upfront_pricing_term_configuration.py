"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ConfigurableUpfrontPricingTermConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.bounded_string
    import aws_sdk_marketplace_agreement.types.dimension_list


class ConfigurableUpfrontPricingTermConfiguration(TypedDict, closed=True):
    selector_value: "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    """<p>Defines the length of time for which the particular pricing/dimension is being purchased by the acceptor.</p>"""
    dimensions: "aws_sdk_marketplace_agreement.types.dimension_list.DimensionList"
    """<p>Defines the dimensions that the acceptor has purchased from the overall set of dimensions presented in the rate card.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConfigurableUpfrontPricingTermConfiguration) -> dict:
    out: dict = {}
    out["selectorValue"] = value["selector_value"]
    import aws_sdk_marketplace_agreement.types.dimension_list

    out["dimensions"] = (
        aws_sdk_marketplace_agreement.types.dimension_list.serialize_aws_json_1_0(
            value["dimensions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConfigurableUpfrontPricingTermConfiguration:
    out: ConfigurableUpfrontPricingTermConfiguration = {}  # type: ignore[typeddict-item]
    if "selectorValue" in data:
        out["selector_value"] = data["selectorValue"]
    else:
        raise DeserializationError(
            "ConfigurableUpfrontPricingTermConfiguration.selector_value required"
        )
    if "dimensions" in data:
        import aws_sdk_marketplace_agreement.types.dimension_list

        out["dimensions"] = (
            aws_sdk_marketplace_agreement.types.dimension_list.deserialize_aws_json_1_0(
                data["dimensions"]
            )
        )
    else:
        raise DeserializationError(
            "ConfigurableUpfrontPricingTermConfiguration.dimensions required"
        )
    return out
