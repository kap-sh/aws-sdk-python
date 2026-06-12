"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Consolidation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.matching_attributes_list


class Consolidation(TypedDict):
    matching_attributes_list: "aws_sdk_customer_profiles.types.matching_attributes_list.MatchingAttributesList"
    """<p>A list of matching criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Consolidation) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.matching_attributes_list

    out["MatchingAttributesList"] = (
        aws_sdk_customer_profiles.types.matching_attributes_list.serialize_json(
            value["matching_attributes_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> Consolidation:
    out: Consolidation = {}  # type: ignore[typeddict-item]
    if "MatchingAttributesList" in data:
        import aws_sdk_customer_profiles.types.matching_attributes_list

        out["matching_attributes_list"] = (
            aws_sdk_customer_profiles.types.matching_attributes_list.deserialize_json(
                data["MatchingAttributesList"]
            )
        )
    else:
        raise DeserializationError("Consolidation.matching_attributes_list required")
    return out
