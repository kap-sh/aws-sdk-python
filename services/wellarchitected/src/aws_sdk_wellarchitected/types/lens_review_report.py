"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensReviewReport``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.base64_string
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.lens_arn


class LensReviewReport(TypedDict):
    lens_alias: NotRequired["aws_sdk_wellarchitected.types.lens_alias.LensAlias"]
    lens_arn: NotRequired["aws_sdk_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens.</p>"""
    base64_string: NotRequired[
        "aws_sdk_wellarchitected.types.base64_string.Base64String"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: LensReviewReport) -> dict:
    out: dict = {}
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "base64_string" in value:
        out["Base64String"] = value["base64_string"]
    return out


def deserialize_json(data: dict) -> LensReviewReport:
    out: LensReviewReport = {}  # type: ignore[typeddict-item]
    if "LensAlias" in data:
        out["lens_alias"] = data["LensAlias"]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "Base64String" in data:
        out["base64_string"] = data["Base64String"]
    return out
