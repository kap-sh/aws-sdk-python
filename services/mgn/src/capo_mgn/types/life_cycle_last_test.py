"""Generated from Smithy shape ``com.amazonaws.mgn#LifeCycleLastTest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.life_cycle_last_test_finalized
    import capo_mgn.types.life_cycle_last_test_initiated
    import capo_mgn.types.life_cycle_last_test_reverted


class LifeCycleLastTest(TypedDict, closed=True):
    initiated: NotRequired[
        "capo_mgn.types.life_cycle_last_test_initiated.LifeCycleLastTestInitiated"
    ]
    """<p>Lifecycle last Test initiated.</p>"""
    reverted: NotRequired[
        "capo_mgn.types.life_cycle_last_test_reverted.LifeCycleLastTestReverted"
    ]
    """<p>Lifecycle last Test reverted.</p>"""
    finalized: NotRequired[
        "capo_mgn.types.life_cycle_last_test_finalized.LifeCycleLastTestFinalized"
    ]
    """<p>Lifecycle last Test finalized.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifeCycleLastTest) -> dict:
    out: dict = {}
    if "initiated" in value:
        import capo_mgn.types.life_cycle_last_test_initiated

        out["initiated"] = capo_mgn.types.life_cycle_last_test_initiated.serialize_json(
            value["initiated"]
        )
    if "reverted" in value:
        import capo_mgn.types.life_cycle_last_test_reverted

        out["reverted"] = capo_mgn.types.life_cycle_last_test_reverted.serialize_json(
            value["reverted"]
        )
    if "finalized" in value:
        import capo_mgn.types.life_cycle_last_test_finalized

        out["finalized"] = capo_mgn.types.life_cycle_last_test_finalized.serialize_json(
            value["finalized"]
        )
    return out


def deserialize_json(data: dict) -> LifeCycleLastTest:
    out: LifeCycleLastTest = {}  # type: ignore[typeddict-item]
    if "initiated" in data:
        import capo_mgn.types.life_cycle_last_test_initiated

        out["initiated"] = (
            capo_mgn.types.life_cycle_last_test_initiated.deserialize_json(
                data["initiated"]
            )
        )
    if "reverted" in data:
        import capo_mgn.types.life_cycle_last_test_reverted

        out["reverted"] = capo_mgn.types.life_cycle_last_test_reverted.deserialize_json(
            data["reverted"]
        )
    if "finalized" in data:
        import capo_mgn.types.life_cycle_last_test_finalized

        out["finalized"] = (
            capo_mgn.types.life_cycle_last_test_finalized.deserialize_json(
                data["finalized"]
            )
        )
    return out
