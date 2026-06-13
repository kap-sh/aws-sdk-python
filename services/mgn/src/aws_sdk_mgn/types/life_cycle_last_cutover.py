"""Generated from Smithy shape ``com.amazonaws.mgn#LifeCycleLastCutover``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.life_cycle_last_cutover_finalized
    import aws_sdk_mgn.types.life_cycle_last_cutover_initiated
    import aws_sdk_mgn.types.life_cycle_last_cutover_reverted


class LifeCycleLastCutover(TypedDict):
    initiated: NotRequired[
        "aws_sdk_mgn.types.life_cycle_last_cutover_initiated.LifeCycleLastCutoverInitiated"
    ]
    """<p>Lifecycle last Cutover initiated.</p>"""
    reverted: NotRequired[
        "aws_sdk_mgn.types.life_cycle_last_cutover_reverted.LifeCycleLastCutoverReverted"
    ]
    """<p>Lifecycle last Cutover reverted.</p>"""
    finalized: NotRequired[
        "aws_sdk_mgn.types.life_cycle_last_cutover_finalized.LifeCycleLastCutoverFinalized"
    ]
    """<p>Lifecycle Cutover finalized date and time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifeCycleLastCutover) -> dict:
    out: dict = {}
    if "initiated" in value:
        import aws_sdk_mgn.types.life_cycle_last_cutover_initiated

        out["initiated"] = (
            aws_sdk_mgn.types.life_cycle_last_cutover_initiated.serialize_json(
                value["initiated"]
            )
        )
    if "reverted" in value:
        import aws_sdk_mgn.types.life_cycle_last_cutover_reverted

        out["reverted"] = (
            aws_sdk_mgn.types.life_cycle_last_cutover_reverted.serialize_json(
                value["reverted"]
            )
        )
    if "finalized" in value:
        import aws_sdk_mgn.types.life_cycle_last_cutover_finalized

        out["finalized"] = (
            aws_sdk_mgn.types.life_cycle_last_cutover_finalized.serialize_json(
                value["finalized"]
            )
        )
    return out


def deserialize_json(data: dict) -> LifeCycleLastCutover:
    out: LifeCycleLastCutover = {}  # type: ignore[typeddict-item]
    if "initiated" in data:
        import aws_sdk_mgn.types.life_cycle_last_cutover_initiated

        out["initiated"] = (
            aws_sdk_mgn.types.life_cycle_last_cutover_initiated.deserialize_json(
                data["initiated"]
            )
        )
    if "reverted" in data:
        import aws_sdk_mgn.types.life_cycle_last_cutover_reverted

        out["reverted"] = (
            aws_sdk_mgn.types.life_cycle_last_cutover_reverted.deserialize_json(
                data["reverted"]
            )
        )
    if "finalized" in data:
        import aws_sdk_mgn.types.life_cycle_last_cutover_finalized

        out["finalized"] = (
            aws_sdk_mgn.types.life_cycle_last_cutover_finalized.deserialize_json(
                data["finalized"]
            )
        )
    return out
