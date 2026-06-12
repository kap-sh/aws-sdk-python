"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentSort``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.sort_attribute_list


class SegmentSort(TypedDict):
    attributes: "aws_sdk_customer_profiles.types.sort_attribute_list.SortAttributeList"
    """<p>A list of attributes used to sort the segments and their ordering preferences.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentSort) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.sort_attribute_list

    out["Attributes"] = (
        aws_sdk_customer_profiles.types.sort_attribute_list.serialize_json(
            value["attributes"]
        )
    )
    return out


def deserialize_json(data: dict) -> SegmentSort:
    out: SegmentSort = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_customer_profiles.types.sort_attribute_list

        out["attributes"] = (
            aws_sdk_customer_profiles.types.sort_attribute_list.deserialize_json(
                data["Attributes"]
            )
        )
    else:
        raise DeserializationError("SegmentSort.attributes required")
    return out
