"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AssociateLensesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_aliases
    import capo_wellarchitected.types.workload_id


class AssociateLensesInput(TypedDict, closed=True):
    workload_id: "capo_wellarchitected.types.workload_id.WorkloadId"
    lens_aliases: NotRequired["capo_wellarchitected.types.lens_aliases.LensAliases"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociateLensesInput) -> dict:
    out: dict = {}
    if "lens_aliases" in value:
        import capo_wellarchitected.types.lens_aliases

        out["LensAliases"] = capo_wellarchitected.types.lens_aliases.serialize_json(
            value["lens_aliases"]
        )
    return out


def deserialize_json(data: dict) -> AssociateLensesInput:
    out: AssociateLensesInput = {}  # type: ignore[typeddict-item]
    if "LensAliases" in data:
        import capo_wellarchitected.types.lens_aliases

        out["lens_aliases"] = capo_wellarchitected.types.lens_aliases.deserialize_json(
            data["LensAliases"]
        )
    return out
