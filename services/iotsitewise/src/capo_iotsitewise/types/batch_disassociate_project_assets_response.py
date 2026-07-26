"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchDisassociateProjectAssetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_disassociate_project_assets_errors


class BatchDisassociateProjectAssetsResponse(TypedDict, closed=True):
    errors: NotRequired[
        "capo_iotsitewise.types.batch_disassociate_project_assets_errors.BatchDisassociateProjectAssetsErrors"
    ]
    """<p>A list of associated error information, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateProjectAssetsResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_iotsitewise.types.batch_disassociate_project_assets_errors

        out["errors"] = (
            capo_iotsitewise.types.batch_disassociate_project_assets_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDisassociateProjectAssetsResponse:
    out: BatchDisassociateProjectAssetsResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import capo_iotsitewise.types.batch_disassociate_project_assets_errors

        out["errors"] = (
            capo_iotsitewise.types.batch_disassociate_project_assets_errors.deserialize_json(
                data["errors"]
            )
        )
    return out
