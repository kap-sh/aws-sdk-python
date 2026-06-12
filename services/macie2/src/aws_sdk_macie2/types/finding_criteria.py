"""Generated from Smithy shape ``com.amazonaws.macie2#FindingCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.criterion


class FindingCriteria(TypedDict):
    criterion: NotRequired["aws_sdk_macie2.types.criterion.Criterion"]
    """<p>A condition that specifies the property, operator, and one or more values to use to filter the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingCriteria) -> dict:
    out: dict = {}
    if "criterion" in value:
        import aws_sdk_macie2.types.criterion

        out["criterion"] = aws_sdk_macie2.types.criterion.serialize_json(
            value["criterion"]
        )
    return out


def deserialize_json(data: dict) -> FindingCriteria:
    out: FindingCriteria = {}  # type: ignore[typeddict-item]
    if "criterion" in data:
        import aws_sdk_macie2.types.criterion

        out["criterion"] = aws_sdk_macie2.types.criterion.deserialize_json(
            data["criterion"]
        )
    return out
