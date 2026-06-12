"""Generated from Smithy shape ``com.amazonaws.iotsitewise#SourceDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.kendra_source_detail


class SourceDetail(TypedDict):
    kendra: NotRequired[
        "aws_sdk_iotsitewise.types.kendra_source_detail.KendraSourceDetail"
    ]
    """<p>Contains details about the Kendra dataset source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceDetail) -> dict:
    out: dict = {}
    if "kendra" in value:
        import aws_sdk_iotsitewise.types.kendra_source_detail

        out["kendra"] = aws_sdk_iotsitewise.types.kendra_source_detail.serialize_json(
            value["kendra"]
        )
    return out


def deserialize_json(data: dict) -> SourceDetail:
    out: SourceDetail = {}  # type: ignore[typeddict-item]
    if "kendra" in data:
        import aws_sdk_iotsitewise.types.kendra_source_detail

        out["kendra"] = aws_sdk_iotsitewise.types.kendra_source_detail.deserialize_json(
            data["kendra"]
        )
    return out
