"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ImportLensOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.import_lens_status
    import aws_sdk_wellarchitected.types.lens_arn


class ImportLensOutput(TypedDict, closed=True):
    lens_arn: NotRequired["aws_sdk_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens that was created or updated.</p>"""
    status: NotRequired[
        "aws_sdk_wellarchitected.types.import_lens_status.ImportLensStatus"
    ]
    """<p>The status of the imported lens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportLensOutput) -> dict:
    out: dict = {}
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "status" in value:
        import aws_sdk_wellarchitected.types.import_lens_status

        out["Status"] = aws_sdk_wellarchitected.types.import_lens_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> ImportLensOutput:
    out: ImportLensOutput = {}  # type: ignore[typeddict-item]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "Status" in data:
        import aws_sdk_wellarchitected.types.import_lens_status

        out["status"] = (
            aws_sdk_wellarchitected.types.import_lens_status.deserialize_json(
                data["Status"]
            )
        )
    return out
