"""Generated from Smithy shape ``com.amazonaws.mgn#SplitOperation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.split_constructs


class SplitOperation(TypedDict):
    split_constructs: NotRequired["aws_sdk_mgn.types.split_constructs.SplitConstructs"]
    """<p>The list of split targets with their CIDR blocks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SplitOperation) -> dict:
    out: dict = {}
    if "split_constructs" in value:
        import aws_sdk_mgn.types.split_constructs

        out["splitConstructs"] = aws_sdk_mgn.types.split_constructs.serialize_json(
            value["split_constructs"]
        )
    return out


def deserialize_json(data: dict) -> SplitOperation:
    out: SplitOperation = {}  # type: ignore[typeddict-item]
    if "splitConstructs" in data:
        import aws_sdk_mgn.types.split_constructs

        out["split_constructs"] = aws_sdk_mgn.types.split_constructs.deserialize_json(
            data["splitConstructs"]
        )
    return out
