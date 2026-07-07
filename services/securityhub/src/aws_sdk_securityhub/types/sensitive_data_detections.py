"""Generated from Smithy shape ``com.amazonaws.securityhub#SensitiveDataDetections``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.long
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.occurrences


class SensitiveDataDetections(TypedDict, closed=True):
    count: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p>The total number of occurrences of sensitive data that were detected.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of sensitive data that was detected. For example, the type might indicate that the data is an email address.</p>"""
    occurrences: NotRequired["aws_sdk_securityhub.types.occurrences.Occurrences"]
    """<p>Details about the sensitive data that was detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveDataDetections) -> dict:
    out: dict = {}
    if "count" in value:
        out["Count"] = value["count"]
    if "type" in value:
        out["Type"] = value["type"]
    if "occurrences" in value:
        import aws_sdk_securityhub.types.occurrences

        out["Occurrences"] = aws_sdk_securityhub.types.occurrences.serialize_json(
            value["occurrences"]
        )
    return out


def deserialize_json(data: dict) -> SensitiveDataDetections:
    out: SensitiveDataDetections = {}  # type: ignore[typeddict-item]
    if "Count" in data:
        out["count"] = data["Count"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Occurrences" in data:
        import aws_sdk_securityhub.types.occurrences

        out["occurrences"] = aws_sdk_securityhub.types.occurrences.deserialize_json(
            data["Occurrences"]
        )
    return out
