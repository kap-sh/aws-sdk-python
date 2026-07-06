"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceSize``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_size_type
    import aws_sdk_cleanroomsml.types.audience_size_value


class AudienceSize(TypedDict, closed=True):
    type: "aws_sdk_cleanroomsml.types.audience_size_type.AudienceSizeType"
    """<p>Whether the audience size is defined in absolute terms or as a percentage. You can use the <code>ABSOLUTE</code> <a>AudienceSize</a> to configure out audience sizes using the count of identifiers in the output. You can use the <code>Percentage</code> <a>AudienceSize</a> to configure sizes in the range 1-100 percent.</p>"""
    value: "aws_sdk_cleanroomsml.types.audience_size_value.AudienceSizeValue"
    """<p>Specify an audience size value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudienceSize) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.audience_size_type

    out["type"] = aws_sdk_cleanroomsml.types.audience_size_type.serialize_json(
        value["type"]
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AudienceSize:
    out: AudienceSize = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_cleanroomsml.types.audience_size_type

        out["type"] = aws_sdk_cleanroomsml.types.audience_size_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("AudienceSize.type required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("AudienceSize.value required")
    return out
