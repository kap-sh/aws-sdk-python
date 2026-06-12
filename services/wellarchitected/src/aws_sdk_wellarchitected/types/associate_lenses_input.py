"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AssociateLensesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_aliases
    import aws_sdk_wellarchitected.types.workload_id


class AssociateLensesInput(TypedDict):
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    lens_aliases: NotRequired["aws_sdk_wellarchitected.types.lens_aliases.LensAliases"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociateLensesInput) -> dict:
    out: dict = {}
    if "lens_aliases" in value:
        import aws_sdk_wellarchitected.types.lens_aliases

        out["LensAliases"] = aws_sdk_wellarchitected.types.lens_aliases.serialize_json(
            value["lens_aliases"]
        )
    return out


def deserialize_json(data: dict) -> AssociateLensesInput:
    out: AssociateLensesInput = {}  # type: ignore[typeddict-item]
    if "LensAliases" in data:
        import aws_sdk_wellarchitected.types.lens_aliases

        out["lens_aliases"] = (
            aws_sdk_wellarchitected.types.lens_aliases.deserialize_json(
                data["LensAliases"]
            )
        )
    return out
