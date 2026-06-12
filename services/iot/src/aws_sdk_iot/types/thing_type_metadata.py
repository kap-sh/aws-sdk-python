"""Generated from Smithy shape ``com.amazonaws.iot#ThingTypeMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.boolean2
    import aws_sdk_iot.types.creation_date
    import aws_sdk_iot.types.deprecation_date


class ThingTypeMetadata(TypedDict):
    deprecated: "aws_sdk_iot.types.boolean2.Boolean2"
    """<p>Whether the thing type is deprecated. If <b>true</b>, no new things could be associated with this type.</p>"""
    deprecation_date: NotRequired["aws_sdk_iot.types.deprecation_date.DeprecationDate"]
    """<p>The date and time when the thing type was deprecated.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.creation_date.CreationDate"]
    """<p>The date and time when the thing type was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThingTypeMetadata) -> dict:
    out: dict = {}
    out["deprecated"] = value.get("deprecated", False)
    if "deprecation_date" in value:
        import aws_sdk_iot.types.deprecation_date

        out["deprecationDate"] = aws_sdk_iot.types.deprecation_date.serialize_json(
            value["deprecation_date"]
        )
    if "creation_date" in value:
        import aws_sdk_iot.types.creation_date

        out["creationDate"] = aws_sdk_iot.types.creation_date.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> ThingTypeMetadata:
    out: ThingTypeMetadata = {}  # type: ignore[typeddict-item]
    if "deprecated" in data:
        out["deprecated"] = data["deprecated"]
    else:
        out["deprecated"] = False
    if "deprecationDate" in data:
        import aws_sdk_iot.types.deprecation_date

        out["deprecation_date"] = aws_sdk_iot.types.deprecation_date.deserialize_json(
            data["deprecationDate"]
        )
    if "creationDate" in data:
        import aws_sdk_iot.types.creation_date

        out["creation_date"] = aws_sdk_iot.types.creation_date.deserialize_json(
            data["creationDate"]
        )
    return out
