"""Generated from Smithy shape ``com.amazonaws.macie2#CustomDetection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__long
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.occurrences


class CustomDetection(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the custom data identifier.</p>"""
    count: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of occurrences of the sensitive data that the custom data identifier detected.</p>"""
    name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name of the custom data identifier.</p>"""
    occurrences: NotRequired["aws_sdk_macie2.types.occurrences.Occurrences"]
    """<p>The location of 1-15 occurrences of the sensitive data that the custom data identifier detected. A finding includes location data for a maximum of 15 occurrences of sensitive data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomDetection) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "count" in value:
        out["count"] = value["count"]
    if "name" in value:
        out["name"] = value["name"]
    if "occurrences" in value:
        import aws_sdk_macie2.types.occurrences

        out["occurrences"] = aws_sdk_macie2.types.occurrences.serialize_json(
            value["occurrences"]
        )
    return out


def deserialize_json(data: dict) -> CustomDetection:
    out: CustomDetection = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "count" in data:
        out["count"] = data["count"]
    if "name" in data:
        out["name"] = data["name"]
    if "occurrences" in data:
        import aws_sdk_macie2.types.occurrences

        out["occurrences"] = aws_sdk_macie2.types.occurrences.deserialize_json(
            data["occurrences"]
        )
    return out
