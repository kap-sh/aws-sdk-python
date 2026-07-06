"""Generated from Smithy shape ``com.amazonaws.securityhub#Detection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.sequence


class Detection(TypedDict, closed=True):
    sequence: NotRequired["aws_sdk_securityhub.types.sequence.Sequence"]
    """<p> Provides details about an attack sequence. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Detection) -> dict:
    out: dict = {}
    if "sequence" in value:
        import aws_sdk_securityhub.types.sequence

        out["Sequence"] = aws_sdk_securityhub.types.sequence.serialize_json(
            value["sequence"]
        )
    return out


def deserialize_json(data: dict) -> Detection:
    out: Detection = {}  # type: ignore[typeddict-item]
    if "Sequence" in data:
        import aws_sdk_securityhub.types.sequence

        out["sequence"] = aws_sdk_securityhub.types.sequence.deserialize_json(
            data["Sequence"]
        )
    return out
