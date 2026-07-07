"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Reference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.data_set_reference


class Reference(TypedDict, closed=True):
    dataset: NotRequired[
        "aws_sdk_iotsitewise.types.data_set_reference.DataSetReference"
    ]
    """<p>Contains the dataset reference information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Reference) -> dict:
    out: dict = {}
    if "dataset" in value:
        import aws_sdk_iotsitewise.types.data_set_reference

        out["dataset"] = aws_sdk_iotsitewise.types.data_set_reference.serialize_json(
            value["dataset"]
        )
    return out


def deserialize_json(data: dict) -> Reference:
    out: Reference = {}  # type: ignore[typeddict-item]
    if "dataset" in data:
        import aws_sdk_iotsitewise.types.data_set_reference

        out["dataset"] = aws_sdk_iotsitewise.types.data_set_reference.deserialize_json(
            data["dataset"]
        )
    return out
