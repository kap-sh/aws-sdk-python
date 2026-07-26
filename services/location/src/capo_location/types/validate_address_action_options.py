"""Generated from Smithy shape ``com.amazonaws.location#ValidateAddressActionOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.validate_address_additional_feature_list


class ValidateAddressActionOptions(TypedDict, closed=True):
    additional_features: NotRequired[
        "capo_location.types.validate_address_additional_feature_list.ValidateAddressAdditionalFeatureList"
    ]
    """<p>A list of optional additional parameters that can be requested for each result.</p> <p>Values:</p> <ul> <li> <p> <code>Position</code> - Return the position coordinates of the address if available.</p> </li> <li> <p> <code>CountrySpecificAttributes</code> - Return additional information about the address specific to the country of origin.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateAddressActionOptions) -> dict:
    out: dict = {}
    if "additional_features" in value:
        import capo_location.types.validate_address_additional_feature_list

        out["AdditionalFeatures"] = (
            capo_location.types.validate_address_additional_feature_list.serialize_json(
                value["additional_features"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidateAddressActionOptions:
    out: ValidateAddressActionOptions = {}  # type: ignore[typeddict-item]
    if "AdditionalFeatures" in data:
        import capo_location.types.validate_address_additional_feature_list

        out["additional_features"] = (
            capo_location.types.validate_address_additional_feature_list.deserialize_json(
                data["AdditionalFeatures"]
            )
        )
    return out
