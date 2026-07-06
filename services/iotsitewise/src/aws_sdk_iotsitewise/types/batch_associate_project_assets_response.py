"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchAssociateProjectAssetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_associate_project_assets_errors


class BatchAssociateProjectAssetsResponse(TypedDict, closed=True):
    errors: NotRequired[
        "aws_sdk_iotsitewise.types.batch_associate_project_assets_errors.BatchAssociateProjectAssetsErrors"
    ]
    """<p>A list of associated error information, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateProjectAssetsResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_iotsitewise.types.batch_associate_project_assets_errors

        out["errors"] = (
            aws_sdk_iotsitewise.types.batch_associate_project_assets_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchAssociateProjectAssetsResponse:
    out: BatchAssociateProjectAssetsResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import aws_sdk_iotsitewise.types.batch_associate_project_assets_errors

        out["errors"] = (
            aws_sdk_iotsitewise.types.batch_associate_project_assets_errors.deserialize_json(
                data["errors"]
            )
        )
    return out
