"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DetectedProfileObjectType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.field_map
    import aws_sdk_customer_profiles.types.key_map
    import aws_sdk_customer_profiles.types.string1_to255


class DetectedProfileObjectType(TypedDict):
    source_last_updated_timestamp_format: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>The format of <code>sourceLastUpdatedTimestamp</code> that was detected in fields.</p>"""
    fields: NotRequired["aws_sdk_customer_profiles.types.field_map.FieldMap"]
    """<p>A map of the name and the <code>ObjectType</code> field.</p>"""
    keys: NotRequired["aws_sdk_customer_profiles.types.key_map.KeyMap"]
    """<p>A list of unique keys that can be used to map data to a profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectedProfileObjectType) -> dict:
    out: dict = {}
    if "source_last_updated_timestamp_format" in value:
        out["SourceLastUpdatedTimestampFormat"] = value[
            "source_last_updated_timestamp_format"
        ]
    if "fields" in value:
        import aws_sdk_customer_profiles.types.field_map

        out["Fields"] = aws_sdk_customer_profiles.types.field_map.serialize_json(
            value["fields"]
        )
    if "keys" in value:
        import aws_sdk_customer_profiles.types.key_map

        out["Keys"] = aws_sdk_customer_profiles.types.key_map.serialize_json(
            value["keys"]
        )
    return out


def deserialize_json(data: dict) -> DetectedProfileObjectType:
    out: DetectedProfileObjectType = {}  # type: ignore[typeddict-item]
    if "SourceLastUpdatedTimestampFormat" in data:
        out["source_last_updated_timestamp_format"] = data[
            "SourceLastUpdatedTimestampFormat"
        ]
    if "Fields" in data:
        import aws_sdk_customer_profiles.types.field_map

        out["fields"] = aws_sdk_customer_profiles.types.field_map.deserialize_json(
            data["Fields"]
        )
    if "Keys" in data:
        import aws_sdk_customer_profiles.types.key_map

        out["keys"] = aws_sdk_customer_profiles.types.key_map.deserialize_json(
            data["Keys"]
        )
    return out
