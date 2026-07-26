"""Generated from Smithy shape ``com.amazonaws.mgn#SplitOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.split_constructs


class SplitOperation(TypedDict, closed=True):
    split_constructs: NotRequired["capo_mgn.types.split_constructs.SplitConstructs"]
    """<p>The list of split targets with their CIDR blocks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SplitOperation) -> dict:
    out: dict = {}
    if "split_constructs" in value:
        import capo_mgn.types.split_constructs

        out["splitConstructs"] = capo_mgn.types.split_constructs.serialize_json(
            value["split_constructs"]
        )
    return out


def deserialize_json(data: dict) -> SplitOperation:
    out: SplitOperation = {}  # type: ignore[typeddict-item]
    if "splitConstructs" in data:
        import capo_mgn.types.split_constructs

        out["split_constructs"] = capo_mgn.types.split_constructs.deserialize_json(
            data["splitConstructs"]
        )
    return out
