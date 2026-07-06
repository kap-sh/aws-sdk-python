"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CalculatedAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.display_name
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.timestamp
    import aws_sdk_customer_profiles.types.type_name
    import aws_sdk_customer_profiles.types.uuid


class CalculatedAttributeValue(TypedDict, closed=True):
    calculated_attribute_name: NotRequired[
        "aws_sdk_customer_profiles.types.type_name.typeName"
    ]
    """<p>The unique name of the calculated attribute.</p>"""
    display_name: NotRequired[
        "aws_sdk_customer_profiles.types.display_name.displayName"
    ]
    """<p>The display name of the calculated attribute.</p>"""
    is_data_partial: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>Indicates whether the calculated attribute's value is based on partial data. If the data is partial, it is set to true.</p>"""
    profile_id: NotRequired["aws_sdk_customer_profiles.types.uuid.uuid"]
    """<p>The profile id belonging to this calculated attribute value.</p>"""
    value: NotRequired["aws_sdk_customer_profiles.types.string1_to255.string1To255"]
    """<p>The value of the calculated attribute.</p>"""
    last_object_timestamp: NotRequired[
        "aws_sdk_customer_profiles.types.timestamp.timestamp"
    ]
    """<p>The timestamp of the newest object included in the calculated attribute calculation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedAttributeValue) -> dict:
    out: dict = {}
    if "calculated_attribute_name" in value:
        out["CalculatedAttributeName"] = value["calculated_attribute_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "is_data_partial" in value:
        out["IsDataPartial"] = value["is_data_partial"]
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "value" in value:
        out["Value"] = value["value"]
    if "last_object_timestamp" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["LastObjectTimestamp"] = (
            aws_sdk_customer_profiles.types.timestamp.serialize_json(
                value["last_object_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> CalculatedAttributeValue:
    out: CalculatedAttributeValue = {}  # type: ignore[typeddict-item]
    if "CalculatedAttributeName" in data:
        out["calculated_attribute_name"] = data["CalculatedAttributeName"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "IsDataPartial" in data:
        out["is_data_partial"] = data["IsDataPartial"]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "LastObjectTimestamp" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["last_object_timestamp"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["LastObjectTimestamp"]
            )
        )
    return out
