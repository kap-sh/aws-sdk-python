"""Generated from Smithy shape ``com.amazonaws.lambda#SnapStart``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.snap_start_apply_on


class SnapStart(TypedDict, closed=True):
    apply_on: NotRequired["capo_lambda.types.snap_start_apply_on.SnapStartApplyOn"]
    """<p>Set to <code>PublishedVersions</code> to create a snapshot of the initialized execution environment when you publish a function version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapStart) -> dict:
    out: dict = {}
    if "apply_on" in value:
        import capo_lambda.types.snap_start_apply_on

        out["ApplyOn"] = capo_lambda.types.snap_start_apply_on.serialize_json(
            value["apply_on"]
        )
    return out


def deserialize_json(data: dict) -> SnapStart:
    out: SnapStart = {}  # type: ignore[typeddict-item]
    if data.get("ApplyOn") is not None:
        import capo_lambda.types.snap_start_apply_on

        out["apply_on"] = capo_lambda.types.snap_start_apply_on.deserialize_json(
            data["ApplyOn"]
        )
    return out
