"""Generated from Smithy shape ``com.amazonaws.macie2#Scoping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.job_scoping_block


class Scoping(TypedDict):
    excludes: NotRequired["aws_sdk_macie2.types.job_scoping_block.JobScopingBlock"]
    """<p>The property- and tag-based conditions that determine which objects to exclude from the analysis.</p>"""
    includes: NotRequired["aws_sdk_macie2.types.job_scoping_block.JobScopingBlock"]
    """<p>The property- and tag-based conditions that determine which objects to include in the analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Scoping) -> dict:
    out: dict = {}
    if "excludes" in value:
        import aws_sdk_macie2.types.job_scoping_block

        out["excludes"] = aws_sdk_macie2.types.job_scoping_block.serialize_json(
            value["excludes"]
        )
    if "includes" in value:
        import aws_sdk_macie2.types.job_scoping_block

        out["includes"] = aws_sdk_macie2.types.job_scoping_block.serialize_json(
            value["includes"]
        )
    return out


def deserialize_json(data: dict) -> Scoping:
    out: Scoping = {}  # type: ignore[typeddict-item]
    if "excludes" in data:
        import aws_sdk_macie2.types.job_scoping_block

        out["excludes"] = aws_sdk_macie2.types.job_scoping_block.deserialize_json(
            data["excludes"]
        )
    if "includes" in data:
        import aws_sdk_macie2.types.job_scoping_block

        out["includes"] = aws_sdk_macie2.types.job_scoping_block.deserialize_json(
            data["includes"]
        )
    return out
