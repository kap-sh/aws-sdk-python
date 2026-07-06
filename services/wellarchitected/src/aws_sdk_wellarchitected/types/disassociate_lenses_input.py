"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DisassociateLensesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_aliases
    import aws_sdk_wellarchitected.types.workload_id


class DisassociateLensesInput(TypedDict, closed=True):
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    lens_aliases: NotRequired["aws_sdk_wellarchitected.types.lens_aliases.LensAliases"]


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateLensesInput) -> dict:
    out: dict = {}
    if "lens_aliases" in value:
        import aws_sdk_wellarchitected.types.lens_aliases

        out["LensAliases"] = aws_sdk_wellarchitected.types.lens_aliases.serialize_json(
            value["lens_aliases"]
        )
    return out


def deserialize_json(data: dict) -> DisassociateLensesInput:
    out: DisassociateLensesInput = {}  # type: ignore[typeddict-item]
    if "LensAliases" in data:
        import aws_sdk_wellarchitected.types.lens_aliases

        out["lens_aliases"] = (
            aws_sdk_wellarchitected.types.lens_aliases.deserialize_json(
                data["LensAliases"]
            )
        )
    return out
